# Deep Dive: Causal Inference, Multi-omics, and Digital Twins in Drug Discovery

> **Purpose**: Evidence base for Section 6.3 (Technical Roadmap) of review manuscript
> **Created**: 2026-04-03
> **Status**: Research notes — not yet integrated into draft

---

## PART 1: Causal Inference in Drug Discovery

### 1.1 Feuerriegel et al. 2024 — Landmark Review

**Full citation**: Feuerriegel S, Frauen D, Melnychuk V, Schweisthal J, Hess K, Curth A, Bauer S, Kilbertus N, Kohane IS, van der Schaar M. Causal machine learning for predicting treatment outcomes. *Nature Medicine*. 2024;30(4):958-968. DOI: 10.1038/s41591-024-02902-1

**Key causal ML methods described**:
- **GANITE** (Generative Adversarial Nets for Individualized Treatment Effects) — uses GANs to estimate individualized treatment effects
- **Causal forests / causal trees** — adapted from random forests and decision trees for heterogeneous treatment effect estimation
- **Meta-learners**: S-learner, T-learner, DR-learner (doubly robust), R-learner — model-agnostic frameworks that combine arbitrary ML models
- **TMLE** (Targeted Maximum Likelihood Learning) — semiparametric efficient estimator
- **Doubly robust methods** — combine propensity score and outcome regression
- **Representation learning approaches** — neural network-based
- **Bayesian methods & conformal prediction** — for uncertainty quantification

**Taxonomy of causal ML approaches** (two dimensions):
1. By effect heterogeneity: ATE (population-level) → CATE (subgroup-specific) → potential outcome prediction (individual)
2. By treatment type: binary → discrete → continuous (dose-response)

**Drug discovery / pharmaceutical examples**:
- Antidiabetic drugs (SGLT2 inhibitors, GLP-1 receptor agonists, DPP-4 inhibitors, sulfonylureas) — heterogeneous treatment effects by patient profile
- Antidepressant drugs — treatment effect heterogeneity by severity
- Radiation therapy dosing in oncology
- Psychiatric hospitalization effects on suicide risk

**Stated limitations**:
1. **Unmeasured confounding**: "estimated treatment effects may suffer from confounding bias and can even have a wrong sign"
2. **Sample size requirements**: flexible causal models require larger datasets than parametric approaches
3. **Assumption validation difficulty**: plausibility of underlying assumptions "often difficult" to assess
4. **Uncertainty quantification gaps**: many causal ML methods "lack uncertainty estimates such as standard errors"
5. **Evaluation obstacles**: ground-truth counterfactual outcomes remain unobservable — cannot directly evaluate CATE predictions
6. **Implementation barriers**: many methods only available in "specialized software libraries"

**Key insight for our review**: Feuerriegel et al. focus on *treatment outcome prediction* (clinical decision support), not drug discovery per se. The gap is that causal ML has been extensively theorized for clinical applications but barely applied to the drug discovery pipeline (target ID, lead optimization). This is our angle.

---

### 1.2 Michoel & Zhang 2023 — Causal Inference in Drug Discovery and Development

**Full citation**: Michoel T, Zhang JD. Causal inference in drug discovery and development. *Drug Discovery Today*. 2023;28(10):103737. DOI: 10.1016/j.drudis.2023.103737

**Key arguments**:
- Causality is "indispensable for intervention, what-if questions, and understanding"
- Present an iterative six-step model for conducting causal inference in drug discovery
- Causal inference "fuels both forward and reverse translation"
- Advocate for adopting causal language and methodology *throughout* the drug discovery pipeline
- Call for better models, open science, and a mindset shift among practitioners

**For our review**: This paper provides the conceptual framework — causal inference is needed not just in clinical settings (Feuerriegel) but throughout the entire drug discovery pipeline. Pair with Pearl's hierarchy.

---

### 1.3 Pearl's Causal Hierarchy Applied to Drug Discovery

