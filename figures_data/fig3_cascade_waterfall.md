# Figure 3: Cascading Valley of Death — Attrition Across Pipeline Stages

## Data Table (per 10,000 initial compounds)

| Stage | Input | Output (Traditional) | Attrition % | Output (AI-enhanced) | Attrition % | Primary Failure Cause |
|-------|-------|---------------------|-------------|---------------------|-------------|----------------------|
| Computational screening | 10,000 | 500 | 95% | 500 | 95% | Low hit rates (1-5% in practice) |
| Biochemical validation | 500 | 50 | 90% | 75 | 85% | False positives, assay artifacts |
| ADMET/Lead optimization | 50 | 5 | 90% | 10 | 80% | PK/solubility/toxicity (AI improvement: 40%→10-15% attrition) |
| Preclinical (animal) | 5 | 1.5 | 70% | 2.5 | 50% | Species translation gap (95% fail: Ineichen 2024) |
| Phase I (safety) | 1.5 | 0.78 | 48% | 2.5 | 2.1 (84%) | Bioavailability, PK/PD, toxicity |
| Phase II (efficacy) | 0.78 | 0.23 | 71% | 2.1 | 0.84 (60%) | Lack of efficacy, pathway redundancy |
| Phase III (pivotal) | 0.23 | 0.13 | 42% | 0.84 | ~0.5 | Endpoints, population diversity |
| Approval | 0.13 | 0.12 | 9% | ~0.5 | ~0.45 | Regulatory |

**Note**: AI-enhanced numbers are estimates combining Jayatunga 2024 Phase I/II data with BIO 2021 baseline. Preclinical AI improvement is speculative — limited data. The key message is: AI dramatically improves early stages (ADMET, Phase I) but Phase II remains the bottleneck.

## Visualization Spec
- Type: Waterfall/funnel diagram, two parallel tracks (Traditional vs AI)
- Start at 10,000, narrow at each stage
- Color: Green zones where AI improves; Red zones where AI = traditional
- Annotation boxes at key handoffs explaining failure causes
- Key insight callout: "AI improves inputs to Phase II but not Phase II itself"

## Citations
- BIO/QLS 2021 (traditional rates)
- Jayatunga et al. 2024 (AI Phase I/II)
- Kola & Landis 2004; Sun et al. 2022 (ADMET evolution)
- Ineichen et al. 2024 (animal translation)
