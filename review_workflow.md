# AI Drug Discovery Review - Writing Workflow

> Target: Nature sub-journal (Nature Reviews Drug Discovery / Nature Machine Intelligence)
> Type: **Editor-invited Review** (focus on content quality, not submission strategy)
> Working dir: `C:\Users\30670\Desktop\szpku\aidd\`

---

## Core Thesis

**AI-driven drug discovery has solved the "Chemistry Problem" but not the "Biology Problem."** Despite >$420B VC investment and revolutionary Phase I success rates (80-90%), Phase II efficacy rates remain at industry norms (~28-40%), and as of early 2025, no AI-designed drug has achieved full FDA approval. This review systematically dissects the cascading failure modes across the AIDD pipeline and charts a path forward.

## Key Differentiators (vs. existing reviews)

1. **Clinical insider perspective** — First author has hospital director + clinical trial center director experience
2. **Cascading failure analysis** — Not just "where AI fails" but quantitative attrition at each handoff
3. **The "Chemistry vs. Biology" framing** — Clean dichotomy that unifies disparate failure modes
4. **Honest AI Agent assessment** — No hype, empirical evaluation of lab automation accuracy
5. **Constructive roadmap** — Not just criticism; actionable integration strategies

---

## Key Data Inventory (from Gemini Deep Research)

### Market & Investment
- Global AI drug discovery market: USD 2.9B (2025) → 12.5B (2035), CAGR 15.7%
- Total VC disclosed funding: **~$17B AIDD-specific since 2019** (PitchBook; note: Gemini's "$420B" figure is all-biotech, NOT AIDD-specific); 2024 rebound to $3.8B
- ML for drug design: expected 45% market share by 2025
- Geographic concentration: CA + MA = ~60% of US deals (2024)
- Mega-rounds: Xaira ($1B Series A), Isomorphic Labs ($600M)
- GLP-1 licensing deals: $18.2B in H1 2025

### Clinical Success Rates

| Phase | Traditional (BIO 2021) | AI-Native (Jayatunga 2024) | Primary Attrition Cause |
|-------|-----------|------------------------|------------------------|
| Phase I (Safety) | 52.0% | 80-90% (21/24) | Bioavailability, PK/PD, Toxicity |
| Phase II (Efficacy) | 28.9% | ~40% (small N) | Lack of Efficacy, Redundant Pathways |
| Phase III (Pivotal) | 57.8% | Insufficient data | Endpoints, Population Diversity |
| Cumulative (I→Approval) | 7.9% | TBD | Multi-factorial |

**Note**: AI Phase II ~40% vs. traditional 28.9% may reflect target selection bias (AI companies choosing validated targets), not genuine efficacy improvement. N for AI Phase II is very small.

**Key insight**: AI doubles Phase I success but hits the same Phase II wall → the "Biology Problem"

### High-Profile Failures (Case Studies)
1. **BenevolentAI BEN-2293** — Pan-Trk inhibitor for atopic dermatitis. Phase IIa: met safety, hit target, but NO efficacy vs placebo. Root cause: immunological redundancy (JAK/STAT, IL-4/13 compensatory pathways)
2. **Exscientia EXS-21546** — A2A receptor antagonist for solid tumors. Wound down: models showed therapeutic index insufficient for clinical benefit in humans

### ADMET Evolution (for historical perspective)

| Era | Technology | Impact |
|-----|-----------|--------|
| Classical (1960s-90s) | Ligand-based, 3D-QSAR | 40% clinical losses from ADMET |
| Early ML (2000s) | ECFP fingerprints, Random Forest | ADMET losses → 11% |
| Deep Learning (2010s) | GNNs | Complex non-linear ADME modeling |
| Modern AI (2020s+) | Transformers (ChemBERTa), PBPK-GNN | 30% reduction in simulation error |

### Self-Driving Labs (SDLs)
- Active learning retrieves ~90% top-tier hits after evaluating just 10% of library (14-fold reduction)
- Exscientia automated lab: 70% timeline reduction, 80% cost reduction
- Key bottleneck: >50% of automation personnel time on proprietary hardware integration
- Standards emerging: SiLA 2, AnIML

### Organ-on-a-Chip (OoC)

| Feature | 2D Cell Culture | Animal Models | Organ-on-a-Chip |
|---------|---------------|--------------|----------------|
| Physiological Relevance | Low | Moderate (species diff) | High |
| Throughput | Very High | Low | Low-Moderate |
| Cost | Inexpensive | Cost-prohibitive at scale | Moderate-High |
| Data Type | Sparse Endpoint | Holistic but species-biased | Continuous, Real-time |
| Regulatory | Standard for early screening | Historically required; shifting | Gaining recognition (FDA Modernization Act) |

### Regulatory
- FDA (April 2025): phased plan to prioritize non-animal testing (OoCs, computational models)
- xAI requirement: SHAP and similar frameworks for transparency
- "Digital twins" for clinical trial optimization gaining regulatory interest

---

## Proposed Outline (Updated)

```
1. Introduction (~800 words)
   - The promise: from serendipity to "drug engineering"
   - Investment landscape: $420B VC, mega-rounds, geographic concentration
   - The paradox: revolutionary speed + persistent 90% failure rate
   - No FDA-approved AI-designed drug as of early 2025
   - Scope and structure of this review

