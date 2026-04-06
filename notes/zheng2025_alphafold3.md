# AlphaFold3 in Drug Discovery — Zheng et al., 2025

**Full citation**: Zheng H, Lin H, Alade AA, Chen J, Monroy EY, Zhang M, Wang J. "AlphaFold3 in Drug Discovery: A Comprehensive Assessment of Capabilities, Limitations, and Applications." bioRxiv. 2025. DOI: 10.1101/2025.04.07.647682.
**Section relevance**: Section 2 (target-to-hit), Section 4 (cascading failures), Section 6 (AF3 limitations)

## Key Findings

### Kinase Selectivity (AMG706, GDC-0941, XMD-1150)
- Tested 3 kinase inhibitors with diverse selectivity profiles:
  - AMG706 (Motesanib) — multi-kinase inhibitor
  - GDC-0941 (Pictilisib) — PI3K inhibitor
  - XMD-1150 — kinase inhibitor
- Generated structural predictions across **379 kinases** for each compound
- Developed AF3-GNINA computational pipeline for kinome profiling
- **Result: ROC-AUC only marginally better than random assignment across all three test cases**
- Exact ROC-AUC values: NOT extracted from full text (biorxiv blocked), but described as "marginally better than random" — implying ~0.5-0.6 range
- Key limitation: "While the model appears effective at identifying gross structural incompatibilities, it struggles to accurately model the more subtle determinants of binding selectivity across the kinome"
- "Kinase selectivity often derives from the absence of specific favorable interactions rather than the presence of outright steric clashes. These missing interactions—whether hydrogen bonds, pi-stacking arrangements, or complementary electrostatic surfaces—represent energetic opportunities not realized, rather than explicit structural conflicts."

### Datasets Used
- **PoseBusters benchmark**: 428 protein-ligand structures released to PDB in 2021 or later
- Curated datasets for: binary protein-ligand complexes, apo/holo structural variations, GPCR-ligand conformations, ternary systems, inhibitor affinity prediction
- Kinome selectivity: 379 kinases x 3 inhibitors
- Strategic division into **static complexes** (RMSD < 0.5A) and **dynamic complexes** (RMSD > 5A)

### Comparison with Docking Methods
- AF3 "significantly outperforming traditional docking methods in side-chain orientation accuracy"
- AF3 "demonstrated a significantly higher success rate (RMSD < 2A) compared to Vina and RoseTTAFold All-Atom (RFAA)"
- In PoseBusters benchmark: AF3 prediction accuracy "much better than that of traditional molecular docking tools"
- AF3 does NOT require structural information (unlike Vina/Gold which need receptor structure)
- Comparison with: AutoDock Vina, GNINA, DiffDock, Gold, RFAA

### Conformational Change Failures (>5A RMSD)
- "AF3 struggles with protein-ligand complexes involving significant conformational changes (>5A RMSD)"
- Dataset strategically divided: static (<0.5A RMSD) vs dynamic (>5A RMSD)
- Exact number of failure cases: NOT extracted (full text blocked)
- This is a critical limitation for drug discovery where induced-fit binding is common

### GPCR Results
- Tested calcium-sensing receptor (CaSR)
- **Critical finding**: "AF3 consistently predicted active conformations for CaSR regardless of whether the input ligand was an agonist or antagonist"
- "All predicted structures showed significantly lower RMSD values when compared to reference active conformations than when compared to inactive conformations, indicating a strong systematic bias"
- **8,000 predictions test**: "Despite generating approximately 8000 structural predictions using different random seeds across multiple GPUs, AF3 invariably produced active-state conformations" for antagonist YP1 (PDB: 7SIN) which experimentally stabilizes inactive conformation
- "This consistent failure to predict the correct inactive conformation, even with extensive sampling, points to a fundamental limitation"
- Cause: "AF3's training methodology may have incorporated imbalanced representation of GPCR conformational states, potentially reflecting biases in the underlying structural database where active conformations might be overrepresented"
- **Drug discovery impact**: "The inability to predict antagonist-bound inactive conformations severely limits AF3's utility for virtual screening campaigns targeting GPCRs, as it would likely miss or mischaracterize antagonists and inverse agonists"

### "Binary Interaction Modeler" Characterization
- AF3 "functions effectively as a 'binary interaction modeler' for experimentally validated pairs"
- This means: AF3 can tell you IF a known pair interacts, but cannot rank affinities or predict selectivity

### Affinity Ranking
- "Lacks reliable affinity ranking capability"
- Performance declined on structures released after training cutoff, "suggesting potential memorization rather than physical understanding of molecular interactions"

## Methods
- Systematic benchmarking using curated datasets
- AF3-GNINA hybrid pipeline for kinome profiling
- Multiple random seeds and GPU runs for sampling
- Comparison against traditional docking (Vina, GNINA, DiffDock, Gold) and ML methods (RFAA)

## Limitations
- Full text blocked by biorxiv (403), exact ROC-AUC values not extracted
- Pre-print (not peer reviewed)
- Authors acknowledge AF3 is a structure predictor, not a drug design tool

## Quotes
- "AF3 excels at predicting static protein-ligand interactions with minimal conformational changes"
- "demonstrates a persistent bias toward active GPCR conformations"
- "binary interaction modeler"
- "marginally better predictive performance than random assignment" (kinase selectivity)
- "suggesting potential memorization rather than physical understanding of molecular interactions"

## Our Take
- **Critical for our review**: AF3 is the poster child of "SOTA != clinical utility"
- The kinase selectivity failure (near-random ROC-AUC across 379 kinases) is devastating for real drug discovery use
- The GPCR active-state bias (8000 samples, all wrong) demonstrates fundamental training data bias
- The "binary interaction modeler" label perfectly encapsulates the benchmark-to-bedside gap
- This supports our Section 4 argument: structure prediction accuracy != binding affinity prediction != drug efficacy
- AF3 cannot replace FEP+/physics-based methods for lead optimization (cf. zasocitinib)
- Recommendation to use "hybrid computational pipelines" aligns with our thesis

## Key Numbers for Review
- 379 kinases tested, near-random selectivity prediction
- 8,000 GPCR predictions, 100% wrong conformation state
- 428 PoseBusters complexes
- Performance drops on post-training structures (memorization concern)
