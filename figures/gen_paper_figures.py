"""
Generate all 6 publication figures for the AIDD review paper.
Uses .venv38 (Python 3.8 + matplotlib + numpy).

Figure 1: The Precision Paradox (Phase I vs II success rates)
Figure 2: Pipeline Architecture with Assumptions (conceptual - text-based)
Figure 3: Cascading Valley of Death (waterfall attrition)
Figure 4: Goodhart Gradient (our key empirical finding)
Figure 5: Integration Framework (3-layer solution)
Figure 6: Strategic Timeline (milestones 2020-2030)
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

# Consistent style
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans'],
    'font.size': 9,
    'axes.titlesize': 12,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.spines.top': False,
    'axes.spines.right': False,
})

OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'figures')
os.makedirs(OUT_DIR, exist_ok=True)

# Colors
C_AI = '#e74c3c'       # red for AI
C_TRAD = '#3498db'     # blue for traditional
C_APPROVED = '#2ecc71'
C_FAILURE = '#e74c3c'
C_DECOY = '#3498db'
C_ACCENT = '#e67e22'
C_DARK = '#2c3e50'
C_GRAY = '#95a5a6'


def fig1_precision_paradox():
    """Figure 1: The Precision Paradox — AI doubles Phase I but not Phase II."""
    fig, ax = plt.subplots(figsize=(7, 4.5))

    phases = ['Phase I\n(Safety)', 'Phase II\n(Efficacy)', 'Phase III\n(Pivotal)', 'Overall\n(I → Approval)']
    traditional = [52.0, 28.9, 57.8, 7.9]
    ai_native = [85, 40, None, None]  # Phase III and Overall not available

    x = np.arange(len(phases))
    width = 0.35

    bars_trad = ax.bar(x - width/2, traditional, width, label='Traditional (BIO 2021, n=12,728)',
                       color=C_TRAD, edgecolor='white', linewidth=0.5, alpha=0.85)

    # AI bars only where data exists
    ai_vals = [85, 40, 0, 0]
    ai_colors = [C_AI, C_AI, 'none', 'none']
    bars_ai = ax.bar(x + width/2, ai_vals, width, label='AI-Native (Jayatunga 2024, n=75)',
                     color=C_AI, edgecolor='white', linewidth=0.5, alpha=0.85)
    # Hide bars with no data
    bars_ai[2].set_visible(False)
    bars_ai[3].set_visible(False)

    # Value labels
    for bar, val in zip(bars_trad, traditional):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1.5,
                f'{val}%', ha='center', va='bottom', fontsize=8, fontweight='bold', color=C_TRAD)
    for bar, val in zip(bars_ai[:2], [85, 40]):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1.5,
                f'~{val}%', ha='center', va='bottom', fontsize=8, fontweight='bold', color=C_AI)

    # Annotation: the gap
    ax.annotate('', xy=(1 + width/2, 40), xytext=(1 + width/2, 85),
                arrowprops=dict(arrowstyle='<->', color=C_ACCENT, lw=2))
    ax.text(1 + width/2 + 0.15, 62, 'The\nBiology\nProblem', fontsize=8, color=C_ACCENT,
            fontweight='bold', ha='left', va='center')

    # "Insufficient data" labels
    ax.text(x[2] + width/2, 5, 'Insufficient\ndata', ha='center', va='bottom',
            fontsize=7, color=C_GRAY, style='italic')
    ax.text(x[3] + width/2, 5, 'Insufficient\ndata', ha='center', va='bottom',
            fontsize=7, color=C_GRAY, style='italic')

    # Phase I improvement annotation
    ax.annotate('', xy=(0 - width/2, 52), xytext=(0 + width/2, 85),
                arrowprops=dict(arrowstyle='->', color='#27ae60', lw=2))
    ax.text(-0.5, 70, '+63%', fontsize=9, color='#27ae60', fontweight='bold')

    ax.set_ylabel('Success Rate (%)')
    ax.set_xticks(x)
    ax.set_xticklabels(phases)
    ax.set_ylim(0, 100)
    ax.legend(loc='upper right', framealpha=0.9)
    ax.set_title('Figure 1: The Precision Paradox', fontweight='bold', pad=15)

    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, 'fig1_precision_paradox.png'))
    fig.savefig(os.path.join(OUT_DIR, 'fig1_precision_paradox.svg'))
    plt.close(fig)
    print("  Figure 1 done.")


def fig3_cascading_valley():
    """Figure 3: Cascading Valley of Death — attrition at each handoff."""
    fig, ax = plt.subplots(figsize=(8, 4.5))

    stages = [
        'Computational\nHits',
        'Biochemical\nValidation',
        'Cell-Based\nAssays',
        'Animal\nModels',
        'Phase I',
        'Phase II',
        'Phase III',
        'FDA\nApproval'
    ]

    # Traditional pipeline (starting from 10,000 compounds)
    trad_counts = [10000, 500, 100, 20, 10, 3, 1.7, 1]
    trad_pcts = [c/10000*100 for c in trad_counts]

    # AI pipeline (same starting, better at early stages, similar late)
    ai_counts = [10000, 1500, 300, 30, 15, 4.5, 2.6, 1]
    ai_pcts = [c/10000*100 for c in ai_counts]

    x = np.arange(len(stages))

    ax.semilogy(x, trad_counts, 'o-', color=C_TRAD, linewidth=2, markersize=7,
                label='Traditional Pipeline', zorder=3)
    ax.semilogy(x, ai_counts, 's-', color=C_AI, linewidth=2, markersize=7,
                label='AI-Enhanced Pipeline', zorder=3)

    # Shade the "Chemistry" vs "Biology" regions
    ax.axvspan(-0.5, 3.5, alpha=0.08, color='#2ecc71', zorder=0)
    ax.axvspan(3.5, 7.5, alpha=0.08, color='#e74c3c', zorder=0)
    ax.text(1.5, 15000, 'Chemistry Problem\n(AI improves)', ha='center', fontsize=9,
            color='#27ae60', fontweight='bold', alpha=0.7)
    ax.text(5.5, 15000, 'Biology Problem\n(AI ≈ traditional)', ha='center', fontsize=9,
            color='#c0392b', fontweight='bold', alpha=0.7)

    # Convergence annotation
    ax.annotate('Curves converge:\nAI advantage\ndisappears', xy=(5, 4.5),
                xytext=(6.2, 50), fontsize=7, color=C_DARK,
                arrowprops=dict(arrowstyle='->', color=C_DARK, lw=1),
                ha='center')

    ax.set_xticks(x)
    ax.set_xticklabels(stages, fontsize=8)
    ax.set_ylabel('Surviving Compounds (log scale)')
    ax.set_ylim(0.5, 30000)
    ax.legend(loc='upper right', framealpha=0.9)
    ax.set_title('Figure 3: The Cascading Valley of Death', fontweight='bold', pad=15)
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, 'fig3_cascading_valley.png'))
    fig.savefig(os.path.join(OUT_DIR, 'fig3_cascading_valley.svg'))
    plt.close(fig)
    print("  Figure 3 done.")


def fig4_goodhart_gradient():
    """Figure 4: The Goodhart Gradient — our key empirical finding."""
    fig, axes = plt.subplots(1, 2, figsize=(11, 5), gridspec_kw={'width_ratios': [1.3, 1]})

    # === Panel A: Category scores across systems ===
    ax = axes[0]
    systems = ['Direct\nLLM', 'LLM +\nTools', 'DruGUI\nPipeline', 'RDKit\nPipeline']

    # Normalized scores (min-max within each system for comparability)
    # Direct LLM: A=5.82, B=5.44, C=5.08
    # LLM+Tools: A=8.28, B=4.94, C=5.69
    # DruGUI: A=0.557, B=0.496, C=0.592
    # RDKit: A=0.724, B=0.653, C=0.758

    # Normalize to 0-1 within each system
    raw = [
        [5.82, 5.44, 5.08],
        [8.28, 4.94, 5.69],
        [0.557, 0.496, 0.592],
        [0.724, 0.653, 0.758],
    ]
    normalized = []
    for r in raw:
        mn, mx = min(r), max(r)
        rng = mx - mn if mx != mn else 1
        normalized.append([(v - mn) / rng for v in r])

    x = np.arange(len(systems))
    width = 0.25

    for i, (cat, color, label) in enumerate([
        (0, C_APPROVED, 'A: FDA-Approved'),
        (1, C_FAILURE, 'B: Clinical Failures'),
        (2, C_DECOY, 'C: Decoys')
    ]):
        vals = [n[cat] for n in normalized]
        bars = ax.bar(x + (i-1)*width, vals, width, color=color, label=label,
                      edgecolor='white', linewidth=0.5, alpha=0.85)

    # Ranking labels
    rankings = ['A > B > C (correct)', 'A > C > B', 'C > A > B (inverted)', 'C > A > B (inverted)']
    colors_rank = ['#27ae60', C_ACCENT, '#c0392b', '#c0392b']
    for i, (rank, col) in enumerate(zip(rankings, colors_rank)):
        ax.text(i, 1.08, rank, ha='center', va='bottom', fontsize=7.5,
                fontweight='bold', color=col)

    ax.set_xticks(x)
    ax.set_xticklabels(systems)
    ax.set_ylabel('Normalized Score (within system)')
    ax.set_ylim(0, 1.25)
    ax.legend(loc='upper left', fontsize=8, framealpha=0.9)
    ax.set_title('A. Category Rankings Across Systems', fontweight='bold', fontsize=11)

    # Arrow showing Goodhart direction
    ax.annotate('', xy=(3.3, 0.15), xytext=(0.3, 0.95),
                arrowprops=dict(arrowstyle='->', color=C_ACCENT, lw=2.5,
                                connectionstyle='arc3,rad=-0.2'))
    ax.text(2.0, 0.25, 'Goodhart\nGradient', fontsize=9, color=C_ACCENT,
            fontweight='bold', ha='center', rotation=-20)

    # === Panel B: AUC comparison ===
    ax2 = axes[1]
    systems_short = ['Direct\nLLM', 'LLM+\nTools', 'DruGUI', 'RDKit']
    auc_ab = [0.642, 0.948, 0.667, 0.694]
    auc_ac = [0.795, 0.951, 0.243, 0.562]

    x2 = np.arange(len(systems_short))
    width2 = 0.35

    bars1 = ax2.bar(x2 - width2/2, auc_ab, width2, color=C_DARK, label='AUC (A vs B)',
                    alpha=0.85, edgecolor='white')
    bars2 = ax2.bar(x2 + width2/2, auc_ac, width2, color=C_ACCENT, label='AUC (A vs C)',
                    alpha=0.85, edgecolor='white')

    # Random chance line
    ax2.axhline(y=0.5, color=C_GRAY, linestyle='--', linewidth=1, alpha=0.7, label='Random (0.5)')

    # Value labels
    for bar, val in zip(bars1, auc_ab):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
                f'{val:.2f}', ha='center', va='bottom', fontsize=7, fontweight='bold')
    for bar, val in zip(bars2, auc_ac):
        color = '#c0392b' if val < 0.5 else C_DARK
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
                f'{val:.2f}', ha='center', va='bottom', fontsize=7, fontweight='bold', color=color)

    # Highlight DruGUI A-vs-C below random
    ax2.annotate('Below random!\nPrefers decoys', xy=(2 + width2/2, 0.243),
                xytext=(2.8, 0.15), fontsize=7, color='#c0392b', fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='#c0392b', lw=1))

    ax2.set_xticks(x2)
    ax2.set_xticklabels(systems_short)
    ax2.set_ylabel('Area Under Curve (AUC)')
    ax2.set_ylim(0, 1.15)
    ax2.legend(loc='upper left', fontsize=7.5, framealpha=0.9)
    ax2.set_title('B. Discrimination Power (AUC)', fontweight='bold', fontsize=11)

    fig.suptitle('Figure 4: The Goodhart Gradient in AI Drug Discovery',
                 fontweight='bold', fontsize=13, y=1.02)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, 'fig4_goodhart_gradient.png'), bbox_inches='tight')
    fig.savefig(os.path.join(OUT_DIR, 'fig4_goodhart_gradient.svg'), bbox_inches='tight')
    plt.close(fig)
    print("  Figure 4 done.")


def fig5_integration_framework():
    """Figure 5: Three-layer integration framework (Data/Process/Algorithm)."""
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Three layers as rounded rectangles
    layers = [
        (1, 5.5, 8, 1.8, '#3498db', 'Layer 1: DATA',
         'Organ-on-a-Chip  •  Patient Organoids  •  Multi-Omics\nContinuous human-relevant biological readouts'),
        (1, 3.2, 8, 1.8, '#e67e22', 'Layer 2: PROCESS',
         'Clinician-in-the-Loop  •  Cross-disciplinary Teams\nDomain expertise integrated at every pipeline stage'),
        (1, 0.9, 8, 1.8, '#9b59b6', 'Layer 3: ALGORITHM',
         'Causal Inference  •  Explainable AI  •  Multi-modal Models\nBiology-aware prediction beyond pattern recognition'),
    ]

    for x0, y0, w, h, color, title, desc in layers:
        rect = mpatches.FancyBboxPatch((x0, y0), w, h, boxstyle="round,pad=0.15",
                                        facecolor=color, alpha=0.15, edgecolor=color, linewidth=2)
        ax.add_patch(rect)
        ax.text(x0 + 0.3, y0 + h - 0.35, title, fontsize=12, fontweight='bold', color=color, va='top')
        ax.text(x0 + 0.3, y0 + 0.45, desc, fontsize=9, color=C_DARK, va='bottom')

    # Feedback arrows
    for y_from, y_to in [(5.5, 5.0), (3.2, 2.7)]:
        ax.annotate('', xy=(5, y_to), xytext=(5, y_from),
                    arrowprops=dict(arrowstyle='->', color=C_DARK, lw=1.5))

    # Side label: feedback loop
    ax.annotate('', xy=(9.3, 7.0), xytext=(9.3, 1.2),
                arrowprops=dict(arrowstyle='->', color='#27ae60', lw=2,
                                connectionstyle='arc3,rad=0.5'))
    ax.text(9.7, 4.0, 'Clinical\nFeedback\nLoop', fontsize=9, color='#27ae60',
            fontweight='bold', ha='center', va='center', rotation=90)

    # Title
    ax.text(5, 7.8, 'Figure 5: Integration Framework for Biology-Aware AIDD',
            fontsize=13, fontweight='bold', ha='center', va='top', color=C_DARK)

    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, 'fig5_integration_framework.png'), bbox_inches='tight')
    fig.savefig(os.path.join(OUT_DIR, 'fig5_integration_framework.svg'), bbox_inches='tight')
    plt.close(fig)
    print("  Figure 5 done.")


def fig6_strategic_timeline():
    """Figure 6: Strategic Timeline / Roadmap 2020-2030."""
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.set_xlim(2019.5, 2030.5)
    ax.set_ylim(-1.5, 3)
    ax.axis('off')

    # Timeline axis
    ax.plot([2020, 2030], [0, 0], '-', color=C_DARK, linewidth=2, zorder=1)
    for year in range(2020, 2031):
        ax.plot(year, 0, '|', color=C_DARK, markersize=10, zorder=2)
        ax.text(year, -0.25, str(year), ha='center', fontsize=8, color=C_GRAY)

    # Past milestones (above line, blue)
    past = [
        (2020, 'AlphaFold2'),
        (2021, 'First AI drugs\nenter clinic'),
        (2023, 'BEN-2293 &\nEXS-21546 fail'),
        (2024, 'AlphaFold3\nChemCrow'),
        (2025, 'Rentosertib\nPhase IIa +'),
    ]
    for x, label in past:
        ax.plot(x, 0, 'o', color=C_TRAD, markersize=8, zorder=3)
        ax.text(x, 0.35, label, ha='center', va='bottom', fontsize=7,
                color=C_TRAD, fontweight='bold')

    # Future milestones (below line, red/orange)
    future = [
        (2026, 'Zasocitinib NDA?\n15-20 Phase III\nreadouts'),
        (2027.5, 'First AI-designed\nFDA approval?'),
        (2029, 'Phase II rate\nimprovement\nsignal?'),
    ]
    for x, label in future:
        ax.plot(x, 0, 'D', color=C_AI, markersize=8, zorder=3)
        ax.text(x, -0.5, label, ha='center', va='top', fontsize=7,
                color=C_AI, fontweight='bold')

    # Parallel tracks
    # Chemistry track (solved)
    ax.fill_between([2020, 2025], [2.3, 2.3], [2.7, 2.7], color='#2ecc71', alpha=0.3)
    ax.text(2022.5, 2.5, 'Chemistry Problem (largely solved)', ha='center', fontsize=8,
            color='#27ae60', fontweight='bold')

    # Biology track (in progress)
    ax.fill_between([2025, 2030], [2.3, 2.3], [2.7, 2.7], color='#e74c3c', alpha=0.2)
    ax.annotate('', xy=(2030, 2.5), xytext=(2025, 2.5),
                arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2))
    ax.text(2027.5, 2.5, 'Biology Problem (the frontier)', ha='center', fontsize=8,
            color='#c0392b', fontweight='bold')

    # OoC/Causal AI track
    ax.fill_between([2022, 2030], [1.7, 1.7], [2.0, 2.0], color='#9b59b6', alpha=0.15)
    ax.annotate('', xy=(2030, 1.85), xytext=(2022, 1.85),
                arrowprops=dict(arrowstyle='->', color='#9b59b6', lw=1.5))
    ax.text(2026, 1.85, 'OoC maturation  +  Causal AI development', ha='center',
            fontsize=7, color='#8e44ad')

    ax.set_title('Figure 6: Strategic Roadmap for AIDD 2020–2030',
                 fontweight='bold', fontsize=12, pad=20)

    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, 'fig6_strategic_timeline.png'), bbox_inches='tight')
    fig.savefig(os.path.join(OUT_DIR, 'fig6_strategic_timeline.svg'), bbox_inches='tight')
    plt.close(fig)
    print("  Figure 6 done.")


def fig2_pipeline_assumptions():
    """Figure 2: Pipeline Architecture with Assumptions vs Reality."""
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.set_xlim(-0.5, 6.5)
    ax.set_ylim(-2.5, 3.5)
    ax.axis('off')

    stages = [
        ('Target ID', '#3498db'),
        ('Structure\nPrediction', '#2980b9'),
        ('Virtual\nScreening', '#1abc9c'),
        ('Lead\nOptimization', '#27ae60'),
        ('Preclinical', '#e67e22'),
        ('Phase I', '#e74c3c'),
        ('Phase II', '#c0392b'),
    ]

    assumptions = [
        'GWAS hits are\ncausal & druggable',
        'Static structure\n= biology',
        'Docking score\n= binding affinity',
        'ADMET score\n= clinical safety',
        'Animal model\n= human',
        'Safe = will\nwork',
        '?',
    ]

    realities = [
        'Many non-causal,\nundruggable',
        'Dynamic ensemble;\nAF3 fails >5Å RMSD',
        '1-5% hit rate;\nrigid-body artifact',
        'ADMET solved;\nefficacy NOT',
        '5% translate\nto humans',
        'Phase I ≠\nPhase II',
        '~70% fail\n(biology)',
    ]

    # Draw pipeline boxes and arrows
    for i, (name, color) in enumerate(stages):
        # Box
        rect = mpatches.FancyBboxPatch((i - 0.4, -0.4), 0.8, 0.8,
                                        boxstyle="round,pad=0.1",
                                        facecolor=color, alpha=0.8,
                                        edgecolor='white', linewidth=1)
        ax.add_patch(rect)
        ax.text(i, 0, name, ha='center', va='center', fontsize=7.5,
                fontweight='bold', color='white')

        # Arrow to next
        if i < len(stages) - 1:
            ax.annotate('', xy=(i + 0.5, 0), xytext=(i + 0.4, 0),
                        arrowprops=dict(arrowstyle='->', color=C_DARK, lw=1.5))

    # Assumptions (above)
    ax.text(3, 2.8, 'AI ASSUMPTIONS', ha='center', fontsize=10, fontweight='bold',
            color='#27ae60')
    for i, assumption in enumerate(assumptions):
        ax.text(i, 1.5, assumption, ha='center', va='center', fontsize=6.5,
                color='#27ae60',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#27ae60', alpha=0.1))
        ax.annotate('', xy=(i, 0.5), xytext=(i, 1.0),
                    arrowprops=dict(arrowstyle='->', color='#27ae60', lw=0.8, alpha=0.5))

    # Realities (below)
    ax.text(3, -2.3, 'BIOLOGICAL REALITY', ha='center', fontsize=10, fontweight='bold',
            color='#c0392b')
    for i, reality in enumerate(realities):
        ax.text(i, -1.5, reality, ha='center', va='center', fontsize=6.5,
                color='#c0392b',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#e74c3c', alpha=0.1))
        ax.annotate('', xy=(i, -0.5), xytext=(i, -1.0),
                    arrowprops=dict(arrowstyle='->', color='#c0392b', lw=0.8, alpha=0.5))

    ax.set_title('Figure 2: AIDD Pipeline — Assumptions vs. Biological Reality',
                 fontweight='bold', fontsize=12, pad=15)

    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, 'fig2_pipeline_assumptions.png'), bbox_inches='tight')
    fig.savefig(os.path.join(OUT_DIR, 'fig2_pipeline_assumptions.svg'), bbox_inches='tight')
    plt.close(fig)
    print("  Figure 2 done.")


if __name__ == '__main__':
    print("Generating publication figures...")
    fig1_precision_paradox()
    fig2_pipeline_assumptions()
    fig3_cascading_valley()
    fig4_goodhart_gradient()
    fig5_integration_framework()
    fig6_strategic_timeline()
    print("\nAll 6 figures generated in:", OUT_DIR)
