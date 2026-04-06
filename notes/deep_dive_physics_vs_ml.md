# Deep Dive: Physics-Based Methods vs ML in Drug Discovery

> Date: 2026-04-04
> Status: Complete

---

## 1. FEP+ (Relative Binding Free Energy) Benchmarks

### Wang et al. 2015 (JACS) — Landmark Validation
- 8 targets, 199 ligands, 330 perturbations
- Overall MUE: **0.9 kcal/mol**, RMSE: ~1.14 kcal/mol
- R-value: **0.75** (weighted average)
- 91% of ligands within 1.0 kcal/mol of experiment
- Comparison: MM-GB/SA R=0.35, Glide SP docking R=0.29
- Citation: Wang L et al. JACS 2015;137(7):2695-2703

### Ross et al. 2023 (Commun Chem) — Current Best Assessment
- Edgewise RMSE: **1.17 kcal/mol** [95% CI: 1.08-1.25]
- R²: **0.56** [95% CI: 0.51-0.60]
- **Critical finding**: experimental reproducibility RMSE = 0.91 kcal/mol, R² = 0.79
- FEP+ approaching ceiling set by experimental noise
- Citation: Ross GA et al. Commun Chem 2023;6:222. DOI: 10.1038/s42004-023-01019-9

### Schindler et al. 2020 (JCIM) — Industrial Validation at Merck KGaA
- 12 targets, 19 chemical series, prospective mode
- ~69% predictions within 1 log unit; 78% true positive rate (<100 nM)
- ~1,500 molecules deprioritized, avoiding costly synthesis
- Citation: Schindler CEM et al. JCIM 2020;60(11):5457-5474. DOI: 10.1021/acs.jcim.0c00900

## 2. ABFE (Absolute Binding Free Energy) — Current State

### Bhati, Wan & Coveney 2024 (JCTC)
- 219 complexes, 31 proteins, 186 ligands
- With empirical correction: MUE=0.93, RMSE=1.22, r=0.77
- **Without correction: RMSE=4.38 kcal/mol** (r=0.40) — poor
- Correction for protein conformational changes is essential
- Citation: Bhati AP et al. JCTC 2024. DOI: 10.1021/acs.jctc.4c01389

### ABFE vs FEP+ Comparison
| Feature | FEP+ (RBFE) | ABFE |
|---------|------------|------|
| RMSE | 0.9-1.2 kcal/mol | 1.2-2.8 kcal/mol |
| Requires reference | Yes | No |
| Scaffold hopping | No | Yes (in principle) |
| Maturity | Production-ready | Developmental |

## 3. ML Scoring Functions — Generalization Failure

### Graber et al. 2025 (Nature Machine Intelligence) — KEY PAPER
- When PDBbind train-test leakage removed ("CleanSplit"):
  - Pafnucy RMSE: 1.046 → **1.484** (42% increase)
  - Nearest-neighbor search: RMSE=1.517 — competitive with deep learning
  - Some models performed equally well **after removing all protein information**
- **Implication**: ML models memorize dataset biases, not physics
- Citation: Graber et al. Nat Mach Intell 2025. DOI: 10.1038/s42256-025-01124-5

### Accuracy Comparison Table
| Method | RMSE (kcal/mol) | Clinical Validation |
|--------|-----------------|-------------------|
| FEP+ (RBFE) | 0.9-1.2 | Zasocitinib (Phase III, $6B) |
| ABFE | 1.2-2.8 | Limited |
| MD (long-timescale) | N/A (conformational) | Zovegalisib (FDA BTD) |
| ML scoring (PDBbind, standard) | 1.4-1.5 (inflated) | None |
| ML scoring (clean split) | 1.5-2.0+ | None |
| Sequence-based DL | 2.0-3.5 | None |

## 4. Zasocitinib Development Story

- **Nimbus Therapeutics + Schrodinger** long-standing collaboration
- Targeted JH2 pseudokinase regulatory domain of TYK2 (allosteric, not catalytic JH1)
- FEP+ scored ~4,000 molecules for potency + selectivity + solubility
- Result: NDI-034858 (TAK-279), oral picomolar TYK2 inhibitor
- **Dec 2022**: Takeda acquired for $4B upfront + $2B milestones = $6B total
- Schrodinger received $111.3M from deal
- Phase III (2025): >50% PASI 90 at Week 16, ~30% PASI 100
- **Key point**: Physics-based FEP+, NOT generative AI

## 5. Zovegalisib (RLY-2608) — MD-Driven Design

- **Relay Therapeutics** Dynamo platform: cryo-EM + long-timescale MD (Anton 2)
- Workflow:
  1. 2.7A cryo-EM of full-length p85a:p110a heterodimer
  2. 10-100μs MD comparing WT vs H1047R mutant
  3. Discovered cryptic allosteric pocket **invisible in static structures**
  4. X-ray crystallography confirmed pocket
  5. Designed mutant-selective PI3Ka inhibitor
- FDA Breakthrough Therapy Designation (Feb 2026) for PIK3CA-mutant HR+/HER2- breast cancer
- Median PFS: 11.0 months in second-line
- Citation: Varkaris A et al. Cancer Discovery 2024;14(2):240-257. DOI: 10.1158/2159-8290.CD-23-0944

## 6. Key Insight for Review

**Physics-based methods (FEP+, MD) are producing the most clinically validated AI-era successes**, while pure ML/generative approaches have yet to produce a comparable clinical milestone. This challenges the narrative that "AI drug discovery = deep learning."

- Zasocitinib: FEP+ → $6B deal, Phase III success
- Zovegalisib: MD → FDA BTD, cryptic pocket discovery
- No ML-only designed drug has matched these milestones
- FEP+ RMSE (0.9-1.2) consistently beats ML scoring (1.5-2.0+) for relative binding affinity
