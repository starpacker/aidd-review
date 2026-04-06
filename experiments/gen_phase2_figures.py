"""
Phase 2: Publication-Quality Figures
Generates comparison figures across all tested agent systems.
"""

import json
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

BASE = os.path.dirname(__file__)
FIG_DIR = os.path.join(os.path.dirname(BASE), "figures_data")
os.makedirs(FIG_DIR, exist_ok=True)

# Color scheme — consistent across all figures
COLORS = {
    "A_approved": "#2ecc71",       # Green
    "B_clinical_failure": "#e74c3c",  # Red
    "C_decoy": "#3498db",           # Blue
}
CAT_LABELS = {
    "A_approved": "A: FDA-Approved",
    "B_clinical_failure": "B: Clinical Failures",
    "C_decoy": "C: Decoys",
}


def load_all_systems():
    """Load results from all completed systems."""
    systems = {}

    # System 1: Direct LLM
    with open(os.path.join(BASE, "results_llm_direct.json")) as f:
        systems["Direct LLM\n(no tools)"] = {
            "data": json.load(f),
            "key": "overall_score",
            "higher_better": True,
        }

    # System 2: LLM+Tools Agent
    with open(os.path.join(BASE, "results_llm_agent.json")) as f:
        systems["LLM+Tools\nAgent"] = {
            "data": json.load(f),
            "key": "overall_score",
            "higher_better": True,
        }

    # System 3: DruGUI
    with open(os.path.join(BASE, "results_drugui.json")) as f:
        systems["DruGUI\n(8-stage VS)"] = {
            "data": json.load(f),
            "key": "composite_score",
            "higher_better": True,
        }

    # System 6: RDKit Pipeline
    with open(os.path.join(BASE, "results_rdkit_pipeline.json")) as f:
        systems["RDKit\nPipeline"] = {
            "data": json.load(f),
            "key": "composite_score",
            "higher_better": True,
        }

    return systems


def get_category_scores(data, key):
    """Extract scores by category."""
    cats = {}
    for cat in ["A_approved", "B_clinical_failure", "C_decoy"]:
        vals = [m[key] for m in data if m["category"] == cat and m.get(key) is not None]
        cats[cat] = [float(v) for v in vals]
    return cats


