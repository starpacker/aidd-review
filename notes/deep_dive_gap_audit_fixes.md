# Gap Audit: Action Items & Missing Data

> Date: 2026-04-04
> Status: Complete

---

## 1. Missed Competitor: Hasselgren & Oprea 2024

**Citation**: Hasselgren C, Oprea TI. "Artificial Intelligence for Drug Discovery: Are We There Yet?" Ann Rev Pharmacol Toxicol 2024.

**Differentiation strategy**:
- Their question ("Are we there yet?") → our answer is structured ("No — here's the chemistry/biology divide")
- They lack our cascading failure framework, OoC integration thesis, and first-hand ADMET-AI experiments
- Must cite and differentiate in Introduction (Section 1)

---

## 2. Antibody/Biologics AI — Must Add

Reviewer will flag our small-molecule-only focus. Add 2-3 sentences in Section 4.4:

**Key developments**:
- IgFold: language model antibody structure prediction
- DiffAb: joint sequence-structure generation
- RFdiffusion: de novo single-domain antibodies and scFv
- ML antibody discovery claims ~60% time reduction, ~50% cost reduction

**Framing**: "The biology problem applies even more acutely to biologics, where immunogenicity, folding, and manufacturing add additional failure modes that current AI cannot predict."

---

## 3. Polaris Benchmark + CACHE Challenge — Must Add

### Polaris (Novartis consortium, ICML 2024)
- Cross-industry: Novartis, AZ, Pfizer, Merck, Relay, Recursion, J&J, Bayer, Valence Labs
- First ADMET competition: 39 competitors on ASAP Discovery MERS-CoV/SARS-CoV-2 data
- Winner: Inductive Bio's Beacon-1
- Key lesson: external task-specific data helps, but pretrained models underperform expectations
- Add to Section 4.3 or 6.3

### CACHE Challenge
- Challenge #1 (LRRK2, Parkinson's): 23 teams, 1,955 predicted molecules → **73 confirmed binders (3.7% hit rate)**, KD 18-140 μM
- Now on Challenge #6; 21 countries, 120+ institutions
- Add to Section 4.3 as concrete validation of computational-to-experimental gap

---

## 4. Federated Learning — Must Add (Section 6.3)

### MELLODDY (J Chem Inf Model 2024)
- 10 pharma companies, 2.6B data points, 21M molecules, 40K assays
- Federated multitask learning: AUC-PR +4-12.5%, R² +2-4.8%
- **Improvement is incremental, not transformative**

### FLuID (Nat Mach Intell 2025;7:423-436)
- 8 pharma companies, federated distillation for privacy-preserving knowledge sharing

### Federated OpenFold3 (2025-2026)
- AbbVie, J&J, Astex, BMS, Takeda fine-tuning on proprietary structural data

**Framing**: Federated learning addresses data fragmentation (Section 4.3) but yields incremental improvements (4-12%), not the transformative gains needed to close the biology gap.

---

## 5. "Scaling Hypothesis" Counter-Argument — Must Address

### The Optimist Claim
- Foundation models on larger multimodal data will close the biology gap
- AlphaFold3 expansion to DNA/RNA/ligand
- NVIDIA $1B Eli Lilly partnership for "large quantitative models"

### Our Rebuttal
- 68% of tech executives cite **poor data quality** (not quantity) as why AI fails
- MELLODDY: 2.6B data points → only 4-12% improvement
- "Diminishing returns when scaling AI by volume alone" (2025 industry reports)
- **The gap is epistemological, not computational**: training on biochemical assays cannot predict in vivo biology regardless of scale
- Scaling within current data paradigm amplifies existing biases rather than correcting them

**Add as paragraph or callout box in Section 4.3 or 6.3**: "Could Scaling Solve the Biology Problem?"

---

## 6. FDA NME Trends + Cost-per-NME — Must Add (Section 1)

### NME Approvals Per Year
- 2020: 53 | 2021: 50 | 2022: 37 | 2023: 55 | 2024: 50 | 2025: 46
- Roughly flat at ~50/year — NOT declining
- **Eroom's Law is about cost-per-NME, not output volume**

### Cost Per NME
- DiMasi (2016, updated): $2.8B (2018 USD, capitalized)
- RAND (Jan 2025): median $708M, mean $1.31B (range $318M-$2.8B)
- Deloitte 2024: $2.23B per asset; development >100 months
- **Only 9% of companies see significant AI ROI** (Deloitte)
- **Only 22% successfully scaled AI** (Deloitte)

**Framing**: ~50 NMEs/year at ever-increasing cost. AI promises to bend the cost curve, but no evidence it has yet.

---

## 7. Investment Data — Key Numbers (Section 1)

### Market Size
- AIDD market: ~$2-4B (2024-2025), projected $8-14B by 2030-2033 (CAGR 24-31%)

### VC Pattern
- 2021 peak ($4.7B) → 2022-23 correction → 2024 rebound ($3.8B)
- Cumulative: >$17B since 2019
- AI biotech valuation premium: median $78M vs $40M for broader biopharma (2x)
- JMIR 2026: deal size grew $0.19M → $7.50M (2010-2024)

### Public Market Correction
- AbCellera: -93.4% from IPO ($15.66B → ~$1B)
- Recursion: -89% from 2021 high
- Schrodinger: -49%

### ROI Reality
- McKinsey projects $60-110B theoretical value
- Deloitte measures: AI hasn't reduced 100-month timeline, cost per NME still rising
- **Stark gap between projected and realized AI value**

---

## 8. Pipeline Phase Breakdown — Must Add

- 173+ AI programs in clinical development (Axis Intelligence 2026)
- Phase I: ~94 | Phase II: ~56 | Phase III: ~15
- This narrowing (94→56→15) directly illustrates the cascading attrition our paper describes

---

## 9. Lab Automation Standards — Key Data (Section 5)

### SiLA 2
- ~30-50 consortium members; limited production use
- Solves device communication but NOT workflow orchestration or data semantics

### FAIR Data
- <20% of pharma data FAIR-compliant (Wilkinson et al. 2016; Wise et al. DDT 2019)
- 80% of scientist time spent on data wrangling
- 80-90% of experimental data never reused ("dark data")
- EC estimated poor data management costs €10.2B/year in European research

### Integration Costs
- Typical pharma lab: 15-25 different software systems
- Custom instrument integration: $50K-$200K per instrument, 3-12 months
- Allotrope Foundation (2012): still pilot-stage after >10 years

---

## 10. Additional Should-Do Items

### Clinical Trial AI (2-3 sentences, Section 6)
- AI recruitment improves enrollment by 65%; timelines 30-50% faster
- Frame as: "AI's greatest near-term clinical impact may be in trial optimization, not drug design"

### Formulation Gap (Section 4.2)
- AI designs molecules but doesn't address crystallization, dissolution, excipients, scale-up
- DeepCeutix: "Your AI Can Design a Molecule. It Can't Formulate a Drug."

### Self-Reported Comparisons Caveat (Section 3)
- Insilico: 18 months at $150K vs traditional 4-6 years at ~$2.6B
- These are company claims, NOT independently validated

### Quantum Computing (1 sentence, Section 7)
- "Quantum computing may eventually address electronic structure calculations, but practical quantum advantage for drug discovery remains years away"

### Recursion-Exscientia Merger + REC-994 Failure (Section 4.1)
- Most integrated AI platform in existence → flagship compound still failed Phase II
- Even maximal integration cannot overcome the biology problem
