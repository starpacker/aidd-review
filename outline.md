# AIDD Review — Detailed Section Outline

> **Working title**: "The Automation Gap: Why AI-Driven Drug Discovery Pipelines Fail Between Benchmarks and Bedside"
> **Target**: Nature Reviews Drug Discovery / Nature Machine Intelligence (editor-invited review)
> **Estimated length**: ~6,000 words + 6 figures + 1 table
> **Last updated**: 2026-04-03

---

## Section 1. Introduction (~800 words)

### Key Arguments
- Open with the **investment paradox**: >$17B cumulative AIDD-specific VC since 2019 (PitchBook; note: broader biotech sector >$420B — must not conflate). Market $2.9B→$12.5B (CAGR 15.7%), mega-rounds (Xaira $1B, Isomorphic Labs $600M) — yet **no AI-designed drug has achieved FDA approval as of the time of writing** (note: Zasocitinib NDA expected 2026; discuss AI attribution debate in Section 7)
- Historical framing: drug discovery evolved from serendipity → rational design → "drug engineering" via AI. Each transition promised to solve the 90% attrition rate; AI is the latest
- Introduce the **core thesis**: AI has solved the "Chemistry Problem" (designing drug-like molecules with good ADMET) but not the "Biology Problem" (predicting clinical efficacy in humans)
- Phase I success rates doubled (80-90% vs. 52% BIO baseline) but Phase II (~40%) shows no clear improvement over industry norm (28.9% BIO baseline; note: ~40% vs. 28.9% may reflect target selection bias, not efficacy improvement) — the "paradox of precision"
- Geographic concentration: CA + MA = ~60% of US deals; implications for research diversity
- Scope statement: this review systematically dissects cascading failure modes across the AIDD pipeline and proposes an integration roadmap

### Required Citations
- [ ] Market data: Precedence Research / Grand View Research 2025 reports
- [ ] VC investment landscape: PitchBook or CB Insights AIDD reports
- [ ] Xaira $1B Series A, Isomorphic Labs $600M — press releases
- [ ] Phase I/II success rates: **Jayatunga et al., Drug Discovery Today, 2024** [R8] ★ KEY
- [ ] Historical drug discovery evolution: Drews 2000 (Science); Swinney & Anthony 2011
- [ ] No FDA-approved AI drug: Wilczok & Zhavoronkov, CPT, 2025 [R27]
- [ ] 173+ AI drugs in clinical development: Axis Intelligence 2026

### Data Sources
- Gemini deep research: market & investment section
- Independent survey: Jayatunga et al. 2024 confirms Phase I/II gap
- ✅ **VC figure CORRECTED**: $420B is all-biotech cumulative, NOT AIDD-specific. AIDD-specific: ~$17B since 2019 (PitchBook). 2024 annual: $3.8B (rebounding). Use $17B as primary figure; may reference $420B broader context if clearly distinguished

### New Figure — "The Precision Paradox" (Figure 1)
- **Type**: Paired bar chart or forest plot
- **Content**: Side-by-side comparison of AI-native vs. traditional success rates at Phase I, Phase II, Phase III
- **Key visual**: Phase I bars show dramatic AI advantage; Phase II/III bars show convergence — the "paradox" is immediately visible
- **Placement**: Section 1 (hook the reader) or Section 4.1 (evidence for the biology problem)
- **Data source**: Jayatunga et al. 2024 [R8]

### Differentiation Note
- vs. Jayatunga (R8): they quantify Phase I/II gap but don't explain WHY
- vs. Nature Medicine review (R4): they focus on positive applications, we focus on failure modes
- Our hook: investment scale × zero approvals = most expensive unresolved gap in pharma

---

## Section 2. The AIDD Pipeline: Architecture and Assumptions (~800 words)

### Key Arguments
- Walk through the standard AIDD pipeline stages: target ID → structure prediction → virtual screening → lead optimization → preclinical → clinical
- At each stage, highlight the **assumptions** that AI models make — and where those assumptions break down
- **Target identification**: knowledge graphs, multi-omics. Assumption: targets identified from genomic associations are druggable and causally linked to disease. Reality: many GWAS hits are non-causal
- **Protein structure prediction**: AlphaFold2/3 revolutionized static structure prediction. But: biology = **dynamic conformational ensembles**. AF3 fails on conformational changes >5A RMSD, GPCR antagonist selectivity (ROC-AUC near random for kinase selectivity). Static snapshot ≠ druggable pocket
- **Virtual screening & docking**: scoring functions assume rigid binding, ignore solvation, entropic effects. In silico hit rates ≈ 1-5% in practice
- **Binding site prediction**: algorithms can identify pockets, but **cannot validate** whether binding leads to therapeutic effect — requires domain expertise (clinician-in-the-loop)
- **Lead optimization & ADMET**: the genuine success story. ADMET-related attrition fell from ~40% (1991; Kola & Landis 2004) to 10-15% (2010-2017; Sun et al. 2022). Modern AI (GNNs, Transformer-PBPK hybrids) further reduces simulation error by ~30%
- **[Figure 2]**: Pipeline schematic with AI assumptions vs. biological reality at each stage

