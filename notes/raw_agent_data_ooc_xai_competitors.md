# Raw Agent Data: OoC Integration, XAI, Competitor Gap Check

> Source: Agent "Deep-read OoC and XAI papers" (2026-04-03)
> Status: Verified

---

## OoC + AI Integration — Concrete Examples

**Critical finding: Very few published proof-of-concept studies. Integration remains largely aspirational. Our "first to bridge" claim is substantiated.**

### Published Examples

**1. DILITracer (Tan et al., Communications Biology, 2025)**
- Closest to OoC + AI, but uses liver *organoids* (3D Matrigel), not true OoC
- Architecture: BEiT-V2 pretrained on 700,000 cell images + spatial ViT + bidirectional LSTM + MLP
- Data: 158 HLO samples, 478 HepG2 spheroid samples; brightfield images, 4 days, 12-20 z-axis
- 30 compounds from FDA DILIrank (Most-DILI, Less-DILI, No-DILI)
- Accuracy: **82.34%** (HLO) vs 77.41% (HepG2)
- First ternary DILI classification from organoid morphology alone
- Authors note: "HLOs remain simplified and lack immune components in comparison to organ-on-a-chip"
- **Citation**: Tan S, et al. *Communications Biology* 8, 886 (2025). DOI: 10.1038/s42003-025-08205-6

**2. Emulate Liver-Chip Validation (Ewart et al., Communications Medicine, 2022)**
- 870 Liver-Chips, 27 blinded drugs
- Sensitivity: **87%**, Specificity: **100%**
- Correctly identified 87% of drugs causing DILI that PASSED animal testing
- **No ML/AI used** — pure experimental validation
- Demonstrates data quality suitable for future ML integration
- Estimated >$3B annual value to pharma
- **Citation**: Ewart L, et al. *Communications Medicine* 2, 209 (2022). DOI: 10.1038/s43856-022-00209-1

**3. Organoid Profiler (Galan et al., bioRxiv, 2026)**
- Open-source Python automated phenotyping pipeline
- >10,000 organoid images longitudinally
- Human-level segmentation (r = 0.99)
- Microfluidic droplet engineering + AI morphological analysis
- 25 morphological metrics; biphasic "remodeling-to-expansion" trajectory
- **Citation**: bioRxiv 2026.01.01.694533v1

**4. OoC Image Dataset for ML (MDPI Data, 2024)**
- 3,072 brightfield images from OoC setups
- CNN model: ~98% accuracy for cell type classification
- **Citation**: MDPI Data 9(2), 28 (2024)

**5. DATAMAP / ARPA-H CATALYST Program (2025)**
- $21M ARPA-H award to Inductive Bio (December 2025)
- Partners: Baylor, Torch Bio, Amgen, Cincinnati Children's
- Goal: in-silico liver/heart toxicity models from MPS data
- **Most ambitious OoC + AI program to date — no results yet**

**6. Zhou, Zhong & Lauschke (Expert Opin Drug Metab Toxicol, 2025)**
- Review: advanced liver models + AI for DILI
- Proposes integrating biochemical, histological, toxicogenomic data from 3D cultures + MPS with ML
- Concludes: benchmarking + data sharing = prerequisites
- **Citation**: PMID: 39893552. DOI: 10.1080/17425255.2025.2462234

**7. LivHeart Multi-Organ-on-Chip (Ferrari et al., 2023)**
- Liver + heart OoC for off-target cardiotoxicity after liver metabolism
- Predicted Terfenadine cardiotoxicity via metabolite pathway
- No AI/ML — purely experimental
- **Citation**: Ferrari E, et al. *Adv Mater Technol* (2023). DOI: 10.1002/admt.202201435

### What R21 and R22 Reviews Cite
- R21 (Biomicrofluidics 2025): cites mostly *potential* rather than completed OoC+AI studies
- R22 (Innovation: Life 2024): synergy is "game-changer" but acknowledges integration is largely conceptual
- Neither identifies published studies with full closed-loop: OoC data → ML training → prediction → validation

### Key Gap Confirmed
**No published study has completed: OoC data → ML model training → drug prediction → OoC validation.** Our bridging claim is substantiated.

---

## Jacobson 2025 — Deep Read

**Full citation**: Jacobson RD. "The AI drug revolution needs a revolution." *npj Drug Discovery* 2, 10 (2025). DOI: 10.1038/s44386-025-00013-6
**Author correction**: DOI: 10.1038/s44386-025-00022-5

### Format
- **Perspective** (NOT full review)
- ~2,000-3,000 words
- Argument-driven, not data-heavy

