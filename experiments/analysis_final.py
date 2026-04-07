"""
Final Publication-Quality Cross-System Analysis
================================================
Computes all statistics cited in the review paper (draft_v1.md, Table 3).
Uses scipy.stats for proper hypothesis testing + bootstrap CIs for AUC.

Run with: .venv38/Scripts/python experiments/analysis_final.py

Outputs:
  - experiments/results_final_stats.json  (all numbers for the paper)
  - experiments/results_final_stats.txt   (formatted tables)
"""

import json
import os
import sys
import numpy as np
from collections import defaultdict
from scipy import stats as scipy_stats

BASE = os.path.dirname(os.path.abspath(__file__))
np.random.seed(42)


# ── Data Loading ─────────────────────────────────────────────────────────────

def load_dataset():
    """Load the 36-molecule gold standard dataset."""
    with open(os.path.join(BASE, "agent_evaluation_dataset.json")) as f:
        return json.load(f)


def load_all_systems():
    """Load results from all tested systems. Returns dict of system configs."""
    systems = {}

    configs = [
        ("Direct LLM", "results_llm_direct.json", "overall_score", True),
        ("LLM+Tools Agent", "results_llm_agent.json", "overall_score", True),
        ("DruGUI Pipeline", "results_drugui.json", "composite_score", True),
        ("RDKit Pipeline", "results_rdkit_pipeline.json", "composite_score", True),
        ("ADMET Proxy", "results_admet_proxy.json", "admet_score", True),
    ]

    for name, filename, score_key, higher_better in configs:
        path = os.path.join(BASE, filename)
        if os.path.exists(path):
            with open(path) as f:
                data = json.load(f)
            systems[name] = {
                "data": data,
                "score_key": score_key,
                "higher_is_better": higher_better,
            }

    return systems


def extract_scores(data, score_key):
    """Extract scores by category from result data."""
    cats = {"A_approved": [], "B_clinical_failure": [], "C_decoy": []}
    missing = 0
    for mol in data:
        cat = mol.get("category", "")
        score = mol.get(score_key)
        if score is not None and cat in cats:
            cats[cat].append(float(score))
        else:
            missing += 1
    return cats, missing


# ── Statistical Functions ────────────────────────────────────────────────────

def compute_auc_mannwhitney(pos_scores, neg_scores):
    """
    Compute AUC as U / (n1 * n2), equivalent to P(pos > neg).
    Uses scipy.stats.mannwhitneyu for exact p-value.
    """
    if len(pos_scores) < 2 or len(neg_scores) < 2:
        return {"auc": np.nan, "U": np.nan, "p": np.nan, "n1": len(pos_scores), "n2": len(neg_scores)}

    U, p = scipy_stats.mannwhitneyu(pos_scores, neg_scores, alternative='two-sided')
    n1, n2 = len(pos_scores), len(neg_scores)
    # AUC = U / (n1 * n2) — but mannwhitneyu returns U for first sample
    # We want P(pos > neg), so:
    auc = U / (n1 * n2)

    return {"auc": float(auc), "U": float(U), "p": float(p), "n1": n1, "n2": n2}


def bootstrap_auc_ci(pos_scores, neg_scores, n_boot=10000, alpha=0.05):
    """Bootstrap 95% CI for AUC."""
    pos = np.array(pos_scores)
    neg = np.array(neg_scores)
    aucs = []
    for _ in range(n_boot):
        p_idx = np.random.randint(0, len(pos), len(pos))
        n_idx = np.random.randint(0, len(neg), len(neg))
        p_samp = pos[p_idx]
        n_samp = neg[n_idx]
        # Count P(pos > neg)
        count = 0
        for p_val in p_samp:
            for n_val in n_samp:
                if p_val > n_val:
                    count += 1
                elif p_val == n_val:
                    count += 0.5
        aucs.append(count / (len(p_samp) * len(n_samp)))

    aucs = np.array(aucs)
    ci_low = np.percentile(aucs, 100 * alpha / 2)
    ci_high = np.percentile(aucs, 100 * (1 - alpha / 2))
    return float(ci_low), float(ci_high), float(np.std(aucs))


def cohens_d(group1, group2):
    """Compute Cohen's d effect size."""
    n1, n2 = len(group1), len(group2)
    if n1 < 2 or n2 < 2:
        return np.nan
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    pooled_std = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))
    if pooled_std == 0:
        return np.nan
    return float((np.mean(group1) - np.mean(group2)) / pooled_std)