### Required Citations
- [ ] AlphaFold2: Jumper et al., Nature, 2021
- [ ] AlphaFold3: Abramson et al., Nature, 2024
- [ ] AF3 limitations: **Zheng et al., bioRxiv, 2025** [R25] — conformational change failures, kinase selectivity
- [ ] AF3 drug discovery review: Desai et al., Cureus, 2024 [R26]
- [ ] ADMET attrition reduction: Kola & Landis, Nature Reviews Drug Discovery, 2004 (40% in 1991); **Sun et al., Acta Pharmaceutica Sinica B, 2022** (10-15% modern); Waring et al., Nature Reviews Drug Discovery, 2015 (safety replaced PK as dominant cause)
- [ ] ADMET ML review: **Venkataraman et al., ADMET & DMPK, 2025** [R39]
- [ ] Virtual screening pipeline: clawrxiv.io/abs/2604.00430; DruGUI (github.com/junior1p/DruGUI)
- [ ] Computational toxicology: Briefings in Bioinformatics, 2025 (~40% preclinical fail from ADMET, ~30% marketed drugs withdrawn)

### Data Sources
- Gemini: ADMET evolution table (Classical → Early ML → DL → Modern AI)
- Independent survey: Zheng et al. 2025 provides quantitative AF3 failure data
- Clinical experience: pH-dependent solubility, enzymatic hydrolysis, solvation errors (from raw.md)

### Figure 2 Specification — Pipeline Architecture with Assumption Breakdown
- **Type**: Horizontal pipeline flowchart (technical/architectural)
- **Content**: Target ID → Structure Prediction → Virtual Screening → Lead Opt/ADMET → Preclinical → Clinical
- **Annotations**: At each stage, show the **key AI assumption** (top) and the **biological reality** that breaks it (bottom). E.g., Structure Prediction: assumption = "static structure suffices" / reality = "dynamic conformational ensemble"
- **Distinct from Figure 1**: Figure 1 is a data figure (bars/numbers); Figure 2 is a conceptual/architectural figure (assumptions vs. reality)
- **Data needed**: Assumptions compiled from Sections 2-4; no quantitative data required

---

## Section 3. The Chemistry Problem: Where AI Excels (~600 words)

### Key Arguments
- Fair acknowledgment of genuine AI successes — this is NOT an anti-AI polemic
- **Multi-parameter optimization**: AI simultaneously optimizes binding affinity, selectivity, ADMET properties, and synthetic accessibility — something human chemists cannot do at scale
- **Phase I success rate doubling**: 80-90% vs. historical 40-65%. AI-designed molecules are genuinely safer and more drug-like. This is a real, quantifiable achievement
- **Concrete successes**:
  - **Insilico Medicine ISM001-055/Rentosertib** (IPF): Phase IIa positive (GENESIS-IPF trial) — 60 mg QD arm: FVC improvement **+98.4 mL** (95% CI: 10.9-185.9) vs. placebo **-20.3 mL** (95% CI: -116.1 to 75.6). 71 patients across 22 sites in China, 12 weeks, 4 arms. Published in Nature Medicine, June 2025 (Ren et al., DOI: 10.1038/s41591-025-03743-2). First drug with both target AND molecule designed entirely by AI to show Phase IIa efficacy. Caveats: small sample (17-18/arm), short duration, single geography, not powered for pivotal efficacy
  - **Relay Therapeutics RLY-2608**: motion-based drug design for PI3Kα-mutant breast cancer
  - **Zasocitinib/TAK-279**: Nimbus→Takeda $4B acquisition. Phase III LATITUDE (two pivotal trials, n=693 + n=1,108, 21 countries): PASI 75 at week 16: 61.3%/51.9% vs. placebo 5.0%/4.0% vs. apremilast 16.8%/15.9%. Met ALL co-primary and 44 ranked secondary endpoints. NDA expected FY2026. Caveat: used Schrodinger FEP+ (physics-based simulation + ML), not generative AI — represents "AI-assisted optimization" not "AI-originated discovery." Target (TYK2 JH2 domain) and scaffold chosen by human researchers from BMS literature
- **ADMET prediction evolution**: QSAR (1960s-90s) → ECFP/Random Forest (2000s) → GNNs (2010s) → Transformer-PBPK hybrids (2020s+). 30% reduction in simulation error
- **Key point**: "faster to clinic" is real, "more likely to work in clinic" is NOT proven

### Required Citations
- [ ] Jayatunga et al., 2024 [R8] — Phase I success rates
- [ ] ISM001-055 Phase IIa: **Nature Medicine, June 2025** (Ren et al.)
- [ ] Zasocitinib Phase III: Takeda press release 2025; BioSpace report
- [ ] RLY-2608: Relay Therapeutics publications
- [ ] ADMET evolution: Kola & Landis 2004; Waring et al. 2015; Venkataraman et al. 2025 [R39]
- [ ] Multi-parameter optimization: Schneider 2018 (Nature Reviews Drug Discovery)

### Data Sources
- Gemini: ADMET evolution table, Rentosertib mention
- Independent survey: ISM001-055 Phase IIa results (NEW — not in Gemini), Zasocitinib Phase III (NEW), detailed success rate data
- Note: Gemini only mentioned Rentosertib as "in development"; we now have published Phase IIa results

---

## Section 4. The Biology Problem: Where AI Fails (~1200 words) ★ CORE SECTION

### Transition from Section 3 (CRITICAL — address reviewer concern)
> "The achievements described above are genuine and significant. Yet they illuminate a troubling asymmetry: AI has demonstrably improved the *chemistry* of drug discovery — designing molecules that are safer, more selective, and more drug-like — while leaving the *biology* of clinical efficacy essentially untouched. The following section examines this asymmetry in detail, not to diminish AI's contribution, but because the failure modes that drive Phase II attrition have received far less systematic analysis in the literature than the successes. Understanding why excellent molecules fail as medicines is prerequisite to the next generation of AIDD."

