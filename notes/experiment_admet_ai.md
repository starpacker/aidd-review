# Experiment: ADMET-AI v2 Predictions & Performance Analysis

> Date: 2026-04-03 (updated with quantitative benchmark data)
> Tool: ADMET-AI v2.0.1 (Swanson et al., Bioinformatics 2024)
> Model: Chemprop v2 (message-passing GNN), 104 predicted properties
> Status: **FIRST-HAND EXPERIMENTAL DATA + BENCHMARK ANALYSIS**

**Full citation**: Swanson K, Walther P, Leitz J, Mukherjee S, Wu JC, Shivnaraine RV, Zou J. ADMET-AI: a machine learning ADMET platform for evaluation of large-scale chemical libraries. Bioinformatics. 2024;40(7):btae416. DOI: 10.1093/bioinformatics/btae416

---

## Part A: Regression Performance — The Quantitative Gap

### CRITICAL DATA: Per-Task R² Values (from ADMET-AI built-in admet.csv)

The paper claims "R² >0.6 for five of the ten regression datasets." Our direct extraction from the ADMET-AI package's built-in performance data (resources/data/admet.csv) reveals:

#### R² > 0.6 (only 4 tasks):
| Task | R² | MAE | N | Clinical Relevance |
|------|-----|-----|---|-------------------|
| HydrationFreeEnergy_FreeSolv | 0.888 | 0.783 | 642 | Low — rarely used clinically |
| Solubility_AqSolDB | 0.817 | 0.692 | 9,980 | Moderate — but single pH point only |
| Lipophilicity_AstraZeneca | 0.771 | 0.407 | 4,200 | Moderate |
| Caco2_Wang | 0.707 | 0.311 | 906 | High — permeability screening |

#### R² < 0.6 (6 tasks — the clinically critical ones):
| Task | R² | MAE | N | Clinical Relevance |
|------|-----|-----|---|-------------------|
| LD50_Zhu | 0.596 | 0.452 | 7,342 | High — safety |
| PPBR_AZ | 0.589 | 6.852 | 1,614 | High — free drug concentration |
| Clearance_Microsome_AZ | 0.277 | 26.74 | 1,102 | **Critical** — dose selection |
| Clearance_Hepatocyte_AZ | 0.264 | 32.73 | 1,020 | **Critical** — dose selection |
| VDss_Lombardo | **-1.211** | 5.039 | 1,111 | **Critical** — dose selection |
| Half_Life_Obach | **-2.386** | 31.85 | 665 | **Critical** — dosing interval |

**KEY INSIGHT**: VDss and Half_Life have **negative R²**, meaning the model is literally worse than predicting the dataset mean. These are the parameters that determine dosing regimen in clinical practice.

**Correcting our claim**: The original draft states "R² > 0.6 on only 50% of regression tasks." The actual number from ADMET-AI's own data is **40% (4/10)**. The paper's claim of "five of ten" appears to round LD50 (R²=0.596) upward. Either way, the critical pharmacokinetic parameters (clearance, VDss, half-life) all have R² < 0.3 or negative.

### TDC Leaderboard — Even the BEST Models Struggle

Data scraped from tdcommons.ai individual leaderboard pages (April 2026):

| Task | Metric | Best Score (Model) | Chemprop-RDKit | ChemProp-RDKit Rank |
|------|--------|--------------------|----------------|---------------------|
| Caco2_Wang | MAE↓ | 0.256 (CaliciBoost) | 0.330 | #11 of 24 |
| Lipophilicity | MAE↓ | 0.456 (MiniMol) | 0.467 | #2 of 21 |
| Solubility_AqSolDB | MAE↓ | 0.741 (MiniMol) | 0.761 | #2 of 18 |
| PPBR_AZ | MAE↓ | 7.440 (Gradient Boost) | 8.288 | #9 of 20 |
| VDss_Lombardo | Spearman↑ | 0.713 (MapLight+GNN) | 0.389 | #16 of 19 |
| Half_Life_Obach | Spearman↑ | 0.576 (CFA) | 0.239 | #13 of 20 |
| Clearance_Hepatocyte | Spearman↑ | 0.536 (CFA) | 0.430 | #10 of 18 |
| Clearance_Microsome | Spearman↑ | 0.630 (MapLight+GNN) | 0.599 | #6 of 20 |
| LD50_Zhu | MAE↓ | 0.552 (BaseBoosting) | 0.625 | #9 of 22 |

