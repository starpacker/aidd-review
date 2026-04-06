# Deep Dive: OoC+AI, Regulatory, SDL & LLM Agents

> Date: 2026-04-04
> Status: Complete

---

## Part 1: Organ-on-Chip + AI Integration

### Ewart Liver-Chip — Current Status
- Original: 780 chips (not 870), 27 drugs, 87% sensitivity, 100% specificity for DILI
- **Sept 2024**: Liver-Chip S1 accepted into FDA ISTAND pilot for DILI prediction
- Economic modeling: routine adoption would generate **$3B annually** for pharma
- **No independent multi-site replication** with fresh compound set as of early 2026
- Rubiano et al. 2023: two decision-support frameworks published (Expert Opin Drug Discov)
- Citation: Ewart L et al. Commun Med 2022;2:209. DOI: 10.1038/s43856-022-00209-1

### Closest Examples to OoC-ML Closed Loop

**Yakavets et al. 2025 (Science Advances)** — BEST PARTIAL EXAMPLE
- ML + automation + large microfluidic arrays of cancer spheroids/PDOs
- ML explored multidrug administration regimens
- Found sequential administration reduces total drug dose at comparable efficacy
- Validation within same organoid system, NOT against clinical outcomes
- DOI: 10.1126/sciadv.adt1851

**Hesperos 2025 (Advanced Science)** — FIRST OoC DIGITAL TWIN
- Multi-organ chip (liver, spleen, endothelial, blood) reproducing P. falciparum lifecycle
- PK/PD modeling + IVIVE generated predictions of MTD, NOAEL, EC50
- Predictions **closely aligned with clinical data** for non-complicated malaria
- Post-hoc digital twin, not prospective closed loop
- DOI: 10.1002/advs.202505206

**PharmaFormer 2025 (npj Precision Oncology)**
- Transfer learning: pre-trained on 2D cell lines, fine-tuned on organoid data
- Predicts clinical drug responses from limited organoid pharmacogenomic data

### KEY FINDING: No Complete Closed-Loop Published
No group has published: OoC training data → ML prediction → new OoC validation → clinical confirmation

### Quris-AI / Merck KGaA
- Two-year validation completed, "significantly higher accuracy" for DILI
- **No peer-reviewed publication with metrics** — press releases only (Jan 2025)
- 29 patents; acquired Nortis (Kidney-on-Chip) Nov 2024

### Wyss AI DataHub
- Infrastructure for curating OoC/organoid datasets for ML training
- **No publications** as of early 2026

### ARPA-H CATALYST ($21M, Dec 2025)
- Inductive Bio + Amgen + Baylor + Torch Bio
- Focus: DILI and cardiotoxicity
- No preliminary results (announced Dec 2025)

---

## Part 2: Regulatory Developments (2024-2026)

### FDA Modernization Act 2.0 (Dec 2022)
- Replaced "preclinical tests (including tests on animals)" with "nonclinical tests"
- **No public statistics on NAM-only IND applications** as of early 2026

### FDA April 2025 Announcement — Phase-Out Plan
- Plan to phase out animal testing for mAbs and other drugs
- Pilot program within 1 year for mAb developers using primarily non-animal strategies
- 3-5 year goal: animal studies "the exception rather than the norm"
- Methods: AI computational toxicity, OoC, organoids, microdosing, imaging
- CAMERA database (beta mid-2025)
- Primate testing reduced 6→3 months for specific mAb studies

### FDA Modernization Act 3.0 (Feb 2025 introduced, Dec 2025 passed Senate)
- Requires FDA to replace all "animal" references with "nonclinical" in IND regulations
- 2-year reporting deadline on qualified methods

### NIH Complementary Actions (2025)
- April 29: shifted funding toward human-based research technologies
- **July 7: grant proposals relying exclusively on animal data no longer eligible**

### FDA AI/ML Guidance (Jan 6, 2025)
- First FDA guidance on AI for drug/biologic development
- Covers: clinical trial design, endpoint adjudication, pharmacovigilance, manufacturing
- **Explicitly excludes**: AI in drug discovery or streamlining operations
- Risk-based credibility assessment framework

### EMA-FDA Joint Principles (Jan 14, 2026)
- 10 guiding principles for AI in medicine development
- Human-centric design, risk-based controls, transparency

### ICH M15 (Nov 2024 endorsed, Step 4 adopted)
- "General Principles for Model-Informed Drug Development"
- **First ICH guideline formally including AI/ML** in MIDD framework
- Scope: PopPK, PBPK, dose-response, QSP/QST, disease progression, agent-based models, AI/ML

### EMA AI Roadmap 2025-2028
- Four pillars: guidance/policy, tools/technology, collaboration, experimentation

---

## Part 3: PBPK+ML and QSP+ML Hybrids

### PBPK + ML
**Li et al. 2024 (Pharmaceutical Research)**
- ML (SVR, RF, XGBoost, GBM, D-MPNN) + whole-body PBPK (14 tissues)
- ML predicts fup, Caco-2, clearance from structure alone
- **Validated on 40 compounds: 65% within 2-fold** (vs 47.5% using in vitro)
- DOI: 10.1007/s11095-024-03725-y

