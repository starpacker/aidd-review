# Deep Dive: OoC+AI Evidence Reassessment

> Date: 2026-04-04
> Status: Complete — requires framing adjustment in Section 6.1

---

## Honest Assessment: The Critic Is Largely Correct

**No published study has completed the OoC → ML → drug prediction → OoC validation loop.**

The OoC+AI integration thesis must be downgraded from "proposed solution" to "emerging opportunity with highest ceiling but least maturity."

---

## 1. Strongest Available Evidence (Partial Loops Only)

### DILITracer (Tan et al., Communications Biology, 2025)
- BEiT-V2 + spatial ViT + LSTM on liver **organoid** (NOT true OoC) images
- 30 FDA DILIrank compounds, 82.34% ternary DILI classification
- Closest proof-of-concept, but: (a) organoids not OoC, (b) N=30 tiny, (c) no validation loop

### Ewart Liver-Chip (Communications Medicine, 2022)
- 870 chips, 27 drugs, 87% sensitivity, 100% specificity for DILI
- OoC → statistical analysis, **NOT** OoC → ML
- No ML applied to this dataset by anyone
- **Not independently replicated** by external group
- Author correction 2023 (Table 2/3 data duplication)

### ARPA-H CATALYST/DATAMAP ($21M+, Dec 2025)
- Inductive Bio + Baylor + Amgen: building AI toxicity models from MPS data
- Draper team: "Human Data Stack" from EMR + organs + biopsies + PREDICT96 MPS
- Most ambitious OoC+AI program — **zero results yet**

### OoC company ML status:
- Emulate: No published ML integration. AVA platform (June 2025) = 96 chips/run, 30K+ data points — ML-relevant throughput but no ML papers
- Hesperos, TissUse, CN Bio, Mimetas: **No published ML integration studies**

---

## 2. OoC Data Characteristics

### Data types (genuinely rich for ML):
- Continuous time-series: TEER, oxygen, pH, glucose/lactate
- Images: brightfield, fluorescence, confocal time-lapse (>200 GB per 72h experiment)
- Electrical: action potentials, field potentials (cardiac), impedance
- Biochemical/metabolomic: protein biomarkers, metabolites
- Mechanical: stiffness, contractile forces

### Data volume (borderline for ML):
- Emulate AVA: 96 chips/run, >30K data points per 7-day experiment
- Largest reported OoC dataset: >20K data points
- Published OoC image dataset for ML: 3,072 images (0.81 accuracy MobileNetV3)
- ML typically needs ~1,000 samples/class minimum
- Sufficient for transfer learning/few-shot, not for training large models from scratch

### Batch-to-batch variability (problematic):
- iPSC cardiac: <30% may acquire mature phenotype in some batches
- GAO Report (GAO-25-107335, May 2025): **only 10-20% of purchased human cells are high quality enough for OoC**
- No published standardized CV% benchmarks across the field

---

## 3. OoC Limitations — More Severe Than Previously Framed

### Throughput:
- Current: 12-48 replicates per plate for simpler systems
- Emulate AVA: 96 chips/run — significant but still orders of magnitude below HTS (100K+ compounds/day)
- Trade-off is fundamental: more physiological relevance = lower throughput

### Cost:
- Per-chip pricing proprietary
- Described as "cost-prohibitive for large-scale screens"
- Emulate claims AVA cuts consumables 4x vs previous generation
- Still far more expensive than HTS per data point

### Standardization:
- ASTM F3570-22 (July 2022): vocabulary only
- ISO/TC 276/SC 2: working draft stage (ISO/WD 25448)
- China group standard (April 2024): liver-on-a-chip terminology
- **No ISO/ASTM performance standard** for OoC data quality or ML-readiness
- JRC roadmap (Jan 2025): priorities for OoC standardization

### Cell quality:
- GAO: only 10-20% of purchased cells meet OoC requirements — devastating for scale-up
- **This is NOT purely an engineering problem** (contradicts our current "engineering problems with clear trajectories" framing)

### Key critical papers:
- **Alver et al., Nature Communications 2024**: "Roadblocks confronting widespread dissemination and deployment of Organs on Chips"
- **GAO-25-107335, May 2025**: "Technologies Offer Benefits Over Animal Testing but Challenges Limit Wider Adoption"

---

## 4. Alternative Biology-Aware Data Sources (SIGNIFICANTLY More Mature)

### Patient-derived organoids + ML — 2-3 years ahead of OoC+ML:
- **PharmaFormer (npj Precision Oncology, 2025)**: Transformer pre-trained on 2D cell lines, fine-tuned on organoid pharmacogenomics. Validated against TCGA clinical outcomes. Significant correlation with actual clinical responses.
- **OPTIC trial (Clinical Cancer Research, 2025)**: Multicenter prospective study showing PDOs predict radiological tumor response AND survival for oxaliplatin chemo in mCRC.
- Brain tumor organoids (Cell Stem Cell, 2025): generated 10 days post-surgery, accurately recapitulate molecular pathology.

### Multi-omics + ML — MOST MATURE:
- **PASO model (PLOS Computational Biology, 2025)**: Multi-omics pathway differences + drug SMILES. Validated against TCGA with significant survival correlation.
- Integrated classifiers: AUCs 0.81-0.87 for early detection.
- Multiple clinical validation designs already deployed.

### Maturity hierarchy:
1. Multi-omics + ML = **available now**, clinical validation underway
2. PDO + ML = **proof-of-concept**, clinical validation emerging (2-3 years ahead of OoC)
3. OoC + ML = **pre-proof-of-concept**, components exist but integration not demonstrated

---

## 5. Realistic Timeline for OoC+AI

- **2025-2026**: ARPA-H teams begin generating MPS data. AVA enables 96-chip throughput. No closed-loop results expected.
- **2027-2028**: First publications using MPS data for ML toxicity models (CATALYST deliverables). Possible partial-loop demos.
- **2029-2031**: If CATALYST succeeds, first IND using OoC+AI toxicity data. Performance standards may emerge.
- **2032+**: Realistic earliest for routine closed-loop OoC→ML→prediction→validation in pharma.

---

## 6. Revised Framing for Section 6.1

### What we CAN say:
1. OoC generates the richest preclinical data type (continuous, multi-modal, human-relevant) — factual
2. Ewart liver-chip demonstrates data quality potentially suitable for ML (87%/100%) — but ML step not done
3. ARPA-H CATALYST ($21M+) = first serious attempt to bridge OoC and AI — funded, no results
4. Communities genuinely siloed — confirmed
5. FDA Mod Act 2.0 + ISTAND creates regulatory pull

### What we must NOT claim:
1. Do NOT imply OoC+AI integration has been demonstrated — it has NOT
2. Do NOT present Ewart as ML-validated — it's statistical only
3. Do NOT ignore that PDO+ML is significantly more mature
4. Do NOT say OoC limitations are "purely engineering" — cell quality (10-20%) and standardization are not purely engineering

### Proposed restructure:
Position OoC+AI as **one component** of a broader "biology-aware data" solution stack:
- **Tier 1 (Ready now)**: Multi-omics + ML (clinical validation underway)
- **Tier 2 (Emerging)**: PDO + ML (clinical validation emerging)
- **Tier 3 (Frontier)**: OoC + ML (highest ceiling, least mature, ARPA-H as inflection point)

This is more honest and more reviewer-proof than presenting OoC as THE solution.
