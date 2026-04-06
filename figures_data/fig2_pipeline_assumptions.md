# Figure 2: Pipeline Architecture — AI Assumptions vs. Biological Reality

## Data Table (Conceptual, not quantitative)

| Pipeline Stage | AI Assumption | Biological Reality | Consequence |
|---------------|---------------|-------------------|-------------|
| Target ID | GWAS/multi-omics hits are causal and druggable | Many associations are non-causal; druggability ≠ therapeutic relevance | Wrong targets enter pipeline |
| Structure Prediction | Static structure suffices (AlphaFold) | Dynamic conformational ensemble; allosteric regulation; IDP regions | Binding optimized to wrong conformation |
| Virtual Screening | Scoring functions capture binding affinity | Rigid docking ignores solvation, entropy, induced fit; hit rates 1-5% | High false positive rate |
| Binding Site Validation | Computational pocket = therapeutic target | Binding ≠ functional effect; pathway context ignored | Target engagement without efficacy |
| Lead Optimization / ADMET | In silico ADMET prediction is reliable | pH-dependent solubility (gastric pH 1.2 vs. plasma 7.4); enzymatic hydrolysis of esters/amides; species-specific CYP metabolism | Molecules fail in vivo despite good in silico profiles |
| Preclinical (Animal) | Animal models predict human response | 95% of animal-tested drugs fail in humans (Ineichen 2024); species-specific immune responses, receptor expression | False confidence from animal efficacy |
| Clinical (Phase I) | Safe molecule = effective medicine | Phase I tests safety, not efficacy; AI optimizes for safety (ADMET) which is why Phase I improves | Phase I success ≠ Phase II success |
| Clinical (Phase II) | Target engagement = clinical benefit | Pathway redundancy, compensatory mechanisms, tissue microenvironment, patient heterogeneity | The Biology Problem |

## Visualization Spec
- Type: Horizontal pipeline flowchart
- Each stage = box with two layers:
  - Top (blue): AI Assumption
  - Bottom (red): Biological Reality
- Arrows between stages show information loss at each handoff
- Green highlight on ADMET/Phase I (where AI assumptions hold)
- Red highlight on Phase II and beyond (where assumptions break)
- NOT a data figure — conceptual/architectural

## Notes
- This figure is distinct from Fig 1 (data bars) and Fig 3 (quantitative waterfall)
- Purpose: help reader understand the STRUCTURAL reasons for AI failure, not just the numbers
- Should be self-contained: reader should grasp the core argument from this figure alone
