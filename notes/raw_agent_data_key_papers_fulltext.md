# Raw Agent Data: Key Papers Full Text Deep-Read

> Source: Agent "Fetch key papers full text" (2026-04-03)
> Status: Verified

---

## Paper 1: Jayatunga et al. 2024 — Additional Details

- 39 AI-native biotechs, **75 molecules** in clinical trials (67 active as of Dec 2023)
- Phase I: 21/24 (87.5%); Phase II: ~40% on "limited sample size"
- **Phase II exact N NOT publicly disclosed** — likely <20 drugs
- All authors = BCG consultants (London, Amsterdam, NJ)
- Sequel to their 2022 NRDD paper ("AI in small-molecule drug discovery: a coming wave?")
- Elder critique: "Such claims have come from the companies themselves. Until independently verified, some caution is in order."
- **Gap**: Full AI-native definition criteria locked behind paywall

---

## Paper 3: Ineichen et al. 2024 (PLOS Biology) — COMPREHENSIVE

**Citation**: Ineichen BV, et al. "Analysis of animal-to-human translation." *PLOS Biology*, 2024. DOI: 10.1371/journal.pbio.3002667

### Translation Cascade (KEY DATA)
| Stage | Rate |
|-------|------|
| Animal → any human study | 50% |
| Animal → RCT | 40% |
| Animal → regulatory approval | **5%** (≈18 of 367 interventions) |

- The "5%" = **regulatory approval** (FDA/MHRA/Swiss), NOT Phase III success
- Concordance RR: 0.86 [0.80-0.92] — 86% agreement overall
- BUT: progressive positivity decline: 79% animal → 61% clinical → 50% RCT

### Scale
- 122 systematic reviews
- 367 therapeutic interventions
- 54 diseases
- 4,443 animal studies
- 1,516 clinical studies

### Disease Breakdown (approval rates)
- Circulatory: **1%** (extremely low)
- Cancer: **20%** (highest)
- Musculoskeletal: **15%**

### Temporal
- Median 5 years animal → first human study
- Median 7 years to RCT
- Median 10 years to approval

### Startling Finding
- **31% of therapies had animal studies AFTER first clinical trial** — questions the assumption that animal testing precedes human testing

### Methodology
- Umbrella review of systematic reviews (highest level of evidence synthesis)
- Searched PubMed, Embase, Web of Science
- Included systematic reviews comparing animal and human efficacy for same interventions
- Risk of bias assessed using AMSTAR-2

### Limitations
- Heterogeneous disease areas, intervention types
- Publication bias in underlying reviews (positive results overrepresented)
- Regulatory approval ≠ clinical utility (approved drugs may later fail post-market)
- Concordance measure may overestimate because both animal and human studies may be biased toward positive results

---

## Paper 4: Sun et al. 2022 — Additional Details

**Citation**: Sun D, et al. "Why 90% of clinical drug development fails." *Acta Pharm Sinica B*, 2022; 12(7):3049-3062.

### Failure Breakdown (2010-2017)
| Cause | % |
|-------|---|
| Lack of efficacy | 40-50% |
| Unmanageable toxicity | 30% |
| Poor drug-like properties (ADMET/PK) | **10-15%** |
| Commercial/strategic | ~10% |

- The "90%" applies to **Phase I entrants** only
- **Key note**: This is a review/perspective — percentages originate from Harrison 2016, Hay 2014, etc., NOT original data collection by Sun et al.
- Historical note: ADMET failures significantly decreased over past 20 years (from 40% in 1991 per Kola & Landis)

### STAR Framework
- Structure-Tissue exposure-Activity Relationship: 4-class system proposed
- NOT empirically validated in the paper
- STAR examples estimated from plasma PK without experimental data

---

## Notes on User's Updates to Case Study Files

### zasocitinib_case.md — User Updated
Key new finding from PMC full text:
- **The Phase 2b paper is Armstrong et al., JAMA Dermatology (NOT JAMA main)**
- DOI: 10.1001/jamadermatol.2024.2701
- **CRITICAL**: Paper describes zasocitinib only as "identified via a computationally enabled design strategy"
- **NO mention of AI, ML, Schrodinger, or FEP+** in the paper itself
- Selectivity: TYK2 Kd = 0.0038 nM vs JAK1 4975 nM, JAK2 23,000 nM
- Comparison with deucravacitinib: same mechanism, higher selectivity

### rentosertib_case.md — User Updated
- Added full author list: Xu Z, Ren F, Rao H, et al.
- Corresponding author: Zuojun Xu (Peking Union Medical College Hospital)
- Trial: NCT05938920
- COI: Multiple Insilico employees; company = sponsor
- Full TEAE rates by arm
- Biomarker data: COL1A1, MMP10, FAP, FN1 decreased; IL-10 increased
- Nature Biotechnology March 2024 = separate TNIK target discovery paper
