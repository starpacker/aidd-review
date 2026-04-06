# Animal-to-Human Translation — Ineichen et al., 2024

**Full citation**: Ineichen BV, et al. "Analysis of animal-to-human translation shows that only 5% of animal-tested therapeutic interventions obtain regulatory approval for human applications." *PLOS Biology*. 2024;22(6):e3002667. DOI: 10.1371/journal.pbio.3002667. PMID: 38870090.
**Institution**: University of Zurich (lead)
**Section relevance**: Section 2 (translational gap), Section 4.2 (preclinical-to-clinical cascade failure)

## Key Findings

### Translation Pipeline (headline numbers)
- **50%** of animal-tested therapies progress to any human clinical study
- **40%** advance to randomized controlled trials (RCTs)
- **5%** achieve regulatory approval for human use
- These are based on **367 therapeutic interventions** across **54 distinct human diseases**

### Scale of Evidence
- Umbrella review of **122 systematic reviews** (from 5,227 initial publications)
- 62 articles analyzed quantitatively
- **4,443 total animal studies** and **1,516 clinical studies** identified
- Median per review: 21 animal studies, 8 human studies

### Concordance Between Animal and Human Studies
- **Overall concordance RR: 0.86** [95% CI: 0.80-0.92]
  - This means ~86% alignment between animal positive results and clinical positive results
  - But: 79% animal studies positive vs. 61% clinical studies positive vs. 50% RCTs positive
  - Progressive decline in positivity at more rigorous study stages
- Analysis restricted to therapies with >=5 animal studies (62 therapies, 1,496 animal studies, 515 clinical studies, 220 RCTs)

### Concordance by Disease Area
| Disease Area | Concordance RR [95% CI] | N therapies |
|---|---|---|
| Neurological | 0.99 [0.66-1.06] | 23 |
| Circulatory | 0.88 [0.76-1.01] | 12 |
| Digestive | 0.86 [0.75-0.99] | 7 |
| Musculoskeletal | 0.67 [0.515-0.862] | 6 |
| Cancer | 0.66 [0.49-0.88] | 3 |
| Mental health | 0.60 [0.37-0.97] | 7 — LOWEST consistency |

### Translation by Disease Area (approval rates)
| Disease Type | To Human Studies | To RCTs | To Approval |
|---|---|---|---|
| Circulatory (166 therapies) | 34% | 29% | 1% |
| Mental health (16 therapies) | 50% | 31% | 0% |
| Musculoskeletal (13 therapies) | 100% | 62% | 15% |
| Cancer (15 therapies) | 73% | 47% | 20% |

### Disease Distribution of Included Reviews
- 32% nervous system diseases
- 11% musculoskeletal/connective tissue
- 9% psychiatric disorders
- 9% circulatory system
- 8% digestive system
- 8% neoplasms
- Others: skin, lung, metabolic

### Temporal Analysis
- **Median lag times** from first animal study:
  - To first human study: **5 years** [95% CI: 5-6]
  - To first RCT: **7 years** [95% CI: 6-8]
  - To FDA approval: **10 years** [95% CI: 4 to not estimable]
- Maximum durations observed: 44 years (clinical trial), 58 years (RCT), 34 years (FDA approval)
- **49 therapies (31%)** had first animal experiment AFTER first clinical trial — raises questions about animal model validation

### Publication Patterns
- 88 of 122 reviews published since 2018
- Geographic: USA (22%), Canada (16%), Netherlands (13%), Australia (11%), Italy (11%), UK (8%)
- Median time from first animal experiment to systematic review: 15 years (range: 3-63 years)

## Methods
- **Umbrella review** (meta-analysis of systematic reviews)
- Searched: Medline, Embase, Web of Science Core Collection (inception through August 1, 2023)
- Two-stage identification: (1) locate reviews on bench-to-bedside translation, (2) extract individual therapeutic interventions
- **Inclusion**: Systematic/scoping reviews investigating translation of interventions in animal disease models; any intervention type (drugs, surgical, neuromodulation, behavioral); >=2 authors, documented systematic search, methodology section
- **Exclusion**: Original studies, non-translation focused, non-English, gray literature
- Three independent reviewers screened in duplicate using SyRF software
- Inter-rater agreement: Cohen's Kappa = 0.76
- Quality: 10-item checklist (protocol registration, flowcharts, COI, dual screening, etc.)
- Data extraction: first animal study year, first clinical study year, first RCT year, outcomes (positive/negative/mixed/neutral), regulatory approval status
- **Concordance analysis**: Meta-analysis using RR, random-effects modeling (DerSimonian-Laird), Q-test and I^2
- **Temporal analysis**: Kaplan-Meier survival analysis for lag times
- Software: R 4.2.2 (packages: meta, survminer, survival)

