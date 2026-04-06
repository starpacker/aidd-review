# AI Drug Discovery Agent Systems: Comprehensive Landscape (April 2026)

> Source: Web search + GitHub analysis (2026-04-06)
> Purpose: Identify testable agent systems for our review paper experiment
> Status: Research complete

---

## Part 1: DruGUI Deep Dive

### What DruGUI Is
- **Repo**: https://github.com/junior1p/DruGUI
- **Stars**: 5 | **Forks**: 4 | **License**: MIT
- **Created**: April 2026 (very new, submitted to Claw4S Conference 2026)
- **Purpose**: End-to-end, agent-executable structure-based virtual screening (SBVS) pipeline. Designed to be run autonomously by AI agents (e.g., Claude) rather than by human operators.

### 8-Stage Pipeline
1. **Environment setup** — pinned conda dependencies
2. **Target protein preparation** — PDB download, water removal, protonation via PDBFixer/OpenMM
3. **Ligand preparation** — SMILES to 3D structure via RDKit
4. **Molecular docking** — AutoDock Vina
5. **ADMET prediction** — scikit-learn-based models (basic, NOT clinically validated)
6. **Drug-likeness filtering** — Lipinski's Rule of Five + PAINS
7. **Synthesis accessibility scoring** — SA Score
8. **Final composite ranking and reporting** — JSON/CSV output

### Input/Output
- **Input**: PDB ID (target protein) + SMILES file (candidate molecules)
- **Output**: Ranked hit list with docking scores, ADMET profiles, SA scores, JSON/CSV reports
- **YES**: Can feed SMILES strings directly

### How to Run
```bash
git clone https://github.com/junior1p/DruGUI.git
cd DruGUI
conda env create -f environment.yml
conda activate druGUI
python druGUI.py run --pdb-id 6JX0 --smiles-file examples/inputs/smiles_examples.txt --output-dir ./output/egfr_screening --top-k 20
```

### Dependencies
- Python 3.9+
- RDKit, pandas, numpy
- AutoDock Vina (via conda)
- PDBFixer + OpenMM (protein preparation)
- wget (for PDB downloads)
- **GPU**: NOT required
- **OS**: Cross-platform (conda-based), should work on Windows via conda

### Can We Actually Run It?
- **Feasibility**: MEDIUM-HIGH
- **Blockers**: AutoDock Vina installation on Windows can be tricky. Conda environment may have compatibility issues.
- **Workaround**: Use WSL2 or a Linux VM if conda fails on native Windows.
- **Time estimate**: 1-2 hours to set up, minutes to run (53 molecules in 28 seconds on test case)
- **Key test**: Feed our 36 molecules (from agent_evaluation_dataset.json) against EGFR (PDB: 6JX0) and see if it ranks Category A > B > C

### Limitations for Our Experiment
- Requires a protein target (PDB structure) — not just SMILES-only evaluation
- ADMET uses basic scikit-learn models, NOT clinically validated
- No wet-lab validation, no clinical outcome integration
- This is EXACTLY the pipeline type our review criticizes

---

## Part 2: Comprehensive Agent System Inventory

### TIER 1: Directly Testable (can evaluate existing molecules, open code, feasible in 1-2 days)

---

#### 1. DruGUI
- **URL**: https://github.com/junior1p/DruGUI
- **Stars**: 5 | **Type**: 8-stage virtual screening pipeline
- **Input**: SMILES + PDB ID
- **Output**: Composite ranking with docking, ADMET, SA, drug-likeness scores
- **LLM**: None (classical pipeline, designed for agent execution)
- **GPU**: No
- **Python**: 3.9+
- **Can evaluate existing molecules**: YES
- **Feasibility**: HIGH (1-2 hours setup)

---

