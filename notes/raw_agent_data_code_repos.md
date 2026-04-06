# Raw Agent Data: Code Repositories and Tools

> Source: Agent "Research code repos and tools" (2026-04-03)
> Status: Verified

---

## 1. DruGUI / clawrxiv Pipeline

**Purpose**: End-to-end, agent-executable structure-based virtual screening (SBVS) pipeline. Designed to be run autonomously by AI agents (e.g., Claude) rather than by human operators.

**Key Capabilities — 8 Stages:**
1. Environment setup with pinned dependencies
2. Target protein preparation (PDB download, water removal, protonation via PDBFixer/OpenMM)
3. Ligand preparation (SMILES to 3D via RDKit)
4. Molecular docking (AutoDock Vina)
5. ADMET property prediction
6. Drug-likeness filtering (Lipinski's Rule of Five + PAINS)
7. Synthesis accessibility scoring
8. Final composite ranking and reporting

**Architecture**: Python 3.9+, Conda. Integrates RDKit, AutoDock Vina, PDBFixer, OpenMM, scikit-learn. Packaged as `SKILL.md` for agent execution.

**Performance**: EGFR test case (PDB: 6JX0) — 53 molecules in 28 seconds. Top candidate AZD3759 scored 0.926 composite. Bit-identical reproducibility.

**Popularity**: 4 stars, 4 forks (very new, April 2026). MIT license. Submitted to Claw4S Conference 2026.

**Limitations**:
- No explicit scalability testing
- ADMET uses basic scikit-learn models, not clinically validated
- No wet-lab validation
- Covers only virtual screening — no lead optimization, synthesis planning, or clinical translation

**Review relevance**: Prime example of "agent-executable skill" paradigm. Demonstrates automation trend but illustrates our thesis: pipeline stops at computational scoring with NO bridge to experimental validation. ADMET component uses simple ML models rather than rigorously validated predictors.

---

## 2. ADMET-AI (Swanson et al., Bioinformatics 2024)

**Purpose**: ML platform for large-scale ADMET property prediction using graph neural networks.

**Key Capabilities**:
- Predicts **41 ADMET properties** from TDC: 10 regression + 31 classification
- Endpoints: hERG toxicity, BBB penetration, solubility, oral bioavailability, general toxicity, etc.
- Contextualized predictions vs. 2,579 approved drugs (DrugBank v5.1.10), filterable by ATC codes
- Available as web server (admet.ai), Python API, CLI tool

**Architecture**:
- v1: Chemprop-RDKit (message-passing GNN + 200 RDKit features)
- v2: Chemprop v2 (without RDKit fingerprints), faster
- GPU-accelerated: 1M molecules in 3.1 hours (32 CPU + GPU)

**Benchmark Performance**:
- Highest average rank on TDC ADMET Benchmark Group leaderboard
- R² > 0.6 for **only 5/10** regression tasks
- AUROC > 0.85 for 20/31 classification tasks
- 45% faster than next-fastest public ADMET web tool

**Popularity**: 286 stars, 76 forks. MIT license. Last release Feb 2026 (v2.0.1).

**Limitations**:
- TDC datasets have known biases and limited chemical diversity
- **R² > 0.6 on only half of regression tasks** = half ADMET predictions unreliable
- No prospective clinical ADMET validation
- v1→v2 trades interpretability for speed

**Review relevance**: Best-in-class ADMET tool, but benchmark numbers expose our argument: even top-ranked model achieves only moderate performance on many endpoints. Half of ADMET predictions are unreliable. Supports thesis about gap between computational ADMET and real PK outcomes.

---

## 3. ChemCrow (Bran et al., NMI 2024)

**Purpose**: LLM-based chemistry agent augmenting GPT-4 with 18 tools.

**18 Tools in 5 Categories**:

| # | Category | Tool | Function |
|---|----------|------|----------|
| 1-4 | General | WebSearch, LitSearch, Python REPL, Human | Search, code, user interaction |
| 5-11 | Molecule | Name2SMILES, SMILES2Price, Name2CAS, Similarity, ModifyMol, PatentCheck, FuncGroups, SMILES2Weight | Molecular operations |
| 12-14 | Safety | ControlledChemicalCheck, ExplosiveCheck, SafetySummary | Safety screening |
| 15-18 | Reaction | NameRXN, ReactionPredict, ReactionPlanner, ReactionExecute | Synthesis planning/execution |

**Evaluation**: Expert chemists strongly preferred ChemCrow over bare GPT-4 on complex tasks. **Critical finding**: EvaluatorGPT paradoxically preferred GPT-4's more fluent but factually incorrect responses — LLM-as-judge unreliable in scientific domains.

**Popularity**: 893 stars, 140 forks. LangChain + GPT-4.

**Code availability**: Public repo explicitly states "does not contain all the tools described in the ChemCrow paper because of API usage restrictions" and "will not give the same results as that paper."

**Limitations**:
- **Incomplete open source** — paper results NOT reproducible from public code
- Tool quality dependency
- Hallucination persists despite tools
- Closed-source LLM limits reproducibility

**Review relevance**: (1) Gap between paper claims and reproducible code. (2) EvaluatorGPT finding = powerful evidence LLM-based evaluation unreliable for chemistry. (3) Tool augmentation helps but doesn't solve hallucination. (4) ReactionExecute = aspiration toward closed-loop but limited to simple syntheses.

---

## 4. Coscientist (Boiko et al., Nature 2023)

**Purpose**: GPT-4-driven autonomous chemical research system.

**4 Core Modules**: GOOGLE, PYTHON, DOCUMENTATION, EXPERIMENT

**Key Results**: Optimized Suzuki cross-couplings. GC-MS confirmed biphenyl at 9.53 min. Procedure generated in <4 minutes.

**LLM Comparison**: GPT-4 > GPT-3.5-turbo > Claude 1.3 > Falcon-40B. Only search-enabled GPT-4 produced acceptable ibuprofen synthesis.

**Popularity**: 196 stars, 29 forks. Only **7 commits post-publication**. Apache 2.0 + Commons Clause (restricts commercial use).

**Code availability**: Repo contains **supporting data and "simple implementation" example ONLY**. Full production codebase withheld. Essentially a research artifacts repo, not a usable tool.

**Limitations**:
- Manual plate movement still required
- Full code withheld for safety
- Only 7 commits post-publication = limited adoption/development

**Review relevance**: (1) Production code withheld = reproducibility crisis. (2) Manual intervention needed = "last mile" problem. (3) Safety restriction vs. open science tension. (4) 7 commits = low community adoption.

---

## 5. Summary Table

| Tool | Stage | Open Source? | Validated? | Stars | Key Gap |
|------|-------|-------------|-----------|-------|---------|
| DruGUI | Virtual screening (8 steps) | Yes (MIT) | In silico only | 4 | No wet-lab validation, basic ADMET |
| ADMET-AI | ADMET (41 properties) | Yes (MIT) | TDC benchmark only | 286 | R²>0.6 on only 50% regression tasks |
| ChemCrow | Multi-task agent | Partial (missing tools) | Expert eval, limited | 893 | Paper results not reproducible |
| Coscientist | Closed-loop synthesis | No (data only) | One reaction class | 196 | Code withheld, manual steps |

**Cross-cutting findings**:
1. **Reproducibility gap**: 3/4 agent tools have significant reproducibility issues
2. **Validation cascade failure**: Every tool validates only at computational/single-experiment level. None bridge to in vivo or clinical
3. **ADMET bottleneck**: Best predictor (ADMET-AI) moderate on half its tasks, yet downstream tools treat predictions as ground truth
4. **Agent paradox**: Tools designed for "autonomous" operation all require significant human intervention or have restricted functionality
