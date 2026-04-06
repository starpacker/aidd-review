# Figure 4: AI Agent Capability Spectrum

## Data Table

| Task Type | Complexity | Example Tasks | Representative Tool | Performance | Evidence |
|-----------|-----------|---------------|--------------------|----|---------|
| Routine | Low | Literature mining, SMILES parsing, safety data retrieval, protocol generation | Base LLM | High (effective) | General consensus |
| Specialized molecular | Low-Med | Name→SMILES conversion, forward synthesis prediction | ChemToolAgent | High (0%→70%, 12%→78%) | ChemToolAgent 2024 |
| Synthesis planning | Medium | Retrosynthesis, organocatalyst synthesis | ChemCrow | Medium-High (4/4 syntheses successful) | Bran et al. 2024 |
| Novel molecule design | Medium-High | Chromophore discovery (9% variance from target) | ChemCrow | Medium | Bran et al. 2024 |
| Reaction optimization | Medium-High | Suzuki coupling optimization (20 iterations) | Coscientist | Medium (GPT-4 only; GPT-3.5 failed) | Boiko et al. 2023 |
| General chemistry reasoning | High | College/graduate chemistry Q&A | ChemToolAgent | **Worse than base LLM** (80.5%→71%, 40.5%→33.8%) | ChemToolAgent 2024 |
| Hypothesis generation | Very High | Target validation, efficacy prediction | None demonstrated | Poor / Not demonstrated | No published evidence |
| Experimental design (iterative) | Very High | Multi-step biological optimization | None demonstrated | Poor / Not demonstrated | No published evidence |

## Key Insight
- Performance drops sharply with task complexity
- Tools HELP on narrow specialized tasks but HURT on broad reasoning
- Root cause: cognitive overload from role-switching (ChemToolAgent)
- The tasks drug discovery NEEDS (hypothesis, experimental design) are where agents perform WORST

## Visualization Spec
- Type: Heatmap or gradient spectrum
- X-axis: Task complexity (Low → Very High)
- Y-axis: Agent performance (High → Low)
- Overlay: Specific tools (ChemCrow, Coscientist, ChemToolAgent) mapped to their zones
- Color gradient: Green (high performance) → Red (poor/absent)
- Annotation: "Drug discovery need" arrow pointing to high-complexity zone
- Dashed line showing where tools help vs. hurt (the crossover point)

## Citations
- ChemCrow: Bran et al., Nature Machine Intelligence, 2024
- Coscientist: Boiko et al., Nature, 2023
- ChemToolAgent: arXiv:2411.07228 (NAACL 2025)
- Lu et al., CTS, 2025 (LLM primer)