#### 2. AgentD (hoon-ock/AgentD)
- **URL**: https://github.com/hoon-ock/AgentD
- **Stars**: 33 | **Forks**: 10
- **Paper**: Ock et al., JCIM 2025 (arXiv 2507.02925)
- **Input**: SMILES, FASTA sequences, natural language queries
- **Output**: QED scores, pKd predictions, Lipinski/Veber/Ghose compliance, literature-grounded answers
- **LLM**: OpenAI GPT-4o (requires API key)
- **GPU**: Optional (REINVENT4 component supports CUDA)
- **Python**: 3.10
- **Can evaluate existing molecules**: YES (QED scoring, drug-rule compliance, property prediction)
- **Feasibility**: HIGH (conda + pip install, needs OpenAI API key)
- **Key features**: Modular agents for literature extraction, property prediction, molecule generation, SMILES refinement

---

#### 3. CLADD (RAG-Enhanced Collaborative LLM Agents)
- **URL**: No public GitHub repo found (AAAI 2025 paper: arXiv 2502.17506)
- **Paper**: AAAI Conference on Artificial Intelligence 2025
- **Input**: Query molecules (SMILES implied)
- **Output**: Drug-target predictions, molecular captioning, biological activity predictions
- **LLM**: GPT-4o mini (OpenAI API)
- **GPU**: Not required (API-based)
- **Can evaluate existing molecules**: YES (drug-target prediction, property captioning)
- **Feasibility**: LOW-MEDIUM (no public code found, would need to reimplement)
- **Key insight**: Uses PrimeKG + PubChem + MolT5; outperforms fine-tuned models

---

#### 4. DEDA (Drug Evaluation and Discovery Agent)
- **URL**: https://github.com/drug-discovery-ai/deda-drug-evaluation-and-discovery-agent
- **Stars**: 17 | **Forks**: 5 | **Commits**: 170
- **Input**: Natural language queries (protein names, drug names — not directly SMILES)
- **Output**: Natural language responses grounded in UniProt, AlphaFold, OpenTargets
- **LLM**: OpenAI (requires API key)
- **GPU**: Not mentioned
- **Python**: 3.12+
- **Can evaluate existing molecules**: PARTIALLY (protein/target exploration, not SMILES-based scoring)
- **Feasibility**: MEDIUM (MCP-based architecture, Electron desktop app available)
- **Key features**: "ChatGPT for bioinformatics researchers"; integrates UniProt, AlphaFold, OpenTargets

---

#### 5. Prompt-to-Pill
- **URL**: https://github.com/ChatMED/Prompt-to-Pill
- **Stars**: 6 | **Forks**: 2 | **Commits**: 39
- **Paper**: Bioinformatics Advances 2025 (DOI: 10.1093/bioadv/vbaf323)
- **Input**: SMILES strings and compound names
- **Output**: Clinical feasibility reports, trial protocols, patient matching, docking scores, ADMET predictions
- **LLM**: OpenAI API + Panacea-7B-Chat (patient matching)
- **GPU**: Required (for Panacea-dependent servers)
- **Python**: 3.11
- **Can evaluate existing molecules**: YES (docking, ADMET, chemical properties)
- **9+ agents**: Drug generation, docking, chemical properties, ADMET, optimization, name2SMILES, patient matching, trial generation, trial prediction
- **Feasibility**: MEDIUM (needs AutoDock Vina 1.1.2, Open Babel 3.1.1, P2Rank, multiple cloned repos)
- **Key insight**: Most ambitious end-to-end system (molecular design to clinical trial simulation)

---

#### 6. RepurAgent
- **URL**: https://github.com/pharmbio/repuragent
- **Stars**: 18 | **Forks**: 0 | **Commits**: 103
- **Input**: SMILES (via Data Agent standardization)
- **Output**: Comprehensive reports, molecular property predictions, knowledge graph analysis
- **LLM**: OpenAI API
- **GPU**: Not required
- **Python**: Not specified (Docker-based)
- **Can evaluate existing molecules**: YES (via Prediction Agent with ML models + Data Agent for SMILES)
- **6 agents**: Planning, Supervisor, Research, Prediction, Data, Report
- **Feasibility**: MEDIUM-HIGH (Docker deployment, Gradio UI, needs OpenAI key)
- **Key features**: Episodic memory, SOP RAG system, human-in-the-loop supervision