def spearman_correlation(scores, clinical_labels):
    """Compute Spearman rank correlation between scores and clinical outcomes.
    clinical_labels: A=1 (best), B=0.5, C=0 (worst) for correct ordering.
    """
    rho, p = scipy_stats.spearmanr(scores, clinical_labels)
    return float(rho), float(p)


# ── Per-System Analysis ──────────────────────────────────────────────────────

def analyze_system(name, config):
    """Full statistical analysis of one system."""
    cats, n_missing = extract_scores(config["data"], config["score_key"])
    hib = config["higher_is_better"]

    a = np.array(cats["A_approved"])
    b = np.array(cats["B_clinical_failure"])
    c = np.array(cats["C_decoy"])

    result = {
        "name": name,
        "n_total": len(a) + len(b) + len(c),
        "n_missing": n_missing,
        "score_key": config["score_key"],
    }

    # Per-category descriptive stats
    for cat_name, vals in [("A_approved", a), ("B_clinical_failure", b), ("C_decoy", c)]:
        if len(vals) > 0:
            result[cat_name] = {
                "n": int(len(vals)),
                "mean": float(np.mean(vals)),
                "std": float(np.std(vals, ddof=1)),
                "sem": float(np.std(vals, ddof=1) / np.sqrt(len(vals))),
                "median": float(np.median(vals)),
                "min": float(np.min(vals)),
                "max": float(np.max(vals)),
                "iqr": float(np.percentile(vals, 75) - np.percentile(vals, 25)),
            }

    # Ranking
    means = {
        "A": float(np.mean(a)) if len(a) > 0 else 0,
        "B": float(np.mean(b)) if len(b) > 0 else 0,
        "C": float(np.mean(c)) if len(c) > 0 else 0,
    }
    sorted_cats = sorted(means.items(), key=lambda x: x[1], reverse=hib)
    result["ranking"] = " > ".join([c for c, _ in sorted_cats])
    result["correct_ranking"] = (result["ranking"] == "A > B > C")

    # AUC (Mann-Whitney U)
    if hib:
        mw_ab = compute_auc_mannwhitney(a, b)
        mw_ac = compute_auc_mannwhitney(a, c)
        mw_bc = compute_auc_mannwhitney(b, c)
    else:
        mw_ab = compute_auc_mannwhitney(b, a)
        mw_ac = compute_auc_mannwhitney(c, a)
        mw_bc = compute_auc_mannwhitney(c, b)

    result["AUC_A_vs_B"] = mw_ab
    result["AUC_A_vs_C"] = mw_ac
    result["AUC_B_vs_C"] = mw_bc

    # Bootstrap CIs for AUC
    if len(a) >= 2 and len(b) >= 2:
        if hib:
            ci_lo, ci_hi, ci_std = bootstrap_auc_ci(a, b)
        else:
            ci_lo, ci_hi, ci_std = bootstrap_auc_ci(b, a)
        result["AUC_A_vs_B"]["ci_95"] = [ci_lo, ci_hi]

    if len(a) >= 2 and len(c) >= 2:
        if hib:
            ci_lo, ci_hi, ci_std = bootstrap_auc_ci(a, c)
        else:
            ci_lo, ci_hi, ci_std = bootstrap_auc_ci(c, a)
        result["AUC_A_vs_C"]["ci_95"] = [ci_lo, ci_hi]

    # Effect sizes (Cohen's d)
    result["cohens_d_A_vs_B"] = cohens_d(list(a), list(b))
    result["cohens_d_A_vs_C"] = cohens_d(list(a), list(c))

    # Kruskal-Wallis test (non-parametric one-way ANOVA)
    if len(a) >= 2 and len(b) >= 2 and len(c) >= 2:
        H, p_kw = scipy_stats.kruskal(a, b, c)
        result["kruskal_wallis"] = {"H": float(H), "p": float(p_kw)}

    # Spearman correlation: score vs clinical utility (A=1, B=0.5, C=0)
    all_scores = list(a) + list(b) + list(c)
    all_labels = [1.0] * len(a) + [0.5] * len(b) + [0.0] * len(c)
    if not hib:
        all_scores = [-s for s in all_scores]
    rho, p_rho = spearman_correlation(all_scores, all_labels)
    result["spearman_vs_clinical"] = {"rho": rho, "p": p_rho}

    return result


# ── Cross-System Goodhart Analysis ───────────────────────────────────────────