## What "5% Approval" Means Exactly
- Of 367 therapeutic interventions tested in animals across 54 diseases, approximately **18 achieved regulatory approval**
- This is **regulatory approval** (FDA, UK MHRA, Swiss equivalents), NOT Phase III success
- The denominator is interventions that were tested in animal models and appeared in translation-focused systematic reviews
- This does NOT include all drugs ever tested in animals — only those captured in systematic reviews of translation
- The figure is for therapies with >=10 years follow-up post-animal study (to allow time for translation pipeline)

## Key Translation Barriers Identified
1. **Methodological disparities**: Young healthy animals vs. elderly multimorbid patients (e.g., stroke research)
2. **Study quality issues**: "Poor study quality and inadequate reporting, predominantly in animal studies"
3. **Effect size reduction**: "Noticeable reduction in effect size from animal to human studies"
4. **Timing differences**: Cardiac arrest example — drug given ~9.5 min post-arrest in animals vs. ~19.4 min clinically
5. **Cancer example**: Oncolytic virus showed 80-100% tumor regression in animals but only 0-24% in humans
6. **More rigorous studies = smaller effects**: Studies with better design consistently showed reduced effect sizes

## The Paradox Explained (Authors' Interpretation)
- High concordance (86%) + substantial early clinical entry (50%) BUT minimal approval (5%)
- Two scenarios:
  1. Strict RCT/regulatory standards unnecessarily exclude valuable treatments
  2. Both animal and early clinical studies suffer design limitations → unreliable findings that rigorous trials cannot replicate
- **Authors favor Scenario 2**: Supported by declining therapy counts at more rigorous stages

## Limitations (Acknowledged by Authors)
1. **Selection bias**: Included only therapies from translation-focused systematic reviews — biased toward fields with demonstrated translational interest
2. **Oversimplification**: Complex drug development reduced to positive/neutral/negative categories
3. **Outcome classification bias**: Clinical outcomes classified per author conclusions — susceptible to "spin" bias
4. **Indirect benefits unaccounted**: Excluded mechanistic/disease understanding contributions not leading to therapy approval
5. **English-only**: Non-English publications excluded
6. No systematic assessment of animal model type differences
7. No comparison between drug vs. non-drug therapy translation
8. No analysis of investigator-initiated vs. industry-sponsored trial effects

## Key Direct Quotes
- "Contrary to widespread assertions, the rate of successful animal-to-human translation may be higher than previously reported."
- "The low rate of final approval indicates potential deficiencies in the design of both animal studies and early clinical trials."
- "Drugs effective across diverse laboratory settings tend to promise better outcomes in human studies."
- "To improve animal-to-human translation, we advocate for enhanced study design robustness of animal and human research which will not only benefit experimental animals but also affected patients."

## Our Take
- **Critical reference** for establishing the translational gap as a STRUCTURAL problem, not just an AI problem
- The 50% → 40% → 5% cascade is powerful framing for our "cascading failure" thesis
- The disease-area breakdown is directly useful: circulatory (1% approval) vs. cancer (20%) shows huge heterogeneity
- The concordance paradox (86% agreement but only 5% approval) parallels our AI precision paradox perfectly
- The "31% of therapies had animal studies AFTER clinical trials" finding is damning for the validation paradigm
- Use in Section 2 to establish baseline translational failure rates BEFORE adding AI complexity
- Key point: if traditional drug discovery only achieves 5% approval from animal testing, AI needs to dramatically improve this, not just optimize molecular properties
- The effect size reduction pattern (animals → early clinical → RCTs) maps directly to our pipeline cascade argument
