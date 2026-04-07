"""
Phase 2: Cross-System Statistical Analysis
Compares all agent systems on their ability to distinguish:
  A (approved drugs) vs B (clinical failures) vs C (decoys)
"""

import json
import math
import os
import numpy as np
from collections import defaultdict

BASE = os.path.dirname(__file__)


def load_results():
    """Load all available system results."""
    systems = {}

    # System 1: Direct LLM
    path = os.path.join(BASE, "results_llm_direct.json")
    if os.path.exists(path):
        with open(path) as f:
            data = json.load(f)
        systems["Direct LLM\n(Claude, no tools)"] = {
            "data": data,
            "score_key": "overall_score",
            "higher_is_better": True,
        }

    # System 2: LLM + Tools Agent
    path = os.path.join(BASE, "results_llm_agent.json")
    if os.path.exists(path):
        with open(path) as f:
            data = json.load(f)
        systems["LLM+Tools Agent\n(Claude+RDKit)"] = {
            "data": data,
            "score_key": "overall_score",
            "higher_is_better": True,
        }

    # System 3: DruGUI
    path = os.path.join(BASE, "results_drugui.json")
    if os.path.exists(path):
        with open(path) as f:
            data = json.load(f)
        systems["DruGUI\n(8-stage VS)"] = {
            "data": data,
            "score_key": "composite_score",
            "higher_is_better": True,
        }

    # System 4: ADMET-AI (if available)
    path = os.path.join(BASE, "results_admet_ai_system.json")
    if os.path.exists(path):
        with open(path) as f:
            data = json.load(f)
        # ADMET-AI needs special handling — use ClinTox score
        for mol in data:
            preds = mol.get("predictions", {})
            mol["clintox_score"] = preds.get("ClinTox", None)
        systems["ADMET-AI\n(Chemprop GNN)"] = {
            "data": data,
            "score_key": "clintox_score",
            "higher_is_better": False,  # Lower ClinTox = safer
        }

    # System 6: RDKit Pipeline (Phase 1 baseline)
    path = os.path.join(BASE, "results_rdkit_pipeline.json")
    if os.path.exists(path):
        with open(path) as f:
            data = json.load(f)
        systems["RDKit Pipeline\n(Phase 1)"] = {
            "data": data,
            "score_key": "composite_score",
            "higher_is_better": True,
        }

    return systems


def compute_auc(scores_pos, scores_neg):
    """Compute AUC (Mann-Whitney U statistic) without sklearn."""
    n_pos = len(scores_pos)
    n_neg = len(scores_neg)
    if n_pos == 0 or n_neg == 0:
        return 0.5

    count = 0
    for p in scores_pos:
        for n in scores_neg:
            if p > n:
                count += 1
            elif p == n:
                count += 0.5
    return count / (n_pos * n_neg)


def mann_whitney_u(x, y):
    """Simple Mann-Whitney U test."""
    nx, ny = len(x), len(y)
    if nx == 0 or ny == 0:
        return 0.5, 1.0

    all_vals = [(v, 0) for v in x] + [(v, 1) for v in y]
    all_vals.sort(key=lambda t: t[0])

    # Assign ranks
    ranks = []
    i = 0
    while i < len(all_vals):
        j = i
        while j < len(all_vals) and all_vals[j][0] == all_vals[i][0]:
            j += 1
        avg_rank = (i + j + 1) / 2  # 1-based
        for k in range(i, j):
            ranks.append((avg_rank, all_vals[k][1]))
        i = j

    r1 = sum(r for r, g in ranks if g == 0)
    u1 = r1 - nx * (nx + 1) / 2
    u = min(u1, nx * ny - u1)

    # Normal approximation for p-value
    mu = nx * ny / 2
    sigma = np.sqrt(nx * ny * (nx + ny + 1) / 12)
    if sigma == 0:
        return u, 1.0
    z = abs(u - mu) / sigma
    # Two-tailed p-value approximation
    p = 2 * (1 - 0.5 * (1 + math.erf(z / math.sqrt(2))))
    return u, p


