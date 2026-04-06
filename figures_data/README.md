# Figures Data Provenance

## Pipeline Evaluation Experiment (Section 5.3)

### Data Sources
- **Test dataset**: `experiments/agent_evaluation_dataset.json` — 36 molecules (12 approved, 12 clinical failures, 12 decoys)
  - Category A SMILES: from PubChem
  - Category B clinical outcomes: from FDA withdrawal records, published trial results
  - Category C decoys: designed using common drug-like scaffolds, validated for Lipinski compliance
- **RDKit pipeline results**: `experiments/results_rdkit_pipeline.json` — computed via `test_rdkit_pipeline.py`
- **ADMET proxy results**: `experiments/results_admet_proxy.json` — computed via `test_admet_proxy.py`
- **Prior ADMET-AI results** (6 molecules): `experiments/results_admet_ai_full.json`

### Generated Figures
| Figure | File | Script | Description |
|--------|------|--------|-------------|
| Score distributions | `fig_pipeline_score_distributions.*` | `experiments/analysis_agent_discrimination.py` | Violin+box+swarm plots of pipeline scores by category |
| Metrics heatmap | `fig_metrics_heatmap.*` | same | Mean computational metrics by category |
| ROC curves | `fig_roc_curves.*` | same | Pipeline discrimination ability (A vs B, A vs C) |
| Failure taxonomy | `fig_failure_taxonomy.*` | same | Clinical failure types + detection matrix |
| Radar comparison | `fig_radar_comparison.*` | same | Multi-dimensional category profiles |
| Molecule rankings | `fig_molecule_rankings.*` | same | All 36 molecules ranked by composite score |

### Key Statistics
- RDKit Pipeline AUC (A vs B): 0.694
- RDKit Pipeline AUC (A vs C): 0.562
- ADMET Proxy AUC (A vs B): 0.410
- ADMET Proxy AUC (A vs C): 0.069
- Clinical failure detection rate: 7/12 (58%)