2. The AIDD Pipeline: Architecture and Assumptions (~800 words)
   - Target identification & validation
   - Protein structure prediction (AlphaFold2/3 era: static snapshots vs dynamic reality)
   - Virtual screening & molecular docking
   - Binding site prediction: why algorithms alone cannot validate
   - Lead optimization & the ADMET revolution (40% → 11% attrition)
   - [Figure 1: Pipeline schematic with failure rates at each handoff]

3. The Chemistry Problem: Where AI Excels (~600 words)
   - Multi-parameter optimization: affinity, selectivity, ADMET, synthesizability
   - Phase I success rate doubling (80-90% vs 40-65%)
   - Concrete successes: Insilico Medicine (Rentosertib), Relay Therapeutics (RLY-2608)
   - ADMET prediction evolution: from QSAR to Transformer-PBPK hybrids
   - Why "faster to clinic" is real but insufficient

4. The Biology Problem: Where AI Fails (~1200 words) ★ CORE SECTION
   4.1 The Phase II Efficacy Wall
       - AI-native Phase II rates = industry norms (28-40%)
       - Case study: BEN-2293 (redundancy problem in immunology)
       - Case study: EXS-21546 (therapeutic index miscalculation)
       - Root cause: training on oversimplified data (cell lines, biochemical assays)
   4.2 The Cascading Valley of Death
       - Computational → Biochemical: environment misconfiguration (pH, enzymatic hydrolysis, solvation)
       - Biochemical → Animal: ADMET failures, off-target effects
       - Animal → Human: species-specific translational gap
       - [Figure 2: Cascading attrition rates with quantitative data]
   4.3 The Data Quality Crisis
       - Publication bias (negative results hidden)
       - "Black box" problem: GNNs, diffusion models lack interpretability
       - Generative model hallucinations: synthesizability, drug-likeness issues
   4.4 Protein Dynamics Gap
       - AlphaFold = static snapshots; biology = dynamic conformational ensemble
       - Allosteric pockets, resistance mutations (e.g., T790M in EGFR)
       - Complex modalities: ADCs, oligonucleotides, LNPs

5. The Automation Mirage: AI Agents and Self-Driving Labs (~800 words)
   5.1 Self-Driving Labs: promise and reality
       - DMTA closed-loop cycles
       - Active learning: 90% hits from 10% library evaluation
       - Real efficiency gains (Exscientia: 70% timeline, 80% cost reduction)
   5.2 The Fragmentation Challenge
       - >50% automation time on hardware integration
       - Vendor lock-in, lack of interoperability
       - SiLA 2, AnIML as emerging standards
   5.3 LLM-based Agents: hype vs capability
       - Routine tasks: literature mining, data summarization → effective
       - Research tasks: iterative, non-deterministic → poor accuracy
       - The VC-driven hype cycle vs empirical evidence
       - [Figure 3: Agent capability spectrum — routine vs research tasks]

