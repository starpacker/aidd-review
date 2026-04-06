# Rentosertib (ISM001-055) Phase IIa — Insilico Medicine, 2025

**Full citation**: Xu Z, Ren F, Rao H, Satler C, Liu Y, Lv Q, Zhao J, Chen Y, Cui Y, Korzinkin M, Gennert K, Zhavoronkov A, et al. "A generative AI-discovered TNIK inhibitor for idiopathic pulmonary fibrosis: a randomized phase 2a trial." *Nature Medicine*. 2025 Aug;31(8):2602-2610. DOI: 10.1038/s41591-025-03743-2. PMID: 40461817. Trial: NCT05938920.
**Corresponding author**: Zuojun Xu (Peking Union Medical College Hospital, Beijing)
**Senior author**: Alex Zhavoronkov (Insilico Medicine)
**COI**: Multiple authors are Insilico Medicine employees; Insilico was trial sponsor.
**Section relevance**: Section 3 (success case), Section 7 (milestone to watch)

## Key Findings

### Primary Endpoint (Safety)
- **TEAEs comparable across groups**: 70.6% placebo, 72.2% (30mg QD), 83.3% (30mg BID), 83.3% (60mg QD)
- Most AEs mild to moderate; SAEs rare; all resolved on discontinuation
- Main safety concerns: **liver toxicity and diarrhea** (led to some discontinuations)
- Primary endpoint MET: rentosertib is safe and well-tolerated

### Secondary Endpoints (Efficacy) — FVC
- **60 mg QD: FVC +98.4 mL** (95% CI: 10.9 to 185.9) — CI excludes zero
- **30 mg BID: FVC +19.7 mL** (modest improvement)
- **30 mg QD: FVC -27.0 mL** (no improvement, comparable to placebo)
- **Placebo: FVC -20.3 mL** (95% CI: -116.1 to 75.6)
- ⚠️ CORRECTION: Gemini/earlier notes said placebo was -62.3 mL — WRONG. Actual is -20.3 mL
- **Delta (60mg QD vs placebo): +118.7 mL** — clinically meaningful for IPF
- Dose-dependent pattern: only 60 mg QD showed meaningful improvement
- No formal p-values reported; CIs suggest nominal significance for 60mg

### Secondary Endpoints — Other
- **DLCO (diffusing capacity)**: No significant differences across groups
- **FEV1**: No significant differences across groups
- **6-Minute Walk Distance (6MWT)**: No significant differences across groups
- **Leicester Cough Questionnaire (LCQ)**: 60 mg QD showed "significantly improved" cough scores vs placebo; 30 mg groups did not
- **Note**: The FVC improvement without corresponding DLCO/6MWT improvement is a notable pattern — suggests functional lung volume preserved but gas exchange not yet improved at 12 weeks

### Biomarker Analysis (post-hoc)
- Serum protein profiling showed dose-dependent changes:
  - **Decreased**: COL1A1, MMP10, FAP, FN1 (profibrotic markers)
  - **Increased**: IL-10 (anti-inflammatory)
- Protein changes **correlated inversely with FVC improvements**
- Supports pharmacological mechanism of action through anti-fibrotic pathway

## Study Design
- GENESIS-IPF: Generative AI Enabled Novel Experimental Study of ISM001-055 in Subjects with IPF
- Phase IIa, multicenter, double-blind, randomized, placebo-controlled
- **128 screened → 71 randomized**
- 4 arms: placebo (n=17), 30mg QD (n=18), 30mg BID (n=18), 60mg QD (n=18)
- 22 sites across China
- 12-week treatment period
- Authors from 11 Chinese respiratory medicine departments (major teaching hospitals)

## AI Methodology — TNIK Target Discovery
- **Target discovery**: TNIK (Traf2- and NCK-interacting kinase) identified as fibrosis driver using Insilico's **PandaOmics** platform (AI-driven target identification)
- **Molecule design**: Rentosertib generated using **Chemistry42** (generative chemistry platform)
- **End-to-end AI**: Both target AND molecule discovered/designed by AI — described as "first-in-class AI-generated small-molecule inhibitor"
- Full target discovery methodology published separately in *Nature Biotechnology* (March 2024)
- AI platform collectively called "Pharma.AI" — uses deep generative models, reinforcement learning, transformers
- **Historical milestone**: First drug where BOTH target identification AND molecular design were AI-driven to reach Phase IIa with positive efficacy signal

## Limitations
- **Small sample**: 17-18 per arm — extremely limited statistical power
- **Short duration**: 12 weeks for a chronic, progressive disease (IPF progresses over years)
- **Single geography**: China only — unclear generalizability
- **Not powered for pivotal efficacy** — Phase IIa is safety-focused by design
- Lead investigator acknowledged: "sample size in each patient group was relatively limited"
- No DLCO/6MWT improvement — FVC alone may not capture full clinical picture
- **Sponsor conflict**: Insilico employees are co-authors and sponsor the trial
- **Conclusion**: Authors state "targeting TNIK with rentosertib is safe and well tolerated and warrants further investigation in larger-scale clinical trials of longer duration"
- Phase IIb/III plans: "begun discussions with regulatory authorities" — no timeline announced

## Our Take
- The most significant AI drug discovery success to date — genuine milestone
- **First proof-of-concept** for end-to-end AI drug discovery (target + molecule + clinical validation)
- But caveats are substantial: needs Phase IIb/III, larger cohort, multi-geography, longer duration
- The delta vs. placebo (+118.7 mL) is clinically meaningful for IPF
- **Critical observation for our review**: Even this "success story" reveals the gap — DLCO/6MWT unchanged, only 12 weeks, single geography, sponsor COI. The "success" is a Phase IIa safety trial with a secondary FVC signal, not a pivotal efficacy trial
- Use in Section 3 as fair acknowledgment of progress, while noting Phase IIb/III is the real test
- The biomarker correlation (COL1A1, FAP etc.) is encouraging for mechanistic validation
- Compare FVC improvement to nintedanib/pirfenidone benchmarks for context
