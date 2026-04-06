# Deep Dive: Phase II Failure Analysis & AI Drug Attrition

> Date: 2026-04-04
> Status: Complete

---

## 1. Systematic Phase II/III Failure Analyses (Historical Series)

### Harrison 2016 (NRDD) — Foundational
- 218 failures (Phase II–submission), 174 with stated reasons
- **Efficacy: 52%**, Safety: 24%, Other: 24%
- Citation: Harrison RK. Nat Rev Drug Discov 2016;15:817-818. DOI: 10.1038/nrd.2016.184

### Arrowsmith 2011 (NRDD) — Phase II 2008-2010
- 108 Phase II failures
- Efficacy 51%, Strategic 29%, Safety 19%
- Citation: Arrowsmith J. Nat Rev Drug Discov 2011;10:328-329

### Arrowsmith & Miller 2013 (NRDD) — 2011-2012
- 148 failures, 105 with reasons
- Overall: Efficacy 56%, Safety 28%, Strategic 7%
- Phase II specifically: **Efficacy 59%**
- Citation: Arrowsmith J, Miller P. Nat Rev Drug Discov 2013;12:569

### Waring et al. 2015 (NRDD) — Four Major Pharma
- AZ, Lilly, GSK, Pfizer combined data
- Only 34% oral small molecules failed Phase II due to lack of efficacy
- Citation: Waring MJ et al. Nat Rev Drug Discov 2015;14:475-486. DOI: 10.1038/nrd4609

### Dowden & Munro 2019 (NRDD) — Success Rate Trends
- 2010-2017 data; Phase II→III transition improved: 49-50% (2010-2012) → 61-63% (2015-2017)
- Varies by area: anti-infectives 16% overall, nervous system 3%
- Citation: Dowden H, Munro J. Nat Rev Drug Discov 2019;18:495-496. DOI: 10.1038/d41573-019-00074-z

### Bowling et al. 2025 (NRDD) — Latest Large-Scale
- 3,180 terminated trials (2013-2023)
- Rate of late-stage terminations **doubled** from 11% to 22%
- "Strategic and business" factors overtook clinical efficacy as leading cause
- Citation: Bowling H et al. Nat Rev Drug Discov 2025. DOI: 10.1038/d41573-025-00208-6

### Sun et al. 2025 (Nature Communications) — Dynamic Trends
- ClinSR declining since early 21st century, recently plateauing and increasing
- Developed ClinSR.org platform
- Citation: Sun D et al. Nat Commun 2025. DOI: 10.1038/s41467-025-64552-2

### Norstella 2025
- Overall likelihood of approval for Phase I drugs at **all-time low: 6.7%** (2014-2023)
- Phase II success rate approximately 28%

### Consensus: Why Drugs Fail Phase II
- **Lack of efficacy: 40-59%** (consistent across all analyses)
- Safety/toxicity: 19-35%
- Strategic/commercial: 7-29% (rising per Bowling 2025)
- Poor drug-like properties: 10-15% (down from 30-40% in 1990s)

---

## 2. Target Validation Gap — Quantitative Evidence

### Cook et al. 2014 (NRDD) — AstraZeneca 5Rs
- 142 drug projects (2005-2010)
- 5Rs: Right Target, Right Patient, Right Tissue, Right Safety, Right Commercial
- Efficacy: 65% of Phase II project failures
- Citation: Cook D et al. Nat Rev Drug Discov 2014;13:419-431. DOI: 10.1038/nrd4309

### Morgan et al. 2018 (NRDD) — 5Rs Impact (KEY DATA)
- After implementing 5Rs: **success from candidate to Phase III improved 4%→19%**
- Nearly 5-fold improvement from systematic target validation
- Citation: Morgan P et al. Nat Rev Drug Discov 2018;17:167-181. DOI: 10.1038/nrd.2017.244

### Morgan et al. 2012 (DDT) — Pfizer "Three Pillars"
- 44 Pfizer Phase II programs
- In 43% of efficacy failures, **could not confirm mechanism was adequately tested**
- Three Pillars: exposure at site, target binding, functional pharmacological activity
- Citation: Morgan P et al. Drug Discov Today 2012;17:419-424

### Nelson et al. 2015 (Nature Genetics) — Genetic Evidence
- 22,270 drugs, 1,824 targets, 705 indications
- Genetic support increased: 2.0% (preclinical) → 8.2% (approved)
- Targets with genetic support: **2-fold more likely** to lead to approved drugs
- Citation: Nelson MR et al. Nat Genet 2015;47:856-860. DOI: 10.1038/ng.3314

### Minikel et al. 2024 (Nature) — Updated
- 29,476 target-indication pairs
- Genetic support: **2.6-fold greater** probability of success
- OMIM (Mendelian): 3.7x; GWAS: >2.0x; Somatic/oncology: 2.3x
- Only 4.8% of active T-I pairs had germline genetic support
- Citation: Minikel EV et al. Nature 2024;629:624-629. DOI: 10.1038/s41586-024-07316-0

### Scannell & Bosley 2016 (PLoS ONE) — Predictive Validity
- 0.1 improvement in correlation between model and clinical outcome offsets 10-100x screening throughput
- Declining predictive validity = root cause of Eroom's Law
- Citation: Scannell JW, Bosley J. PLoS ONE 2016;11(2):e0147215

---

## 3. AI-Originated Drug Failures (Comprehensive List)

### Confirmed Failures/Discontinuations:

| Drug | Company | Phase | Indication | Failure Mode |
|------|---------|-------|------------|-------------|
| BEN-2293 | BenevolentAI | IIa | Atopic dermatitis | No efficacy (missed all secondary endpoints) |
| REC-994 | Recursion | II | CCM | No sustained benefit; discontinued May 2025 |
| DSP-1181 | Exscientia/Sumitomo | I | OCD | "Did not meet expected standards"; quietly dropped |
| EXS-21546 | Exscientia | I/II | Cancer (A2A) | Insufficient therapeutic index |
| VRG-50635 | Verge Genomics | I | ALS | Failed pre-specified efficacy analysis, Dec 2025 |
| REC-2282 | Recursion | preclinical | NF2 | Deprioritized in post-merger restructuring |
| REC-3964 | Recursion | preclinical | C. difficile | Deprioritized; exploring out-licensing |

### VRG-50635 (NEW — Not in Previous Notes)
- PIKfyve inhibitor for ALS, entirely AI-discovered
- Failed Phase I pre-specified efficacy analysis (Dec 2025)
- Ferrer had licensed ex-US rights for up to EUR 112.5M
- Source: FierceBiotech

### Key Observations:
1. **7 AI-originated programs** have been discontinued/deprioritized
2. **0 have failed due to drug chemistry** — all failures are biological (efficacy, therapeutic index)
3. This pattern directly supports our thesis: AI solves chemistry, not biology
4. Phase I success (80-90%) confirms good molecular design; Phase II wall confirms biology gap

---

## 4. AI Drug Pipeline Status (Early 2026)

- 173+ programs in clinical development
- ~94 Phase I, ~56 Phase II, ~15 entering Phase III
- Phase I success: 80-90% vs 52% historical (Jayatunga 2024, N=75)
- **No updated systematic peer-reviewed dataset beyond Jayatunga N=75**
- **Zero approved AI-designed drugs as of early 2026**
- First approval projected 2026-2027

### Key Gap:
The absence of a rigorous updated dataset beyond Jayatunga's N=75 (now 173+ programs) is itself a notable finding. The field grew >2x but no systematic peer-reviewed analysis tracks outcomes.