---

#### 7. AIAgents4Pharma (VirtualPatientEngine)
- **URL**: https://github.com/VirtualPatientEngine/AIAgents4Pharma
- **Stars**: 76 | **Forks**: 46 | **Commits**: 348
- **Input**: Natural language queries about biological models, knowledge graphs, literature
- **Output**: Systems biology analysis, knowledge graph exploration, literature recommendations
- **LLM**: GPT-4o-mini (OpenAI) or Llama 3.1/3.3 (NVIDIA API)
- **GPU**: Optional (NVIDIA for Llama models)
- **Python**: 3.x (pyproject.toml)
- **Can evaluate existing molecules**: PARTIALLY (Talk2BioModels for systems biology, not direct SMILES scoring)
- **5 agents**: Talk2BioModels, Talk2KnowledgeGraphs, Talk2Scholars, Talk2Cells, Talk2AIAgents4Pharma
- **Feasibility**: MEDIUM (Docker or pip install, needs API keys)

---

#### 8. ChemMCP (OSU-NLP-Group)
- **URL**: https://github.com/OSU-NLP-Group/ChemMCP
- **Input**: SMILES (via MCP tools)
- **Output**: Molecular analysis, property predictions, reaction predictions
- **LLM**: Any MCP-compatible client (Claude Desktop, etc.)
- **19 chemistry tools**: General (web search), Molecule (analysis, property prediction, conversion), Reaction (prediction, analysis)
- **Can evaluate existing molecules**: YES (property prediction, molecular analysis tools)
- **Feasibility**: HIGH (MCP server, integrates with Claude Desktop)
- **Key insight**: Successor to ChemToolAgent; continuously updated

---

### TIER 2: Partially Testable (generation/optimization focus, may not directly score existing molecules)

---

#### 9. LIDDiA (Language-based Intelligent Drug Discovery Agent)
- **URL**: https://github.com/ninglab/LIDDiA
- **Stars**: 5 | **Forks**: 1 | **Commits**: 6
- **Paper**: EMNLP 2025
- **Input**: Target name (e.g., EGFR), uses Pocket2Mol for structure-based generation
- **Output**: Generated drug candidates with pharmaceutical properties
- **LLM**: Claude 3.5 Sonnet (Anthropic API)
- **GPU**: Not specified
- **Can evaluate existing molecules**: UNCLEAR (generates and selects, may not score arbitrary SMILES)
- **Feasibility**: LOW-MEDIUM (only 6 commits, very sparse documentation)
- **Key stat**: Produces candidates satisfying key properties on >70% of 30 major therapeutic targets

---

#### 10. DrugAssist
- **URL**: https://github.com/blazerye/DrugAssist
- **Stars**: 141 | **Forks**: 14
- **Paper**: Briefings in Bioinformatics 2025
- **Input**: SMILES (molecule optimization)
- **Output**: Optimized SMILES with improved properties
- **LLM**: Llama2-7B-Chat (fine-tuned)
- **GPU**: Yes for full model; quantized 4-bit GGUF available for CPU
- **Python**: 3.8
- **Can evaluate existing molecules**: NO (optimization only, transforms input SMILES)
- **Feasibility**: MEDIUM (needs model download from HuggingFace, GPU recommended)

---

#### 11. MT-Mol (Multi-Agent Tool-based Molecular Optimization)
- **URL**: https://github.com/icecream126/mt_mol
- **Stars**: 4 | **Forks**: 0
- **Paper**: EMNLP 2025 Findings
- **Input**: SMILES (molecular optimization)
- **Output**: Optimized molecules with tool-aligned reasoning
- **LLM**: Not specified in README
- **Can evaluate existing molecules**: PARTIALLY (uses RDKit tools for analysis, but optimization-focused)
- **Feasibility**: LOW-MEDIUM (sparse documentation)

