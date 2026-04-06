# Deep Dive: Resolving the "Chemistry Solved" Contradiction

> Date: 2026-04-04
> Status: Complete — requires Section 3 title change

---

## The Contradiction

Paper simultaneously claims:
- (a) "AI solved the Chemistry Problem" (Section 3)
- (b) AI molecules lack structural diversity (DSP-1181: 58% haloperidol shape match)
- (c) >90% training data is Ro5, systematic bRo5 failure
- (d) ADMET-AI R²=-1.21 (VDss), R²=-2.39 (Half_Life)

**Resolution**: These are NOT contradictory — they describe AI at different granularities. The error is in the framing "solved" as a blanket claim.

---

## 1. What AI Has Actually Solved

### (a) Multi-parameter optimization within Ro5 space — GENUINE
- Simultaneously optimizes binding affinity, selectivity, ADMET, synthetic accessibility
- Human medchemists cannot efficiently navigate 5-10 dimensional property space at scale
- This is real and significant

### (b) Filtering out bad molecules earlier — GENUINE
- Phase I success 80-90% reflects fewer PK disasters, fewer obvious toxicity flags
- ADMET attrition: ~40% (1991, Kola & Landis) → 10-15% (2017, Sun et al.)
- AI-designed molecules genuinely have better drug-like properties

### (c) Speed of lead identification — GENUINE
- 12-18 months vs 4-6 years documented (but faster ≠ better clinically)

---

## 2. What AI Has NOT Solved

### (a) Clinical PK prediction
- ADMET-AI v2: VDss R²=-1.21, Half_Life R²=-2.39
- These are the parameters that matter for human dosing, not assay-level predictions

### (b) pH-dependent behavior
- Atazanavir: >1000-fold solubility variation across GI pH
- Not captured by standard models

### (c) Pharmacogenomics
- CYP2C19 polymorphisms for clopidogrel: HR 2.81 for stent thrombosis in poor metabolizers
- Population-level variation invisible to molecular-level AI

### (d) Formulation, active metabolites, protein binding displacement

### (e) Anything in bRo5 space (ADCs, PROTACs, macrocycles)

---

## 3. AI Molecular Novelty — Systematic Evidence

### JCIM 2025 (65(17):8924-8933) — Definitive novelty study
- Analyzed 71 AI-designed active compounds
- **Ligand-based models**: 58.1% have Tcmax > 0.4 (high similarity to known molecules = low novelty)
- **Structure-based models**: only 17.9% have Tcmax > 0.4 (significantly more novel)
- DSP-1181 CAS analysis (58% haloperidol match) aligns exactly with the 58.1% ligand-based figure
- **Method matters enormously**: novelty is not binary

### MOSES benchmark (Polykovskiy et al. 2020)
- "Novelty" metric = STRING novelty (different SMILES), not STRUCTURAL novelty
- Models can score high "novelty" while generating minor variations of training scaffolds

### Goldman/Walters ACD framework (J Med Chem 2022)
- Level 1: "Machine provides ideas selected by person" — where most published systems operate
- Walters 2024: of 1,000 DiffLinker molecules, only 88 (8.8%) survive basic filters; one structure appeared 145 times
- "Not creative chemistry; noisy enumeration"

### Counter-evidence:
- Structure-based approaches (17.9% Tcmax > 0.4) DO show genuine scaffold novelty
- RLY-2608 used motion-based design for genuinely novel PI3Kα conformational selectivity

---

## 4. The Ro5 Boundary — Quantitative

### Price et al. 2024 (J Med Chem 67(7):5683-5698) — AbbVie data
- NOTE: Currently miscited as "Morreale2024bRo5" in references.bib — actually Price et al.
- ~1,000 compounds with human absorption data + ~10,000 AbbVie compounds
- Standard ADMET predictors show **NO correlation** with PROTAC permeability
- bRo5 "chameleonic" behavior requires entirely new descriptors (EPSA, AB-MPS, ETR)
- Existing ML models trained on Ro5 data are **useless** for bRo5

### Training data bias (verified):
- ChEMBL: ~9.2% non-Lipinski (Capecchi 2019)
- PubChem: ~7.6% break ≥1 Lipinski constraint
- **>90% of ML training data is Ro5-compliant**

### Clinical gap:
- 275 ADC trials: 0 AI-designed
- ~30 PROTAC trials: 0 AI-designed from scratch
- Fastest-growing modalities = LEAST amenable to current AI

---

## 5. Proposed Section 3 Reframe

### Old title: "The Chemistry Problem: Where AI Excels"
### New title: "The Chemistry Problem: What AI Has — and Has Not — Solved"

### Structure:
1. **Genuine achievements**: MPO, Phase I rates, speed — with caveats about target selection bias contributing to Phase I success
2. **The property prediction gap**: ADMET-AI R² data, VDss/half-life failures
3. **The chemical space boundary**: Ro5 vs bRo5 training bias, 0 AI-first bRo5 drugs
4. **The novelty spectrum**: JCIM 2025 systematic analysis, method-dependent (ligand-based = low novelty, structure-based = higher novelty)

### Key sentence:
"AI has solved multi-parameter optimization of drug-like properties within conventional small-molecule Ro5 space — a genuine and significant achievement that explains the doubling of Phase I success rates. However, three boundaries circumscribe this achievement: the property prediction gap (clinical PK parameters remain poorly predicted), the chemical space boundary (>90% Ro5 training data, zero AI-first bRo5 drugs in trials), and the novelty spectrum (ligand-based models predominantly produce variations of known pharmacophores)."

---

## 6. Key New References

- JCIM 2025;65(17):8924-8933 — AI molecule novelty systematic evaluation
- Price et al. J Med Chem 2024;67(7):5683-5698 — bRo5 ADMET failure (fix Morreale attribution)
- Goldman et al. J Med Chem 2022 — ACD levels framework
- Polykovskiy et al. Front Pharmacol 2020 — MOSES benchmark
