# Research Deep-Dive Summary

> Date: 2026-04-04 (updated with Round 2 + Round 3 deep dives)
> Status: ALL research gaps resolved — ready for drafting

---

## Round 2 Deep Dives (2026-04-04) — NEW DATA

### Deep Dive 1: Physics-Based vs ML Methods
- **FEP+ RMSE: 0.9-1.2 kcal/mol** vs ML 1.5-2.0+ (after cleaning leakage)
- **Graber et al. 2025 (Nature Machine Intelligence)**: removing PDBbind leakage increases ML RMSE by 42%; nearest-neighbor competitive with DL
- **Zasocitinib**: FEP+ scored ~4,000 molecules, $4B+$2B = $6B deal — physics-based, NOT generative AI
- **Zovegalisib (RLY-2608)**: 10-100μs MD revealed cryptic allosteric pocket invisible in static structures, FDA BTD Feb 2026
- **Ross et al. 2023**: FEP+ approaching experimental noise ceiling (0.91 kcal/mol)
- **Key insight**: Physics-based methods producing most clinically validated successes; pure ML has none
- **File**: `notes/deep_dive_physics_vs_ml.md`

### Deep Dive 2: Phase II Failures & AI Drug Attrition
- **Harrison 2016**: Efficacy 52%, Safety 24% (218 failures)
- **Morgan et al. 2018**: AZ 5Rs improved success 4%→19% (nearly 5-fold)
- **Morgan 2012**: 43% of "efficacy failures" couldn't confirm mechanism was tested
- **Bowling 2025**: Late-stage terminations doubled (11%→22%); strategic > efficacy now
- **NEW AI failures**: VRG-50635 (Verge Genomics, ALS, Phase I, Dec 2025) — now 7 total AI drug discontinuations
- **All 7 AI failures are biological** (efficacy, therapeutic index) — zero failed due to chemistry
- **Jayatunga dataset**: no peer-reviewed update beyond N=75 despite 173+ programs now
- **Norstella 2025**: overall LoA at all-time low 6.7%
- **File**: `notes/deep_dive_phase2_failures.md`

