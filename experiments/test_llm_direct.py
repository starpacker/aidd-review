"""
Phase 2 - System 1: Direct LLM Evaluation
Test whether Claude's internal chemical knowledge can distinguish
approved drugs (A) from clinical failures (B) and decoys (C).

No tools — pure LLM reasoning from SMILES.
"""

import json
import time
import os
from openai import OpenAI

# === Config ===
API_BASE = "https://ai-gateway-internal.dp.tech/v1"
API_KEY = os.environ.get("AIDD_API_KEY", "YOUR_API_KEY_HERE")
MODEL = "cds/Claude-4.6-opus"
TEMPERATURE = 0.1  # Low temp for consistency

DATASET_PATH = os.path.join(os.path.dirname(__file__), "agent_evaluation_dataset.json")
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "results_llm_direct.json")

EVAL_PROMPT = """You are an expert medicinal chemist with 20 years of drug development experience.
Evaluate the following molecule as a drug candidate based ONLY on its SMILES structure.

SMILES: {smiles}

Score each dimension on a 1-10 scale (10 = best):
1. Drug-likeness: Does this molecule have properties consistent with successful oral drugs?
2. ADMET safety: Based on structural features, how likely is this molecule to have acceptable ADMET properties?
3. Synthetic feasibility: How easy is this molecule to synthesize?
4. Clinical potential: Overall, how likely is this molecule to succeed in clinical trials?

Also provide:
- An overall score (1-10, weighted average emphasizing clinical potential)
- A recommendation: "Advance" (score >= 7), "Caution" (4-6), or "Reject" (< 4)
- Key structural concerns (if any)
- Key structural strengths (if any)

IMPORTANT: Output ONLY valid JSON in this exact format:
{{
  "drug_likeness": <int>,
  "admet_safety": <int>,
  "synthetic_feasibility": <int>,
  "clinical_potential": <int>,
  "overall_score": <float>,
  "recommendation": "<Advance|Caution|Reject>",
  "concerns": ["<concern1>", ...],
  "strengths": ["<strength1>", ...],
  "reasoning": "<brief 2-3 sentence explanation>"
}}"""


def evaluate_molecule(client, smiles, name, retries=3):
    """Call Claude API to evaluate a single molecule."""
    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "user", "content": EVAL_PROMPT.format(smiles=smiles)}
                ],
                temperature=TEMPERATURE,
                max_tokens=1000,
            )
            content = response.choices[0].message.content.strip()
            # Try to extract JSON from response
            if "```json" in content:
                content = content.split("```json")[1].split("```")[0].strip()
            elif "```" in content:
                content = content.split("```")[1].split("```")[0].strip()
            result = json.loads(content)
            return result
        except json.JSONDecodeError as e:
            print(f"  JSON parse error for {name} (attempt {attempt+1}): {e}")
            print(f"  Raw response: {content[:200]}...")
            if attempt < retries - 1:
                time.sleep(2)
        except Exception as e:
            print(f"  API error for {name} (attempt {attempt+1}): {e}")
            if attempt < retries - 1:
                time.sleep(5)
    return None


def main():
    # Load dataset
    with open(DATASET_PATH) as f:
        dataset = json.load(f)

    print(f"Loaded {len(dataset)} molecules")
    print(f"API: {API_BASE}")
    print(f"Model: {MODEL}")
    print()

    client = OpenAI(base_url=API_BASE, api_key=API_KEY)

    # Test API connectivity first
    print("Testing API connectivity...")
    try:
        test_resp = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": "Reply with just: OK"}],
            max_tokens=10,
        )
        print(f"API OK: {test_resp.choices[0].message.content.strip()}")
    except Exception as e:
        print(f"API connection failed: {e}")
        return

    results = []
    for i, mol in enumerate(dataset):
        name = mol["name"]
        smiles = mol["smiles"]
        category = mol["category"]
        print(f"[{i+1}/{len(dataset)}] Evaluating {name} ({category})...")

        eval_result = evaluate_molecule(client, smiles, name)

        entry = {
            "name": name,
            "smiles": smiles,
            "category": category,
            **({k: v for k, v in eval_result.items()} if eval_result else {
                "drug_likeness": None,
                "admet_safety": None,
                "synthetic_feasibility": None,
                "clinical_potential": None,
                "overall_score": None,
                "recommendation": None,
                "concerns": [],
                "strengths": [],
                "reasoning": "API call failed"
            })
        }
        results.append(entry)

        # Rate limiting — be polite to the API
        time.sleep(1)

    # Save results
    with open(OUTPUT_PATH, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {OUTPUT_PATH}")

    # Quick summary
    print("\n=== Summary ===")
    for cat in ["A_approved", "B_clinical_failure", "C_decoy"]:
        cat_results = [r for r in results if r["category"] == cat and r["overall_score"] is not None]
        if cat_results:
            scores = [r["overall_score"] for r in cat_results]
            recs = [r["recommendation"] for r in cat_results]
            avg = sum(scores) / len(scores)
            advance = sum(1 for r in recs if r == "Advance")
            caution = sum(1 for r in recs if r == "Caution")
            reject = sum(1 for r in recs if r == "Reject")
            print(f"{cat}: avg_score={avg:.2f}, Advance={advance}, Caution={caution}, Reject={reject}")


if __name__ == "__main__":
    main()