### "Human-Agnostic" Definition
- Current AIDD paradigm trains/validates on non-human data (animal models, cell lines, recombinant assays, in silico benchmarks)
- AI discovers drugs *agnostic to human biology*
- Optimizes molecular properties against computational/animal endpoints rather than human-relevant functional data
- Ignores human-specific variability, tissue-specific responses, population heterogeneity

### Solutions Proposed
1. Incorporate functional human data in preclinical AI training
2. Include human variability (genetic, metabolic, immune) as feature
3. Maintain scientific reasoning throughout (not just pattern-matching)
4. Leverage AI to measure human responses during preclinical stages

### Evidence Provided
- Argument-driven, NOT data-heavy
- Cites general clinical failure statistics, no original quantitative analysis
- Does NOT provide: systematic pipeline data, case studies, quantitative failure modes, concrete roadmap

### Where Jacobson Stops / Our Review Continues
Jacobson DOES NOT discuss:
- OoC as concrete solution
- Automation/standardization requirements
- Cascading failure analysis
- Chemistry vs. Biology Problem framing
- XAI requirements
- Domain-specific pitfalls (pH, enzymatic hydrolysis)
- Specific drug failure case studies
- Quantitative data or systematic evidence
- ~2-3K words vs. our ~6-8K + figures

---

## XAI in Drug Discovery

### Ding et al. (DDDT, 2025)
- **573 articles** analyzed (from 920), 2002-June 2024, Web of Science
- Growth: pre-2017 <5/year → 2019-2021 avg 36.3/year → 2022-2024 avg >100/year
- ARIMA predicts 694 cumulative by end 2024
- **Dominant techniques (ranked)**:
  1. SHAP (most prevalent)
  2. Attention mechanisms
  3. LIME
  4. Feature importance / Permutation
  5. LRP
- Top countries: China 212 (37%), USA 145 (25.3%), Germany 48, UK 42
- Top journals: JCIM (44), Briefings in Bioinformatics (37), Bioinformatics (22)
- 4 research clusters: ML+drug design/safety, DL+drug interactions, disease-specific, precision medicine
- **Accuracy-interpretability tradeoff**: key unresolved challenge
- **Citation**: Ding Q, et al. *DDDT* 2025;19:4025-4055. DOI: 10.2147/DDDT.S525171

### Lavecchia (WIREs, 2025)
- XAI categories: gradient-based, perturbation, surrogate, counterfactual, self-explaining
- Techniques: SHAP, attention, concept whitening, saliency maps
- Applications: molecular property, de novo design, toxicity via DNNs/GNNs
- Black-box opacity limits pharma acceptance; XAI bridges prediction + understanding
- References FDA 2025 + EMA reflection paper
- **Citation**: Lavecchia A. *WIREs Comput Mol Sci* 2025;15(5):e70049. DOI: 10.1002/wcms.70049

---

## Competitor Gap Check — Final Results

### Annual Review of Pharmacology and Toxicology
- Hasselgren & Oprea (2024): "AI for Drug Discovery: Are We There Yet?" Vol 64, pp 527-550. Capabilities focus, NOT failure analysis. **Not a competitor.**
- Vol 65 (2025): iPSC + genomics + AI focus. **Not a competitor.**

### Journal of Medicinal Chemistry (ACS)
- 2025 editorial: "A New Era of AI" — capabilities focus
- 2025 perspective: "Thinking on the Use of AI" — general reflection
- **No review analyzing Phase II failures**

### ACS Medicinal Chemistry Letters
- 2025 Special Issue: AI/ML methods collection
- **No review on clinical translation failures**

### Nature Reviews Drug Discovery
- December 2025: "Analysis of phase II and phase III clinical trial terminations from 2013 to 2023" — general pharma analysis (Epistemic AI database), NOT AI-specific. Finds ~50% Phase II/III failures = lack of efficacy. **Not a direct competitor** but important reference.
- **No AIDD-specific failure review** in 2025-2026

### Other
- Nature Communications 2025: "Dynamic clinical trial success rates" — general, not AI-specific
- Drug Target Review 2025: journalism, not peer-reviewed

### VERDICT
**No 2025-2026 review in target journals systematically analyzes WHY AI-discovered drugs fail in Phase II.** Gap confirmed. Closest competitors remain:
1. Jayatunga et al. 2024 — quantifies but doesn't explain
2. Jacobson 2025 — identifies "human-agnostic" but short Perspective
3. NRDD Dec 2025 termination analysis — general pharma, not AI
