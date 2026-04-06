# Raw Agent Data: ADMET, AlphaFold, Market Data Verification

> Source: Agent "Verify ADMET and AlphaFold data" (2026-04-03)
> Status: Verified

---

## ADMET Attrition Reduction — Primary Sources

### Kola & Landis, 2004
**Full citation**: Kola I, Landis J. "Can the pharmaceutical industry reduce attrition rates?" *Nature Reviews Drug Discovery*, 2004, 3:711-716. PMID: 15286737.

- In **1991**: PK/bioavailability = **~40%** of failures (single largest cause)
- By **2000**: PK/bioavailability dropped to **~10%**
- Shift: efficacy (~30%) and safety (~30%) became dominant by 2000

### Waring et al., 2015
**Full citation**: Waring MJ, Arrowsmith J, Leach AR, et al. "An analysis of the attrition of drug candidates from four major pharmaceutical companies." *Nature Reviews Drug Discovery*, 2015, 14:475-486. DOI: 10.1038/nrd4609. PMID: 26091267.

- Analyzed oral small-molecule candidates from AZ, Lilly, GSK, Pfizer (2000-2010)
- Safety/toxicology = ~25% of failures across Phase I and Phase II
- **Does NOT explicitly report "11%" for ADMET** — focused on safety vs PK tradeoff
- The "~11%" figure appears derived from secondary citations or interpolation

### Sun et al., 2022 (Best modern source)
**Full citation**: Sun D, Gao W, Hu H, Zhou S. "Why 90% of clinical drug development fails and how to improve it?" *Acta Pharmaceutica Sinica B*, 2022, 12(7):3049-3062. DOI: 10.1016/j.apsb.2022.02.002. PMC9293739.

- 2010-2017 data:
  - Lack of efficacy: 40-50%
  - Unmanageable toxicity: 30%
  - Poor drug-like properties (ADMET/PK): **10-15%**
  - Commercial/strategic: ~10%
- Confirms: "poor drug-like properties contributed to 30-40% failures in 1990s; only 10-15% today"

### Correction Applied
- Changed "40% → ~11%" to "~40% (1991; Kola & Landis) → 10-15% (2010-2017; Sun et al. 2022)"
- Waring 2015 cited as supporting evidence, not primary source for the number

---

## AlphaFold3 Limitations

### Zheng et al., 2025
**Full citation**: Zheng H, Lin H, Alade AA, et al. "AlphaFold3 in Drug Discovery: A Comprehensive Assessment of Capabilities, Limitations, and Applications." *bioRxiv*, 2025. DOI: 10.1101/2025.04.07.647682.

| Claim | Status | Details |
|-------|--------|---------|
| Conformational changes >5A RMSD: AF3 fails | ✅ CONFIRMED | Exact quote verified |
| GPCR antagonist prediction: poor selectivity | ✅ CONFIRMED | "Persistent bias toward active conformations regardless of ligand type" |
| Kinase selectivity ROC-AUC near random | ✅ CONFIRMED | AF3-GNINA pipeline: "marginally better than random assignment" across 3 kinase inhibitors |
| "Binary interaction modeler" | ✅ CONFIRMED | Exact phrase: "true-hit binary interaction modeler" |

### Desai et al., 2024
**Full citation**: Desai D, et al. "Review of AlphaFold 3: Transformative Advances in Drug Design and Therapeutics." *Cureus*, 2024, 16(7):e63646. DOI: 10.7759/cureus.63646. PMC11292590.

- 40-80% accuracy variability: ✅ CONFIRMED ("Success rates fluctuate significantly, ranging from 40% to over 80%")
- 50% more accurate on PoseBusters (from original DeepMind Nature paper)
- Note: narrative review in Cureus, not primary benchmarking. Zheng et al. is stronger.

---

## Market Data — "$420B VC" Correction

### Finding: $420B is NOT AIDD-specific
The "$420B" = cumulative funding across entire biotech sector historically, NOT AI drug discovery.

### AIDD-specific figures (PitchBook)
- Cumulative AIDD VC since 2019: **~$17 billion**
- 2024 annual: **$3.8 billion** (rebounding from 3 years decline)
- 2025 annual: **$3.8 billion** globally / **$5.6 billion** US-based firms (tripled YoY per one source)
- Over 12 months through Q3 2025: **$3.2 billion across 135 startups**

### CB Insights
- AI drug R&D equity funding rebounded from $3B to $3.8B in 2024, surpassing pre-pandemic $2.7B (2019)

### Correction Applied
- Changed to "$17B AIDD-specific since 2019 (PitchBook)"
- Note: may reference $420B broader biotech context if clearly distinguished
