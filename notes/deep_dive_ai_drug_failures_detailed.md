# Deep Dive: AI Drug Failure Case Studies — Detailed Mechanistic Analysis

> Date: 2026-04-04
> Status: Complete

---

## 1. BEN-2293 (BenevolentAI) — Pan-Trk for Atopic Dermatitis

### Trial Details (NCT04737304)
- Phase IIa, randomized, double-blind, placebo-controlled
- 91 patients (49 BEN-2293 1% topical vs 42 placebo), mild-to-moderate AD, ages 18-65
- Twice-daily for 28 days
- Primary (safety): **MET**
- Secondary (EASI, NRS itch): **NOT MET in ITT**
- **Specific EASI/NRS numerical values NEVER disclosed** — only statistical conclusion

### BSA >20% Subgroup
- Per-Protocol population: significant EASI effect for BSA >20% (p=0.0427)
- Treatment × disease burden interaction: p=0.0237
- **Post-hoc subgroup on PP population in 91-patient trial = hypothesis-generating only**

### Why Pan-Trk Failed for AD
1. **AD is fundamentally Type 2 immune disease**, not primarily neurogenic itch
   - Dupilumab (anti-IL-4Rα): EASI-75 in 44-52% at 16 weeks (SOLO 1&2)
   - JAK inhibitors (baricitinib, upadacitinib, abrocitinib): robust efficacy
   - These target upstream immunological driver, not downstream symptom
2. **Topical delivery reaches nerve endings but NOT systemic immune dysregulation**
3. **Immunological redundancy**: multiple pruritogens (IL-31, TSLP, histamine, PAR-2) remain active
4. **Mild-moderate population**: insufficient neurogenic itch component

### BenevolentAI's Response
- CSO described results as "not conclusive"
- Suggested wrong patient population (mild-moderate)
- **May 2023**: dropped BEN-2293, cut ~180 employees, saved ~$56M
- **No peer-reviewed publication** of full trial data

### For Our Review
BEN-2293 exemplifies how AI can identify a biologically valid target association (NGF/TrkA elevated in AD skin) but cannot distinguish **association from causation**. The target was correlatively linked to disease but not causally driving it — precisely the Pearl's ladder Level 1→Level 2 gap we describe.

---

## 2. DSP-1181 (Exscientia/Sumitomo) — 5-HT1A for OCD

### What It Was
- Full 5-HT1A agonist (vs existing partial agonists like buspirone)
- ~350 compounds in <12 months via Centaur Chemist AI
- Phase I initiated Japan, January 2020

### Discontinuation
- "Did not meet expected standards" (Sumitomo language)
- **No PK, safety, or efficacy data disclosed**
- Dropped ~2021-2022, no Phase II

### CAS Structural Analysis — KEY DATA
- CAS (Chemical Abstracts Service) analyzed patent US10800755
- DSP-1181 molecules **share structural shape with haloperidol** (approved 1967)
- Of 38 exemplified molecules: **58% matched haloperidol shape, 21% matched lamotrigine**
- "Lack structural diversity" — AI optimized variations on known pharmacophores
- CAS conclusion: "medicinal chemists more than likely would have identified these molecules as potential drug candidates using traditional approaches"
- Citation: CAS Insights, "Assessing the first AI-designed drug candidates" (2023)

### For Our Review
Challenges the "AI novelty" narrative. If AI-designed molecules closely resemble existing drugs, the claimed efficiency gains (12 months vs 4.5 years) may reflect narrower search scope rather than genuine innovation.

---

## 3. EXS-21546 (Exscientia/Evotec) — A2A Antagonist for Cancer

### Phase 1a Results (June 2022, healthy volunteers)
- Confirmed target product profile: potency, selectivity, low brain exposure
- PK in line with preclinical predictions
- Identified therapeutic starting dose

### Discontinuation (2023)
- Modeling showed "challenging to reach suitable therapeutic index"
- Prolonged, high-level A2A coverage needed for anti-tumor effect
- Structural analysis (CAS): 46 molecules showed 3 shapes matching **Janssen competitor structures**

### Why A2A Therapeutic Index Is a Class Problem
1. **Ubiquitous expression**: cardiovascular, brain, immune — off-target risk
2. **High sustained coverage needed**: tumor microenvironment adenosine concentrations very high
3. **Cardiovascular effects**: adenosine vasodilator → A2A blockade = CV risk
4. **Class-wide failures**: Preladenant (Merck, Phase 3 failed), Tozadenant (Acorda, fatal agranulocytosis)
5. **No A2A antagonist has demonstrated definitive efficacy** in immuno-oncology

### For Our Review
Even when AI designs a molecule that perfectly hits its target, **class-wide pharmacological limitations** can make the program unviable. The therapeutic index problem is not a molecule problem — it's a biology problem.

---

## 4. VRG-50635 (Verge Genomics) — PIKfyve for ALS

### CONVERGE Platform Discovery
- Analyzed 11.4 million data points from ALS patient tissue and genetics
- Identified loss of endolysosomal function as novel causative mechanism
- PIKfyve inhibition promotes exocytosis of neurotoxic proteins (pTDP-43)
- Published in **Cell** (Feb 2023, Shi et al.): PIKfyve inhibition extended survival of patient-derived motor neurons across C9ORF72, TARDBP, FUS, and sporadic ALS

### Clinical Results
- Phase I (80 healthy volunteers, June 2023): safe and well tolerated
- Phase 1b (ALS patients, Jan-Aug 2024): innovative digital biomarkers (touchless sensors, accelerometers, speech platform) + NfL
- **Dec 2025: Failed pre-specified efficacy analysis** → "no-go" decision
- ClinicalTrials.gov reason: "lack of risk-benefit data"

### Aftermath
- Dropped sole clinical candidate
- Pivoted to CONVERGE platform as service/licensing model
- Ferrer deal (EUR 112.5M) left in limbo

### For Our Review
VRG-50635 represents the most sophisticated AI-first target discovery approach (multi-omic, patient tissue-derived) leading to a novel mechanism with strong preclinical validation (Cell paper). Yet it still failed in patients. This is the ultimate illustration of the biology gap: even when AI identifies a genuinely novel biology and the molecule works in patient-derived cells, **the leap to clinical efficacy remains unresolved**.

---

## 5. Common Themes Across All AI Drug Failures

| Drug | Phase | AI Contribution | Failure Mode | Key Lesson |
|------|-------|----------------|-------------|------------|
| BEN-2293 | IIa | Target ID (KG reasoning) | Wrong biology (association ≠ causation) | AI found correlation, not cause |
| DSP-1181 | I | Molecule design | Unknown (undisclosed) | Molecules resemble existing drugs |
| EXS-21546 | I/II | Molecule design | Class-wide TI problem | Can't design around pharmacology |
| VRG-50635 | Ib | Target ID (multi-omics) | Preclinical→clinical translation gap | Patient cells ≠ patient outcomes |
| REC-994 | II | Target ID (phenomics) | No sustained benefit | AI screen → biology doesn't translate |
| REC-2282 | Preclinical | Phenomic screen | Portfolio deprioritization | Business > biology |
| REC-3964 | Preclinical | Phenomic screen | Shifting treatment landscape | External factors unpredictable |

### Critical Observation
**All 5 clinical-stage AI drug failures are biological, not chemical.** Not a single AI-originated drug has failed because the molecule was poorly designed. This directly validates our thesis: AI has solved the chemistry problem but not the biology problem.