---

#### 12. AgentDrug (Zero-Shot Molecular Editing)
- **URL**: No public GitHub found (arXiv 2410.13147, EMNLP 2025 Findings)
- **Input**: SMILES
- **Output**: Edited SMILES with improved properties
- **LLM**: Qwen-2.5-3B/7B
- **Can evaluate existing molecules**: NO (editing/optimization focus)
- **Feasibility**: LOW (no public code found)

---

### TIER 3: Important Context Systems (not directly testable for our experiment but relevant to review)

---

#### 13. TxAgent (Harvard MIMS Lab)
- **URL**: https://github.com/mims-harvard/TxAgent
- **Stars**: 613 | **Commits**: 11
- **Paper**: arXiv 2503.10970 (March 2025)
- **What it does**: Therapeutic reasoning — drug interactions, contraindications, patient-specific treatment strategies
- **211 tools**: All FDA-approved drugs since 1939, Open Targets data
- **LLM**: Custom (requires H100 GPU with 80GB+ VRAM)
- **GPU**: YES (H100 recommended — 80GB+)
- **Can evaluate existing molecules**: NOT for SMILES-based scoring; evaluates drug-drug interactions and treatment plans
- **Feasibility**: LOW for our experiment (needs H100, not molecule-scoring focused)
- **Key stat**: 92.1% accuracy on drug reasoning, outperforms GPT-4o by 25.8%
- **Review relevance**: Impressive system but focused on treatment reasoning, not molecular evaluation

---

#### 14. TxGemma (Google DeepMind)
- **URL**: https://huggingface.co/google/txgemma-9b-predict
- **Paper**: arXiv 2504.06196 (April 2025)
- **What it does**: Property prediction + agentic reasoning for therapeutics
- **Models**: 2B, 9B, 27B parameter variants (fine-tuned from Gemma-2)
- **Agentic-Tx**: 18 tools including TxGemma-Predict and TxGemma-Chat
- **GPU**: YES (2B model might run on consumer GPU; 9B/27B need more)
- **Can evaluate existing molecules**: YES (property prediction across 66 therapeutic tasks)
- **Feasibility**: MEDIUM-HIGH for predict model (HuggingFace, 2B model manageable); LOW for Agentic-Tx (needs Gemini 2.5 API)
- **Key stat**: Superior on 45/66 tasks vs generalist SOTA; superior on 26/66 vs specialist SOTA

---

#### 15. PharmAgents (Virtual Pharma)
- **URL**: No public GitHub found (arXiv 2503.22164, March 2025)
- **What it does**: Full drug discovery pipeline simulation — target discovery, lead identification, optimization, preclinical evaluation
- **LLM**: Not specified
- **Can evaluate existing molecules**: YES (lead evaluation)
- **Feasibility**: LOW (no public code)
- **Key stat**: Triples lead generation success rate from 15.7% to 37.9%

---

#### 16. SciAgents Discovery
- **URL**: https://github.com/lamm-mit/SciAgentsDiscovery
- **Stars**: 600 | **Forks**: 107
- **What it does**: Multi-agent scientific discovery via knowledge graph reasoning (biologically inspired materials)
- **LLM**: OpenAI API + AG2 (AutoGen) framework
- **Can evaluate existing molecules**: NO (hypothesis generation, not molecular scoring)
- **Feasibility**: LOW for our experiment (materials science focus, not drug molecules)

---

#### 17. ChatInvent (AstraZeneca, proprietary)
- **URL**: NOT publicly available (described in Drug Discovery Today, Jan 2026)
- **What it does**: Molecular design + synthesis planning, integrated in AZ pipeline
- **Key insight**: "Evolved from proof-of-concept single agent into extensible multi-agent architecture with GUI"
- **Feasibility**: ZERO (proprietary, no public code)
- **Review relevance**: Important example of industry adoption of agentic AI