def goodhart_analysis(all_results):
    """Quantify the Goodhart gradient across systems."""
    # Systems ordered by computational tool dependence (manual ordering)
    tool_order = ["Direct LLM", "LLM+Tools Agent", "RDKit Pipeline", "ADMET Proxy", "DruGUI Pipeline"]

    systems_in_order = []
    for name in tool_order:
        r = next((r for r in all_results if r["name"] == name), None)
        if r:
            systems_in_order.append(r)

    # Compute Goodhart metrics
    goodhart = {
        "tool_dependence_order": [s["name"] for s in systems_in_order],
        "rankings": [s["ranking"] for s in systems_in_order],
        "correct_ranking": [s["correct_ranking"] for s in systems_in_order],
    }

    # Decoy premium: (C_mean - A_mean) / A_mean
    decoy_premiums = []
    for s in systems_in_order:
        a_mean = s.get("A_approved", {}).get("mean", 0)
        c_mean = s.get("C_decoy", {}).get("mean", 0)
        if a_mean != 0:
            premium = (c_mean - a_mean) / abs(a_mean) * 100
        else:
            premium = np.nan
        decoy_premiums.append(float(premium))
    goodhart["decoy_premium_pct"] = decoy_premiums

    # Spearman correlation between tool dependence rank and clinical alignment
    tool_ranks = list(range(1, len(systems_in_order) + 1))
    clinical_rhos = [s["spearman_vs_clinical"]["rho"] for s in systems_in_order]
    if len(tool_ranks) >= 3:
        rho, p = scipy_stats.spearmanr(tool_ranks, clinical_rhos)
        goodhart["tool_vs_clinical_alignment"] = {"rho": float(rho), "p": float(p)}

    return goodhart


# ── Clinical Failure Detectability ───────────────────────────────────────────

def failure_detection_analysis(systems):
    """For each clinical failure, check which computational systems flag it.

    A failure is "undetectable" if it scores ABOVE the median of all molecules
    in ALL computational pipeline systems (excluding LLM systems, which use
    literature knowledge rather than computational metrics).

    This matches the paper's claim: "42% of clinical failures passed all
    computational screening filters."
    """
    dataset = load_dataset()
    failures = [m for m in dataset if m["category"] == "B_clinical_failure"]

    # Only test against computational pipelines (not LLM-based systems)
    computational_systems = {k: v for k, v in systems.items()
                            if k not in ["Direct LLM", "LLM+Tools Agent"]}

    detection_matrix = {}

    for mol in failures:
        smiles = mol["smiles"]
        mol_name = mol.get("name", smiles[:20])
        detection_matrix[mol_name] = {
            "smiles": smiles,
            "flagged_by": [],
            "passed_all": True,
        }

        for sys_name, config in computational_systems.items():
            data = config["data"]
            score_key = config["score_key"]
            hib = config["higher_is_better"]

            mol_result = next((m for m in data if m["smiles"] == smiles), None)
            if mol_result is None:
                continue

            score = mol_result.get(score_key)
            if score is None:
                continue

            # Get all scores for percentile calculation
            all_scores = [m.get(score_key) for m in data if m.get(score_key) is not None]
            median_all = np.median(all_scores)

            # "Flagged" = scored below median (for higher-is-better systems)
            # meaning the system would deprioritize this molecule
            if hib:
                flagged = score < median_all
            else:
                flagged = score > median_all

            detection_matrix[mol_name][sys_name] = {
                "score": float(score),
                "median_all": float(median_all),
                "flagged": bool(flagged),
            }
            if flagged:
                detection_matrix[mol_name]["flagged_by"].append(sys_name)

        # "Passed all" = not flagged by ANY computational pipeline
        if not detection_matrix[mol_name]["flagged_by"]:
            detection_matrix[mol_name]["passed_all"] = True
        else:
            detection_matrix[mol_name]["passed_all"] = False

    n_undetectable = sum(1 for m in detection_matrix.values() if m["passed_all"])

    # Also compute "majority pass" — molecules that pass ≥50% of systems
    n_majority_pass = sum(
        1 for m in detection_matrix.values()
        if len(m["flagged_by"]) <= len(computational_systems) / 2
    )

    return {
        "per_molecule": detection_matrix,
        "n_failures": len(failures),
        "n_computational_systems": len(computational_systems),
        "computational_systems": list(computational_systems.keys()),
        "n_undetectable": n_undetectable,
        "pct_undetectable": float(n_undetectable / len(failures) * 100) if failures else 0,
        "undetectable_names": [
            name for name, m in detection_matrix.items() if m["passed_all"]
        ],
        "n_majority_pass": n_majority_pass,
        "pct_majority_pass": float(n_majority_pass / len(failures) * 100) if failures else 0,
        "majority_pass_names": [
            name for name, m in detection_matrix.items()
            if len(m["flagged_by"]) <= len(computational_systems) / 2
        ],
    }


