# Deep Dive: Why Successful AI Drugs Succeeded — Biology Analysis

> Date: 2026-04-04
> Status: Complete — CRITICAL for balanced thesis

---

## Core Finding: Every Clinically Successful AI Drug Stands on Pre-Validated Biology

**Zero AI drugs have succeeded on genuinely novel, AI-discovered biological targets with no prior validation.**

---

## 1. Rentosertib / ISM001-055 (Insilico, IPF) — Phase IIa Positive

### Target: TNIK (Traf2- and Nck-interacting kinase)
- TNIK was **already known** in Wnt signaling, intestinal/colorectal cancer, inflammation
- Application to IPF was relatively less explored but not unknown
- Wnt/β-catenin signaling is **heavily implicated** in fibrogenesis — established pathway
- AI (PandaOmics) identified TNIK-for-IPF as a target-indication pairing via multi-omics prioritization

### Assessment:
- **Strongest case for "AI contributing to biology"** because indication pairing was non-obvious
- But underlying biology (Wnt-fibrosis axis) was well-established
- AI contribution = **computational target prioritization within known biology**, NOT discovery of new biology
- Phase IIa only (N=71, small, single geography) — the least clinically advanced success
- **The most "biological" AI contribution is also the least validated clinically**

---

## 2. Zasocitinib / TAK-279 (Nimbus → Takeda, TYK2) — Phase III Positive

### Target: TYK2 JH2 pseudokinase domain
- **BMS pioneered this entirely**: deucravacitinib (Sotyktu) approved Sept 2022
- Burke et al. 2019 (Nature): described JH2 as druggable allosteric site
- Biological hypothesis **fully validated by BMS** before Nimbus entered clinical trials
- Nimbus contribution = **superior molecule** via Schrödinger FEP+ for same validated target

### Key evidence of zero biological novelty:
- Armstrong et al. JAMA Dermatology 2024 (zasocitinib Phase 2b): **no mention of AI, ML, Schrödinger, or FEP+** in manuscript
- TYK2 has robust GWAS support for autoimmune disease
- $6B Takeda deal validated AI-assisted **molecular optimization**, not biological discovery

### Assessment:
- Textbook case of AI solving chemistry for already-solved biology
- **Strengthens** the thesis: success ≠ AI solving biology

---

## 3. Zovegalisib / RLY-2608 (Relay, PI3Kα) — Phase III

### Target: PIK3CA mutations (most frequently mutated oncogene in solid tumors)
- Alpelisib (Novartis, approved 2019) already validated PI3Kα in PIK3CA-mutated breast cancer
- Innovation = **mutant-selectivity** via conformational dynamics modeling
- Relay's Dynamo: cryo-EM + MD simulations to capture protein motion

### Is mutant-selectivity biology or chemistry?
- Understanding conformational differences = structural biology knowledge
- Concept of mutant-selective inhibitors existed (KRAS G12C: sotorasib)
- Relay's AI contributed **computational modeling of dynamic conformations** → primarily chemistry/structural biology
- AI did NOT predict PI3Kα would be a good target → designed a molecule distinguishing mutant from WT

### Assessment:
- Target fully validated. Innovation is molecular design, not biology.
- Physics-based methods (MD, cryo-EM) drove success, not pattern recognition ML.

---

## 4. Baricitinib Repurposing (BenevolentAI, COVID-19) — Validated

- Knowledge graph predicted baricitinib (already approved JAK inhibitor for RA) could work in COVID via AAK1-mediated viral endocytosis
- Published Lancet Feb 2020, validated in ACTT-2 and COV-BARRIER trials
- Arguably most "biological" AI contribution among successes
- **But**: drug repurposing, not de novo discovery; baricitinib already approved
- AAK1-endocytosis mechanism used existing biological knowledge

---

## 5. Pattern Analysis — All Successes

| Drug | Target Validated? | Genetic Evidence | Method Type | Phase | AI Bio Contribution |
|------|------------------|-----------------|-------------|-------|-------------------|
| Rentosertib | Partially (known pathway) | Pathway-level | Generative AI | IIa | Target prioritization (low) |
| Zasocitinib | Fully (BMS approved) | Strong GWAS | FEP+ (physics) | III | Zero |
| Zovegalisib | Fully (Novartis approved) | Extremely strong | MD + cryo-EM | III | Zero |
| Baricitinib | Fully (approved drug) | Known | Knowledge graph | Approved | Low (repurposing) |

### Key patterns:
1. **Every success targets validated biology** — not one involves genuinely novel AI-discovered mechanism
2. **Most advanced programs (Phase III) use physics-based methods**, not pure ML
3. **Strong genetic evidence correlates with clinical success** (TYK2 GWAS, PIK3CA somatic mutations)
4. **No "AI-first biology" drug has reached Phase III** — the furthest are AI-assisted chemistry on validated targets
5. **The one semi-novel target (TNIK) is the least advanced and most uncertain**

---

## 6. Critical Implication for Thesis

### The strongest version of the thesis:

"AI has demonstrated the ability to accelerate molecular design (chemistry) dramatically. Its contribution to biological target discovery and validation remains unproven at the clinical level. The successful AI drugs succeed because they stand on decades of prior biological research — the biology was already solved by traditional methods."

### This means:
- Rate-limiting step = **biological attrition** (wrong target, wrong mechanism, poor translation)
- AI solving the **cheaper** problem (chemistry, ~$millions) not the **expensive** problem (biology, ~$billions in Phase II/III)
- Industry narrative conflates chemistry optimization (proven) with biological discovery (unproven)

### For Section 3 reframe:
- Successes validate "AI solves chemistry" claim
- Successes simultaneously prove AI hasn't solved biology — every success required pre-validated biology
- **The success pattern is the thesis's strongest evidence**, not the failures
