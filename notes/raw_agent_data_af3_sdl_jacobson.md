# Raw Agent Data: AF3 Deep-Read, SDL Deep-Read, Jacobson, Zasocitinib Full Text

> Source: Agent "Deep-read AF3 and SDL papers" (2026-04-03)
> Status: Verified (some data limited by paywall)

---

## Zheng et al. 2025 — AlphaFold3 in Drug Discovery

### Kinase Selectivity
- Tested 3 inhibitors (AMG706/Motesanib, GDC-0941/Pictilisib, XMD-1150) across **379 kinases**
- ROC-AUC: "only marginally better than random assignment" for all three
- Pipeline cannot distinguish subtle selectivity determinants

### GPCR Bias
- CaSR (calcium-sensing receptor) tested
- AF3 shows **persistent bias toward active conformations** regardless of ligand type
- **8,000 predictions** with different random seeds for antagonist YP1 (PDB: 7SIN)
- **100% predicted active state** when correct answer is inactive
- Characterized as "fundamental limitation"

### Conformational Change
- Strategic split: static (<0.5A RMSD) vs dynamic (>5A RMSD) complexes
- AF3 excels at static, "struggles" with dynamic

### Docking Comparison
- AF3 outperforms AutoDock Vina, GNINA, DiffDock, Gold, RFAA on **PoseBusters (428 complexes)**
- Superior side-chain accuracy and RMSD <2A success rate
- But: this is for KNOWN interactions, not selectivity prediction

### "Binary Interaction Modeler"
- Can confirm known interactions but cannot rank affinities or predict selectivity
- Exact phrase: "true-hit binary interaction modeler"

### Memorization Concern
- Performance declines on post-training-cutoff structures
- Raises questions about generalization vs memorization

### Gaps (paywall-limited)
- Exact ROC-AUC numerical values not extracted
- Exact failure count for >5A RMSD cases not extracted
- Exact GPCR test set size not extracted

---

## Tom et al. 2024 — Self-Driving Laboratories

### Pharma-Specific SDLs Catalogued
- **Adam** (2009): Genomics hypotheses + biological assays
- **Eve** (2009/2015): Drug hit identification with QSAR feedback loop
- **Novartis MicroCycle** (2024): Best-in-class pharma SDL

### MicroCycle Details
- Autonomously: synthesizes compounds (2-6 μmol), purifies, runs assays
- Assays: biochemical, cellular, permeability, microsomal stability, solubility, lipophilicity
- Active learning: Autofocus algorithm selects next cycle
- Throughput: **"100 unique chemicals in the time it used to take to evaluate a handful"**

### SiLA 2 + AnIML
- SiLA 2 = communication protocol ("lab ROS")
- AnIML = analytical data markup/transfer
- "Promising direction" but NOT universally adopted
- Various in-house orchestrators (ChemOS, Helao, AresOS) = fragmentation evidence

### Pharma vs Materials
- Pharma = "key driver in SDL technologies"
- But most published SDL examples = materials science (batteries, catalysts, polymers)
- Pharma SDLs remain minority in literature

### Gaps (paywall-limited)
- Total SDL count not extracted
- Exact DMTA cycle time improvements not quantified
- "Last mile" problem discussion not fully captured
- Other pharma companies beyond Novartis not identified from available text

---

## Jacobson 2025 — "AI Drug Revolution Needs a Revolution"

### Key Quotes Confirmed
- "When the AI revolution marched into the drug development sector and flipped biotechs into techbios..."
- "While cutting time (and costs) is commendable, we have yet to see these accelerated timelines translate into revolutionary improvements in clinical efficacy"
- "if these first few AI drugs serve as proverbial canaries in the coal mine, our current AI approaches may not do much to improve clinical efficacy"

### Core Thesis
- AI drug discovery is "human-agnostic" — trained on molecular/non-human data
- Cannot predict clinical outcomes because it doesn't incorporate functional human biology

### Proposed Solution
- Incorporate "functional human data, including its inherent variability" into preclinical AI
- Maintain scientific reasoning in model training

### Author
- Rachel DeVay Jacobson, CSO of Powerhouse Biology
- Author Correction published: DOI: 10.1038/s44386-025-00022-5

### Gaps (paywall-limited)
- OoC/organoid/MPS mentions NOT confirmed in available text
- Jayatunga citation NOT confirmed
- Word count unknown
- Detailed solutions not fully extracted

---

## Zasocitinib Phase 2 — FULL TEXT Extracted (PMC11339701)

### CRITICAL FINDING: AI Attribution in the Paper
- **Described only as**: "identified via a computationally enabled design strategy"
- **NO mention of**: Schrodinger, FEP+, AI, machine learning, computational chemistry, or any specific methodology
- This is in JAMA Dermatology (Armstrong AW et al.), NOT JAMA main journal
- DOI: 10.1001/jamadermatol.2024.2701

### Clinical Data (complete)
- 287 randomized, 259 dosed (90.2%)
- 1:1:1:1:1 to 2mg, 5mg, 15mg, 30mg, placebo; once daily; 12 weeks + 4 week follow-up
- PASI 75 week 12: placebo 6% (3), 2mg 18% (9), 5mg 44% (23), 15mg 68% (36), 30mg 67% (35)
- PASI 90: 30mg 46% (24)
- PASI 100: 30mg 33% (17)
- DLQI: greatest reduction in 30mg arm

### Safety (complete)
- TEAEs: placebo 44%, active arms 53-62%
- Most frequent: COVID-19 (12%), acne/acneiform dermatitis (2-6%), diarrhea (2-6%)
- No dose dependency in AEs
- No MACE, thromboembolic events, or opportunistic infections
- 1 serious AE: severe pleural + pericardial effusion (considered unrelated)
- CK elevations observed, no rhabdomyolysis
- Discontinuations: 1-2 patients (2-4%) per zasocitinib arm

### Selectivity Data
- TYK2 Kd = 0.0038 nM
- JAK1 Kd = 4,975 nM
- JAK2 Kd = 23,000 nM
- >1 million-fold selectivity for TYK2 over JAK1

### vs Deucravacitinib
- "Higher level of selectivity than deucravacitinib for the JH2 domain"
- "Whether these differences translate into corresponding levels of clinical efficacy remains to be confirmed"

### Review Relevance
The clinical paper's near-silence about the computational contribution perfectly illustrates the AI attribution gap. If even the molecule's own clinical trial paper doesn't mention AI/ML, the broader claims of "AI-designed drug" rest on external marketing, not scientific documentation.