def analyze_system(name, config):
    """Analyze a single system's results."""
    data = config["data"]
    score_key = config["score_key"]
    higher_is_better = config["higher_is_better"]

    cats = defaultdict(list)
    for mol in data:
        score = mol.get(score_key)
        if score is not None:
            cats[mol["category"]].append(float(score))

    results = {"name": name}
    for cat in ["A_approved", "B_clinical_failure", "C_decoy"]:
        vals = cats.get(cat, [])
        if vals:
            results[cat] = {
                "n": len(vals),
                "mean": np.mean(vals),
                "std": np.std(vals),
                "median": np.median(vals),
                "min": np.min(vals),
                "max": np.max(vals),
            }

    # AUC calculations
    a_scores = cats.get("A_approved", [])
    b_scores = cats.get("B_clinical_failure", [])
    c_scores = cats.get("C_decoy", [])

    if higher_is_better:
        results["AUC_A_vs_B"] = compute_auc(a_scores, b_scores)
        results["AUC_A_vs_C"] = compute_auc(a_scores, c_scores)
        results["AUC_A_vs_rest"] = compute_auc(a_scores, b_scores + c_scores)
    else:
        results["AUC_A_vs_B"] = compute_auc(b_scores, a_scores)
        results["AUC_A_vs_C"] = compute_auc(c_scores, a_scores)
        results["AUC_A_vs_rest"] = compute_auc(b_scores + c_scores, a_scores)

    # Mann-Whitney tests
    if a_scores and b_scores:
        _, p_ab = mann_whitney_u(a_scores, b_scores)
        results["p_A_vs_B"] = p_ab
    if a_scores and c_scores:
        _, p_ac = mann_whitney_u(a_scores, c_scores)
        results["p_A_vs_C"] = p_ac

    # Ranking order
    means = {}
    for cat in ["A_approved", "B_clinical_failure", "C_decoy"]:
        if cat in results and isinstance(results[cat], dict):
            means[cat] = results[cat]["mean"]

    if means:
        sorted_cats = sorted(means.items(), key=lambda x: x[1], reverse=higher_is_better)
        results["ranking"] = " > ".join([c.split("_")[0] for c, _ in sorted_cats])

    return results