# ========================================================
# Figure 1: Cross-System Category Comparison (Grouped Bar)
# ========================================================
def fig1_system_comparison(systems):
    fig, ax = plt.subplots(figsize=(10, 6))

    sys_names = list(systems.keys())
    n_sys = len(sys_names)
    x = np.arange(n_sys)
    width = 0.25

    for i, cat in enumerate(["A_approved", "B_clinical_failure", "C_decoy"]):
        means = []
        stds = []
        for name in sys_names:
            scores = get_category_scores(systems[name]["data"], systems[name]["key"])
            vals = scores.get(cat, [])
            if vals:
                means.append(np.mean(vals))
                stds.append(np.std(vals))
            else:
                means.append(0)
                stds.append(0)

        # Normalize to 0-1 range per system for comparability
        bars = ax.bar(x + (i - 1) * width, means, width,
                      yerr=stds, capsize=3,
                      color=COLORS[cat], label=CAT_LABELS[cat],
                      alpha=0.85, edgecolor='white', linewidth=0.5)

    ax.set_xlabel("AI Agent System", fontsize=12, fontweight='bold')
    ax.set_ylabel("Mean Score", fontsize=12, fontweight='bold')
    ax.set_title("Cross-System Evaluation: Score Distribution by Molecule Category",
                 fontsize=13, fontweight='bold', pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(sys_names, fontsize=10)
    ax.legend(loc='upper right', fontsize=10, framealpha=0.9)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Add ranking annotations
    for i, name in enumerate(sys_names):
        scores = get_category_scores(systems[name]["data"], systems[name]["key"])
        means_dict = {c: np.mean(v) for c, v in scores.items() if v}
        sorted_cats = sorted(means_dict.items(), key=lambda x: x[1], reverse=True)
        ranking = " > ".join([c.split("_")[0] for c, _ in sorted_cats])
        ax.annotate(ranking, xy=(i, ax.get_ylim()[1] * 0.02),
                    ha='center', fontsize=8, fontstyle='italic', color='#555')

    plt.tight_layout()
    path = os.path.join(FIG_DIR, "fig_phase2_system_comparison.png")
    plt.savefig(path, dpi=300, bbox_inches='tight')
    plt.savefig(path.replace('.png', '.pdf'), bbox_inches='tight')
    print(f"Saved: {path}")
    plt.close()


# ========================================================
# Figure 2: Normalized Comparison (all on 0-1 scale)
# ========================================================
def fig2_normalized_comparison(systems):
    fig, ax = plt.subplots(figsize=(10, 6))

    sys_names = list(systems.keys())
    n_sys = len(sys_names)

    # Normalize scores within each system to 0-1
    normalized = {}
    for name in sys_names:
        scores = get_category_scores(systems[name]["data"], systems[name]["key"])
        all_vals = sum(scores.values(), [])
        if all_vals:
            vmin, vmax = min(all_vals), max(all_vals)
            rng = vmax - vmin if vmax > vmin else 1
            normalized[name] = {
                cat: [(v - vmin) / rng for v in vals]
                for cat, vals in scores.items()
            }

    x = np.arange(n_sys)
    width = 0.25

    for i, cat in enumerate(["A_approved", "B_clinical_failure", "C_decoy"]):
        means = [np.mean(normalized[n][cat]) if normalized[n][cat] else 0 for n in sys_names]
        stds = [np.std(normalized[n][cat]) if normalized[n][cat] else 0 for n in sys_names]
        ax.bar(x + (i - 1) * width, means, width,
               yerr=stds, capsize=3,
               color=COLORS[cat], label=CAT_LABELS[cat],
               alpha=0.85, edgecolor='white')

    ax.set_xlabel("AI Agent System", fontsize=12, fontweight='bold')
    ax.set_ylabel("Normalized Score (0-1)", fontsize=12, fontweight='bold')
    ax.set_title("Normalized Cross-System Comparison\n(Within-system min-max normalization)",
                 fontsize=13, fontweight='bold', pad=10)
    ax.set_xticks(x)
    ax.set_xticklabels(sys_names, fontsize=10)
    ax.legend(fontsize=10, framealpha=0.9)
    ax.set_ylim(0, 1.1)
    ax.axhline(y=0.5, color='gray', linestyle='--', alpha=0.3)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    path = os.path.join(FIG_DIR, "fig_phase2_normalized_comparison.png")
    plt.savefig(path, dpi=300, bbox_inches='tight')
    plt.savefig(path.replace('.png', '.pdf'), bbox_inches='tight')
    print(f"Saved: {path}")
    plt.close()


# ========================================================
# Figure 3: AUC Comparison Bar Chart
# ========================================================
def compute_auc(pos, neg):
    n_pos, n_neg = len(pos), len(neg)
    if n_pos == 0 or n_neg == 0:
        return 0.5
    count = sum(1 for p in pos for n in neg if p > n) + 0.5 * sum(1 for p in pos for n in neg if p == n)
    return count / (n_pos * n_neg)


def fig3_auc_comparison(systems):
    fig, ax = plt.subplots(figsize=(10, 5))

    sys_names = list(systems.keys())
    x = np.arange(len(sys_names))
    width = 0.35

    auc_ab = []
    auc_ac = []

    for name in sys_names:
        scores = get_category_scores(systems[name]["data"], systems[name]["key"])
        a = scores.get("A_approved", [])
        b = scores.get("B_clinical_failure", [])
        c = scores.get("C_decoy", [])
        auc_ab.append(compute_auc(a, b))
        auc_ac.append(compute_auc(a, c))

    bars1 = ax.bar(x - width/2, auc_ab, width, label='AUC (A vs B)', color='#e67e22', alpha=0.85)
    bars2 = ax.bar(x + width/2, auc_ac, width, label='AUC (A vs C)', color='#9b59b6', alpha=0.85)

    ax.axhline(y=0.5, color='red', linestyle='--', alpha=0.5, label='Random (0.5)')
    ax.set_xlabel("AI Agent System", fontsize=12, fontweight='bold')
    ax.set_ylabel("AUC", fontsize=12, fontweight='bold')
    ax.set_title("Discrimination Power: AUC Across Systems",
                 fontsize=13, fontweight='bold', pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(sys_names, fontsize=10)
    ax.set_ylim(0, 1.05)
    ax.legend(fontsize=10, framealpha=0.9)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Add value labels
    for bars in [bars1, bars2]:
        for bar in bars:
            h = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., h + 0.02,
                    f'{h:.2f}', ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    path = os.path.join(FIG_DIR, "fig_phase2_auc_comparison.png")
    plt.savefig(path, dpi=300, bbox_inches='tight')
    plt.savefig(path.replace('.png', '.pdf'), bbox_inches='tight')
    print(f"Saved: {path}")
    plt.close()


# ========================================================
# Figure 4: Goodhart Gradient (LLM → Agent → Pipeline)
# ========================================================
def fig4_goodhart_gradient(systems):
    fig, ax = plt.subplots(figsize=(10, 5))

    # Order: Pure LLM → Agent → DruGUI → RDKit
    order = ["Direct LLM\n(no tools)", "LLM+Tools\nAgent", "DruGUI\n(8-stage VS)", "RDKit\nPipeline"]
    x_labels = ["Pure LLM\n(no tools)", "LLM + Tools\n(Agent)", "DruGUI\n(Pipeline)", "RDKit\n(Pipeline)"]

    # Compute normalized advantage: (A_mean - C_mean) / A_mean
    # Positive = A ranked above C (correct)
    # Negative = C ranked above A (Goodhart inversion)
    advantages = []
    for name in order:
        scores = get_category_scores(systems[name]["data"], systems[name]["key"])
        a_mean = np.mean(scores["A_approved"]) if scores["A_approved"] else 0
        c_mean = np.mean(scores["C_decoy"]) if scores["C_decoy"] else 0
        if a_mean != 0:
            adv = (a_mean - c_mean) / a_mean * 100
        else:
            adv = 0
        advantages.append(adv)

    colors = ['#27ae60' if a > 0 else '#c0392b' for a in advantages]
    bars = ax.bar(range(len(order)), advantages, color=colors, alpha=0.85,
                  edgecolor='white', linewidth=1)

    ax.axhline(y=0, color='black', linewidth=1)
    ax.set_xlabel("System (increasing reliance on computational metrics →)", fontsize=11, fontweight='bold')
    ax.set_ylabel("Approved Drug Advantage over Decoys (%)", fontsize=11, fontweight='bold')
    ax.set_title("The Goodhart Gradient: More Tools = More Metric Bias",
                 fontsize=13, fontweight='bold', pad=15)
    ax.set_xticks(range(len(order)))
    ax.set_xticklabels(x_labels, fontsize=10)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Value labels
    for bar, adv in zip(bars, advantages):
        h = bar.get_height()
        y_pos = h + 1 if h >= 0 else h - 3
        ax.text(bar.get_x() + bar.get_width()/2., y_pos,
                f'{adv:+.1f}%', ha='center', va='bottom' if h >= 0 else 'top',
                fontsize=11, fontweight='bold')

    # Annotation — position to avoid overlap
    ymax = max(advantages)
    ymin = min(advantages)
    ax.annotate("Correct direction\n(A > C)", xy=(0.5, ymax * 0.85),
                fontsize=9, ha='center', color='#27ae60', fontstyle='italic')
    ax.annotate("Goodhart inversion\n(C > A)", xy=(3.2, ymin * 1.6),
                fontsize=9, ha='center', color='#c0392b', fontstyle='italic')

    # Arrow showing gradient — below the bars
    arrow_y = ymin * 2.2
    ax.annotate('', xy=(3.5, arrow_y), xytext=(0.5, arrow_y),
                arrowprops=dict(arrowstyle='->', color='gray', lw=1.5))
    ax.text(2, arrow_y - abs(ymin) * 0.4, "More computational reliance",
            ha='center', fontsize=8, color='gray', fontstyle='italic')
    ax.set_ylim(ymin * 3, ymax * 1.3)

    plt.tight_layout()
    path = os.path.join(FIG_DIR, "fig_phase2_goodhart_gradient.png")
    plt.savefig(path, dpi=300, bbox_inches='tight')
    plt.savefig(path.replace('.png', '.pdf'), bbox_inches='tight')
    print(f"Saved: {path}")
    plt.close()


# ========================================================
# Figure 5: LLM Recommendation Heatmap
# ========================================================
def fig5_recommendation_heatmap(systems):
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    for idx, (sys_name, ax_title) in enumerate([
        ("Direct LLM\n(no tools)", "System 1: Direct LLM"),
        ("LLM+Tools\nAgent", "System 2: LLM+Tools Agent"),
    ]):
        ax = axes[idx]
        data = systems[sys_name]["data"]

        # Create recommendation matrix
        cats = ["A_approved", "B_clinical_failure", "C_decoy"]
        recs = ["Advance", "Caution", "Reject"]
        matrix = np.zeros((3, 3))

        for mol in data:
            cat_idx = cats.index(mol["category"]) if mol["category"] in cats else -1
            rec = mol.get("recommendation", "")
            rec_idx = recs.index(rec) if rec in recs else -1
            if cat_idx >= 0 and rec_idx >= 0:
                matrix[cat_idx][rec_idx] += 1

        im = ax.imshow(matrix, cmap='YlOrRd', aspect='auto')

        ax.set_xticks(range(3))
        ax.set_xticklabels(recs, fontsize=10)
        ax.set_yticks(range(3))
        ax.set_yticklabels(["A: Approved", "B: Failed", "C: Decoy"], fontsize=10)
        ax.set_title(ax_title, fontsize=12, fontweight='bold')

        # Add text
        for i in range(3):
            for j in range(3):
                text = ax.text(j, i, f'{int(matrix[i][j])}',
                              ha='center', va='center', fontsize=14, fontweight='bold',
                              color='white' if matrix[i][j] > 6 else 'black')

        fig.colorbar(im, ax=ax, shrink=0.8, label='Count')

    fig.suptitle("LLM Recommendation Distribution: Pure LLM vs Tool-Augmented Agent",
                 fontsize=13, fontweight='bold', y=1.02)
    plt.tight_layout()
    path = os.path.join(FIG_DIR, "fig_phase2_recommendation_heatmap.png")
    plt.savefig(path, dpi=300, bbox_inches='tight')
    plt.savefig(path.replace('.png', '.pdf'), bbox_inches='tight')
    print(f"Saved: {path}")
    plt.close()


def main():
    print("Loading system results...")
    systems = load_all_systems()
    print(f"Loaded {len(systems)} systems\n")

    print("Generating figures...")
    fig1_system_comparison(systems)
    fig2_normalized_comparison(systems)
    fig3_auc_comparison(systems)
    fig4_goodhart_gradient(systems)
    fig5_recommendation_heatmap(systems)

    print(f"\nAll figures saved to {FIG_DIR}/")


if __name__ == "__main__":
    main()