**2025 J Med Chem study**: ~800 drugs with digitized human IV PK profiles
- Neural-ODE outperformed LightGBM and LSTM

**2026 bioRxiv preprint**: Model-Driven Hybrid AI Framework
- Structure → PBPK-ready parameters → exposure simulation → clinical PK decision support

### Certara/Simcyp
- **Aug 2025**: Simcyp = **first PBPK software formally qualified by EMA** (DDI risk assessment)
- CertaraIQ (Oct 2025): pre-validated QSP models
- Limited peer-reviewed ML+Simcyp hybrid validation

### QSP + ML
**Applied BioMath (acquired by Certara Dec 2023)**
- ADC QSP model: **successfully predicted PFS for T-DM1 and T-DXd** in HER2+ breast cancer
- Including differential efficacy by HER2 expression status
- J Pharmacokinet Pharmacodyn 2023. DOI: 10.1007/s10928-023-09884-6

**Folguera-Blasco et al. 2024 (AstraZeneca team)**
- Frontiers in Systems Biology review
- Concluded: **No clinical validation achieved** for QSP+ML
- "Early stage of this collaboration"
- Key challenge: QSP needs mechanistic knowledge (small data) vs ML needs large data
- DOI: 10.3389/fsysb.2024.1380685

---

## Part 4: Self-Driving Labs in Pharma

### Novartis MicroCycle — Best-Documented
- 100 compounds per learning cycle (vs "handful" manually)
- 2-6 μmol scale; biochemical, cellular, permeability, stability, solubility, lipophilicity
- Active learning for multiparameter optimization
- "Best-in-class platform" per 2025 review
- Citation: J Med Chem 2024;67:2118-2128

### AstraZeneca iLab
- Goal: complete DMTA automation
- Own admission: **"not yet been achieved"**
- PIP: ~250 models, >300M calculations/month (Drug Discov Today 2024, PMID: 38460568)

### Eli Lilly → Arctoris
- San Diego SDL via Strateos (2020), >100 instruments, >5M compounds
- **Acquired by Arctoris** (Sept 2024), relocated to Oxford
- No peer-reviewed SDL outcomes

### Strateos (Cloud Lab)
- >1.2M compounds screened in one month (100K/day max)
- 14 analogs in ~40 hours vs ~2 weeks conventional (70% faster)
- **Company claims, not peer-reviewed**

### Recursion-Exscientia Merger (Nov 2024)
- $688M all-stock deal
- Combined >10 clinical/preclinical programs
- ~$100M annual synergies, runway to 2027
- Goal: vertically integrated end-to-end platform
- **No peer-reviewed integration outcomes**

### Carnegie Mellon + Emerald Cloud Labs
- >200 instrument types at **$40M** cost
- Source: Nature 2026

### KEY FINDING: Almost All Pharma SDL Results Are Press Releases, Not Peer-Reviewed

---

## Part 5: LLM Agents for Drug Discovery

### ScienceAgentBench (ICLR 2025) — KEY CITATION
- 102 tasks from 44 peer-reviewed papers across 4 disciplines
- **Best agent: 32.4% tasks solved** (34.3% with expert knowledge)
- o1-preview + self-debug: 42.2% but >10x cost
- Conclusion: "current language agents have limitations in generating code for data-driven discovery"
- Citation: arXiv 2410.05080

### Chemistry = LLMs' Weakest Domain
- FrontierScience (OpenAI 2025): chemistry **51.3%** accuracy (lowest of all subjects; physics 76.3%)
- Japanese Pharmacist Exam: chemical structure questions = lowest accuracy across 18 models

### Hallucination Rates (Quantitative)
- GPT-3.5: **39.6%** reference fabrication
- Google Bard: **91.4%** reference fabrication
- GPT-4: **28.6%** reference fabrication
- ChemLLM: only 20.89% consistency with reference descriptions
- Clinical decision support: LLMs repeated planted errors in **83%** of cases

### Dual-Use Risk
- **Urbina et al. 2022 (Nature Machine Intelligence)**: inverted MegaSyn generator
- Generated 40,000 candidate toxic molecules in <6 hours on a 2015 Mac
- Outputs included **VX and novel molecules predicted more toxic than VX**
- DOI: 10.1038/s42256-022-00465-9

### New Agent Frameworks (Post-ChemCrow)
- **DrugAgent** (arXiv 2408.13378): multi-agent for DTI; outperformed GPT-4o mini by 45% F1
- **Prompt-to-Pill** (Bioinformatics Advances 2025): comprehensive target-to-recruitment pipeline
- **ChemToolAgent** (arXiv 2411.07228): tools help specialized tasks but hurt general reasoning

### KEY FINDING: Agent Reproducibility Crisis
- ChemCrow repo explicitly warns it "will not give the same results as the paper"
- Most agent papers depend on proprietary LLM APIs whose behavior changes over time
- Exact reproduction is **fundamentally impossible** for API-dependent agents