6. Bridging the Gap: Toward Biology-Aware AIDD (~1000 words)
   6.1 Better Preclinical Models
       - Organ-on-a-Chip: human physiology in miniature
       - OoC vs 2D culture vs animal models (comparison table)
       - FDA Modernization Act: regulatory shift toward non-animal testing
       - Current disconnect: AI biotechs use 2D; OoC ignores ML
   6.2 Human-AI Collaboration
       - Clinician-in-the-loop for binding site validation
       - "Systems strategist" role: Bayesian thinking + domain adjudication
       - Cross-disciplinary teams: biologists + chemists + AI engineers
   6.3 Technical Roadmap
       - From pattern recognition to causal/reasoning architectures
       - Multi-modal human data integration (genomics, transcriptomics, organoids)
       - xAI for regulatory compliance (SHAP, attention visualization)
       - Standardized validation: beyond benchmark leaderboards
       - [Figure 4: Proposed integration framework — AI + OoC + clinical feedback loop]

7. Outlook & Conclusion (~500 words)
   - The "paradox of precision" is a transient phase
   - Key milestones to watch: Rentosertib, RLY-2608 pivotal trials
   - Timeline perspective: 2-5 year horizon for first AI-designed FDA approval
   - The ultimate test: can AI solve diseases, not just design molecules?
   - [Figure 5: Strategic roadmap timeline]
