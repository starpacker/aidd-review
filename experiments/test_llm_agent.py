"""
Phase 2 - System 2: LLM + Tools Agent
A minimal ReAct-style agent that uses RDKit tools + Claude LLM.
Tests whether tool-augmented LLM is better than pure LLM (System 1).

Uses .venv38 (Python 3.8 + RDKit + openai).
No LangChain dependency — implements a simple tool-calling loop directly.
"""

import json
import time
import os
import re
from openai import OpenAI

# RDKit imports
from rdkit import Chem
from rdkit.Chem import Descriptors, QED, rdMolDescriptors, FilterCatalog
from rdkit.Chem.FilterCatalog import FilterCatalogParams

# === Config ===
API_BASE = "https://ai-gateway-internal.dp.tech/v1"
API_KEY = os.environ.get("AIDD_API_KEY", "YOUR_API_KEY_HERE")
MODEL = "cds/Claude-4.6-opus"

DATASET_PATH = os.path.join(os.path.dirname(__file__), "agent_evaluation_dataset.json")
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "results_llm_agent.json")

# === Tool Definitions ===

def compute_drug_properties(smiles):
    """Compute molecular properties: MW, LogP, QED, Lipinski violations, TPSA, RotBonds, HBD, HBA."""
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return json.dumps({"error": "Invalid SMILES"})

    mw = Descriptors.MolWt(mol)
    logp = Descriptors.MolLogP(mol)
    qed_score = QED.qed(mol)
    hbd = Descriptors.NumHDonors(mol)
    hba = Descriptors.NumHAcceptors(mol)
    tpsa = Descriptors.TPSA(mol)
    rotbonds = Descriptors.NumRotatableBonds(mol)
    rings = Descriptors.RingCount(mol)
    aromatic_rings = Descriptors.NumAromaticRings(mol)

    # Lipinski violations
    violations = sum([mw > 500, logp > 5, hbd > 5, hba > 10])

    # Veber rules
    veber_pass = tpsa <= 140 and rotbonds <= 10

    return json.dumps({
        "MW": round(mw, 1),
        "LogP": round(logp, 2),
        "QED": round(qed_score, 3),
        "HBD": hbd,
        "HBA": hba,
        "TPSA": round(tpsa, 1),
        "RotBonds": rotbonds,
        "Rings": rings,
        "AromaticRings": aromatic_rings,
        "Lipinski_violations": violations,
        "Lipinski_pass": violations <= 1,
        "Veber_pass": veber_pass,
        "Formula": rdMolDescriptors.CalcMolFormula(mol)
    })


def check_structural_alerts(smiles):
    """Check for PAINS, Brenk, and other structural alerts."""
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return json.dumps({"error": "Invalid SMILES"})

    alerts = []

    # PAINS filter
    params_pains = FilterCatalogParams()
    params_pains.AddCatalog(FilterCatalogParams.FilterCatalogs.PAINS)
    catalog_pains = FilterCatalog.FilterCatalog(params_pains)
    if catalog_pains.HasMatch(mol):
        entry = catalog_pains.GetFirstMatch(mol)
        alerts.append({"type": "PAINS", "name": entry.GetDescription()})

    # Brenk filter
    params_brenk = FilterCatalogParams()
    params_brenk.AddCatalog(FilterCatalogParams.FilterCatalogs.BRENK)
    catalog_brenk = FilterCatalog.FilterCatalog(params_brenk)
    if catalog_brenk.HasMatch(mol):
        entry = catalog_brenk.GetFirstMatch(mol)
        alerts.append({"type": "Brenk", "name": entry.GetDescription()})

    # Common toxicophores (manual SMARTS)
    toxicophores = {
        "nitro_aromatic": "[$(c-[N+](=O)[O-])]",
        "epoxide": "C1OC1",
        "acyl_halide": "C(=O)[F,Cl,Br,I]",
        "aldehyde": "[CH]=O",
        "michael_acceptor": "C=CC(=O)",
        "aniline": "c-[NH2]",
        "thiol": "[SH]",
    }

    for name, smarts in toxicophores.items():
        pat = Chem.MolFromSmarts(smarts)
        if pat and mol.HasSubstructMatch(pat):
            alerts.append({"type": "Toxicophore", "name": name})

    return json.dumps({
        "num_alerts": len(alerts),
        "alerts": alerts,
        "clean": len(alerts) == 0
    })


