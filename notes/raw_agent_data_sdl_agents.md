# Raw Agent Data: SDL, AI Agents, FDA Regulatory

> Source: Agent "Deep-read SDL and agent papers" (2026-04-03)
> Status: Verified

---

## Tom et al., Chemical Reviews, 2024 — Self-Driving Labs

**Full citation**: Tom G, Schmid SP, Baird SG, et al. "Self-Driving Laboratories for Chemistry and Materials Science." *Chemical Reviews*, 2024, 124(16), 9633-9732. DOI: 10.1021/acs.chemrev.4c00055

### SDL Efficiency
- "Up to 6x acceleration and up to 23x performance enhancement" vs. traditional workflows
- Novartis MicroCycle: autonomously synthesizes, purifies, assays, selects next compounds
- Argonne Polybot: 90,000 material combinations in weeks vs. months

### Pharma vs. Materials
- No census or breakdown provided
- Pharma is "a key driver" but vast majority of published SDL examples = materials science
- MicroCycle (Novartis, 2024) = best-in-class pharma example

### Active Learning Hit Rate
- "90% from 10%" NOT directly in Tom et al.
- Supported by: Graff et al., Chemical Science, 2021 (MolPAL): 94.8% of top-50K from 2.4% of 100M library (UCB acquisition); 89.3% with greedy
- On 2.1M library: 97.6% of top-1K from 2.4%; 93.3% from 1.2%
- JCTC 2024: "up to 90% of top-1% hits after docking just 10%" using linear regression
- Cite Graff et al. 2021 (DOI: 10.1039/D0SC06805E), not Tom et al.

### Hardware Integration
- "The most formidable" challenge
- "Adaptation of an instrument...requires significant time investment to write custom code"
- "Few manufacturers develop their software to consider self-driving laboratories"
- **">50%" figure NOT quantified** in the review — soften to qualitative

### SiLA 2 / AnIML
- SiLA 2: "communication protocol aiming to replicate ROS for chemical devices"
- AnIML: "provides vendor-neutral analytical/biological data representations, audit trails, regulatory metadata"
- Combination = "promising direction"
- Adoption "is not standardized across the chemistry community" — no quantitative stats

### Pharma-Specific Challenges
- Inert atmosphere synthesis uniquely hard to automate
- Separate liquid handlers for organic vs. aqueous biochemical
- Hit-to-lead optimization = "major bottleneck"
- De novo hit prediction = "lofty long-term goal" with "limited success"

---

## ChemCrow — Bran et al., Nature Machine Intelligence, 2024

**Full citation**: Bran AM, Cox S, Schilter O, Baldassari C, White AD, Schwaller P. "Augmenting large language models with chemistry tools." *Nature Machine Intelligence*, 2024, 6, 525-535. DOI: 10.1038/s42256-024-00832-8

### The 18 Tools

| # | Category | Tool | Function |
|---|----------|------|----------|
| 1 | General | WebSearch | Google search |
| 2 | General | LitSearch | Scientific literature via embeddings |
| 3 | General | Python REPL | Code execution |
| 4 | General | Human | User input/permission |
| 5 | Molecule | Name2SMILES | Name/CAS → SMILES |
| 6 | Molecule | SMILES2Price | Purchasability/pricing |
| 7 | Molecule | Name2CAS | CAS numbers |
| 8 | Molecule | Similarity | Tanimoto similarity |
| 9 | Molecule | ModifyMol | Local chemical space generation |
| 10 | Molecule | PatentCheck | Patent status (bloom filters) |
| 11 | Molecule | FuncGroups | Functional group ID |
| 12 | Reaction | NameRXN | Named reaction classification |
| 13 | Reaction | ReactionPredict | Transformer product prediction |
| 14 | Reaction | ReactionPlanner | Multi-step retrosynthesis |
| 15 | Reaction | ReactionExecute | Robotic execution |
| 16 | Safety | ControlledChemicalCheck | CWC/Australia Group lists |
| 17 | Safety | ExplosiveCheck | GHS explosive ID |
| 18 | Safety | SafetySummary | PubChem safety data |