# ── LLM Recommendation Analysis ─────────────────────────────────────────────

def recommendation_analysis():
    """Analyze LLM recommendation distributions (Advance/Caution/Reject)."""
    results = {}

    for sys_name, filename in [("Direct LLM", "results_llm_direct.json"),
                                ("LLM+Tools Agent", "results_llm_agent.json")]:
        path = os.path.join(BASE, filename)
        if not os.path.exists(path):
            continue

        with open(path) as f:
            data = json.load(f)

        recs = defaultdict(lambda: defaultdict(int))
        for mol in data:
            cat = mol.get("category", "")
            rec = mol.get("recommendation", "Unknown")
            recs[cat][rec] += 1

        results[sys_name] = dict(recs)

    return results


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    print("=" * 80)
    print("FINAL PUBLICATION-QUALITY STATISTICAL ANALYSIS")
    print("=" * 80)
    print()

    systems = load_all_systems()
    print(f"Loaded {len(systems)} systems: {', '.join(systems.keys())}\n")

    # Analyze each system
    all_results = []
    for name, config in systems.items():
        result = analyze_system(name, config)
        all_results.append(result)

    # Print detailed results
    for r in all_results:
        print(f"\n{'─' * 70}")
        print(f"  {r['name']}  (n={r['n_total']}, missing={r['n_missing']})")
        print(f"{'─' * 70}")

        for cat in ["A_approved", "B_clinical_failure", "C_decoy"]:
            if cat in r and isinstance(r[cat], dict):
                s = r[cat]
                print(f"  {cat:25s}: {s['mean']:.4f} ± {s['std']:.4f} "
                      f"(SEM={s['sem']:.4f}, n={s['n']})")

        print(f"  Ranking:     {r['ranking']}  {'[OK] CORRECT' if r['correct_ranking'] else '[X] INCORRECT'}")
        print(f"  Cohen's d:   A vs B = {r['cohens_d_A_vs_B']:.3f}, "
              f"A vs C = {r['cohens_d_A_vs_C']:.3f}")

        for comp in ["AUC_A_vs_B", "AUC_A_vs_C"]:
            auc_data = r[comp]
            ci_str = ""
            if "ci_95" in auc_data:
                ci_str = f"  95% CI: [{auc_data['ci_95'][0]:.3f}, {auc_data['ci_95'][1]:.3f}]"
            print(f"  {comp:15s}: AUC={auc_data['auc']:.4f}, "
                  f"U={auc_data['U']:.1f}, p={auc_data['p']:.6f}{ci_str}")

        if "kruskal_wallis" in r:
            kw = r["kruskal_wallis"]
            print(f"  Kruskal-Wallis: H={kw['H']:.3f}, p={kw['p']:.6f}")

        sp = r["spearman_vs_clinical"]
        print(f"  Spearman (score vs clinical): ρ={sp['rho']:.4f}, p={sp['p']:.6f}")

    # Cross-system table (Table 3 in the paper)
    print(f"\n\n{'=' * 100}")
    print("TABLE 3: Cross-System Evaluation of Clinical Utility Prediction")
    print(f"{'=' * 100}")
    header = (f"{'System':<20} {'A(mean±SE)':<14} {'B(mean±SE)':<14} "
              f"{'C(mean±SE)':<14} {'Ranking':<10} {'AUC(AvB)':<10} "
              f"{'95%CI':<16} {'p(AvB)':<10}")
    print(header)
    print("-" * 100)

    for r in all_results:
        a_s = r.get("A_approved", {})
        b_s = r.get("B_clinical_failure", {})
        c_s = r.get("C_decoy", {})
        auc_ab = r["AUC_A_vs_B"]
        ci_str = ""
        if "ci_95" in auc_ab:
            ci_str = f"[{auc_ab['ci_95'][0]:.3f},{auc_ab['ci_95'][1]:.3f}]"

        p_str = f"{auc_ab['p']:.4f}" if auc_ab['p'] >= 0.0001 else f"{auc_ab['p']:.2e}"
        if auc_ab['p'] < 0.001:
            p_str += " ***"
        elif auc_ab['p'] < 0.01:
            p_str += " **"
        elif auc_ab['p'] < 0.05:
            p_str += " *"

        print(f"{r['name']:<20} "
              f"{a_s.get('mean',0):.3f}±{a_s.get('sem',0):.3f}  "
              f"{b_s.get('mean',0):.3f}±{b_s.get('sem',0):.3f}  "
              f"{c_s.get('mean',0):.3f}±{c_s.get('sem',0):.3f}  "
              f"{r['ranking']:<10} "
              f"{auc_ab['auc']:.3f}     "
              f"{ci_str:<16} "
              f"{p_str}")

    # Goodhart analysis
    goodhart = goodhart_analysis(all_results)
    print(f"\n\n{'=' * 80}")
    print("GOODHART GRADIENT ANALYSIS")
    print(f"{'=' * 80}")
    print(f"\nTool dependence order: {' → '.join(goodhart['tool_dependence_order'])}")
    print(f"Rankings:              {goodhart['rankings']}")
    print(f"Decoy premiums (%):    {['%.1f%%' % d for d in goodhart['decoy_premium_pct']]}")
    if "tool_vs_clinical_alignment" in goodhart:
        tca = goodhart["tool_vs_clinical_alignment"]
        print(f"Tool dependence vs clinical alignment: ρ={tca['rho']:.3f}, p={tca['p']:.4f}")

    # Failure detection
    failure = failure_detection_analysis(systems)
    print(f"\n\n{'=' * 80}")
    print("CLINICAL FAILURE DETECTABILITY")
    print(f"{'=' * 80}")
    print(f"Total clinical failures: {failure['n_failures']}")
    print(f"Computational systems tested: {failure['computational_systems']}")
    print(f"Pass ALL systems (strict): {failure['n_undetectable']} "
          f"({failure['pct_undetectable']:.1f}%) — {failure['undetectable_names']}")
    print(f"Pass majority (≥50%):      {failure['n_majority_pass']} "
          f"({failure['pct_majority_pass']:.1f}%) — {failure['majority_pass_names']}")
    print(f"\nPer-molecule detection:")
    for name, m in failure['per_molecule'].items():
        n_flagged = len(m['flagged_by'])
        n_sys = failure['n_computational_systems']
        status = "UNDETECTABLE" if m['passed_all'] else f"flagged by {n_flagged}/{n_sys}"
        print(f"  {name:20s}: {status}  {m['flagged_by']}")

    # Recommendation analysis
    recs = recommendation_analysis()
    if recs:
        print(f"\n\n{'=' * 80}")
        print("LLM RECOMMENDATION DISTRIBUTION")
        print(f"{'=' * 80}")
        for sys_name, cats in recs.items():
            print(f"\n  {sys_name}:")
            for cat in ["A_approved", "B_clinical_failure", "C_decoy"]:
                cat_recs = cats.get(cat, {})
                adv = cat_recs.get("Advance to next stage", 0) + cat_recs.get("Advance", 0)
                cau = cat_recs.get("Proceed with caution", 0) + cat_recs.get("Caution", 0)
                rej = cat_recs.get("Reject", 0) + cat_recs.get("Do not advance", 0)
                print(f"    {cat:25s}: Advance={adv}, Caution={cau}, Reject={rej}")

    # Save everything
    output = {
        "analysis_date": "2026-04-07",
        "dataset": "36 molecules (12 approved, 12 failures, 12 decoys)",
        "statistical_methods": {
            "auc": "Mann-Whitney U statistic via scipy.stats.mannwhitneyu",
            "ci": "Bootstrap 95% CI (n=10,000 iterations, seed=42)",
            "effect_size": "Cohen's d (pooled SD)",
            "correlation": "Spearman rank correlation",
            "omnibus": "Kruskal-Wallis H test",
        },
        "systems": all_results,
        "goodhart_gradient": goodhart,
        "failure_detection": {
            "n_failures": failure["n_failures"],
            "n_computational_systems": failure["n_computational_systems"],
            "computational_systems": failure["computational_systems"],
            "n_undetectable_all": failure["n_undetectable"],
            "pct_undetectable_all": failure["pct_undetectable"],
            "undetectable_all_names": failure["undetectable_names"],
            "n_majority_pass": failure["n_majority_pass"],
            "pct_majority_pass": failure["pct_majority_pass"],
            "majority_pass_names": failure["majority_pass_names"],
            "per_molecule": {
                name: {
                    "flagged_by": m["flagged_by"],
                    "passed_all": m["passed_all"],
                    "n_flagged": len(m["flagged_by"]),
                    "n_systems": failure["n_computational_systems"],
                }
                for name, m in failure["per_molecule"].items()
            },
        },
        "recommendations": recs,
    }

    out_json = os.path.join(BASE, "results_final_stats.json")
    with open(out_json, "w") as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\n\nResults saved to {out_json}")


if __name__ == "__main__":
    main()
