# Deep Dive: Multi-Omics, Digital Twins & Foundation Models (Updated)

> Date: 2026-04-04
> Status: Complete

---

## 1. Genetic Evidence → Clinical Success (Quantified)

### Minikel et al. 2024 (Nature) — CONFIRMED
- 29,476 target-indication pairs, 81,939 gene-trait pairs
- Genetic support → **2.6x greater** probability of success
- OMIM (Mendelian): **3.7x**; Open Targets/GWAS: **>2.0x**; Somatic/oncology: **2.3x**
- Only 4.8% of active T-I pairs had germline genetic support
- Only 1.1% of genetically supported pairs had been clinically explored
- Citation: Minikel EV et al. Nature 2024;629:624-629. DOI: 10.1038/s41586-024-07316-0

### Ochoa et al. 2022 (NRDD)
- Human genetics supports **~67%** of 2021 FDA-approved drugs
- Citation: Ochoa D et al. Nat Rev Drug Discov 2022;21(8):551. DOI: 10.1038/d41573-022-00120-3

### King et al. 2019 (PLoS Genetics) — NOT Drug Discov Today
- When causal genes clear (Mendelian, coding GWAS): **>2-fold** approval increase
- Citation: King EA et al. PLoS Genet 2019;15(12):e1008489. DOI: 10.1371/journal.pgen.1008489

### Ravarani et al. 2026 (medRxiv) — MR+ML Integration
- 11,482 target-indication pairs with Phase II outcomes
- MR significance alone does **NOT** enrich for Phase II success
- MR features + XGBoost → **55% approval rate** = **6.4x enrichment**
- Citation: Ravarani CNJ et al. medRxiv 2026. DOI: 10.1101/2026.02.19.26346536

---

## 2. scRNA-seq and Spatial Transcriptomics

### Dann et al. 2024 (medRxiv) — scRNA-seq Impact
- 30 diseases, 13 tissues
- Cell-type specificity + disease-cell specificity → **~triple** Phase III chances
- Preferentially prioritizes therapeutically tractable gene classes (membrane-bound proteins)
- Citation: Dann E et al. medRxiv 2024. DOI: 10.1101/2024.04.04.24305313

### Spatial Transcriptomics
- Still proof-of-concept stage for drug discovery
- Takeda uses spatial technologies for clinical trial design and microenvironment characterization
- **No validated drug targets discovered purely via spatial transcriptomics**

---

## 3. UK Biobank Proteomics (UKB-PPP)

### Pilot Phase (2024)
- ~3,000 proteins in 54,000 participants (Olink Explore 3072)
- Generated **>100 peer-reviewed papers** in 2024 alone
- **>14,000 genetic-protein links**, >80% previously unknown
- 4 proteins detect dementia **up to 15 years** before diagnosis
- Proteins as early warning for **19 cancer types**
- 38 proteins associated with incident Parkinson's

### Full-Scale (Jan 2025 launch)
- 5,400 proteins in 600,000 samples
- Data releases from 2026

---

## 4. Digital Twins — Updated Evidence

### Unlearn.AI PROCOVA (EMA-Qualified)
- **Sept 2022**: EMA qualified PROCOVA — **first ML method qualified for reducing clinical trial sample sizes**
- FDA confirmed consistency with current guidance (not formal qualification)
- Published in Alzheimer's & Dementia: TRCI (2025):
  - Variance reduction: **9-15%** (vs <5% with standard ANCOVA alone)
  - Sample size reduction: **9-15%** maintaining 90% power
  - Control arm reduction: **17-26%**
  - CDR-SB: 23% control-only savings (range 16-29%)
  - Partial correlations: 0.30-0.46 across validation trials
  - Training data: 6,736 subjects; primary trial: 453 participants
  - Method: Conditional Restricted Boltzmann Machine (CRBM)
- Citation: Wang D et al. Alzheimers Dement (TRCI) 2025;11:e70181. DOI: 10.1002/trc2.70181

### Phesi — Trial Design
- >132M patients, 195 countries, 4,000+ indications
- Hematology validation: forecasted GSER=0.067, actual=0.061
- 2025 Clinical Trials Arena Excellence Award

### EMA Synthetic Control Arms
- Workshop Nov 2025; **Reflection Paper expected 2026**
- No formal qualification yet

### Drug Discovery Digital Twins
- **No validated drug-discovery-specific digital twin with clinical data**
- Huntington's disease twin (23K nodes, 5.3M interactions) identified novel target — no clinical validation

---

## 5. Foundation Models for Biology

### scGPT / Geneformer — Limitations Exposed
**Kedzierska et al. 2025 (Genome Biology)** — First systematic zero-shot evaluation
- Both **underperformed simple baselines** (highly variable genes + Harmony/scVI) on cell-type clustering
- Geneformer ranked **last** on batch integration, sometimes amplifying batch effects
- Gene expression prediction: essentially **median value prediction** regardless of true expression
- scGPT drug sensitivity: AUROC=0.737, AUPRC=0.732 (with fine-tuning, not zero-shot)
- **No foundation model has contributed to a clinical-stage drug** as of early 2026
- Citation: Kedzierska KZ et al. Genome Biol 2025;26:101. DOI: 10.1186/s13059-025-03574-x

### Boltz-2 (MIT + Recursion, mid-2025) — Promising
- Open-source: predicts structure + binding affinity simultaneously
- **Near-FEP accuracy at >1,000x speed**, 20 seconds on single GPU
- Trained on ~5M binding affinity measurements
- Outperformed all CASP16 affinity challenge participants
- Citation: Wohlwend J et al. bioRxiv 2025. DOI: 10.1101/2025.06.14.659707

### KEY FINDING: Foundation models overpromise
- Zero-shot performance worse than baselines for most tasks
- Fine-tuning helps but requires labeled data — negating the "foundation" advantage
- Clinical impact: zero as of early 2026

---

## 6. AI Drug Deals Landscape (2024-2025)

- Merck KGaA → Biolojic Design: tens of millions EUR + EUR 346M milestones (AI antibodies)
- GSK → Ochre Bio: $37.5M (single-cell liver data)
- Novartis → Generate:Biomedicines: $65M upfront (generative protein platform)
- Rentosertib: first generative-AI drug with Phase IIa PoC (Nature Medicine 2025)
- By 2024: **>15 AI-designed molecules** in clinical trials industry-wide
