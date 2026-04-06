# Raw Agent Data: OoC+ML Additional Evidence, Regulatory Documents, Publication Bias

> Source: Agent "OoC+ML and additional evidence" (2026-04-03)
> Status: Verified

---

## TASK 1: Additional OoC + ML Integration Evidence

### Key Empirical Studies

**1. Tak et al., Frontiers in Bioengineering, 2024**
- **STRONGEST empirical OoC+ML study found**
- CNN trained on 2,674 cell images from 3D microfluidic bladder cancer chip
- Predicted gemcitabine resistance at 4 levels
- **Accuracy: 95.2%, sensitivity 90.5%, specificity 96.8%, AUC >0.988**
- Citation: Tak S, et al. *Front Bioeng Biotechnol* 2024, 11:1302983. DOI: 10.3389/fbioe.2023.1302983

**2. PNAS 2022 — Microfluidics + DL for Immunotherapy Screening**
- Automated high-throughput microfluidic platform + clinical TIL score analyzer
- Deep learning tracked 100 spheroids and >7,000 immobilized tumor spheroids under 30 treatment conditions
- Citation: *PNAS* 2022, 119(46):e2214569119. DOI: 10.1073/pnas.2214569119

**3. uPharma Platform (2025)**
- Microfluidic AI-driven pharmacotyping
- Single-cell drug sensitivity prediction in leukemia
- Predicts sensitivity within 4 hours without direct drug exposure

### Key Review Papers

**4. Gangwal & Lavecchia, Drug Discovery Today, 2025**
- DOI: 10.1016/j.drudis.2025.104360
- AI + OoC + digital twins to replace animal testing
- Notes AI "plays critical role in overcoming limitations of DTs and OoC"
- Mentions Tox-GAN for toxicity prediction alongside OoC

**5. Theranostics 2023** — "Organ-on-a-chip meets artificial intelligence in drug evaluation"
- PMC10465229
- DL architectures (DBN, autoencoders, CNN, RNN, GAN) applied to OoC data

**6. Research 2022** — "Overview of Organs-on-Chips Based on Deep Learning"
- spj.science.org/doi/10.34133/2022/9869518

### Company Updates

**7. Emulate AVA System (June 2025)**
- 96-channel high-throughput organ-chip
- 7-day experiment → >30,000 time-stamped data points; with omics → millions
- AI applied to morphology scoring for consistency
- Described as "AI-ready data generation" but NO published ML study on AVA data yet

**8. Wyss Institute**
- Established AI DataHub for ML partnerships on organ-chip data
- Recent: multi-omics + AI for heavy menstrual bleeding model
- Original DARPA Body-on-Chip (2012) included computational modeling
- Published ML-on-chip-data papers from Wyss = limited

**9. CN Bio / TissUse**: No specific AI/ML publications found

### Key Gap (Reinforced)
Despite many review papers, actual empirical OoC + ML studies remain **surprisingly rare**. Most work = (a) AI for image analysis of chip microscopy, or (b) theoretical proposals. The full bridge (OoC data → predictive ML models for drug response) is still largely aspirational.

---

## TASK 2: NRDD Phase II/III Termination Analysis

**Citation**: Bowling H, Cocucci A, Koo DCE, Harrison RK. "Analysis of phase II and phase III clinical trial terminations from 2013 to 2023." *NRDD*, Dec 2025. DOI: 10.1038/d41573-025-00208-6. PMID: 41413264.

- Database: Epistemic AI platform (EpistemicGPT + Knowledge Graph)
- N = 3,180 terminated trials
- Termination rate doubled: 11% (2013) → 22% (2023); absolute: 209 → 435
- #1 cause: Strategic/business (36%), NOT efficacy
- Efficacy: 24% (notably lower than ~50% reported a decade ago)
- Enrollment: 18%
- Safety: 5% (remarkably stable over time)
- Phase 3 cost: $50-250M per asset
- NO AI-drug-specific subanalysis

---

## TASK 3: Computational Toxicology (Briefings in Bioinformatics 2025)

**Citation**: Zhang J, et al. "Computational toxicology in drug discovery: applications of AI in ADMET and toxicity prediction." *Briefings in Bioinformatics*, 2025, 26(5):bbaf533. DOI: 10.1093/bib/bbaf533