### Tasks Demonstrated
1. DEET synthesis: autonomous, successful
2. Three organocatalyst syntheses (Schreiner's thiourea, Ricci's squaramide, Takemoto's): all successful
3. Novel chromophore: targeted 369 nm absorption; measured 336 nm (~9% variance)

### Performance
- "Four syntheses yielded the anticipated compounds successfully"
- Expert chemists "strong preference" for ChemCrow over base GPT-4 on complex tasks
- GPT-4 alone better only on simpler memorization tasks
- No quantitative success rate percentages; evaluation = expert preference

### Limitations Acknowledged
1. Quality depends on tools
2. Synthesis planning limited by underlying engine
3. "Inaccurate or incomplete reasoning due to lack of sufficient chemistry knowledge"
4. "Selected evaluation tasks are limited"
5. "Lack of reproducibility...under current API-based approach" with closed-source models

---

## Coscientist — Boiko et al., Nature, 2023

**Full citation**: Boiko DA, MacKnight R, Kline B, Gomes G. "Autonomous chemical research with large language models." *Nature*, 2023, 624, 570-578. DOI: 10.1038/s41586-023-06792-0

### Architecture
- Primary: GPT-4 (Planner)
- Multiple instances: GPT-4 for Planner + Web Searcher; GPT-3.5-turbo tested
- Embedding: OpenAI ada model
- Four modules: GOOGLE, PYTHON, DOCUMENTATION, EXPERIMENT

### Six Tasks
1. Chemical synthesis planning (web search): 7 compounds; max scores 4/7; ibuprofen min acceptable
2. Documentation navigation: Opentrons OT-2 API, ECL SLL functions
3. Cloud lab control: valid ECL SLL code for HPLC
4. Robotic liquid handler: plate-based drawing on Opentrons OT-2
5. Integrated multi-module: liquid handling + UV-Vis spectroscopy (one guiding prompt needed)
6. Reaction optimization: Suzuki + Buchwald-Hartwig coupling, 20 iterations, GC-MS confirmed

### Error Rates
- GPT-3.5 "performed significantly worse" than GPT-4
- Falcon 40B "failed in most cases"
- All non-browsing models "incorrectly synthesized ibuprofen"
- Initial Suzuki attempt: wrong heater-shaker method name; self-corrected via docs
- HPLC: air bubbles alongside analyte
- JSON formatting failures prevented GPT-3.5 from completing optimization iterations
- Specific yields NOT reported

### Reproducibility
- GitHub: github.com/gomesgroup/coscientist
- Full data/prompts WITHHELD "because of safety concerns"

---

## ChemToolAgent — arXiv:2411.07228 (NAACL 2025)

**Full citation**: OSU-NLP-Group. "ChemToolAgent: The Impact of Tools on Language Agents for Chemistry Problem Solving." arXiv:2411.07228, 2024. Accepted NAACL 2025 Findings.

### Key Finding
"While ChemToolAgent substantially outperforms ChemCrow on all chemistry tasks, it does not consistently outperform the base LLMs without tools."

### Where Tools HELPED (SMolInstruct)
- Name Conversion: ChemToolAgent (GPT) 70% vs. base GPT-4o 0%
- Forward Synthesis: 78% vs. base 12%

### Where Tools HURT
- MMLU-Chemistry: base 80.5% vs. agent 71.0%
- SciBench-Chemistry: base 60.7% vs. agent 60.1%
- GPQA-Chemistry: base 40.5% vs. agent 33.8%

### Benchmarks
1. SMolInstruct: 700 samples, 14 molecule/reaction tasks
2. MMLU-Chemistry: 70 verified questions
3. SciBench-Chemistry: 223 college-level calculations
4. GPQA-Chemistry: 93 graduate-level expert questions

### Error Analysis
- SMolInstruct: >99% tool errors (neural network tools with inherent inaccuracy)
- MMLU-Chemistry: >90% reasoning errors (wrong knowledge, oversight, algebraic mistakes)

### Root Causes
1. **Cognitive overload**: "backbone LLM tasked with multiple responsibilities...frequent role-switching"
2. **Conflicting information**: tool outputs vs. internal model knowledge

---

## Exscientia Automated Lab Stats

### "70% timeline, 80% cost" Claims
- **Source**: AWS case study — "accelerated drug design by up to 70% while decreasing capital cost by 80%, compared with industry benchmarks"
- UKRI source: "slashed up to two-thirds off the cost" (67%, not 80%)
- DSP-1181: 12 months vs. ~5 years; 350 compounds vs. 2,500-5,000
- Exscientia: 10x fewer compounds than industry average
- ⚠️ Self-reported, no peer-reviewed validation. AWS = marketing case study

---

## FDA Regulatory Landscape

### FDA Modernization Act 2.0 (December 29, 2022)
- S.5002, 117th Congress, signed by Biden
- Removed statutory requirement for animal testing in IND applications
- Permits: cell-based assays (iPSCs, organoids, OoC), AI/ML methods, in silico trials, biomarkers
- Does NOT ban animal testing — removes the requirement

### FDA April 2025 Announcement (April 10, 2025)
- Phase out animal testing for mAbs and other drugs
- "Reduced, refined, or potentially replaced" using NAMs
- Timeline: animal studies = "exception rather than norm within 3-5 years"
- Phased: immediate for early IND; initial focus mAbs; then biologics; then NCEs
- Pilot program for NAM-primary submissions
- NAMs specified: OoC, AI computational toxicity, advanced in vitro, in silico, microdosing
- Strong NAM data → streamlined review

### FDA January 2025 Draft Guidance (January 6, 2025)
- Title: "Considerations for the Use of AI To Support Regulatory Decision-Making for Drug and Biological Products"
- 7-step credibility framework:
  1. Define question of interest
  2. Define Context of Use (COU)
  3. Assess AI model risk
  4. Develop credibility plan
  5. Execute plan
  6. Document results/deviations
  7. Determine model adequacy
- Risk-based tiers: Low (basic docs), Medium (hold-out testing, bias), High (prospective validation, external datasets, lifecycle monitoring)
- **CRITICAL**: Explicitly EXCLUDES drug discovery. Only covers AI supporting regulatory decisions on safety/efficacy/quality
- Comment deadline: April 7, 2025