**Reference**: Pearl J. *Causality: Models, Reasoning, and Inference*. Cambridge University Press, 2nd ed., 2009.

**The Ladder of Causation** (relevant to our argument):
1. **Association** (seeing): P(Y|X) — "patients who take drug X have outcome Y" — this is where most current AIDD operates
2. **Intervention** (doing): P(Y|do(X)) — "what happens if we give drug X?" — requires causal models, not just correlations
3. **Counterfactual** (imagining): P(Y_x|X', Y') — "would this patient have responded differently with drug Z?" — the ultimate goal for personalized medicine

**Key gap**: Most AIDD models operate at Level 1 (association/correlation). They learn patterns like "molecules with feature X tend to bind target Y" but cannot answer "will modifying target Y *cause* disease improvement?" This is why Phase II fails — the targets were associated with disease but not causally responsible.

**Structural Causal Models (SCMs)** and **do-calculus** provide the mathematical framework to move from Level 1 to Level 2, but require domain knowledge (DAGs) that most AIDD pipelines lack.

---

### 1.4 Companies Using Causal ML for Drug Discovery

#### Recursion Pharmaceuticals — Causal AI in Practice
- Recursion leveraged **multi-omic and real-world patient data with causal AI modeling** to select platinum-resistant ovarian cancer as the first combination cohort for **REC-617** (CDK7 inhibitor)
- Nov 2023: collaboration with **Tempus** for de-identified oncology datasets to train causal AI models for biomarker-enriched therapeutics
- May 2024: multi-year agreement with **Helix** for genomic + longitudinal health records to train causal AI models for patient stratification
- July 2025: merger with **Exscientia** created largest combined AI drug discovery entity
- **REC-617 clinical result**: confirmed durable partial response (PR) by RECIST in metastatic platinum-resistant ovarian cancer patient, ongoing >6 months on monotherapy
- **Key distinction**: Recursion uses causal AI primarily for *patient/indication selection*, not for target discovery or molecular design — an important nuance

#### Aitia (formerly GNS Healthcare) — Causal-First Platform
- Founded 2000 by Colin Hill and Iya Khalil; rebranded as Aitia Jan 2023 (Greek: "causality")
- **Gemini Digital Twins**: computational representations of human disease using causal AI
- **REFS engine** (Reverse Engineering Forward Simulation): reverse-engineers genetic and molecular interactions driving clinical outcomes, then forward-simulates interventions
- Process: Multiomic patient datasets → Causal AI analysis → Counterfactual in silico experiments across millions of patient-derived twins
- Disease areas: multiple myeloma, prostate cancer, Alzheimer's, Parkinson's, Huntington's
- Partners: 7 of top 10 pharma companies; collaboration with **Gustave Roussy** (cancer)
- **Limitation**: No disclosed clinical-stage candidates yet; platform is pre-clinical/discovery stage
- **Reference**: Nature Advertiser Feature: "Causal artificial intelligence and digital twins are transforming drug discovery and development." *Nature*. 2024. DOI: 10.1038/d43747-024-00077-9

#### BenevolentAI — Causal Reasoning over Knowledge Graphs
- **Benevolent Knowledge Graph**: maps billions of relationships across diseases, proteins, genes, drugs, biological processes, clinical outcomes from 85+ data sources
- **RPath algorithm**: prioritizes drugs by reasoning over *causal paths* in a knowledge graph, guided by drug-perturbed and disease-specific transcriptomic signatures
  - Reference: Ruiz C, Zitnik M, Leskovec J. Causal reasoning over knowledge graphs leveraging drug-perturbed and disease-specific transcriptomic signatures for drug discovery. *PLOS Computational Biology*. 2022;18(2):e1009909. DOI: 10.1371/journal.pcbi.1009909
  - Note: RPath was published by Enveda Biosciences, not BenevolentAI directly, but represents the same methodological approach