### 4.1 The Phase II Efficacy Wall (~400 words)

#### Key Arguments
- **Systematic framing first**: Per Jayatunga et al. 2024 (BCG analysis of 39 AI-native biotechs, 67 drugs in clinical development as of Dec 2023), Phase I success rate = 80-90% (21/24), but Phase II success drops to **~40%** — comparable to the industry norm of **28.9%** (BIO/QLS 2011-2020 report, n=12,728 transitions). Note: AI Phase II (~40%) is technically slightly above BIO baseline (28.9%), but this may reflect selection bias (AI companies choosing validated targets) rather than genuine efficacy improvement. The case studies below are selected as **representative failure modes** from the systematic record, not cherry-picked
- The "Chemistry Problem" solution (Phase I improvement) does NOT transfer to the "Biology Problem" (Phase II efficacy)
- **Root cause**: AI models train on oversimplified data — biochemical assays, 2D cell lines, recombinant protein binding. These capture molecular interactions but NOT systems-level biology (pathway redundancy, compensatory mechanisms, tissue microenvironment)
- **Case study: BenevolentAI BEN-2293** (failure mode: **target hypothesis failure**)
  - Pan-Trk inhibitor for atopic dermatitis
  - Phase IIa: met safety endpoints, confirmed target engagement, but **NO efficacy** vs. placebo (EASI, NRS endpoints)
  - Root cause (our analysis, NOT BenevolentAI's stated explanation): immunological redundancy — JAK/STAT and IL-4/13 compensatory pathways likely rendered Trk inhibition insufficient as monotherapy. BenevolentAI called results "not conclusive" and noted a subgroup signal (BSA ≥20%, PP p=0.0427)
  - AI correctly identified a novel target and designed a safe, well-tolerated molecule; the **biological hypothesis was insufficient for clinical efficacy**
  - Consequence: ~180 staff laid off, multiple programs paused
- **Case study: Exscientia EXS-21546** (failure mode: **therapeutic index miscalculation**)
  - A2A receptor antagonist for solid tumors
  - Phase I: dose-dependent A2A receptor inhibition confirmed
  - Phase Ia: 60 healthy volunteers, confirmed target profile — potency, high selectivity, low brain exposure, dose-dependent CREB phosphorylation inhibition in CD8+ cells
  - Terminated (Oct 2023): Exscientia stated "it will be challenging for [EXS-21546] to reach a suitable therapeutic index" — prolonged high target coverage needed but not achievable at tolerable doses. Peer data (AstraZeneca's AZD4635/imaradenant, also abandoned) further undermined the A2A mechanism
  - AI designed a highly selective molecule but **could not predict the therapeutic window** in humans
- **Case study: Recursion REC-994 / Tempol** (failure mode: **efficacy not sustained / surrogate endpoint misleading**)
  - Cerebral cavernous malformation. SYCAMORE trial: 62 patients, 3 arms (placebo/200mg/400mg), 12 months + open-label extension
  - 12-month MRI: 400mg arm showed -457 mm³ mean lesion volume decrease (50% of patients improved vs. 28% placebo), but p=0.449 (not significant). 200mg no better than placebo
  - Patient-reported outcomes (mRS, PROMIS29, NIHSS): **no differences** between any arm
  - Long-term extension: crossover patients showed NO benefit; 400mg→400mg arm **not sustained**, became indistinguishable from natural history. Initial 12-month signal was likely statistical artifact in underpowered study
  - Recursion halted 4 pipeline programs (May 2025), $464M net loss in 2024
- **Case study: DSP-1181** (failure mode: **undisclosed — speed ≠ viability**)
  - OCD treatment, one of first AI-designed drugs to enter trials
  - Phase I complete with favorable safety, but **discontinued without Phase II**
  - Speed of discovery (12 months vs. typical 4-6 years) ≠ clinical viability
- **Summary table of failure modes**: Each case illustrates a DISTINCT biology problem — target hypothesis, therapeutic window, endpoint validity, unknown — reinforcing that there is no single fix

#### Required Citations
- [ ] Jayatunga et al. 2024 [R8] — Phase II rates
- [ ] BEN-2293: FierceBiotech, Evaluate reports; BenevolentAI disclosures
- [ ] EXS-21546: BusinessWire 2022; Exscientia disclosures
- [ ] REC-994: BioPharma Dive May 2025; Pharmaceutical Technology 2025
- [ ] DSP-1181: Sumitomo Pharma/Exscientia press releases
- [ ] Pathway redundancy in immunology: general immunology references (JAK/STAT review)

### 4.2 The Cascading Valley of Death (~300 words)

#### Key Arguments
- Failures don't happen at one stage — they **cascade** across handoffs
- **Computational → Biochemical**: environment misconfiguration
  - In silico models assume idealized conditions; real assays have pH variation, ionic strength effects, buffer artifacts
  - pH-dependent solubility ignored: a compound predicted soluble at pH 7.4 may precipitate at gastric pH 1.2
  - Enzymatic hydrolysis: ester/amide bonds stable in computation, hydrolyzed by esterases in vivo
  - Solvation effects: implicit solvent models miss specific water-mediated interactions
- **Biochemical → Animal**: ADMET failures and off-target effects
  - Species differences in metabolic enzymes (CYP polymorphisms)
  - Protein binding differences between species
  - Off-target effects not captured by single-target computational screens
- **Animal → Human**: the translational gap
  - Only 5% of animal-tested therapeutic interventions gain regulatory approval (Ineichen et al., PLOS Biology, 2024: umbrella review of 122 systematic reviews, 4,443 animal studies, 367 interventions across 54 diseases)
  - Overall Phase I→approval: 7.9% (BIO 2021); cumulative failure rate ~92%
  - Species-specific immune responses, receptor expression patterns
  - Pharmacogenomic variability in human populations
- Each handoff introduces a **domain-specific knowledge gap** that current AI cannot bridge because it lacks training data from the downstream stage

#### Required Citations
- [ ] Translational failure: **Ineichen et al., PLOS Biology, 2024** (5% approval rate from animal testing; DOI: 10.1371/journal.pbio.3002667) — preferred over "92%" claim which conflates all clinical failure with animal-human translation
- [ ] Overall clinical LOA: **BIO/QLS 2021 report** (Phase I→Approval: 7.9%, n=12,728 transitions, 2011-2020 data)
- [ ] BIO report also shows: programs using patient preselection biomarkers had **2x higher LOA** (25.9% vs 8.4%) — supports our biology-aware AIDD argument
- [ ] CYP polymorphisms and species differences: standard pharmacology references
- [ ] Solvation modeling limitations: Mobley & Gilson 2017
- [ ] Clinical domain pitfalls (pH, enzymatic hydrolysis): first author's clinical experience

#### Figure 3 Specification — Cascading Valley of Death
- **Type**: Cascade/waterfall diagram
- **Content**: Show 1000 initial computational hits narrowing at each handoff stage, with **AI vs. traditional** comparison lanes
- **Annotations**: At each step, show % lost and primary failure cause. Highlight where AI improves attrition (early stages) vs. where it doesn't (later stages)
- **Distinct from Figure 1**: Figure 1 = aggregate Phase I/II/III bars; Figure 3 = granular cascade through ALL stages including pre-clinical
- **Key insight**: cumulative attrition shows why 90% overall failure persists despite AI improvements at individual stages

### 4.3 The Data Quality Crisis (~300 words)

#### Key Arguments
- **Publication bias**: negative results rarely published → AI trains on success-biased data
  - Estimated 50%+ of drug discovery experiments never published
  - Models learn "what works" without learning "what fails and why"
- **"Black box" problem**: GNNs, diffusion models, large transformers lack interpretability
  - Regulatory barrier: FDA increasingly requires explainability (SHAP, attention maps)
  - Clinical trust barrier: physicians won't act on unexplainable predictions
  - Newer AI models did NOT significantly outperform older methods for protein-ligand interaction (Pharmaceuticals 2025, R2)
- **Generative model hallucinations**:
  - Molecules that look good on paper but are unsynthesizable
  - Diffusion models achieve >98.5% atom stability but synthesizability remains unresolved
  - Drug-likeness metrics (Lipinski, QED) are necessary but not sufficient for clinical success
- **Benchmark-to-reality gap**: models optimized for leaderboard metrics (AUROC, RMSE) on clean datasets perform poorly on messy real-world data

#### Required Citations
- [ ] Publication bias in drug discovery: Smaldino & McElreath 2016; AllTrials initiative
- [ ] XAI in drug discovery: **Ding et al., DDDT, 2025** [R37]; **Lavecchia, WIREs, 2025** [R38]
- [ ] Generative model limitations: Tang et al. 2024 [R28]; Biology MDPI 2025 [R30]
- [ ] AI ≠ outperform older methods: Pharmaceuticals 2025 [R2]
- [ ] FDA AI guidance: FDA draft guidance, January 2025

### 4.4 The Protein Dynamics Gap: An Emerging Risk (~250 words)

#### Key Arguments
- **Positioning note**: The Phase II failures above (4.1) stem primarily from target hypothesis errors and translational gaps, NOT from structure prediction failures. The protein dynamics gap is a distinct, **emerging** risk that will become increasingly critical as AIDD tackles harder targets (allosteric modulators, protein-protein interactions, intrinsically disordered proteins). We flag it here as a structural limitation of current pipelines, not as the primary driver of today's Phase II wall
- AlphaFold revolutionized **static** structure prediction; drug discovery requires **dynamics**
- AF3 specific failures (Zheng et al. 2025):
  - Conformational changes >5A RMSD: AF3 fails
  - GPCR antagonist prediction: poor selectivity
  - Kinase selectivity: ROC-AUC near random
  - Functions as a "binary interaction modeler," not a dynamics engine
- **Allosteric pockets**: many drug targets are allosterically regulated; static structures miss these sites entirely
- **Resistance mutations**: e.g., EGFR T790M — AI models trained on wild-type structures fail to predict mutant binding
- **Complex modalities beyond small molecules**: ADCs (antibody-drug conjugates), oligonucleotides (ASOs, siRNAs), LNP delivery — current AI pipelines are predominantly small-molecule-centric
- The protein dynamics gap means AI optimizes binding to the **wrong conformation**

#### Required Citations
- [ ] AF3 limitations: **Zheng et al., bioRxiv, 2025** [R25]
- [ ] AlphaFold cannot handle disordered proteins: Chemistry World 2024 opinion
- [ ] Protein dynamics in drug design: Boehr et al. 2009 (Nature Chemical Biology)
- [ ] EGFR T790M resistance: Yun et al. 2008 (PNAS)
- [ ] Complex modalities: ADC reviews, ASO reviews (Crooke et al.)

---

## Section 5. The Automation Mirage: AI Agents and Self-Driving Labs (~800 words)

### Transition / Framing Paragraph
> Sections 3-4 established that AI excels at molecular optimization (the Chemistry Problem) but fails at predicting clinical efficacy (the Biology Problem). A natural question follows: can **automation** — self-driving labs and AI agents — bridge this gap by accelerating the experimental feedback loop? This section argues that current automation largely **reinforces** the chemistry-biology asymmetry: SDLs automate chemical synthesis and screening (further accelerating chemistry), while the biological validation steps remain manual, low-throughput, and disconnected from the computational pipeline. Automation is powerful, but it automates the part of the problem that AI has already solved.

### 5.1 Self-Driving Labs: Promise and Reality (~300 words)

#### Key Arguments
- DMTA (Design-Make-Test-Analyze) closed-loop cycles are the real value of automation
- **Genuine efficiency gains**:
  - Active learning retrieves ~95% of top-scoring ligands after evaluating just 2-10% of library (Graff et al., Chemical Science, 2021: 94.8% of top-50K from 2.4% of 100M library)
  - Exscientia reports up to 70% timeline reduction and ~67% cost reduction vs. industry benchmarks (self-reported; DSP-1181: 12 months vs. ~5 years, 350 compounds vs. 2,500-5,000 industry average)
  - These are real improvements in the CHEMISTRY domain, though independent peer-reviewed validation is limited
- But SDLs are primarily chemistry automation — synthesis, purification, basic assay. They do NOT automate biology (cell-based assays, animal models, clinical endpoints)
- The SDL literature (Tom et al. 2024, 100-page Chemical Reviews) is overwhelmingly chemistry/materials-focused, not pharma

#### Required Citations
- [ ] SDL definitive review: **Tom et al., Chemical Reviews, 2024** [R16]
- [ ] Active learning: **Graff et al., Chemical Science, 2021** (MolPAL: 94.8% top-50K from 2.4% of 100M library). DOI: 10.1039/D0SC06805E
- [ ] Exscientia stats: AWS case study (self-reported); UKRI report. Note: not peer-reviewed. DSP-1181 timeline from Exscientia press releases
- [ ] SDL for biology: Royal Society Open Science 2025 [R17]

### 5.2 The Fragmentation Challenge (~200 words)

#### Key Arguments
- **The majority of automation integration effort** is spent on proprietary hardware adaptation, not science (Tom et al. 2024: "the most formidable" challenge; no published quantification exists — soften from ">50%")
- Vendor lock-in: each instrument maker has proprietary software, data formats, APIs
- Lab-to-lab reproducibility suffers because workflows are hardware-specific
- **Emerging standards**: SiLA 2 (Standardization in Lab Automation), AnIML (Analytical Information Markup Language) — but adoption is slow
- The "last mile" problem: connecting automated synthesis to biological testing remains manual in most pharma organizations

#### Required Citations
- [ ] Automation fragmentation: Gemini research data (>50% figure)
- [ ] SiLA 2 standard: SiLA consortium publications
- [ ] AnIML standard: ASTM E1947

### 5.3 LLM-based Agents: Hype vs. Capability (~300 words)

#### Key Arguments
- **Capability spectrum** — NOT a binary "works/doesn't work":
  - ✅ **Routine tasks**: literature mining, data summarization, protocol generation, SMILES parsing → LLMs are effective and useful
  - ⚠️ **Semi-structured tasks**: retrosynthesis planning, property prediction → tool-augmented LLMs (ChemCrow) show promise but inconsistent
  - ❌ **Research tasks**: hypothesis generation, experimental design, iterative optimization → poor accuracy, hallucination-prone, non-deterministic
- **Key evidence**:
  - ChemCrow (Bran et al., Nature Machine Intelligence 2024): GPT-4 + 18 chemistry tools. 4 successful syntheses (DEET, 3 organocatalysts, 1 novel chromophore). Expert chemists preferred ChemCrow over base GPT-4 on complex tasks, but evaluation was preference-based, not quantitative success rates
  - Coscientist (Boiko et al., Nature 2023): GPT-4 multi-module agent with Opentrons robotic control. Suzuki/Buchwald-Hartwig coupling optimization over 20 iterations. But: GPT-3.5 "failed in most cases"; full data withheld for safety
  - **ChemToolAgent (arXiv 2024, accepted NAACL 2025)**: tools help on specialized tasks (name conversion: 0%→70%, forward synthesis: 12%→78%) but **hurt on general chemistry reasoning** (MMLU: 80.5%→71%, GPQA: 40.5%→33.8%). Root cause: cognitive overload from role-switching between task comprehension, tool selection, and output interpretation
- The **VC-driven hype cycle**: "agentic AI" as marketing term vs. empirical evidence of capability
  - Industry claims of ">400x cycle time reduction" lack peer-reviewed validation
  - Advocacy pieces (R19) vs. critical assessment are 10:1 ratio in the literature
- Honest assessment: LLM agents are **excellent assistants** for drug discovery teams, **not autonomous researchers**

#### Required Citations
- [ ] ChemCrow: **Bran et al., Nature Machine Intelligence, 2024** [R32]
- [ ] Coscientist: **Boiko et al., Nature, 2023** [R33]
- [ ] ChemToolAgent: **arXiv 2024** [R34] — tools don't consistently help
- [ ] Agentic AI advocacy: arXiv 2510.27130 [R18]; PMC12048886 [R19]
- [ ] Nature Biotech agentic AI: Nature Biotechnology 2026 [R20]
- [ ] LLM primer for drug discovery: Lu et al., CTS, 2025 [R15]

#### Figure 4 Specification — Agent Capability Spectrum
- **Type**: Capability spectrum / heatmap
- **Content**: X-axis = task complexity (routine → semi-structured → research); Y-axis = LLM performance (high → low)
- **Overlay**: Map specific tools (ChemCrow, Coscientist, ChemToolAgent) onto their demonstrated capability zones
- **Key insight**: Agent capability drops sharply as task complexity increases; the zone where drug discovery NEEDS agents (research tasks) is where they perform worst

---

## Section 6. Bridging the Gap: Toward Biology-Aware AIDD (~1100 words)

### Unifying Framework (open Section 6 with this)
> Before diving into individual solutions, present Figure 4's three-layer integration architecture upfront as a conceptual map for the entire section:
> - **Layer 1 — Data** (6.1): Replace 2D cell assays with OoC/organoid systems that generate human-relevant, continuous, multi-dimensional data
> - **Layer 2 — Process** (6.2): Integrate clinical expertise into the AI pipeline via human-in-the-loop workflows, not just as downstream validators but as upstream hypothesis partners
> - **Layer 3 — Algorithm** (6.3): Shift AI from pattern recognition to causal reasoning, with explainability as a design requirement, not an afterthought
> 
> This framing tells the reader: the gap is not a single missing piece but a three-level systems failure requiring coordinated intervention.

### 6.1 Better Preclinical Models (~450 words) [expanded from 350]

#### Key Arguments
- **Organ-on-a-Chip (OoC)**: microfluidic devices that recapitulate human organ physiology
  - Comparison table: 2D cell culture vs. animal models vs. OoC (physiological relevance, throughput, cost, data type, regulatory status)
  - OoC provides **continuous, real-time, human-relevant** data — exactly what AI models need but currently lack
- **FDA Modernization Act 2.0** (Dec 29, 2022; S.5002): removed statutory requirement for animal testing in IND applications. Explicitly permits OoC, iPSC assays, AI/ML methods, in silico trials as alternatives
  - FDA (April 10, 2025): phased plan to make animal studies "the exception rather than the norm within 3-5 years." Initial focus: monoclonal antibodies. Pilot program for NAM-primary submissions
  - **Critical gap to highlight**: FDA Jan 2025 AI draft guidance explicitly EXCLUDES drug discovery from its scope — only covers AI supporting regulatory decisions. No FDA framework currently governs AI in the discovery phase
- **The critical disconnect**: AIDD companies use 2D cell assays; OoC community develops sophisticated platforms but doesn't integrate ML
  - These two communities are **completely siloed** (no review bridges them — our unique contribution)
  - Proposed bridge: OoC data → standardized endpoints → AI training data → improved Phase II prediction
- **Concrete bridging evidence** (OoC data quality + early AI integration):
  - Emulate Liver-Chip (Ewart et al., Communications Medicine, 2022): 870 chips, 27 blinded drugs — 87% sensitivity, 100% specificity for DILI. Identified 87% of drugs that PASSED animal testing but caused DILI in patients. No ML used yet, but demonstrates OoC data quality suitable for ML training
  - DILITracer (Tan et al., Communications Biology, 2025): BEiT-V2 + spatial ViT + LSTM trained on liver organoid images — 82.34% accuracy for ternary DILI classification. Closest proof-of-concept, though uses organoids not true OoC
  - ARPA-H CATALYST / DATAMAP ($21M award, Dec 2025): Inductive Bio + Baylor + Amgen — building in silico liver/heart toxicity models from MPS data. Most ambitious OoC+AI program to date, no results yet
  - **Key gap confirmed**: No published study has completed the full loop (OoC data → ML training → drug prediction → OoC validation). The communities remain siloed
- **Concrete bridging vision**: How OoC data could specifically improve Phase II prediction:
  - OoC toxicity readouts → replace static ADMET predictions with dynamic, human-tissue toxicity curves
  - Multi-organ OoC (liver-kidney-heart, e.g., LivHeart platform: Ferrari et al., Adv Mater Technol, 2023) → capture systemic drug interactions that 2D assays miss
  - OoC + ML closed loop: use OoC dose-response data as training signal for AI models, creating the feedback loop that current pipelines lack
- **Current OoC limitations**: low throughput, high cost, lack of standardization, limited multi-organ connectivity. These are engineering problems with clear trajectories, unlike the fundamental biology problem

#### Required Citations
- [ ] OoC + AI review: Biomicrofluidics 2025 [R21]
- [ ] AI meets organoids/OoC: The Innovation: Life 2024 [R22]
- [ ] OoC regulatory: ScienceDirect 2025 [R23]
- [ ] FDA Modernization Act 2.0: Public Law 117-328 (S.5002, Dec 29, 2022)
- [ ] FDA April 2025 plan: FDA press announcement (April 10, 2025)
- [ ] FDA Jan 2025 AI guidance: "Considerations for the Use of AI..." (Federal Register 2024-31542)
- [ ] Ingber lab OoC work: Huh et al., Science, 2010 (original lung-on-chip)
- [ ] **Ewart et al., Communications Medicine, 2022** — Emulate Liver-Chip validation (870 chips, 87% sensitivity)
- [ ] **Tan et al., Communications Biology, 2025** — DILITracer (organoid + ViT, 82.34% accuracy)
- [ ] **Ferrari et al., Adv Mater Technol, 2023** — LivHeart multi-organ chip
- [ ] **Zhou, Zhong & Lauschke, Expert Opin Drug Metab Toxicol, 2025** — liver models + AI for DILI review
- [ ] ARPA-H DATAMAP/CATALYST program ($21M, Dec 2025) — Inductive Bio press release

#### Table 1 Specification (inline in text)
- **Content**: 2D Cell Culture vs. Animal Models vs. Organ-on-a-Chip
- **Dimensions**: Physiological relevance, Throughput, Cost, Data type, Regulatory status, AI-readiness of data
- Data from Gemini research (OoC comparison table) + additions

### 6.2 Human-AI Collaboration (~300 words)

#### Key Arguments
- **Clinician-in-the-loop**: binding site prediction algorithms identify pockets, but validating therapeutic relevance requires clinical/pharmacological expertise
  - Our first author's clinical experience exemplifies this: seeing patients who fail on computationally "perfect" drugs
- **"Systems strategist" role**: the ideal AI-era drug designer combines:
  - Bayesian reasoning (prior probability of target relevance)
  - Domain adjudication (which computational prediction to trust)
  - Cross-disciplinary judgment (when to override the algorithm)
- **Cross-disciplinary teams**: the current silo structure (CS team → biology team → clinical team, with handoffs) must evolve into integrated teams where biologists, chemists, and AI engineers work concurrently
- **Jacobson's argument extended**: he argues for "human data" integration (R9); we extend to argue for **human expertise** integration at every pipeline stage, not just data

#### Required Citations
- [ ] Jacobson 2025 [R9] — "AI drug revolution needs a revolution"
- [ ] Human-in-the-loop ML: general references
- [ ] Cross-disciplinary drug discovery teams: Schuhmacher et al. 2020 (Nature Reviews Drug Discovery)
- [ ] Bayesian approaches in drug discovery: relevant references

### 6.3 Technical Roadmap (~350 words)

#### Key Arguments
- **From pattern recognition to causal inference**:
  - Current AI = correlative (learns statistical patterns from training data)
  - Needed: causal/reasoning architectures that model biological mechanisms, not just molecular features
  - Causal inference frameworks (Pearl) applied to drug discovery
- **Multi-modal human data integration**:
  - Genomics + transcriptomics + proteomics + metabolomics + clinical outcomes
  - Patient-derived organoids as training data bridges
  - Real-world evidence (EHR, claims data) for post-market AI training
- **Explainable AI (xAI) for regulatory compliance**:
  - SHAP, LIME, attention visualization — not just desirable, becoming mandatory
  - FDA draft guidance (January 2025) signals regulatory expectation
  - xAI builds clinical trust and enables meaningful human oversight
- **Standardized validation beyond benchmarks**:
  - Current problem: models compete on clean benchmark leaderboards (MoleculeNet, PDBbind)
  - Needed: prospective validation on real discovery projects, with wet-lab confirmation
  - Community standards for reporting: what was generated, what was synthesized, what was tested, what worked
- **Digital twins for clinical trial optimization**:
  - Computational modeling of patient populations
  - Currently mostly pilots; few in routine clinical practice (Silva & Vale 2025)
  - Potential to reduce Phase III sample sizes and improve trial design

#### Required Citations
- [ ] Causal inference in drug discovery: Pearl 2009; Feuerriegel et al. 2024
- [ ] Multi-modal data integration: Hasin et al. 2017 (Genome Biology)
- [ ] xAI: Ding et al. 2025 [R37]; Lavecchia 2025 [R38]
- [ ] FDA AI guidance: FDA draft guidance January 2025; Niazi 2026 (J Chemistry, Wiley)
- [ ] Digital twins: Silva & Vale 2025 [R35]; Lancet Digital Health 2025 [R36]
- [ ] Benchmark limitations: Walters & Barzilay 2021

#### Figure 5 Specification — Integration Framework
- **Type**: Integration framework diagram
- **Content**: Three-layer architecture (introduced at Section 6 opening):
  - Layer 1 (Data): OoC + organoids + multi-omics + clinical data → standardized data lake
  - Layer 2 (AI): Causal models + xAI + multi-task learning → biology-aware predictions
  - Layer 3 (Validation): Clinician-in-the-loop + prospective testing + regulatory feedback
- **Key insight**: Closed-loop system where clinical outcomes feed back into AI training, breaking the current one-directional pipeline

---

## Section 7. Outlook & Conclusion (~500 words)

### Key Arguments
- **The "paradox of precision" is a transient phase** — not a fundamental limitation of AI in drug discovery. The tools exist; the integration is missing
- **Key milestones to watch in 2026-2028**:
  - Rentosertib (ISM001-055): Phase IIb/III for IPF — first full AI-designed drug approaching pivotal trials
  - Zasocitinib (TAK-279): NDA expected April 2026 — could be first "AI-assisted" FDA approval
  - RLY-2608: Relay Therapeutics motion-based design in clinical development
  - ~15-20 AI-originated Phase III readouts expected in 2026
- **The AI attribution debate** (address directly): Zasocitinib used physics-based simulation (Schrodinger) + ML, not generative AI. If it gains FDA approval, the community must honestly discuss what "AI-designed" means. A spectrum exists from "AI-assisted" (computational tools in an otherwise traditional workflow) to "AI-native" (target and molecule both identified by AI). This review's thesis — that the Biology Problem persists — holds regardless of where individual drugs fall on this spectrum, because the core issue is not molecular design quality but biological prediction
- **Timeline perspective**: 2-3 year horizon for first AI-designed FDA approval; 5-10 years for AI to meaningfully impact Phase II success rates
- **Hedging for time sensitivity**: Use "as of the time of writing" for all approval status claims. Explicitly note in the conclusion that even if individual AI-assisted drugs gain approval during this review's publication cycle, the systemic Phase II efficacy gap described here would remain — one approval does not solve the Biology Problem
- **The ultimate test**: Can AI solve diseases, not just design molecules? Moving from "molecule-first" to "disease-first" AI
- **Closing**: The gap between benchmarks and bedside is not a failure of AI — it is a failure of integration. The next decade of AIDD must be defined not by faster chemistry but by deeper biology

### Required Citations
- [ ] Rentosertib Phase IIa: Nature Medicine 2025
- [ ] Zasocitinib NDA timeline: Takeda FY2026 guidance
- [ ] Phase III pipeline overview: Axis Intelligence 2026; BIO reports
- [ ] Future of AIDD: Schneider et al. 2020; relevant perspective pieces

#### Figure 6 Specification — Strategic Timeline
- **Type**: Strategic timeline / roadmap
- **Content**: 2020 → 2030 timeline showing:
  - Past milestones: AF2 (2020), first AI drugs in clinic (2021-22), Phase II failures (2023-25), Rentosertib Phase IIa (2025)
  - Expected near-term: Zasocitinib NDA (2026), multiple Phase III readouts (2026-27)
  - Projected: first AI-designed FDA approval (2027-28?), Phase II improvement signal (2028-30?)
  - Parallel track: OoC maturation, causal AI development, regulatory frameworks
- **Key insight**: The "Chemistry Problem" was solved 2020-2025; the "Biology Problem" is the 2025-2030 challenge

---

## Cross-Cutting Elements

### Competitor Positioning Strategy

| Closest Competitor | Their Contribution | Our Extension |
|---|---|---|
| Jayatunga et al. 2024 [R8] | Quantified Phase I/II gap | We explain WHY (cascading failures, biology problem) |
| Jacobson 2025 [R9] | Short perspective: need "human data" | We provide systematic analysis + concrete solutions (OoC, clinician-in-the-loop, causal AI) |
| Tom et al. 2024 [R16] | Definitive SDL review (chemistry/materials) | We focus on pharma-specific SDL challenges and agent limitations |
| OoC reviews [R21-23] | Engineering advances in isolation | We bridge OoC ↔ AIDD for the first time |
| Nature Medicine 2024 [R4] | Positive AI applications review | We provide the critical counterpart: where and why it fails |

### Outstanding Verification Tasks
- [ ] **Verify no missed direct competitors**: Search Annual Review of Pharmacology and Toxicology, Medicinal Chemistry Reviews (ACS), and Drug Discovery Today Reviews for 2025-2026 reviews specifically analyzing Phase II failure causes for AI drugs
- [ ] **$420B VC scope**: Verify with PitchBook/CB Insights whether this is AIDD-specific or broader AI+health
- [ ] **Systematic Phase II statistics**: Extract from Jayatunga 2024 the exact N of AI-native Phase II trials and their outcomes to frame case study selection

### Key Quotes to Consider Including
- "AI has really let us all down in the last decade when it comes to drug discovery" — unnamed CEO, Drug Target Review 2025
- "Newer AI models did NOT significantly outperform older methods for protein-ligand interaction prediction" — Pharmaceuticals 2025
- "AI's clinical impact remains limited, with many systems still confined to retrospective validations" — Nature Medicine 2024

### Estimated Reference Count
- Section 1: ~15 refs
- Section 2: ~20 refs
- Section 3: ~12 refs
- Section 4: ~35 refs
- Section 5: ~20 refs
- Section 6: ~25 refs
- Section 7: ~8 refs
- **Total: ~135 references** (within 100-200 target)

---

## Figure Summary (6 figures + 1 table)

| # | Title | Type | Section | Purpose |
|---|---|---|---|---|
| Fig 1 | The Precision Paradox | Paired bar chart | 1 or 4.1 | Hook: AI doubles Phase I but not Phase II |
| Fig 2 | Pipeline Assumptions vs. Reality | Flowchart | 2 | Architectural overview of where assumptions break |
| Fig 3 | Cascading Valley of Death | Waterfall diagram | 4.2 | Quantitative attrition across handoffs (AI vs. traditional) |
| Fig 4 | Agent Capability Spectrum | Heatmap | 5.3 | Honest assessment of LLM agent performance by task type |
| Fig 5 | Integration Framework | 3-layer diagram | 6 (opening) | Proposed solution architecture (Data/Process/Algorithm) |
| Fig 6 | Strategic Roadmap | Timeline | 7 | Past milestones → projected future |
| Table 1 | Preclinical Model Comparison | Comparison table | 6.1 | 2D vs. Animal vs. OoC |
