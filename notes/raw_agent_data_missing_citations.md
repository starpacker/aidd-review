# Raw Agent Data: Missing Citations (10 Papers)

> Source: Agent "Find missing citation papers" (2026-04-03)
> Status: Verified

---

## 1. Relay Therapeutics RLY-2608

**Citation**: Varkaris A, Pazolli E, Gunaydin H, et al. "Discovery and Clinical Proof-of-Concept of RLY-2608, a First-in-Class Mutant-Selective Allosteric PI3Kα Inhibitor That Decouples Antitumor Activity from Hyperinsulinemia." *Cancer Discovery*, 2024; 14(2): 240-257. DOI: 10.1158/2159-8290.CD-23-0944

**Status**: Phase 3 (ReDiscover-2 trial, NCT06982521), RLY-2608 + fulvestrant vs capivasertib + fulvestrant in PIK3CA-mutant HR+/HER2- breast cancer.

**Clinical data (Phase 1/2)**:
- Median PFS: 10.3 months overall; 11.0 months in 2L; kinase-domain mutations: **18.4 months**
- ORR: 39%
- Safety: hyperglycemia 42.4% (only 2.5% Grade 3); **no Grade 4/5 treatment-related AEs**

**Motion-based drug design (Dynamo platform)**:
- Solved full-length cryo-EM structure of PI3Kα
- Long-timescale MD simulations revealed conformational differences WT vs mutant
- Identified allosteric network explaining mutant activation
- RLY-2608 = first-in-class allosteric, pan-mutant, isoform-selective inhibitor
- Binds outside ATP pocket → spares WT PI3Kα → decouples efficacy from hyperinsulinemia

**Review relevance**: Strongest current example of physics-based/dynamics-driven AI reaching clinical validation. Understanding protein dynamics (not just static structure) solved a real clinical problem.

---

## 2. Schneider 2018 — Multi-parameter Optimization

**Citation**: Schneider G. "Automating drug discovery." *Nature Reviews Drug Discovery*, 2018; 17: 97-113. DOI: 10.1038/nrd.2017.232

**Key arguments**:
- Drug discovery = multi-dimensional optimization (efficacy, PK, safety in parallel)
- Advocates closing DMTA cycle through automation
- AI value = navigating vast chemical space under multiple constraints
- Microfluidics-assisted synthesis supports automation

**Review relevance**: Foundational MPO reference. 2018 vision of fully automated DMTA has not materialized — the gap is what our review addresses.

---

## 3. Walters & Barzilay 2021 — Benchmark Limitations

**Citation**: Walters WP, Barzilay R. "Critical assessment of AI in drug discovery." *Expert Opinion on Drug Discovery*, 2021; 16(9): 937-947. DOI: 10.1080/17460441.2021.1915982

**Key arguments**:
- Molecule generation methods "relatively new and unproven"
- Benchmark datasets (MoleculeNet, Tox21) problematic: labels imputed, datasets altered, loss of comparability
- **Random data splits inflate metrics** vs. time-based splits (real-world deployment)
- Overfitting to benchmarks without genuine generalization
- **Data leakage** between train/test undermines performance
- ML for property prediction = routine but not transformative

**Review relevance**: Critical for "benchmark-to-bedside gap" thesis. Random vs temporal splits + data leakage = concrete evidence metrics overstate real-world utility.

---

## 4. Mobley & Gilson 2017 — Solvation Modeling

**Citation**: Mobley DL, Gilson MK. "Predicting binding free energies: Frontiers and benchmarks." *Annual Review of Biophysics*, 2017; 46: 531-558. DOI: 10.1146/annurev-biophys-070816-033654

**Key limitations**:
1. Fixed-charge force fields underestimate polarization
2. Sampling difficulties: binding mode transitions as slow as 0.07 flips/ns
3. Wetting/dewetting transitions on 50 ns timescale
4. **Buffer/salt composition shifts binding free energies by 2.5-2.8 kcal/mol** = ~100-fold error in predicted affinity
5. Three error sources: (a) inadequate conformational sampling, (b) force field inaccuracy, (c) system misrepresentation (wrong protonation states)

**Review relevance**: 2.5-2.8 kcal/mol from salt effects alone is devastating — most AI docking pipelines ignore solvent/salt entirely.

---

## 5. Schuhmacher et al. — Cross-disciplinary Teams

**STATUS: The specific "Schuhmacher et al. 2020 NRDD" paper CANNOT be verified.**

Closest candidates:
- Schuhmacher A et al. "Changing R&D models in research-based pharmaceutical companies." *J Transl Med*, 2016; 14: 105. DOI: 10.1186/s12967-016-0838-4
- Schuhmacher A et al. "Investigating the origins of recent pharmaceutical innovation." *NRDD*, 2023; 22(10): 781-782. DOI: 10.1038/d41573-023-00102-z — found 65% of drugs approved 2015-2021 originated externally; only 28% in-house (FIPCO→BIPCO transition)