- **Key innovation**: addresses limitation of standard link-prediction algorithms that "fail to model causal relationships in complex dynamic biological systems" — RPath retains only paths observable in biologically meaningful context
- BenevolentAI platform generates confidence scores, biological evidence chains, and traceable reasoning paths (not black-box)
- BenevolentAI validated approach in Nature Communications 2024: "An experimentally validated approach to automated biological evidence generation in drug discovery using knowledge graphs." *Nature Communications*. 2024;15:5624. DOI: 10.1038/s41467-024-50024-6

---

### 1.5 Causal vs. Correlative: Where Causal Reasoning Would Have Caught Failures

**The fundamental problem**: Most AIDD operates at Pearl's Level 1 (association). A model trained on observational data learns that "gene X is differentially expressed in disease Y" — but differential expression is NOT evidence of causality. The gene may be:
- A downstream consequence (effect, not cause)
- Confounded by a shared upstream driver
- Context-dependent (causal in one tissue, bystander in another)

**Concrete failure mode**: GWAS-identified targets
- Many GWAS hits are non-causal (in LD with causal variant, or reflect reverse causation)
- Drugs targeting non-causal GWAS associations will pass Phase I (safe molecule) but fail Phase II (wrong target)
- This is *exactly* the "precision paradox" we describe in Section 1 — Phase I success ≠ Phase II success

**The confounding-by-indication problem** (Feuerriegel et al.):
- In observational data, sicker patients receive more aggressive treatment
- Correlative ML trained on such data may conclude "treatment X is associated with worse outcomes" — the opposite of truth
- Causal methods (propensity scores, instrumental variables, MR) can correct this; standard ML cannot

**Published comparison**:
- ML-based causal algorithms (double ML, doubly robust learner, forest DML, generalized random forest) applied to dexamethasone response prediction found that "estimated CATE did not correlate with predicted risk" — risk prediction and treatment effect estimation require fundamentally different approaches
  - Reference: Scientific Reports. 2023;13:8505. DOI: 10.1038/s41598-023-34505-0

---

### 1.6 Mendelian Randomization as Causal Drug Target Validation