---

#### 18. BioAutoMATED (MIT/Wyss Institute)
- **URL**: https://github.com/jackievaleri/BioAutoMATED
- **Paper**: Cell Systems 2023
- **What it does**: AutoML for biological sequence analysis (nucleic acids, peptides, glycans)
- **Can evaluate existing molecules**: NO (sequence analysis, not small-molecule scoring)
- **Feasibility**: LOW for our experiment (wrong modality — sequences not SMILES)

---

### Previously Catalogued Systems (from notes/raw_agent_data_code_repos.md)

#### 19. ChemCrow
- **URL**: https://github.com/guestrin-lab/ChemCrow (partial code only)
- **Stars**: ~893 | 18 chemistry tools
- **Key issue**: "Does not contain all the tools described in the paper" — results NOT reproducible
- **Can evaluate existing molecules**: PARTIALLY (property tools available, but incomplete)

#### 20. Coscientist
- **URL**: https://github.com/gomesgroup/coscientist (data only)
- **Stars**: ~196 | Code withheld for safety
- **Feasibility**: ZERO (no usable code)

---

## Part 3: Prioritized Test Plan

### Priority A — Must Test (high feasibility, directly relevant)
| # | System | Input | Can Score SMILES? | Setup Time | API Cost |
|---|--------|-------|------------------|------------|----------|
| 1 | **DruGUI** | SMILES + PDB | Yes | 1-2 hrs | Free |
| 2 | **AgentD** | SMILES | Yes | 1 hr | OpenAI API |
| 3 | **ChemMCP** | SMILES via MCP | Yes | 30 min | Claude API |
| 4 | **RepurAgent** | SMILES | Yes | 1-2 hrs | OpenAI API |

### Priority B — Should Test (medium feasibility, valuable results)
| # | System | Input | Can Score SMILES? | Setup Time | Blocker |
|---|--------|-------|------------------|------------|---------|
| 5 | **Prompt-to-Pill** | SMILES | Yes | 3-4 hrs | GPU needed, complex deps |
| 6 | **DEDA** | NL queries | Partially | 1-2 hrs | Not SMILES-native |
| 7 | **TxGemma-2B** | SMILES | Yes (property pred) | 2-3 hrs | GPU recommended |
| 8 | **AIAgents4Pharma** | NL queries | Partially | 2-3 hrs | Not SMILES-native |

### Priority C — Context Only (cite in review, don't test)
| # | System | Reason |
|---|--------|--------|
| 9 | TxAgent | H100 GPU required, treatment reasoning not molecular scoring |
| 10 | PharmAgents | No public code |
| 11 | ChatInvent | Proprietary (AstraZeneca) |
| 12 | SciAgents | Materials science, not drug molecules |
| 13 | BioAutoMATED | Sequence analysis, not small molecules |
| 14 | ChemCrow | Incomplete public code, already simulated in RDKit pipeline |
| 15 | Coscientist | Code withheld |

---

## Part 4: Key Paper — "Beyond SMILES: Evaluating Agentic Systems for Drug Discovery"
- **arXiv**: 2602.10163 (February 2026)
- **Author**: Edward Wijaya
- **What it does**: Evaluates 6 AI drug discovery frameworks across 15 task classes
- **5 Capability Gaps Identified**:
  1. No protein language model or peptide-specific prediction support
  2. Missing connections between in vivo and in silico data
  3. Dependence on LLM inference without ML training or RL pathways
  4. Assumptions requiring large-pharma resources
  5. Single-objective optimization ignoring safety-efficacy-stability trade-offs
- **Key quote**: "The bottleneck is architectural rather than epistemic"
- **HIGHLY RELEVANT to our review** — validates our thesis from a different angle

---