### Deep Dive 3: Multi-Omics, Digital Twins & Foundation Models
- **Minikel 2024 confirmed**: 2.6x (Nature, 29,476 T-I pairs); OMIM 3.7x
- **Ochoa 2022**: genetics supports ~67% of 2021 FDA-approved drugs
- **Ravarani 2026**: MR alone ≠ Phase II enrichment, but MR+XGBoost = 55% approval (6.4x)
- **Dann 2024**: scRNA-seq can ~triple Phase III chances
- **UKB-PPP**: >14,000 genetic-protein links, >80% novel; full-scale 5,400 proteins × 600K samples
- **Unlearn PROCOVA**: EMA-qualified, 9-15% sample reduction (Alzheimer's TRCI 2025)
- **scGPT/Geneformer**: underperform simple baselines on zero-shot (Genome Biology 2025)
- **Boltz-2**: near-FEP accuracy at >1,000x speed, 20s on single GPU
- **No foundation model has contributed to a clinical-stage drug**
- **File**: `notes/deep_dive_multiomics_digitaltwin_updated.md`

### Deep Dive 4: OoC+AI, Regulatory & PBPK/QSP
- **Ewart Liver-Chip**: now in FDA ISTAND pilot (Sept 2024), still unreplicated independently
- **Closed-loop OoC-AI**: does NOT exist in published form; Yakavets 2025 (Sci Adv) and Hesperos 2025 (Adv Sci) are closest
- **Hesperos**: first OoC-derived digital twin with clinical alignment (malaria)
- **FDA April 2025**: phase-out plan for animal testing (mAbs first)
- **FDA Mod Act 3.0**: passed Senate Dec 2025
- **NIH July 2025**: animal-only proposals no longer eligible
- **ICH M15**: first ICH guideline formally including AI/ML
- **FDA AI/ML guidance Jan 2025**: explicitly excludes drug discovery
- **PBPK+ML**: best result 65% within 2-fold (Li et al. 2024) — not clinical-grade
- **QSP+ML**: AZ team says "early stage", essentially zero clinical validation
- **File**: `notes/deep_dive_ooc_regulatory_sdl.md`

### Deep Dive 5: LLM Agents & Pharma SDLs
- **ScienceAgentBench (ICLR 2025)**: best agents solve 32-42% of scientific tasks
- **Chemistry = LLMs' weakest domain**: 51.3% accuracy (FrontierScience, lowest of all subjects)
- **Hallucination**: GPT-3.5 39.6%, Bard 91.4%, GPT-4 28.6% reference fabrication
- **Urbina 2022**: 40,000 toxic molecules generated in <6 hours, including VX
- **Novartis MicroCycle**: best pharma SDL (100 compounds/cycle, J Med Chem 2024)
- **AstraZeneca**: "complete DMTA automation has not yet been achieved"
- **Recursion-Exscientia merger**: $688M, goal end-to-end platform — no results yet
- **$40M**: cost of building pharma-grade SDL (CMU + Emerald)
- **ChemCrow repo**: explicitly warns "will not give same results as paper"
- **Key insight**: pharma SDL results almost exclusively press releases, not peer-reviewed
- **File**: `notes/deep_dive_ooc_regulatory_sdl.md`

---

## Round 1 Deep Dives (2026-04-03) — RETAINED

### Experiment 1: ADMET-AI v2 Predictions on Case Study Drugs
- **File**: `notes/experiment_admet_ai.md`, `experiments/results_admet_ai_full.json`
- VDss R²=-1.21, Half_Life R²=-2.39; Imatinib flagged highest risk; Rofecoxib missed

### Experiment 2: Drug-Likeness Filter Analysis
- **File**: `experiments/results_filter_analysis.json`
- 5/5 failures pass all filters; 1/2 successes fails

### Experiment 3: Cumulative Pipeline Probability
- **File**: `experiments/results_vs_gap.json`
- Computational hit→FDA: ~0.003% (1 in 33,000); AI: ~0.004% (1 in 25,000)

### Benchmark Gap (Section 4.3) — Quantified
- Random splits: 18% R² inflation; PDBBind leakage documented; DiffLinker: 8.8% yield

### Competitor Check — No Direct Competitor
- NRDD, Nature MI, Ann Rev, J Med Chem, DDT, Trends Pharmacol, Chem Rev — gap confirmed

### OoC+AI Silo — Quantified
- ~10-15 empirical papers; 70-80% image analysis, not drug response

### Causal Inference — Substantiated
- Pearl's ladder; MR 2.6x; Recursion, Aitia, BenevolentAI examples

---

## Updated Status of All Research Gaps

### FULLY RESOLVED
- [x] ADMET-AI performance verified experimentally
- [x] Benchmark gap quantified (18% R² inflation, PDBbind leakage, DiffLinker cascade)
- [x] Competitor check complete (no direct competitor)
- [x] OoC+AI silo quantified (~10-15 papers)
- [x] Causal inference substantiated with companies + MR data
- [x] Multi-omics updated (2023-2026) with scRNA-seq, spatial, UKB-PPP
- [x] Digital twins expanded (3 types, Unlearn PROCOVA EMA-qualified)
- [x] Agent code reproducibility documented
- [x] **NEW** Physics-based vs ML quantified (FEP+ 0.9-1.2 vs ML 1.5-2.0+)
- [x] **NEW** Phase II failures systematized (Harrison→Bowling 2013-2025 series)
- [x] **NEW** AI drug failure catalog (7 programs, all biological failures)
- [x] **NEW** Target validation gap quantified (5Rs: 4%→19%; Nelson 2x; Minikel 2.6x)
- [x] **NEW** LLM agent capabilities benchmarked (ScienceAgentBench 32-42%)
- [x] **NEW** Pharma SDL landscape mapped (Novartis, AZ, Arctoris, Strateos)
- [x] **NEW** Regulatory landscape comprehensive (FDA, EMA, NIH, ICH M15)
- [x] **NEW** Foundation models assessed (scGPT/Geneformer < baselines)
- [x] **NEW** PBPK+ML and QSP+ML assessed (early stage, minimal validation)

### REMAINING GAPS (acceptable for first draft)
- [ ] No primary PitchBook report (use secondary + JMIR 2026 peer-reviewed with caveat)
- [ ] BEN-2293 no peer-reviewed paper (press-release-based, caveat explicitly — EASI/NRS values never disclosed)

### PREVIOUSLY FLAGGED GAPS — NOW RESOLVED (Round 3)
- [x] **ADC/oligonucleotide/PROTAC AI limitations**: fully researched — >90% Ro5 training bias, 0 AI-first ADCs/PROTACs in trials
- [x] **SiLA 2 adoption**: ~30-50 members, limited production use; FAIR <20% compliance; 80-90% dark data
- [x] **BEN-2293 mechanism**: Type 2 immunity (not Trk/NGF) drives AD; CAS showed DSP-1181 resembles haloperidol
- [x] **Investment data**: Deloitte 2024 ($2.23B/NME, 9% AI ROI); VC pattern (2021 peak→correction→rebound)
- [x] **Competitor audit**: Hasselgren & Oprea 2024 (Annual Reviews) identified — must cite and differentiate
- [x] **Polaris + CACHE benchmarks**: 3.7% hit rate in CACHE, pretrained models underperform in Polaris
- [x] **Federated learning**: MELLODDY (10 pharma, 2.6B points, 4-12% improvement), FLuID
- [x] **Scaling counter-argument**: 68% cite data quality not quantity; MELLODDY 2.6B→only 4-12%
- [x] **FDA NME trends**: ~50/year (flat); cost $708M-$2.8B per NME
- [x] **Antibody/biologics AI**: IgFold, DiffAb, RFdiffusion — biology problem applies even more to biologics
- [x] **VRG-50635 detailed**: PIKfyve inhibitor, Cell 2023 paper, Phase 1b failed Dec 2025
- [x] **AI pipeline phase breakdown**: 94 Phase I / 56 Phase II / 15 Phase III (demonstrates cascading attrition)

---

## Round 3 Deep Dives (2026-04-04) — MINOR GAPS FIXED + AUDIT

### Deep Dive 6: Complex Modalities (ADC, ASO, PROTAC, bRo5)
- **>90% ADMET training data is Ro5-compliant** — severe domain shift for bRo5
- **0 AI-designed ADCs in clinical trials** (275 ADC trials, none AI-first)
- **0 AI-designed PROTACs from scratch** (~30 in trials, all traditional + computational assist)
- **No approved siRNA targets extrahepatic tissue** — delivery unsolved by AI
- **ASO hepatotoxicity** not predictable from sequence (Crooke 2021)
- **PROTAC ternary complex**: conformational ensembles, not single structures
- **File**: `notes/deep_dive_complex_modalities.md`

### Deep Dive 7: AI Drug Failure Case Studies (Detailed)
- **BEN-2293**: EASI/NRS never disclosed; AD is Type 2 immune, not Trk/NGF
- **DSP-1181**: CAS analysis — 58% match haloperidol shape, "lack structural diversity"
- **EXS-21546**: class-wide A2A therapeutic index problem; no A2A antagonist has shown definitive efficacy
- **VRG-50635**: PIKfyve (Cell 2023), Phase 1b failed efficacy analysis Dec 2025
- **All 5 clinical AI drug failures are biological** — zero chemical failures
- **File**: `notes/deep_dive_ai_drug_failures_detailed.md`

### Deep Dive 8: Investment, Standards, & Gap Audit
- **Deloitte 2024**: cost $2.23B/NME, >100 months, only 9% significant AI ROI
- **VC**: $4.7B peak (2021) → correction → $3.8B rebound (2024); cumulative >$17B
- **Public markets**: AbCellera -93%, Recursion -89%, Schrodinger -49%
- **SiLA 2**: ~30-50 members, limited production; FAIR <20%; 80-90% dark data
- **Hasselgren & Oprea 2024**: missed competitor — must cite and differentiate
- **Polaris**: pretrained models underperform; CACHE 3.7% hit rate
- **MELLODDY**: 2.6B data points → only 4-12% improvement (federated learning)
- **FDA NMEs**: ~50/year (flat); Eroom's Law is cost, not volume
- **File**: `notes/deep_dive_gap_audit_fixes.md`

---

## References.bib Status
- Entries after Round 2: ~130
- New citations needed from Round 3: ~20-30
- Critical new Round 3 citations: Hasselgren 2024, Capecchi 2019, Morreale 2024, Crooke 2021, MELLODDY 2024, FLuID 2025, CAS DSP-1181 analysis, Polaris/CACHE, Deloitte 2024, JMIR 2026 VC, RAND 2025 cost
- Total target: ~150-160 references

---

## Round 4 Deep Dives (2026-04-04) — CRITICAL THESIS DEFENSE

### Deep Dive 9: Phase II ~40% vs 28.9% Statistical Analysis
- **Phase II N likely <15** (never disclosed); 95% CI: ~15-72% → statistically indistinguishable from 28.9%
- **Selection bias**: 6/7 most-analyzed AI drugs target already-validated mechanisms
- **TA confounding**: no TA-matched comparison performed; AI clusters in favorable TAs
- **Temporal confound**: Dowden & Munro 2019 show contemporary baseline may be 35-40%
- **Even if real**: doubling Phase II (28.9%→58%) only raises LOA to ~16%
- **No systematic Phase II failure analysis exists for AI drugs** — our catalog is best available
- **File**: `notes/deep_dive_critic_phase2_stats.md`

### Deep Dive 10: Why AI Drug Successes Succeeded (Biology Analysis)
- **Every clinically successful AI drug stands on pre-validated biology**
- **Zero** have succeeded on genuinely novel, AI-discovered biological targets
- Zasocitinib: TYK2 JH2 fully validated by BMS deucravacitinib (zero bio novelty)
- Zovegalisib: PI3Kα fully validated by Novartis alpelisib (innovation = molecular design)
- Rentosertib: TNIK semi-novel (known pathway, novel indication) — least advanced (Phase IIa)
- **Most advanced programs use physics-based methods (FEP+, MD), not pure ML**
- **The success pattern is the thesis's strongest evidence** — successes prove AI solves chemistry, not biology
- **File**: `notes/deep_dive_ai_success_biology.md`

### Deep Dive 11: Resolving "Chemistry Solved" Contradiction
- Paper's four claims (a)-(d) are NOT contradictory at different granularities
- **Correct framing**: "AI solved MPO within Ro5 small-molecule space" (not blanket "Chemistry Problem")
- **JCIM 2025 (65(17):8924-8933)**: 71 AI molecules — ligand-based 58.1% high similarity (low novelty), structure-based 17.9% (more novel)
- **Price et al. J Med Chem 2024** (NOT Morreale): bRo5 ADMET models show NO correlation for PROTACs
- **Section 3 title change**: "Where AI Excels" → "What AI Has — and Has Not — Solved"
- **Three boundaries**: property prediction gap, chemical space boundary, novelty spectrum
- **File**: `notes/deep_dive_chemistry_solved_reframe.md`

### Deep Dive 12: OoC+AI Evidence Reassessment
- **Critic is largely correct**: no full OoC→ML→prediction→validation loop published
- **PDO+ML is 2-3 years more mature** (PharmaFormer, OPTIC trial with clinical validation)
- **Multi-omics+ML is most mature** (PASO model, AUC 0.81-0.87)
- **GAO Report (May 2025)**: only 10-20% purchased cells meet OoC quality — devastating for scale-up
- **Alver et al., Nature Communications 2024**: roadblocks paper from within OoC community
- **Revised framing**: three-tier solution stack (multi-omics > PDO > OoC by maturity)
- **OoC = highest ceiling, least mature** — "emerging opportunity" not "proposed solution"
- **File**: `notes/deep_dive_ooc_evidence_reassessment.md`

### Deep Dive 13: AI-Specific Failure Modes (vs Universal Biology Problem)
- **Six AI-specific failure categories** that don't exist in traditional drug discovery:
  1. Illusory performance (data leakage: 20-60% inflation, Briefings Bioinform 2025)
  2. Physically invalid predictions (PoseBusters: no DL docking beats AutoDock Vina)
  3. Hallucinated molecules (DiffLinker: 8.8% survive basic filters)
  4. Hidden distribution bias (>90% Ro5, PDB conformational bias)
  5. Black box vs interpretable SAR (opaque failures, no learning)
  6. Uncalibrated confidence (overconfident OOD, no "I don't know")
- **"Breadth without understanding"**: AI fails wide (10M screened, can't explain why); traditional fails deep (knows why)
- **Speed risk**: faster to clinic ≠ better in clinic; may skip validation steps
- **Organizational gap**: CS teams separated from biology teams (CAS 2025, Frontiers 2023)
- **Core rebuttal**: "Traditional drug discovery fails honestly. AI can fail opaquely."
- **File**: `notes/deep_dive_ai_specific_failures.md`

---

## FINAL ASSESSMENT: Research Completeness (Updated After Round 4)

### Strengths (unique to our review, updated)
1. **First-hand ADMET-AI experiments** with quantitative failure data
2. **Comprehensive AI drug failure catalog** (7 programs, all biological)
3. **Physics vs ML quantified** (FEP+ 0.9-1.2 vs ML 1.5-2.0+)
4. **Cascading failure framework** (computational hit→FDA = 0.003%)
5. **bRo5 training data bias** identified (>90% Ro5 in training)
6. **Closed-loop OoC-AI gap** confirmed (none published)
7. **Clinical insider perspective** (hospital director + trial center director)
8. **NEW: AI success pattern analysis** — every success on pre-validated biology → strongest thesis evidence
9. **NEW: Six AI-specific failure modes** — differentiates from generic drug discovery critique
10. **NEW: Phase II statistical deconstruction** — 95% CI demolishes ~40% vs 28.9% claim
11. **NEW: Three-tier biology-aware data stack** (multi-omics > PDO > OoC) — more honest than OoC-only

### Thesis Refinements from Round 4
1. **Section 3 reframe**: "Where AI Excels" → "What AI Has — and Has Not — Solved" (resolves internal contradiction)
2. **Section 4.1 strengthened**: Phase II statistical analysis + success pattern analysis = airtight argument
3. **Section 6.1 restructured**: three-tier maturity stack replaces OoC-centric framing
4. **New differentiator**: six AI-specific failure modes (vs Hasselgren/Oprea who don't make this distinction)
5. **Core rebuttal prepared**: "Traditional drug discovery fails honestly; AI can fail opaquely"

### Honest Caveats (updated)
1. BEN-2293: no peer-reviewed data (press release only)
2. Investment data: secondary sources (no primary PitchBook)
3. AI timeline/cost claims: self-reported by companies, no independent validation
4. Our mechanistic interpretations are our analysis, not company stated
5. **NEW**: OoC+AI thesis must be downgraded to "emerging opportunity" (critic is correct about evidence gap)
6. **NEW**: Phase II comparison is underpowered — we must acknowledge this openly rather than building argument on it

### References.bib Status (updated)
- Current entries: ~126
- New Round 4 citations needed: ~15-20
- Key additions: Dowden2019, Buttenschoen2024PoseBusters, Guo2024ScaffoldSplits, JCIM2025Novelty, Price2024bRo5 (fix Morreale), PharmaFormer2025, OPTIC2025, Alver2024OoCRoadblocks, GAO2025OoC, Walters2024NatMachIntell, WaltersMurcko2020
- Total target: ~150-160 references

### Ready for Drafting: YES ✅ (with thesis refinements incorporated)