def predict_admet_proxy(smiles):
    """Predict ADMET properties using RDKit descriptors as proxy.

    This uses rule-based estimation — not ML prediction — to simulate what
    a real ADMET tool would report.
    """
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return json.dumps({"error": "Invalid SMILES"})

    mw = Descriptors.MolWt(mol)
    logp = Descriptors.MolLogP(mol)
    tpsa = Descriptors.TPSA(mol)
    hbd = Descriptors.NumHDonors(mol)
    hba = Descriptors.NumHAcceptors(mol)
    rotbonds = Descriptors.NumRotatableBonds(mol)

    predictions = {}

    # Absorption: based on Lipinski and Veber rules
    predictions["oral_absorption"] = "Good" if (mw < 500 and logp < 5 and hbd < 5 and hba < 10 and tpsa < 140 and rotbonds < 10) else "Poor"

    # BBB penetration: MW < 400, LogP 1-3, TPSA < 90, HBD < 3
    bbb_score = sum([mw < 400, 1 <= logp <= 3, tpsa < 90, hbd < 3])
    predictions["BBB_penetration"] = "High" if bbb_score >= 3 else ("Moderate" if bbb_score >= 2 else "Low")

    # hERG liability: LogP > 3.7 AND basic amine
    has_basic_amine = mol.HasSubstructMatch(Chem.MolFromSmarts("[NH2,NH1,NH0;!$(NC=O)]"))
    predictions["hERG_risk"] = "High" if (logp > 3.7 and has_basic_amine) else ("Moderate" if logp > 3.7 else "Low")

    # CYP inhibition risk: MW > 400 and LogP > 4
    predictions["CYP_inhibition_risk"] = "High" if (mw > 400 and logp > 4) else "Low"

    # Hepatotoxicity risk: reactive groups
    reactive_smarts = ["C(=O)Cl", "[N+](=O)[O-]", "C1OC1", "[SH]"]
    has_reactive = any(mol.HasSubstructMatch(Chem.MolFromSmarts(s)) for s in reactive_smarts if Chem.MolFromSmarts(s))
    predictions["hepatotoxicity_risk"] = "High" if has_reactive else ("Moderate" if logp > 5 else "Low")

    # Plasma protein binding
    predictions["plasma_protein_binding"] = "High (>90%)" if logp > 3.5 else "Moderate (50-90%)"

    # Solubility estimate (ESOL-like)
    log_s = 0.16 - 0.63 * logp - 0.0062 * mw + 0.066 * rotbonds - 0.74 * Descriptors.NumAromaticRings(mol)
    predictions["estimated_solubility_logS"] = round(log_s, 2)
    predictions["solubility_class"] = "Good" if log_s > -4 else ("Moderate" if log_s > -6 else "Poor")

    return json.dumps(predictions)


TOOLS = {
    "compute_drug_properties": compute_drug_properties,
    "check_structural_alerts": check_structural_alerts,
    "predict_admet": predict_admet_proxy,
}

TOOL_DESCRIPTIONS = """Available tools:
1. compute_drug_properties(smiles) - Compute molecular properties: MW, LogP, QED, Lipinski violations, TPSA, RotBonds, HBD, HBA, Rings
2. check_structural_alerts(smiles) - Check for PAINS, Brenk, and toxicophore structural alerts
3. predict_admet(smiles) - Predict ADMET properties: oral absorption, BBB, hERG, CYP inhibition, hepatotoxicity, solubility"""


AGENT_SYSTEM_PROMPT = """You are a medicinal chemistry expert evaluating drug candidates. You have access to computational chemistry tools.

{tool_descriptions}

For each molecule, you MUST:
1. Use compute_drug_properties to get the molecular properties
2. Use check_structural_alerts to check for red flags
3. Use predict_admet to assess ADMET profile
4. Synthesize all information into a final assessment

To use a tool, write:
TOOL_CALL: tool_name(smiles)

After receiving tool results, provide your final assessment as JSON:
FINAL_ANSWER:
{{
  "drug_likeness": <1-10>,
  "admet_safety": <1-10>,
  "synthetic_feasibility": <1-10>,
  "clinical_potential": <1-10>,
  "overall_score": <float 1-10>,
  "recommendation": "<Advance|Caution|Reject>",
  "concerns": ["..."],
  "strengths": ["..."],
  "reasoning": "<2-3 sentences synthesizing tool results with your expert knowledge>"
}}"""