## Part 5: Cross-Cutting Observations

### Finding 1: The Shared Metrics Problem Extends to ALL Agent Systems
Every testable agent system uses some combination of:
- QED / drug-likeness (we showed r = -0.38 with clinical utility)
- SA Score (real drugs harder to synthesize)
- Lipinski/Veber filters (100% pass for decoys vs 83% for approved)
- Docking scores (r^2 ~ 0.1-0.3 with binding affinity)
- ADMET predictions (r = -0.43 with clinical utility)

**New systems (AgentD, Prompt-to-Pill, RepurAgent, DruGUI) ALL use these same metrics.**

### Finding 2: LLM Layer Adds Reasoning But Not New Data
Agent systems that add an LLM (AgentD, RepurAgent, CLADD) gain:
- Natural language interface
- Multi-step reasoning
- Literature retrieval
But they do NOT add:
- Clinical outcome data
- Patient pharmacogenomics
- Systems biology/pathway models
- In vivo ADMET validation

### Finding 3: Most Systems Are Paper-Only or Prototype
- Of 18 systems catalogued, only ~6-8 have fully functional public code
- ChemCrow's repo explicitly says "will not give same results as paper"
- Coscientist withholds production code
- PharmAgents has no public code
- Many repos have <10 commits post-publication

### Finding 4: The Evaluation Paradox
- Systems that CAN evaluate molecules (DruGUI, AgentD, ChemMCP) use the same anti-predictive metrics
- Systems with better data access (TxAgent, TxGemma) can't easily evaluate arbitrary SMILES
- No system integrates clinical outcome databases (ClinicalTrials.gov results, FDA approval rates by target)

---

## Sources

- [DruGUI GitHub](https://github.com/junior1p/DruGUI)
- [TxAgent GitHub](https://github.com/mims-harvard/TxAgent)
- [TxAgent Paper](https://arxiv.org/abs/2503.10970)
- [AgentD GitHub](https://github.com/hoon-ock/AgentD)
- [DrugAgent GitHub](https://github.com/FermiQ/drugagent)
- [DEDA GitHub](https://github.com/drug-discovery-ai/deda-drug-evaluation-and-discovery-agent)
- [AIAgents4Pharma GitHub](https://github.com/VirtualPatientEngine/AIAgents4Pharma)
- [RepurAgent GitHub](https://github.com/pharmbio/repuragent)
- [Prompt-to-Pill GitHub](https://github.com/ChatMED/Prompt-to-Pill)
- [Prompt-to-Pill Paper](https://academic.oup.com/bioinformaticsadvances/article/6/1/vbaf323/8403080)
- [LIDDiA GitHub](https://github.com/ninglab/LIDDiA)
- [LIDDiA Paper](https://arxiv.org/abs/2502.13959)
- [DrugAssist GitHub](https://github.com/blazerye/DrugAssist)
- [DrugAssist Paper](https://academic.oup.com/bib/article/26/1/bbae693/7942355)
- [MT-Mol GitHub](https://github.com/icecream126/mt_mol)
- [ChemMCP GitHub](https://github.com/OSU-NLP-Group/ChemMCP)
- [SciAgents GitHub](https://github.com/lamm-mit/SciAgentsDiscovery)
- [BioAutoMATED GitHub](https://github.com/jackievaleri/BioAutoMATED)
- [TxGemma Paper](https://arxiv.org/abs/2504.06196)
- [TxGemma Models](https://huggingface.co/google/txgemma-9b-predict)
- [PharmAgents Paper](https://arxiv.org/abs/2503.22164)
- [CLADD Paper](https://arxiv.org/abs/2502.17506)
- [AgentDrug Paper](https://arxiv.org/abs/2410.13147)
- [Beyond SMILES Paper](https://arxiv.org/abs/2602.10163)
- [ChatInvent / AZ Agentic AI](https://www.sciencedirect.com/science/article/pii/S1359644626000103)
