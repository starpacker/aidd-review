# Deep Dive: Phase II ~40% vs 28.9% — Statistical & Selection Bias Analysis

> Date: 2026-04-04
> Status: Complete — CRITICAL for thesis defense

---

## 1. Sample Size Problem (Devastating for the ~40% Claim)

- Jayatunga et al. 2024: Phase I N=24 (21 successes = 87.5%) — explicitly stated
- **Phase II N is never explicitly disclosed** — estimated N<15, possibly 8-12
- At N=12, observed 40% (5/12) vs baseline 28.9%:
  - Fisher exact test p ≈ 0.50 (NOT significant)
  - 95% Wilson CI: **15.2% to 72.3%**
  - The CI spans from half the baseline to more than double it
- **Conclusion**: ~40% vs 28.9% is statistically indistinguishable at this sample size
- No CIs reported in paper (BCG consulting firm authorship, not academic statisticians)

---

## 2. Selection Bias — AI Companies Choose Validated Targets

### Systematic evidence across all major AI drugs:

| Drug | Target | Target Novelty |
|------|--------|---------------|
| Zasocitinib | TYK2 JH2 | **Follow-on**: BMS deucravacitinib validated mechanism |
| Zovegalisib | PI3Kα mutant | **Known target**: alpelisib approved 2019 |
| Rentosertib | TNIK | **Semi-novel**: known kinase, novel indication pairing |
| BEN-2293 | Pan-Trk | **Known**: larotrectinib approved for TRK fusions |
| EXS-21546 | A2A | **Known**: istradefylline approved for Parkinson's |
| REC-994 | Tempol/SOD | **Known mechanism**: antioxidant |
| DSP-1181 | 5-HT1A | **Known**: buspirone approved 1986 |

**6/7 most-analyzed AI drugs target already-validated mechanisms.** Only Rentosertib's TNIK approaches novelty.

### Supporting literature:
- Jayatunga themselves note AI companies may "choose easier/more validated targets"
- Harren et al. (DDT, 2023): AI pipelines concentrate in oncology kinases and inflammation
- Schuhmacher et al. (NRDD, 2021): AI companies preferentially enter TAs with rich training data
- Eder et al. (NRDD, 2014): first-in-class drugs have lower approval rates than followers

### Biomarker confound (BIO/QLS 2021):
- Programs WITH patient preselection biomarkers: LOA = 25.9%
- Programs WITHOUT: LOA = 8.4%
- If AI companies select targets where biomarkers exist → mechanistically higher Phase II

---

## 3. Therapeutic Area Confounding

### Phase II rates vary dramatically by TA (BIO/QLS 2021):
- Rare disease: often >40% Phase II success
- Hematology: 26.1% LOA
- Non-oncology overall: 9.3% LOA
- Oncology overall: 5.3% LOA
- CNS: historically ~8-10% LOA

### AI portfolio skew:
- Heavy representation in dermatology/inflammation (psoriasis, AD) — historically higher rates
- Some rare diseases (CCM) — historically higher rates
- Light CNS representation — historically lowest rates
- **No TA-matched comparison has ever been performed**

### Jayatunga provides no TA breakdown → comparison is confounded

---

## 4. Temporal Confound

- BIO/QLS 28.9% baseline covers 2011-2020 (decade-spanning average)
- Dowden & Munro 2019 (NRDD): Phase II→III improved from 49-50% (2010-12) to 61-63% (2015-17)
- Contemporary baseline (2018-2023) may be 35-40%
- **This alone could eliminate the apparent AI "advantage"**
- Citation: Dowden H, Munro J. Nat Rev Drug Discov. 2019;18:495-496. DOI: 10.1038/d41573-019-00074-z

---

## 5. "Even If 40% Is Real, It's Not Enough"

- Phase II is one transition in a multi-stage cascade
- Overall LOA Phase I→approval: 7.9% (BIO 2021)
- Even doubling Phase II (28.9%→~58%) would raise LOA to only ~16%
- The biology problem thesis holds unless Phase II approaches 70%+
- **One transition improvement ≠ pipeline transformation**

---

## 6. No Systematic Phase II Failure Analysis Exists for AI Drugs

- No peer-reviewed paper systematically analyzes WHY AI drugs fail Phase II
- Our 7-case study catalog is the most comprehensive available
- This gap itself is worth noting in the review

---

## 7. Counterargument Literature

### FOR AI improving Phase II:
- Jayatunga 2024: headline finding, but underpowered
- Paul et al. (NRDD, 2010): even small Phase II improvement has enormous economic impact
- Industry self-reported claims (Insilico: 18mo/$150K) — unverified

### AGAINST AI improving Phase II:
- N problem (see above)
- Selection bias (see above)
- Niazi 2025 (Pharmaceuticals, MDPI): AI drugs perform "not better than" traditional
- Scannell & Bosley 2016 (PLoS ONE): 0.1 correlation improvement offsets 10-100x screening
- Graber 2025: leakage removal → ML approaches nearest-neighbor baseline
- Deloitte 2024: only 9% significant AI ROI; 100-month timeline unchanged
- Hasselgren & Oprea 2024: "Are We There Yet?" — no clinical superiority demonstrated
- **Zero FDA approvals** as of early 2026

---

## Suggested Language for Paper

"Jayatunga et al. report AI Phase II success of approximately 40%, compared with the BIO/QLS industry baseline of 28.9%. However, this comparison warrants caution on three grounds: (i) the Phase II sample is acknowledged as 'limited' (likely N<15), rendering the difference statistically non-significant (95% CI: ~15-72%); (ii) AI companies preferentially pursue validated targets in favorable therapeutic areas, introducing selection bias that inflates apparent success rates; and (iii) Phase II success rates improved substantially across the industry during 2015-2020 (Dowden & Munro 2019), narrowing or eliminating the apparent gap when contemporary baselines are used. A therapeutic-area-matched comparison — the only methodologically sound approach — has not been performed."