```

**Estimated total: ~5,700 words + 5 figures** (within 5,000-8,000 target)

---

## Phase 1: Scoping & Outline (Week 1) — CURRENT

### Tasks

- [x] **1.1 Survey existing reviews** — Gemini deep research + independent cross-validation (39 reviews catalogued in `existing_reviews.md`)
- [x] **1.2 Define unique angle** — "Chemistry Problem vs Biology Problem" framing confirmed
- [x] **1.3 Finalize outline** — `outline.md` generated with per-section key points, ~135 citations mapped, 5 figure specs, competitor positioning
- [ ] **1.4 Confirm editor requirements** — Check with editor on: word limit, figure count, structured abstract, reference style

### Deliverables
- `outline.md` — ✅ Finalized section outline with mapped data sources
- `existing_reviews.md` — ✅ 39 reviews across 7 categories with gap analysis

### Key Findings from Independent Survey (cross-validated with Gemini)
- **New case studies** not in Gemini: Recursion REC-994 Phase II failure (May 2025), DSP-1181 discontinued, Zasocitinib/TAK-279 Phase III success ($4B Takeda acquisition)
- **Updated data**: ISM001-055/Rentosertib Phase IIa positive results published in Nature Medicine (June 2025) — Gemini only had "in development"
- **Key competitor papers**: Jayatunga et al. 2024 (Phase I/II gap quantification), Jacobson 2025 (closest to our thesis)
- **ChemToolAgent (arXiv 2024)**: tools don't consistently improve LLM chemistry reasoning — supports our honest agent assessment
- **173+ AI drug programs** in clinical development (Axis Intelligence 2026)

---

## Phase 2: Literature Research (Week 2-3)

### Goal
Fill citation gaps — Gemini research provides the framework, but we need primary sources.

### Tasks

- [x] **2.1 Verify and source Gemini claims** — 5 parallel agents verified all key data points. Major corrections: $420B→$17B AIDD-specific; ADMET 11%→10-15%; Rentosertib placebo -62.3→-20.3 mL; BEN-2293 pathway argument = our analysis not company's; 92% animal failure → use Ineichen 2024 (95%)
- [x] **2.2 Deep-read key papers** — Notes created for: Jayatunga 2024, BIO/QLS 2021, Kola & Landis 2004, BEN-2293, EXS-21546, REC-994, Rentosertib, Zasocitinib, ChemCrow, Coscientist, ChemToolAgent, Tom 2024 (SDL), Jacobson 2025, OoC+AI studies, XAI reviews, FDA guidance. Raw agent data preserved in `notes/raw_agent_data_*.md`
- [x] **2.3 Collect missing data for figures** — 6 figure data specs in `figures_data/`: Fig 1 (precision paradox bars), Fig 2 (pipeline assumptions), Fig 3 (cascade waterfall), Fig 4 (agent capability), Fig 5 (integration framework), Fig 6 (timeline)
- [x] **2.4 Build references.bib** — Initial ~45 entries covering all sections. Will expand to 100-150 during drafting

### Deliverables
- `notes/` — ✅ 6 per-paper annotations + 4 raw agent data files
- `references.bib` — ✅ Initial bibliography (~45 entries, expandable)
- `figures_data/` — ✅ 6 figure data specification files

---

## Phase 3: Drafting (Week 3-5)

### Goal
Write the first complete draft, section by section.

### Tasks

- [ ] **3.1 Write Section 1 (Introduction)** — Hook with the $420B investment paradox + zero FDA approvals. Set up "Chemistry vs Biology" framing.
- [ ] **3.2 Write Section 2 (Pipeline)** — Technical overview accessible to Nature audience. Reference clawrxiv pipeline, DruGUI.
- [ ] **3.3 Write Section 3 (Chemistry Problem — Success)** — Fair acknowledgment of genuine progress. ADMET evolution as success story.
- [ ] **3.4 Write Section 4 (Biology Problem — Failure)** ★ — The core contribution. BEN-2293 and EXS-21546 case studies. pH/enzymatic hydrolysis errors from clinical experience. Cascading quantitative data.
- [ ] **3.5 Write Section 5 (Automation Mirage)** — SDLs vs LLM agents. Empirical evidence of low accuracy on research tasks. VC hype cycle.
- [ ] **3.6 Write Section 6 (Bridging the Gap)** — Constructive: OoC integration, clinician-in-the-loop, causal architectures, xAI.
- [ ] **3.7 Write Section 7 (Outlook)** — Concise, forward-looking. Key milestones to watch.
- [ ] **3.8 Create figures** — 5 figures (see outline for specifications)

### Writing Guidelines
- Active voice, concise sentences, Nature-level English
- Every claim → citation
- Critical but constructive tone
- Quantitative > qualitative ("28% success rate" not "most drugs fail")
- Distinguish: in silico / in vitro / in vivo / clinical

### Deliverables
- `draft_v1.md` — Complete first draft
- `figures/` — Figure drafts

---

## Phase 4: Revision & Polish (Week 5-6)

### Tasks

- [ ] **4.1 Self-review** — Logical flow, argument consistency, missing citations, redundancy
- [ ] **4.2 Domain expert review** — Send to clinicians/biochemists for factual accuracy
- [ ] **4.3 Language polish** — Nature-level English, active voice, no filler
- [ ] **4.4 Figure refinement** — Publication-quality (BioRender for schematics, matplotlib for data)
- [ ] **4.5 Citation verification** — Cross-check all references, verify DOIs

### Deliverables
- `draft_v2.md` — Revised draft
- `figures/` — Publication-ready figures

---

## Phase 5: Submission Prep (Week 6-7)

### Tasks

- [ ] **5.1 Final proofread**
- [ ] **5.2 Format to journal spec** — Abstract, references, figures, supplementary
- [ ] **5.3 Write cover letter** (if needed for invited submission)
- [ ] **5.4 Submit**

---

## How Claude Code Helps at Each Phase

| Phase | CC Capability | How |
|-------|--------------|-----|
| 1 Scoping | Agent + memory | Integrate Gemini research into outline |
| 2 Research | WebSearch + WebFetch + PDF Read | Verify claims, find primary sources |
| 2 Research | Parallel Agents | Simultaneously verify 5+ data categories |
| 3 Drafting | Write + Edit + skills | `/draft-section` for structured writing |
| 3 Figures | Bash (Python/matplotlib) | `/figure-gen` for data-driven figures |
| 4 Revision | Read + Edit | `/citation-check` for verification |
| 5 Submission | Write | Cover letter, formatting |

---

## Directory Structure

```
C:\Users\30670\Desktop\szpku\aidd\
├── raw.md                    # Original raw ideas
├── gemini_deep_research.md   # Gemini deep research report (key data source)
├── review_workflow.md        # This workflow document
├── outline.md                # [Phase 1] Detailed outline with data mapping
├── existing_reviews.md       # [Phase 1] Review landscape analysis
├── papers/                   # [Phase 2] Downloaded PDFs
├── notes/                    # [Phase 2] Per-paper annotations
├── references.bib            # [Phase 2] Bibliography
├── figures_data/             # [Phase 2] Raw data for figures
├── draft_v1.md               # [Phase 3] First draft
├── figures/                  # [Phase 3-4] Figures + generation scripts
├── draft_v2.md               # [Phase 4] Revised draft
└── cover_letter.md           # [Phase 5] Cover letter
```