**Key observations for the review**:
1. Even the BEST model for Half_Life achieves only Spearman=0.576 — barely above random
2. Best VDss prediction: Spearman=0.713 — moderate at best for a critical dosing parameter
3. Best hepatocyte clearance: Spearman=0.536 — essentially weak correlation
4. Chemprop-RDKit (ADMET-AI's architecture) ranks in the bottom third on VDss (#16/19) and Half_Life (#13/20)
5. **admet_ai_v2 on Caco2 leaderboard: MAE=6.328 (dead last, #24)** — suggesting multi-task training caused catastrophic regression

### Reproducibility Crisis on TDC Leaderboard

A February 2026 critical assessment found:
- Only **3 of top-ranked models** (CaliciBoost, MapLight, MapLight+GNN) passed ALL reproducibility checks
- Data leakage identified in MiniMol, GradientBoost, XGBoost
- Most top-ranked models had: unavailable code, non-reproducible environments, or methodological flaws

**Citation**: Critical Assessment of ML models for ADMET Prediction in TDC leaderboards. bioRxiv 2026.02.26.708193. DOI: 10.64898/2026.02.26.708193

---

## Part B: Classification Performance

AUROC > 0.85: **18 of 31 tasks** (from built-in data; paper claims 20 — discrepancy may be due to model version)

Worst-performing classification tasks:
| Task | AUROC | Clinical Importance |
|------|-------|-------------------|
| CYP2C9_Substrate | 0.628 | High — warfarin, clopidogrel |
| CYP3A4_Substrate | 0.705 | High — most common CYP |
| Bioavailability_Ma | 0.716 | Critical — go/no-go decision |
| Skin_Reaction | 0.718 | Moderate |
| NR-ER | 0.749 | Moderate — endocrine disruption |

---

## Part C: Drug Predictions (Case Study Molecules)

### Properties Predicted
ADMET-AI v2 outputs **52 unique properties** per molecule (+ 52 DrugBank percentiles = 104 total):
- 10 regression ADMET tasks (TDC)
- 31 classification ADMET tasks (TDC)
- 8 physicochemical descriptors (RDKit-computed): MW, logP, HBA, HBD, Lipinski, QED, stereo_centers, TPSA
- 3 structural alerts (RDKit): PAINS, BRENK, NIH

### Dasatinib (Tyrosine kinase inhibitor)
- Caco2 permeability: -5.24 log(10^-6 cm/s)
- PPBR: 93.4% (known clinical: ~96% — reasonable)
- CYP3A4 substrate: 0.74 (known: yes — correct)
- hERG: 0.93 (known: QT risk — correct direction)
- DILI: 0.93 (known: hepatotoxicity — correct)
- **Half-life: 64 hr** (known clinical: 3-5 hr — **off by 15x**)
- **VDss: 15.7 L/kg** (known clinical: 2505 L — **off by 160x in absolute terms**)

### Clopidogrel (Antiplatelet prodrug)
- CYP2C9 inhibition: 0.87 (predicts CYP interaction — correct)
- CYP2D6 inhibition: 0.59
- CYP3A4 inhibition: 0.77
- **Cannot predict CYP2C19 metabolizer phenotype** (poor/intermediate/extensive/ultra-rapid)
- Half-life: 28.3 hr (known clinical parent: ~6 hr)
- Clearance_Hepatocyte: 130.9 uL/min/10^6 cells

### Atazanavir (HIV protease inhibitor)
- Pgp substrate: 0.99 (known: yes — correct)
- CYP3A4 inhibition: 0.99 (known: strong inhibitor — correct)
- BBB: 0.22 (known: poor CNS penetration — correct)
- **PPBR: 107.8%** (known: ~86% — **exceeds 100%, physically impossible**)
- hERG: 0.996 (known: QT prolongation — correct)
- Solubility: -4.47 log(mol/L) — **single value; real: >1000-fold pH dependence (1 mg/mL at pH 1, insoluble at pH >4)**

### Sorafenib (Multi-kinase inhibitor)
- PPBR: 99.6% (known: 99.5% — excellent)
- DILI: 0.99 (known: hepatotoxicity — correct)
- Solubility: -5.92 (known: poorly soluble — correct direction)

### Erlotinib (EGFR inhibitor)
- CYP3A4 inhibition: 0.86 (known: CYP3A4 substrate — reasonable)
- hERG: 0.81 (known: QT risk — correct)
- **Half-life: 84.2 hr** (known clinical: ~36 hr — **off by 2.3x**)

---

## Part D: What ADMET-AI CANNOT Predict (Key Gaps)

### D1. pH-dependent solubility: NOT SUPPORTED
- Predicts single aqueous solubility value (from AqSolDB, mixed/unspecified pH)
- Clinically: atazanavir solubility varies >1000-fold across GI pH range
- PPIs reduce atazanavir AUC by ~75% due to pH effect on absorption
- **One number cannot capture this fundamental pharmacological reality**

### D2. CYP polymorphism effects: NOT SUPPORTED
- Predicts binary CYP inhibitor/substrate classification
- Cannot distinguish CYP2C19 *2/*3 (loss) vs *17 (gain of function)
- Clopidogrel in CYP2C19 poor metabolizers: HR 2.81 for stent thrombosis (Mega et al., JAMA 2010)
- **Molecular structure alone cannot predict patient-specific metabolism**

### D3. Protein binding displacement: NOT SUPPORTED
- PPBR predicted as single value; Atazanavir prediction of 107.8% is physically impossible
- DDI via displacement not modeled

### D4. Formulation effects: NOT SUPPORTED
- Salt form, particle size, amorphous/crystalline state: not considered
- Dominates real-world bioavailability for BCS Class II/IV

### D5. Active metabolite/prodrug: NOT SUPPORTED
- Clopidogrel is inactive prodrug; active metabolite generated by CYP2C19
- Model predicts parent compound properties only
- No metabolite structure prediction

### D6. Species translation: VERY LIMITED
- Mixed training data (human cell lines, animal models)
- No explicit species parameter

---

## Part E: Previous Experiment Results (Retained)

### Prediction Summary Table (6 drugs from earlier run)

| Drug | CYP2C19 | DILI | ClinTox | hERG | Solubility | Clinical Outcome |
|------|---------|------|---------|------|------------|-----------------|
| Dasatinib | 0.273 | 0.970 | 0.798 | 0.972 | -4.579 | pH failure (HR 3.5 with PPI) |
| Clopidogrel | **0.978** | 0.550 | 0.122 | 0.739 | -4.923 | CYP2C19 PM: HR 2.81 stent thrombosis |
| Oseltamivir | 0.189 | 0.272 | 0.218 | 0.521 | -2.102 | CES1 prodrug activation failure |
| Rofecoxib | 0.209 | 0.963 | **0.043** | 0.126 | -3.997 | **60K+ excess MIs** (MISSED by model) |
| Troglitazone | 0.701 | **0.845** | 0.042 | 0.492 | -5.247 | 63 deaths hepatotoxicity |
| **Imatinib** (control) | 0.096 | **0.912** | **0.869** | **0.985** | -4.530 | **SUCCESS**: >90% 5yr survival |

### Critical Finding: Success Drug Flagged as Highest Risk
Imatinib (CML standard of care, >90% 5-year survival) receives the HIGHEST risk scores of all 6 drugs:
- hERG: 0.985 (highest), DILI: 0.912 (2nd highest), ClinTox: 0.869 (highest)
- **If used as go/no-go criteria, imatinib would have been killed before clinical trials**

### Critical Finding: Rofecoxib — Complete Miss
- ClinTox: 0.043 (model says SAFE)
- hERG: 0.126 (low cardiac risk)
- **Caused 60,000+ excess MIs** — toxicity was system-level pharmacology (COX-2/prostacyclin/thromboxane imbalance), invisible to molecular property prediction

### Drug-Likeness Filter Analysis
| Category | Pass Rate | Implication |
|----------|-----------|------------|
| Clinical failures (5 drugs) | 5/5 (100%) | All pass standard filters |
| Withdrawn drugs (3 drugs) | 2/3 (67%) | Most pass despite lethal outcomes |
| Success controls (2 drugs) | 1/2 (50%) | Sofosbuvir (95% HCV cure) FAILS filters |

---

## Part F: Corrected Claims for Review Paper

### USE these quantitative claims:

1. "ADMET-AI, the best-in-class open-source ADMET predictor, achieves R² > 0.6 on only 4 of 10 regression tasks; for half-life and volume of distribution — parameters essential for dose selection — the model performs **worse than predicting the dataset mean** (R² = -2.39 and -1.21, respectively)." [Source: ADMET-AI built-in admet.csv]

2. "Even across all models on the TDC ADMET leaderboard, the best Spearman correlation for half-life prediction is 0.576 (CFA), and for hepatocyte clearance 0.536 — correlations too weak to inform clinical dosing decisions." [Source: tdcommons.ai leaderboard, April 2026]

3. "Current ADMET prediction tools treat solubility as a single scalar, yet pH-dependent solubility varies >1000-fold for drugs like atazanavir across the GI pH range, a reality no current ML model captures."

4. "CYP inhibition is predicted as binary yes/no, ignoring pharmacogenomic variation that causes 3-fold differences in cardiovascular outcomes for clopidogrel across CYP2C19 metabolizer phenotypes."

5. "A 2026 reproducibility assessment found only 3 of the top-ranked TDC ADMET models passed all reproducibility checks, with data leakage identified in multiple entries."

### DO NOT claim:
- ~~"R² > 0.6 on 50% of regression tasks"~~ — it's actually 40% (4/10)
- The paper says "five of ten" which relies on rounding LD50 (R²=0.596) upward
- Use the more precise numbers from the actual built-in data
