"""
Consistent color palette for all review paper figures.
"""

# Category colors for pipeline evaluation experiments
CAT_APPROVED = '#2ecc71'        # green — FDA-approved drugs
CAT_FAILURE = '#e74c3c'         # red — clinical failures
CAT_DECOY = '#3498db'           # blue — computational decoys

CATEGORY_COLORS = {
    'A_approved': CAT_APPROVED,
    'B_clinical_failure': CAT_FAILURE,
    'C_decoy': CAT_DECOY,
}

CATEGORY_LABELS = {
    'A_approved': 'A: Approved Drugs',
    'B_clinical_failure': 'B: Clinical Failures',
    'C_decoy': 'C: Decoys',
}

# General palette for bar charts, line charts, etc.
PRIMARY = '#2c3e50'
SECONDARY = '#7f8c8d'
ACCENT = '#e67e22'
HIGHLIGHT = '#9b59b6'

# Sequential palette for heatmaps
HEATMAP_CMAP = 'RdYlGn_r'

# Matplotlib rcParams for consistent styling
RC_PARAMS = {
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans'],
    'font.size': 9,
    'axes.titlesize': 12,
    'axes.labelsize': 10,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 9,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
}