def main():
    systems = load_results()
    print(f"Loaded {len(systems)} systems\n")

    all_results = []
    for name, config in systems.items():
        result = analyze_system(name, config)
        all_results.append(result)

        print(f"{'='*60}")
        print(f"System: {name.replace(chr(10), ' / ')}")
        print(f"{'='*60}")

        for cat in ["A_approved", "B_clinical_failure", "C_decoy"]:
            if cat in result and isinstance(result[cat], dict):
                r = result[cat]
                print(f"  {cat}: mean={r['mean']:.3f} ± {r['std']:.3f} "
                      f"(median={r['median']:.3f}, range=[{r['min']:.3f}, {r['max']:.3f}], n={r['n']})")

        print(f"  Ranking: {result.get('ranking', 'N/A')}")
        print(f"  AUC(A vs B): {result.get('AUC_A_vs_B', 'N/A'):.3f}")
        print(f"  AUC(A vs C): {result.get('AUC_A_vs_C', 'N/A'):.3f}")
        print(f"  AUC(A vs rest): {result.get('AUC_A_vs_rest', 'N/A'):.3f}")
        if "p_A_vs_B" in result:
            print(f"  p-value(A vs B): {result['p_A_vs_B']:.4f}")
        if "p_A_vs_C" in result:
            print(f"  p-value(A vs C): {result['p_A_vs_C']:.4f}")
        print()

    # Cross-system comparison table
    print("=" * 80)
    print("CROSS-SYSTEM COMPARISON TABLE")
    print("=" * 80)
    header = f"{'System':<25} {'A(mean)':<10} {'B(mean)':<10} {'C(mean)':<10} {'Ranking':<12} {'AUC(AvB)':<10} {'AUC(AvC)':<10}"
    print(header)
    print("-" * 80)

    for r in all_results:
        name = r["name"].replace("\n", " / ")[:24]
        a_mean = r.get("A_approved", {}).get("mean", 0)
        b_mean = r.get("B_clinical_failure", {}).get("mean", 0)
        c_mean = r.get("C_decoy", {}).get("mean", 0)
        ranking = r.get("ranking", "N/A")
        auc_ab = r.get("AUC_A_vs_B", 0)
        auc_ac = r.get("AUC_A_vs_C", 0)
        print(f"{name:<25} {a_mean:<10.3f} {b_mean:<10.3f} {c_mean:<10.3f} {ranking:<12} {auc_ab:<10.3f} {auc_ac:<10.3f}")

    print()

    # Key findings
    print("=" * 80)
    print("KEY FINDINGS")
    print("=" * 80)

    correct_rankings = [r for r in all_results if r.get("ranking") == "A > B > C"]
    inverted_rankings = [r for r in all_results if r.get("ranking", "").startswith("C")]
    decoy_trap = [r for r in all_results if "ranking" in r and r["ranking"] not in ["A > B > C", "A > C > B"] and r["ranking"].startswith("C")]

    print(f"1. Systems with correct ranking (A > B > C): {len(correct_rankings)}/{len(all_results)}")
    for r in correct_rankings:
        print(f"   - {r['name'].replace(chr(10), ' / ')}")

    print(f"2. Systems with inverted ranking (C first): {len(inverted_rankings)}/{len(all_results)}")
    for r in inverted_rankings:
        print(f"   - {r['name'].replace(chr(10), ' / ')}")

    # Tool augmentation effect
    llm_direct = next((r for r in all_results if "Direct" in r["name"]), None)
    llm_agent = next((r for r in all_results if "Agent" in r["name"]), None)

    if llm_direct and llm_agent:
        print(f"\n3. Tool Augmentation Effect:")
        print(f"   Direct LLM:  ranking={llm_direct.get('ranking', 'N/A')}, AUC(AvB)={llm_direct.get('AUC_A_vs_B', 0):.3f}")
        print(f"   LLM+Tools:   ranking={llm_agent.get('ranking', 'N/A')}, AUC(AvB)={llm_agent.get('AUC_A_vs_B', 0):.3f}")
        if llm_direct.get("ranking") == "A > B > C" and llm_agent.get("ranking") != "A > B > C":
            print(f"   => ADDING TOOLS WORSENS RANKING: LLM correctly ranks, but tools introduce Goodhart bias!")
        elif llm_agent.get("AUC_A_vs_B", 0) > llm_direct.get("AUC_A_vs_B", 0):
            print(f"   => Tools improve A-vs-B discrimination")

    # Goodhart effect
    pipeline_systems = [r for r in all_results if any(k in r["name"] for k in ["DruGUI", "RDKit"])]
    if pipeline_systems:
        print(f"\n4. Goodhart's Law Evidence:")
        for r in pipeline_systems:
            print(f"   {r['name'].replace(chr(10), ' / ')}: ranking={r.get('ranking', 'N/A')}")
        if all(r.get("ranking", "").startswith("C") for r in pipeline_systems):
            print(f"   => ALL computational pipelines rank decoys highest — metrics are anti-predictive!")

    # Save summary
    summary = {
        "systems": [{
            "name": r["name"].replace("\n", " / "),
            "ranking": r.get("ranking"),
            "A_mean": r.get("A_approved", {}).get("mean"),
            "B_mean": r.get("B_clinical_failure", {}).get("mean"),
            "C_mean": r.get("C_decoy", {}).get("mean"),
            "AUC_A_vs_B": r.get("AUC_A_vs_B"),
            "AUC_A_vs_C": r.get("AUC_A_vs_C"),
            "AUC_A_vs_rest": r.get("AUC_A_vs_rest"),
            "p_A_vs_B": r.get("p_A_vs_B"),
            "p_A_vs_C": r.get("p_A_vs_C"),
        } for r in all_results],
        "n_systems": len(all_results),
        "n_correct_ranking": len(correct_rankings),
        "n_inverted_ranking": len(inverted_rankings),
    }

    with open(os.path.join(BASE, "results_phase2_summary.json"), "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nSummary saved to experiments/results_phase2_summary.json")


if __name__ == "__main__":
    main()