**Recommendation**: Use the 2023 NRDD paper or find alternative reference for cross-disciplinary teams.

---

## 6. Feuerriegel et al. 2024 — Causal Inference

**Citation**: Feuerriegel S, Frauen D, Melnychuk V, et al. "Causal machine learning for predicting treatment outcomes." *Nature Medicine*, 2024; 30(4): 958-968. DOI: 10.1038/s41591-024-02902-1

**Key contributions**:
- Causal ML vs standard ML: standard finds correlations; causal ML estimates individualized treatment effects (ITE)
- Methods: GANITE, various causal inference frameworks
- Three applications: (1) drug efficacy, (2) safety monitoring, (3) personalized therapy
- Works with clinical trial data AND real-world data (EHR, registries)
- Caveat: RWD applications risk biased predictions without proper confounder control

**Review relevance**: Key reference for correlative→causal reasoning argument. "Will this drug work for this patient?" is the causal question AI can't yet answer.

---

## 7. Yun et al. 2008 — EGFR T790M

**Citation**: Yun CH, et al. "The T790M mutation in EGFR kinase causes drug resistance by increasing the affinity for ATP." *PNAS*, 2008; 105(6): 2070-2075. DOI: 10.1073/pnas.0709662105

**Key findings**:
- **Overturned prevailing hypothesis**: T790M was thought to be steric blockade
- **Actual mechanism**: T790M increases ATP affinity >10-fold → drugs outcompeted by ATP
- Crystal structures: T790M can still accommodate diverse inhibitors
- Irreversible inhibitors overcome via covalent binding, not alternative binding mode

**Review relevance**: Classic example of static structural predictions being fundamentally wrong. AI trained on structure alone would predict steric clash, missing thermodynamic/kinetic reality.

---

## 8. Crooke et al. — ASO Review

**Citation**: Crooke ST, Liang XH, Baker BF, Crooke RM. "Antisense technology: A review." *J Biol Chem*, 2021; 296: 100416. DOI: 10.1016/j.jbc.2021.100416

**Key challenges**:
- Delivery = greatest challenge
- Higher-affinity modifications (LNA, cEt) paradoxically INCREASE cytotoxicity/hepatotoxicity (via paraspeckle proteins, RNase H1 interactions — NOT off-target hybridization)
- GalNAc conjugation: 15-30x increase in hepatocyte potency (transformative)
- 10 RNA-targeted drugs approved (8 ASOs, 2 siRNAs) at time of writing
- **No discussion of AI/computational approaches** — telling absence

**Review relevance**: ASO challenges (delivery, tissue targeting, modification-toxicity tradeoffs) largely beyond current AI. The paradox that optimizing binding affinity worsens safety = our MPO argument.

---

## 9. NRDD December 2025 — Phase II/III Terminations

**Citation**: Bowling H, Cocucci A, Koo DCE, Harrison RK. "Analysis of phase II and phase III clinical trial terminations from 2013 to 2023." *NRDD*, Dec 2025. DOI: 10.1038/d41573-025-00208-6. PMID: 41413264.

**Key data**:
- Database: Epistemic AI platform
- N = 3,180 terminated trials (2013-2023)
- Termination rate doubled: 11% (2013) → 22-23% (2023)

**Termination reasons**:
| Reason | % |
|--------|---|
| Strategic/business | **36%** |
| Lack of efficacy | **24%** |
| Enrollment | **18%** |
| Operational | 7% |
| Safety | **5%** |
| Unknown | 10% |

- Efficacy (24%) now LOWER than previously reported (~50% a decade ago)
- Business/strategic (36%) = #1 driver, displacing efficacy
- No AI-drug-specific subanalysis
- Phase 3: $50-250M per asset

**Review relevance**: Even with perfect AI target validation, 36%+18%+7% = 61% of terminations unrelated to target biology. Fundamentally limits how much AI can reduce attrition.

---

## 10. Hasin et al. 2017 — Multi-omics

**Citation**: Hasin Y, Seldin M, Lusis A. "Multi-omics approaches to disease." *Genome Biology*, 2017; 18(1): 83. DOI: 10.1186/s13059-017-1215-1

**Three integration frameworks**:
1. Genome-first: GWAS locus → mechanism
2. Phenotype-first: clinical outcomes → molecular basis
3. Environment-first: perturbations × genetic variation

**Layers**: Genomics, transcriptomics, proteomics, metabolomics, epigenomics

**Review relevance**: Foundation for arguing single-modal AI pipelines miss cross-layer interactions. Frameworks map well to our discussion of where pipelines break down.