**Verification**:
- "~40% of preclinical candidates fail due to insufficient ADMET profiles" — ✅ CONFIRMED, cited to their Ref [26]
- "nearly 30% of marketed drugs withdrawn due to unforeseen toxic reactions" — ✅ CONFIRMED, same Ref [26]

**⚠️ IMPORTANT CAVEAT**: Both claims trace to Ref [26], likely Kola & Landis 2004. The 40% = **historical 1991 figure**, not current. Current ADMET attrition = 10-15% (Sun et al. 2022). Must distinguish historical vs current in our review.

**The 30% withdrawal figure**: Closest match = Yale study (~1/3 of drugs approved 2001-2010 had post-approval safety issues). Onakpoya et al., *BMC Medicine*, 2016: 462 drugs withdrawn 1953-2013, hepatotoxicity + immune reactions = >30% of withdrawals. May conflate withdrawal with safety events.

---

## TASK 4: Pharmaceuticals 2025 — AI vs Older Methods

**Citation**: Niazi SK. "Artificial Intelligence in Small-Molecule Drug Discovery: A Critical Review." *Pharmaceuticals*, 2025, 18(9):1271. DOI: 10.3390/ph18091271

**Comparison**:
- Traditional docking scoring: AUC 0.70-0.80
- AI-enhanced methods: AUC 0.72-0.82
- "Competitive performance" but "results vary significantly depending on specific target and dataset"
- Emphasizes modest rather than transformative improvements

**Caveat**: Single-author critical review, not primary benchmarking study. AUC ranges compiled from multiple sources. Cite as "a critical review found..." not "a benchmarking study demonstrated..."

---

## TASK 5: FDA Regulatory Documents — URLs

**A. FDA Modernization Act 2.0**
- Full text: https://www.congress.gov/bill/117th-congress/senate-bill/5002/text
- PDF: https://www.govinfo.gov/content/pkg/BILLS-117s5002es/pdf/BILLS-117s5002es.pdf
- Signed Dec 29, 2022. Removes animal testing requirement for IND applications.

**B. FDA January 2025 AI Draft Guidance**
- Press release: https://www.fda.gov/news-events/press-announcements/fda-proposes-framework-advance-credibility-ai-models-used-drug-and-biological-product-submissions
- Federal Register: https://www.federalregister.gov/documents/2025/01/07/2024-31542/
- Comment deadline: April 7, 2025

**C. FDA April 2025 Animal Testing Phase-Out**
- Press release: https://www.fda.gov/news-events/press-announcements/fda-announces-plan-phase-out-animal-testing-requirement-monoclonal-antibodies-and-other-drugs
- NAMs: AI computational models, OoC, organoids, cell lines, in silico, microdosing
- Timeline: animal studies → "exception rather than norm within 3-5 years"

---

## TASK 6: Publication Bias References

### Smaldino & McElreath 2016
- "The natural selection of bad science." *Royal Society Open Science*, 2016, 3(9):160384. DOI: 10.1098/rsos.160384
- Agent-based model: publication volume incentive → selection for low-power methods → more false positives
- **NOT drug-discovery-specific** — general science

### Better Drug Discovery-Specific References

**1. Begley & Ellis 2012** ★ CANONICAL
- "Drug development: Raise standards for preclinical cancer research." *Nature*, 2012, 483:531-533. DOI: 10.1038/483531a
- Amgen replicated 53 "landmark" cancer studies: **only 6/53 (11%) confirmed**

**2. Prinz, Schlange & Asadullah 2011**
- "Believe it or not: how much can we rely on published data on potential drug targets?" *NRDD*, 2011, 10:712
- Bayer: only ~25% of published findings could be validated

**3. Reproducibility Project: Cancer Biology**
- 193 experiments from 53 top cancer papers (2010-2012)
- Only 50 experiments from 23 papers replicated
- Effect sizes **85% smaller** on average

### Recommendation
Use Smaldino 2016 for theoretical mechanism (why bad methods persist) + Begley & Ellis 2012 for empirical drug discovery evidence.