**Concept**: MR uses genetic variants as "natural experiments" (instrumental variables) to estimate causal effects of modifiable exposures on outcomes. Because genotypes are randomly allocated at conception (Mendel's 2nd law), MR avoids confounding and reverse causation — effectively a "natural RCT."

**Relevance to AIDD**: MR can validate whether a computationally-identified target is *causally* linked to disease *before* committing to expensive clinical development. This bridges the gap between correlative target ID and clinical validation.

#### Key Evidence: Nelson et al. 2015
- **Citation**: Nelson MR, Tipney H, Painter JL, et al. The support of human genetic evidence for approved drug indications. *Nature Genetics*. 2015;47(8):856-860. DOI: 10.1038/ng.3314
- **Finding**: Among well-studied indications, proportion of drug mechanisms with direct genetic support increases from 2.0% (preclinical) to 8.2% (approved drugs)
- **Conclusion**: selecting genetically supported targets could **double the success rate** in clinical development
- **Impact**: First empirical demonstration that human genetic data can measurably improve drug development odds

#### Refinement: Minikel et al. / Ochoa et al.
- **Citation**: Minikel EV, Painter JL, Dong CC, Nelson MR. Refining the impact of genetic evidence on clinical success. *Nature*. 2024;629:624-629. DOI: 10.1038/s41586-024-07316-0
- **Key refinement**: probability of success for drug mechanisms with genetic support is **2.6× greater** than those without (up from 2× in Nelson 2015)
- Success varies by therapy area and development phase; improves with increasing confidence in causal gene
- Largely unaffected by genetic effect size, minor allele frequency, or year of discovery

#### Key Validation: MR-Informed ML for Target Prioritization (2026 Preprint)
- **Citation**: (Authors TBC). Retrospective evaluation of human genetic evidence for clinical trial success using Mendelian randomization and machine learning. *medRxiv*. 2026. DOI: 10.64898/2026.02.19.26346536
- **Methodology**: Systematic evaluation of MR across **11,482 target-indication pairs** with documented Phase II outcomes
- **Key finding 1**: MR statistical significance *alone* does NOT enrich for Phase II success (important caveat!)
- **Key finding 2**: When MR-derived features (instrument strength, explained variance) are integrated into **XGBoost classifier**, the model identifies target-indication pairs with **55% overall approval rate** — a **6.4-fold enrichment** over unstratified populations
- **Implication**: MR is most powerful when used as a *feature* in ML models, not as a binary filter — causal evidence must be quantified, not just binarized

#### Canonical Success Examples
- **PCSK9 inhibitors** (evolocumab, alirocumab): Loss-of-function variants in PCSK9 → reduced LDL → reduced CAD risk. MR prediction validated by clinical trials. Rapid FDA approval.
- **HMGCR** (statins): MR instruments at HMGCR locus replicate statin trial effects on LDL and CVD with 95-99% agreement in direction of effect
- **IL-6 receptor antagonists** (tocilizumab, sarilumab): MR predicted protective effects on COVID-19 severity → confirmed by RECOVERY trial results. MR also predicted null effects on pulmonary arterial hypertension → confirmed by subsequent Phase 2 findings.

#### MR Limitations
- Requires strong genetic instruments (weak instruments → bias toward null)
- Pleiotropy can violate exclusion restriction (genetic variant affects outcome through pathways other than target)
- Cannot capture all aspects of drug action (e.g., dose-response, off-target effects)
- Population-level estimates; limited insight into individual heterogeneity

---

## PART 2: Multi-omics Integration — Updated from Hasin 2017

### 2.1 Current Landscape (2023-2026)

**Original reference**: Hasin Y, Seldin M, Lusis A. Multi-omics approaches to disease. *Genome Biology*. 2017;18:83. DOI: 10.1186/s13059-017-1215-1

**What has changed since 2017**:
1. Single-cell resolution is now standard (scRNA-seq, scATAC-seq, CITE-seq)
2. Spatial transcriptomics adds tissue context (10x Visium, MERFISH, Slide-seq)
3. AI/ML integration is routine (not aspirational as in 2017)
4. Multi-omics → drug target ID is now empirically validated (not theoretical)

### 2.2 Key Recent Reviews

1. **Jaeger S et al.** Applications of single-cell RNA sequencing in drug discovery and development. *Nature Reviews Drug Discovery*. 2023;22:496-520. DOI: 10.1038/s41573-023-00688-4
   - Comprehensive review of scRNA-seq applications across drug discovery pipeline
   - scRNA-seq identified targets with cell-type-specific expression more likely to enter clinical development and pass Phase I

2. **Frontiers review 2024**: Single-cell multiomics: a new frontier in drug research and development. *Frontiers in Drug Discovery*. 2024;4:1474331. DOI: 10.3389/fddsv.2024.1474331
   - Covers integration of AI with single-cell multiomics
   - Highlights LILRB4 identification in multiple myeloma as promising immunotherapy target

3. **Spatial transcriptomics review**: Spatial transcriptomics: a powerful tool in disease understanding and drug discovery. *Theranostics*. 2024;14(8):2946. DOI: 10.7150/thno.95908

### 2.3 Concrete Multi-omics → Drug Discovery Successes

#### scRNA-seq Validation of Drug Targets
- **Citation**: (Authors TBC). Estimating the impact of single-cell RNA sequencing of human tissues on drug target validation. *medRxiv*. 2024. DOI: 10.1101/2024.04.04.24305313
- **Key finding**: scRNA-seq data across **30 diseases and 13 tissues** — both classes of scRNA-seq support significantly increase odds of clinical success
- **Quantitative result**: Combined scRNA-seq support could approximately **triple the chances** of a target reaching Phase III
- scRNA-seq preferentially identifies therapeutically tractable gene classes (e.g., membrane-bound proteins)

#### Specific Target Discoveries via Multi-omics
- **LILRB4** in multiple myeloma: scRNA-seq revealed enrichment in pre-matured plasma cells → promising immunotherapy target for both tumor cells and myeloid-derived suppressive cells
- **NNMT and HILPDA** in clear cell renal cell carcinoma: identified via scRNA-seq + spatial transcriptomics
- **AQP5 and KPNA2** as lung cancer drug targets: identified via single-cell sub-cluster analysis

#### No Approved Drug Yet from Multi-omics Pipeline
- **Critical honest assessment**: Despite extensive target identification, no drug discovered *primarily through* multi-omics integration has achieved FDA approval as of 2026
- Multi-omics currently enhances target validation and patient stratification, but has not yet produced a de novo approved therapeutic
- This mirrors the broader AIDD challenge: computational advances in target ID ≠ clinical success

### 2.4 Spatial Transcriptomics for Drug Target Validation — State of the Art

**Key advances (2024-2025)**:
- Spatial transcriptomics reveals **tumor microenvironment-driven drug responses** and clonal therapeutic heterogeneity
  - Reference: *NAR Cancer*. 2024;6(4):zcae046. DOI: 10.1093/narcan/zcae046
  - Finding: genetically identical subclones show different drug responses depending on spatial location within tumor — drug sensitivity gradient from tumor core to periphery
- **3D spatial analysis**: spherical neighborhoods (50 μm) reveal 10 multicellular niches including "vascular stroma" vs. "desmoplastic stroma" with distinct drug response profiles
  - Reference: *Cell Systems*. 2025. DOI: 10.1016/j.cels.2025
- **Therapy resistance**: spatial omics reveals novel resistance mechanisms driven by tumor-microenvironment heterogeneity
  - Reference: *Cancer and Metastasis Reviews*. 2025. DOI: 10.1007/s10555-025-10304-z
- **PD-1 blockade biomarkers**: spatial single-cell transcriptomics in breast cancer identified potential biomarkers for PD1 therapy response based on spatial organization of immune cells

**Implication for our review**: Spatial transcriptomics demonstrates that drug response is not just a property of the target gene — it depends on *spatial context* (tissue architecture, cell neighborhoods, niche composition). This is information that no current AIDD pipeline captures, and explains why in vitro validated targets fail in vivo.

---

## PART 3: Digital Twins in Drug Discovery

### 3.1 Unlearn.AI — Virtual Control Arms (Most Advanced)

**Company**: Unlearn AI, San Francisco
**Technology**: PROCOVA™ (Prognostic Covariate Adjustment)
**Method**: Conditional Restricted Boltzmann Machine (CRBM) trained on historical control data → generates probabilistic forecast of each participant's placebo trajectory → used as prognostic covariate to reduce variance

#### Regulatory Status
- **EMA**: Positive Qualification Opinion (September 2022) for use in Phase 2 and 3 trials with continuous outcomes — **first AI-generated digital twin methodology qualified by a major regulator**
- **FDA**: Approach "aligns with existing guidance" on covariate adjustment in RCTs; no formal qualification yet

#### Quantitative Results — Alzheimer's Disease (AWARE Trial)
- **Citation**: Wang D, Florian H, Lynch SY, et al. Using AI-generated digital twins to boost clinical trial efficiency in Alzheimer's disease. *Alzheimer's & Dementia: Translational Research & Clinical Interventions*. 2025;11:e70181. DOI: 10.1002/trc2.70181
- Trained on historical data from **6,736 unique subjects**
- Validated on AbbVie's AWARE trial (453 participants, Phase 2, tilavonemab in early AD)
- **Variance reduction**: 9-15% reduction in total residual variance (vs. <5% with standard baseline covariate adjustment)
- **Sample size savings**: 9-15% overall; **control arm specifically reducible by 17-26%**
- **CDR-SB endpoint**: ~13% total sample size savings (23% control-only savings)
- Correlation between digital twin predictions and actual outcomes: 0.30-0.46

#### Other Partnerships
- **Johnson & Johnson**: showed digital twins could reduce control arm sizes by **up to 33%** in Phase 3 Alzheimer's trials
- **AbbVie**: AWARE trial collaboration (above)

### 3.2 Phesi — AI-Powered Digital Twin Control Arms

**Citation**: Phesi et al. Construction of a digital twin of chronic graft vs. host disease patients with standard of care. *Bone Marrow Transplantation*. 2024. DOI: 10.1038/s41409-024-02324-0

- Created digital twin for chronic graft-versus-host disease (cGvHD) first-line treatment (prednisone)
- **Scale**: 2,042 patients from 32 cohorts → digital twin cohort; 438 patients from 8 cohorts → validation
- **Result**: standard-of-care 6-month overall response rate barrier = 52.7%
- **Application**: digital twin could function as External Control Arm in single-arm trials, addressing ethical concerns about placebo arms in rare diseases

### 3.3 Aitia (formerly GNS Healthcare) — Causal Digital Twins

(See Section 1.4 above for details)
- Gemini Digital Twins use causal AI (not just predictive models) to simulate disease biology
- Distinguish from Unlearn/Phesi: Aitia focuses on *disease mechanism* digital twins for drug discovery; Unlearn/Phesi focus on *patient trajectory* digital twins for trial design

### 3.4 FDA Position on Digital Twins / In Silico Trials

**Key developments**:
1. **FDA Strategic Document (2024)**: "In silico technologies, a strategic imperative for accelerating breakthroughs and market leadership for FDA-regulated products" — acknowledges potential to "enhance drug development, help bring safe and effective drugs to patients faster"
2. **FDA Digital Health Center of Excellence**: fostering responsible digital health innovation including computational modeling
3. **FDA-Dassault Systèmes collaboration (2019-2024)**: In Silico Clinical Trial Enrichment Project → published Playbook for regulatory use of in silico clinical trials (completed 2024)
4. **FDA April 2025 announcement**: phased plan to make animal studies "the exception rather than the norm within 3-5 years" — creates space for in silico alternatives
5. **FDA Modernization Act 2.0** (Dec 2022): explicitly permits AI/ML methods, in silico trials as alternatives to animal testing in IND applications

**EMA Position**:
- "AI Action Plan" includes frameworks for digital twins
- Favorable qualification opinion for Unlearn's PROCOVA in Phase 2 and 3 trials
- EMA qualification = strongest regulatory endorsement to date for digital twins in drug development

**Regulatory gap**: FDA has guidance on AI in medical devices and AI supporting *regulatory decisions*, but **no framework governs AI in the discovery phase** (as noted in our outline, Section 6.1). Digital twins for clinical trials are advancing faster regulatorily than digital twins for drug discovery.

### 3.5 Other Pharma Companies

- **Roche**: Dimitris Christodoulou (global business lead, digital health) stated at DACH 2025 that fully simulating patient physiology "remains on the horizon" — current focus on operational and behavioral twins
- **Novartis**: partnered with Zontal for digital lab models
- **AbbVie**: collaborated with Unlearn on AWARE trial (see 3.1)

### 3.6 PNAS Nexus 2025 — Future of In Silico Trials

**Citation**: (Authors TBC). The future of in silico trials and digital twins in medicine. *PNAS Nexus*. 2025;4(5):pgaf123. DOI: 10.1093/pnasnexus/pgaf123
- Based on roundtable at first International Summit on Virtual Imaging Trials in Medicine (VITM24, spring 2024)
- Convened leading thought-leaders from academia, industry, government, and regulators
- Defined gaps and priorities for in silico and digital twin technology development

### 3.7 Lancet Digital Health 2025 — Pediatric Digital Twins

**Citation**: (Authors TBC). Digital twins, synthetic patient data, and in-silico trials: can they empower paediatric clinical trials? *The Lancet Digital Health*. 2025. DOI: 10.1016/S2589-7500(25)00007-X
- Special focus on pediatric trials where recruitment is ethically and practically challenging
- Argues digital twins could be particularly transformative for rare pediatric diseases

---

## Synthesis: Key Arguments for Section 6.3

### The Causal Inference Argument (strongest new evidence)
1. **The problem is clear**: Current AIDD operates at Pearl's Level 1 (association). Phase II failures are *caused by* this — targets are associated with disease, not causally responsible.
2. **Solutions exist**: MR (genetic causal inference) doubles/triples success rates; causal ML (GANITE, causal forests, etc.) can estimate treatment effects; causal reasoning over KGs (RPath) can validate mechanisms.
3. **Industry is moving**: Recursion (causal AI for indication selection), Aitia (causal digital twins for discovery), BenevolentAI (causal KG reasoning).
4. **But implementation lags theory**: Most AIDD companies still use correlative models. Causal methods require domain knowledge (DAGs), larger datasets, and are harder to validate (no ground-truth counterfactuals).

### The Multi-omics Argument
1. **scRNA-seq triples Phase III chances** for identified targets (medRxiv 2024)
2. **Spatial transcriptomics** reveals that drug response depends on tissue context — not captured by current AIDD
3. **No approved drug yet** from multi-omics-first discovery — honest acknowledgment needed
4. Update Hasin 2017 with single-cell and spatial advances

### The Digital Twin Argument
1. **Regulatory momentum**: EMA qualified PROCOVA; FDA strategic positioning; FDA-Dassault Playbook
2. **Quantitative benefits**: 9-26% sample size reduction (Unlearn); up to 33% control arm reduction (J&J); potential full control arm replacement (Phesi)
3. **Two types**: Patient trajectory twins (Unlearn, Phesi — trial design) vs. disease mechanism twins (Aitia — drug discovery). Distinguish clearly.
4. **Current limitation**: "Fully simulating patient physiology remains on the horizon" (Roche). Most applications are operational, not mechanistic.

---

## Citation Checklist for Section 6.3

- [ ] Pearl J. Causality. Cambridge, 2009.
- [ ] Feuerriegel et al. Nature Medicine. 2024;30:958-968.
- [ ] Michoel & Zhang. Drug Discovery Today. 2023;28:103737.
- [ ] Nelson et al. Nature Genetics. 2015;47:856-860.
- [ ] Minikel et al. Nature. 2024;629:624-629.
- [ ] MR + XGBoost preprint. medRxiv. 2026. (check for peer-reviewed version)
- [ ] Ruiz et al. (RPath). PLOS Comp Biol. 2022;18:e1009909.
- [ ] BenevolentAI. Nature Communications. 2024;15:5624.
- [ ] Daghlas & Gill. Cambridge Prisms: Precision Medicine. 2023;1:e16.
- [ ] Jaeger et al. Nature Reviews Drug Discovery. 2023;22:496-520.
- [ ] scRNA-seq target validation. medRxiv. 2024. (check for peer-reviewed)
- [ ] Wang et al. (Unlearn/AD). Alzheimer's & Dementia: TRC&I. 2025;11:e70181.
- [ ] Phesi cGvHD. Bone Marrow Transplantation. 2024.
- [ ] Vidovszky et al. Clinical and Translational Science. 2024;17:e13897.
- [ ] Aitia/Nature advertiser feature. Nature. 2024. (note: advertorial, not peer-reviewed)
- [ ] PNAS Nexus in silico trials. 2025;4:pgaf123.
- [ ] Lancet Digital Health pediatric twins. 2025.
- [ ] Spatial transcriptomics drug response. NAR Cancer. 2024;6:zcae046.