def run_agent(client, smiles, name, max_steps=6):
    """Run a simple ReAct agent loop for one molecule."""
    messages = [
        {"role": "system", "content": AGENT_SYSTEM_PROMPT.format(tool_descriptions=TOOL_DESCRIPTIONS)},
        {"role": "user", "content": f"Evaluate this drug candidate:\nName: {name}\nSMILES: {smiles}\n\nUse all three tools, then provide your FINAL_ANSWER."}
    ]

    tool_trace = []  # Record the full agent trace

    for step in range(max_steps):
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=messages,
                temperature=0.1,
                max_tokens=2000,
            )
            content = response.choices[0].message.content
        except Exception as e:
            tool_trace.append({"step": step, "error": str(e)})
            break

        messages.append({"role": "assistant", "content": content})
        tool_trace.append({"step": step, "type": "assistant", "content": content[:500]})

        # Check if final answer
        if "FINAL_ANSWER:" in content:
            json_str = content.split("FINAL_ANSWER:")[1].strip()
            if "```json" in json_str:
                json_str = json_str.split("```json")[1].split("```")[0].strip()
            elif "```" in json_str:
                json_str = json_str.split("```")[1].split("```")[0].strip()
            try:
                result = json.loads(json_str)
                result["agent_trace"] = tool_trace
                result["num_steps"] = step + 1
                return result
            except json.JSONDecodeError:
                # Try to extract JSON with regex
                match = re.search(r'\{[^{}]*"overall_score"[^{}]*\}', json_str, re.DOTALL)
                if match:
                    try:
                        result = json.loads(match.group())
                        result["agent_trace"] = tool_trace
                        result["num_steps"] = step + 1
                        return result
                    except:
                        pass

        # Check for tool calls
        tool_calls = re.findall(r'TOOL_CALL:\s*(\w+)\(([^)]*)\)', content)
        if tool_calls:
            tool_results = []
            for tool_name, tool_arg in tool_calls:
                tool_arg = tool_arg.strip().strip('"').strip("'")
                if not tool_arg:
                    tool_arg = smiles  # Default to the molecule's SMILES
                if tool_name in TOOLS:
                    result = TOOLS[tool_name](tool_arg)
                    tool_results.append(f"Result of {tool_name}:\n{result}")
                    tool_trace.append({"step": step, "type": "tool", "name": tool_name, "result": result[:300]})
                else:
                    tool_results.append(f"Error: Unknown tool '{tool_name}'")

            messages.append({"role": "user", "content": "\n\n".join(tool_results) + "\n\nContinue your evaluation. If you have used all tools, provide your FINAL_ANSWER."})
        else:
            # No tool call and no final answer — ask for completion
            messages.append({"role": "user", "content": "Please provide your FINAL_ANSWER as JSON now."})

        time.sleep(1)  # Rate limiting

    # If we ran out of steps, return partial
    return {
        "drug_likeness": None, "admet_safety": None,
        "synthetic_feasibility": None, "clinical_potential": None,
        "overall_score": None, "recommendation": None,
        "concerns": [], "strengths": [],
        "reasoning": f"Agent did not converge in {max_steps} steps",
        "agent_trace": tool_trace, "num_steps": max_steps
    }


def main():
    with open(DATASET_PATH) as f:
        dataset = json.load(f)

    print(f"Loaded {len(dataset)} molecules")
    print(f"Model: {MODEL} (with RDKit tools)")
    print()

    client = OpenAI(base_url=API_BASE, api_key=API_KEY)

    # Test connectivity
    print("Testing API...")
    try:
        resp = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": "Reply: OK"}],
            max_tokens=10,
        )
        print(f"API OK: {resp.choices[0].message.content.strip()}")
    except Exception as e:
        print(f"API failed: {e}")
        return

    results = []
    for i, mol in enumerate(dataset):
        name = mol["name"]
        smiles = mol["smiles"]
        category = mol["category"]
        print(f"[{i+1}/{len(dataset)}] Agent evaluating {name} ({category})...")

        eval_result = run_agent(client, smiles, name)

        entry = {
            "name": name,
            "smiles": smiles,
            "category": category,
        }
        entry.update(eval_result)
        results.append(entry)

        time.sleep(1)

    # Save results
    with open(OUTPUT_PATH, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nResults saved to {OUTPUT_PATH}")

    # Summary
    print("\n=== Summary ===")
    for cat in ["A_approved", "B_clinical_failure", "C_decoy"]:
        cat_results = [r for r in results if r["category"] == cat and r.get("overall_score") is not None]
        if cat_results:
            scores = [r["overall_score"] for r in cat_results]
            avg = sum(scores) / len(scores)
            steps = [r.get("num_steps", 0) for r in cat_results]
            avg_steps = sum(steps) / len(steps)
            print(f"{cat}: avg_score={avg:.2f}, avg_steps={avg_steps:.1f}, n={len(cat_results)}")


if __name__ == "__main__":
    main()
