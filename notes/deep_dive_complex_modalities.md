# Deep Dive: AI Limitations for Complex Drug Modalities (ADC, ASO, PROTAC, bRo5)

> Date: 2026-04-04
> Status: Complete

---

## 1. Training Data Bias — The Fundamental Problem

**>90% of ML training data is Ro5-compliant**, yet the fastest-growing modalities all occupy bRo5 space:
- ChEMBL: ~9.2% non-Lipinski out of ~2M entries (Capecchi et al., Mol Inform 2019. DOI: 10.1002/minf.201900016)
- PubChem: ~7.6% break at least one Lipinski constraint (7M of 94M)
- Standard ADMET models systematically under-predict for bRo5 compounds
- Permeability models show NO correlation with standard predictors for PROTACs
- "Chameleonic" behavior (different conformations in polar vs nonpolar environments) not captured by standard models
- Citation: Morreale et al., J Med Chem 2024;67(6). DOI: 10.1021/acs.jmedchem.3c02332

---

## 2. ADC (Antibody-Drug Conjugates)

### Computational Challenges Unique to ADCs
- High-dimensional coupled space: antibody × linker × payload × DAR × conjugation site
- AF2/AF3 not designed for small-molecule conjugation or glycan modeling
- DAR heterogeneity: mixture-level PK/tox behavior unpredictable
- Bystander killing: no published AI model predicts magnitude
- Data scarcity for multimodal training

### Published ML Models
| Model | Task | Accuracy | Publication |
|-------|------|----------|-------------|
| ADCNet | Activity prediction (all 5 components) | 87.12%, AUROC 0.93 | Brief Bioinform 2025 |
| DumplingGNN | Payload activity | 91.48%, spec 97.54% | Int J Mol Sci 2025 |
| XGBoost DAR | DAR prediction | R²=0.85 (lysine), 0.95 (cysteine) | JCIM 2025 |

**Critical caveat**: All predict in vitro activity — NONE predict clinical efficacy or in vivo therapeutic index.

### Clinical Landscape
- 15 ADCs approved globally; 275 active clinical trials; 24 in Phase III
- ADC PTRS in Phase III: 53% (vs 41% oncology overall)
- Market: $11.4B (2023) → $24B by 2030

### **Zero AI-designed ADCs in clinical trials** — 275 trials, none AI-first

### Key Reviews
- Nature Chemical Biology 2025. DOI: 10.1038/s41589-025-01950-z
- npj Precision Oncology 2025. DOI: 10.1038/s41698-025-01159-2

---

## 3. Oligonucleotides (ASO/siRNA)

### What AI CAN Predict
- Sequence-level efficacy: ASOptimizer, eSkipFinder (Mol Ther Nucleic Acids 2024)
- Off-target binding reduction: 40-60% improvement via DL (Bereczki et al., Br J Pharmacol 2025)
- GalNAc-siRNA PK: sequence-independent, conserved across species (McDougall et al., Clin Pharmacol Ther 2023)

### What AI CANNOT Predict
- **Hepatotoxicity mechanism**: 2'-F-modified ASOs bind DBHS proteins → toxicity. Not predictable from sequence (Crooke et al., NRDD 2021)
- **Extrahepatic delivery**: No approved siRNA targets non-liver tissue. GalNAc works for liver; CNS/muscle/kidney/lung delivery unsolved by AI
- **Immunostimulation**: TLR7/8/9 and RIG-I engagement — poorly predicted, remains empirical
- **In vivo tissue distribution**: computational models insufficient for safe extrahepatic targeting

### Crooke et al. 2021 Key Points (Nat Rev Drug Discov 20:427-453)
- 9 single-stranded ASO drugs approved across 4 chemical classes
- Major toxicity mechanism: sequence-dependent protein binding → pro-inflammatory effects
- >20 years of development, attrition still high

---

## 4. PROTACs / Molecular Glues

### Ternary Complex Prediction
- **Drummond et al. 2024 (JCIM)**: Benchmarked PRosettaC, MOE, ICM on 36 crystal structures. Models produce experimentally observed conformations BUT also many deviating ones. PROTACs exist as **conformational ensembles**, not single structures.
- **AF3 vs Boltz-2** (Riepenhausen et al. 2026): AF3 produced 33/40 complexes RMSD <1Å, BUT performance inflated by accessory proteins
- **PRosettaC vs AF3** (Sci Rep 2025): PRosettaC outperforms AF3 for PROTAC ternary complexes in some systems. Critically, models with poor static alignment achieved **high DockQ with specific MD trajectory frames** — static benchmarking misses dynamic reality

### Hook Effect & Cooperativity
- MM/GBSA characterizes cooperativity but requires 50-100 ns MD (JCIM 2024)
- DL-QSP hybrid (J Cheminformatics 2026): first framework explicitly modeling hook effect
- Coarse-grained approaches capture principles but limited quantitative accuracy

### Degradation Prediction
| Model | Accuracy | AUROC | Notes |
|-------|----------|-------|-------|
| DeepPROTACs | 77.95% | 0.847 | Nat Commun 2022; limited by 2D representations |
| DegradeMaster | +2.6% over SOTA | +6.9% AUROC | Bioinformatics 2025; E(3)-equivariant GNN |

### Key Challenges Unique to Degraders
1. Conformational flexibility (ensembles, not single structures)
2. Non-additive cooperativity (binary ≠ ternary)
3. Hook effect requires mechanistic PK/PD
4. Linker space explosion
5. Only 2/~600 E3 ligases routinely used (CRBN, VHL)
6. Ubiquitination geometry (lysine accessibility) almost never modeled

### ~30 PROTACs in clinical trials; NONE explicitly AI-designed from scratch
- ARV-471 (vepdegestrant): Phase III / NDA (ER degrader)
- BMS-986365: Phase III (AR degrader)
- All designed with traditional medchem + computational assistance

---

## 5. Key Insight for Review

**The AI drug discovery field is optimized for Ro5 small molecules, but the frontier of drug development has moved to bRo5 space.** This creates a growing mismatch:
- >90% training data is Ro5
- ADCs, PROTACs, macrocycles, oligonucleotides are all bRo5
- Standard ADMET models fail outside their training domain
- Zero AI-first ADCs or PROTACs in clinical trials
- The fastest-growing therapeutic modalities are the LEAST amenable to current AI approaches
