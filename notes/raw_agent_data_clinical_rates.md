# Raw Agent Data: Clinical Success Rates Verification

> Source: Agent "Verify clinical success rates data" (2026-04-03)
> Status: Verified

---

## Jayatunga et al. 2024 — Deep Read

**Full citation**: Jayatunga MKP, Ayers M, Bruens L, Jayanth D, Meier C. "How successful are AI-discovered drugs in clinical trials? A first analysis and emerging lessons." *Drug Discovery Today*, 2024 Jun;29(6):104009. DOI: 10.1016/j.drudis.2024.104009. Epub 2024 Apr 30. PMID: 38692505.

**Authors are from Boston Consulting Group (BCG).**

| Metric | Value | Notes |
|--------|-------|-------|
| Phase I success rate | 80-90% (21/24) | 21 out of 24 AI-discovered drugs met Phase I clinical endpoints |
| Phase II success rate | ~40% | "Albeit on a limited sample size"; N for Phase II not explicitly stated |
| Phase III data | None reported | Too few drugs had reached Phase III |
| Companies analyzed | 39 AI-native biotech companies | |
| Total drugs tracked | ~67 in clinical development by Dec 2023 | Growth: 3 (2016) → 17 (2020) → 67 (2023) |

### Definitions
- **"AI-native"**: Biotechnology companies specializing in AI as a core approach
- **"AI-assisted"**: Distinguished from AI-native; includes drug repurposing. When excluding repositioned drugs, "a significant increase in PoS is still observed" for Phase I
- Sequel to their 2022 paper in Nature Reviews Drug Discovery ("AI in small-molecule drug discovery: a coming wave?")

### Key Limitations
- Limited sample size, especially for Phase II
- Very few drugs had reached Phase III
- Selection bias: AI-native companies may choose easier/more validated targets
- Phase I advantage may partly reflect ADMET optimization rather than efficacy

### Discrepancy Note
- AI Phase II ~40% vs. traditional 28.9% (BIO). These should NOT be presented as a single "28-40%" range for AI drugs
- AI Phase I 80-90% matches exactly

---

## BIO/QLS Clinical Success Rate Report (2011-2020)

**Full citation**: BIO, Informa Pharma Intelligence, QLS Advisors. "Clinical Development Success Rates and Contributing Factors 2011-2020." Published February 17, 2021. URL: https://go.bio.org/rs/490-EHZ-999/images/ClinicalDevelopmentSuccessRates2011_2020.pdf

### Overall Phase Transition Rates (2011-2020)

| Transition | Success Rate |
|-----------|-------------|
| Phase I → Phase II | 52.0% |
| Phase II → Phase III | 28.9% |
| Phase III → NDA/BLA | 57.8% |
| NDA/BLA → Approval | 90.6% |
| Overall LOA (Phase I → Approval) | 7.9% |

### Scale
- 12,728 clinical and regulatory phase transitions
- 9,704 clinical drug development programs
- 1,779 biopharmaceutical companies
- Data from Biomedtracker database, Jan 2011 to Nov 2020

### By Drug Modality
- Small molecules (NMEs): 5.7% overall LOA
- Biologics: 9.1%
- Vaccines: 9.7%

### By Therapeutic Area (LOA from Phase I)
- Hematology: 26.1% (highest)
- Infectious disease: 13.2%
- Oncology: 5.3% (lowest)
- Non-oncology overall: 9.3% (n=8,549)
- Oncology overall: 5.3% (n=4,179)

### Critical Finding
- Programs using patient preselection biomarkers: LOA = **25.9%**
- Programs WITHOUT biomarkers: LOA = **8.4%**
- 2x improvement with biomarker-guided development

---

## "92% Animal Testing Failure" Claim — Verification

### Primary Source
FDA, "Innovation or Stagnation: Challenge and Opportunity on the Critical Path to New Medical Products," March 2004.
> "A new medicinal compound entering Phase 1 testing...is estimated to have only an 8 percent chance of reaching the market."

This 8% approval = 92% failure. During 1995-2000: 1 in 8 (~12.5%); by 2000-2002: 1 in 13 (~7.7%).

### Important Nuance
The 92% refers to drugs entering Phase I that fail to reach market. It does NOT specifically mean "drugs that pass animal testing fail in humans." The conflation occurs because Phase I entry requires preclinical success, but failures span all clinical phases.

### Updated Sources
1. **BIO 2011-2020**: Overall LOA = 7.9% → 92.1% failure (confirms same number)
2. **Ineichen et al., PLOS Biology, 2024**: "Only 5% of animal-tested therapeutic interventions obtain regulatory approval." DOI: 10.1371/journal.pbio.3002667. Umbrella review: 122 systematic reviews, 4,443 animal studies, 1,516 clinical studies, 367 interventions, 54 diseases. = **95% failure rate**
3. **Sun et al., Acta Pharmaceutica Sinica B, 2022**: "Why 90% of clinical drug development fails." DOI: 10.1016/j.apsb.2022.02.002. Review article, not primary source.
4. **Kola & Landis, NRDD, 2004**: Cumulative Phase I→registration: 11% (1991-2000, 10 major pharma)

### Recommendation
- Do NOT cite "92%" as animal testing failure specifically
- For animal-to-human translation: Ineichen et al. 2024 (5% approval = 95% failure)
- For overall clinical attrition: BIO 2021 (7.9% LOA) or FDA 2004 (8%)
