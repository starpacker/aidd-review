# Figure 5: Integration Framework — Biology-Aware AIDD Architecture

## Three-Layer Architecture

### Layer 1: DATA (Section 6.1)
| Data Source | Current Status | What It Provides | AI Readiness |
|------------|---------------|------------------|-------------|
| 2D Cell Assays | Standard, widely used | Sparse endpoint data; low physiological relevance | High throughput, but low predictive value |
| Animal Models | Regulatory default (shifting) | Holistic but species-biased; 95% translation failure | Low throughput, questionable relevance |
| Organ-on-Chip | Emerging; Emulate 87% DILI sensitivity | Continuous, real-time, human-relevant multi-parametric | Low throughput currently; high data quality |
| Patient-derived Organoids | Growing adoption | Patient-specific, 3D tissue architecture | Medium throughput; standardization lacking |
| Multi-omics (genomics, transcriptomics, proteomics) | Mature for individual -omics | Molecular-level disease understanding | Integration across modalities still challenging |
| Clinical data (EHR, RWE) | Abundant but messy | Post-market outcomes, patient diversity | Privacy, standardization, bias issues |

**Key flow**: OoC/organoid data → standardized endpoints → ML-ready datasets

### Layer 2: PROCESS (Section 6.2)
| Process Element | Current State | Proposed State |
|----------------|--------------|----------------|
| Pipeline handoffs | Sequential silos (CS → bio → clinical) | Integrated cross-disciplinary teams |
| Binding site validation | Algorithm-only | Clinician-in-the-loop |
| Target prioritization | Data-driven ranking | Bayesian reasoning + domain adjudication |
| Experimental design | Human or AI in isolation | Human-AI collaborative ("systems strategist") |
| Quality control | Post-hoc | Embedded at each stage |

### Layer 3: ALGORITHM (Section 6.3)
| Algorithmic Approach | Current | Proposed | Key References |
|---------------------|---------|----------|---------------|
| Learning paradigm | Correlative (pattern recognition) | Causal inference (mechanism modeling) | Pearl 2009; Feuerriegel 2024 |
| Interpretability | Black box (post-hoc XAI) | Interpretable by design (SHAP, attention as first-class) | Ding 2025; Lavecchia 2025 |
| Validation | Benchmark leaderboards (MoleculeNet, PDBbind) | Prospective wet-lab validation + clinical outcomes | Walters & Barzilay 2021 |
| Data integration | Single-modal (SMILES, structures) | Multi-modal (omics + imaging + clinical) | Hasin 2017 |
| Regulatory readiness | Ad hoc | FDA-aligned credibility framework | FDA draft guidance Jan 2025 |

## Feedback Loop (Critical)
- Clinical outcomes (Phase II results, post-market data) feed back to Layer 1 (Data)
- Breaking the current one-directional pipeline: Computation → Clinic → [dead end]
- Proposed: Computation → Clinic → Outcomes → Data → Computation (closed loop)

## Visualization Spec
- Type: Three-layer stacked diagram with feedback arrows
- Layer 1 (bottom, green): Data sources flowing into standardized data lake
- Layer 2 (middle, blue): Process nodes showing human-AI interaction points
- Layer 3 (top, purple): Algorithm components producing predictions
- RIGHT SIDE: Downward feedback arrow from "Clinical Outcomes" back to Layer 1
- LEFT SIDE: Current pipeline (one-directional, gray, faded) for contrast
- Key insight callout: "Closed-loop biology-aware system"

## Key Proof-of-Concept Data Points
- Emulate Liver-Chip: 87% sensitivity for DILI (Layer 1 data quality)
- BIO report: biomarker-guided trials = 2x LOA (Layer 2 process improvement)
- DILITracer: 82.34% ternary DILI classification from organoid images (Layer 1→3 integration)
- ARPA-H CATALYST: $21M for OoC+AI liver/heart models (Layer 1→3 investment)
