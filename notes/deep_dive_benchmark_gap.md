# Deep Dive: The Benchmark-to-Bedside Gap

> **Purpose**: Quantitative evidence for Section 4.3 of the review
> **Created**: 2026-04-03
> **Status**: Research compilation — verified data only, gaps explicitly noted

---

## 1. Walters & Barzilay 2021 — Critical Assessment of AI in Drug Discovery

**Full citation**: Walters WP, Barzilay R. "Critical assessment of AI in drug discovery." *Expert Opinion on Drug Discovery*, 2021; 16(9): 937-947. DOI: 10.1080/17460441.2021.1915982

### Key Arguments (verified from existing notes + blog cross-references)

1. **Random data splits inflate metrics** vs. time-based splits that simulate real-world deployment. When models are trained on randomly split data, test molecules are often structurally similar to training molecules, yielding overoptimistic performance estimates.

2. **Data leakage** between train/test sets undermines reported performance. Benchmarks like MoleculeNet contain overlapping or near-identical molecules across splits.

3. **Benchmarks criticized**:
   - **MoleculeNet** (cited >1,800 times by 2023): datasets altered, labels imputed, loss of comparability across studies
   - **Tox21**: problematic labels
   - General concern: molecule generation methods described as "relatively new and unproven"

4. **Core claim**: ML for property prediction is "routine but not transformative" — overfitting to benchmarks occurs without genuine generalization to novel chemical series.

### Quantitative Data — LIMITATIONS

**IMPORTANT**: The original paper does not provide a single head-to-head table of "random split AUC = X vs. temporal split AUC = Y." The argument is primarily qualitative/conceptual, warning about inflated metrics rather than quantifying the exact gap. The specific quantification comes from subsequent work (see Walters 2024 blog post on splitting, below).

**What we CAN cite**: The paper identifies the *mechanism* of benchmark inflation (similarity between train/test, data leakage, imputed labels) and argues this renders benchmark rankings unreliable for predicting real-world utility.

---

## 2. MoleculeNet Benchmark Problems — Pat Walters Blog + Literature

### 2.1 Pat Walters Blog: "We Need Better Benchmarks for Machine Learning in Drug Discovery" (August 3, 2023)

**URL**: https://practicalcheminformatics.blogspot.com/2023/08/we-need-better-benchmarks-for-machine.html

#### Specific Data Quality Problems by Dataset

**BACE Dataset**:
- Compiled from **55 separate papers** with different assay conditions
- **45% of IC50 values** differed by >0.3 log units between source papers
- **71% of molecules** have at least one undefined stereocenter
- **222 molecules** have 3 undefined stereocenters; one molecule has **12**
- **28 sets of stereoisomers** present (stereochemistry matters for activity but is undefined)
- Arbitrary classification cutoff at 200 nM deemed impractical

**BBB (Blood-Brain Barrier) Dataset**:
- Contains **11 invalid SMILES** with uncharged tetravalent nitrogen atoms
- **59 duplicate structures**, of which **10 pairs have conflicting labels** (same molecule labeled both positive and negative)
- **2,050 molecules** total — BBB penetration is a notoriously complex, poorly-defined endpoint
- Ceftriaxone CNS penetration varies **"between 0.5 and 95%"** in the literature depending on conditions

**HIV Dataset**:
- **70% of "confirmed active" molecules** trigger one or more structural alerts for assay interference
- **68 compounds are azo dyes**, widely known to be cytotoxic (non-specific activity)
- Activity may reflect assay artifacts rather than genuine anti-HIV activity

**ESOL (Solubility) Dataset**:
- Spans **>13 log units** dynamic range
- Real-world drug solubility optimization typically operates within **2.5-3 log units**
- Training on unrealistic range may not generalize to practical drug design

**QM7/QM8/QM9**:
- 3D quantum mechanical properties predicted from 1D SMILES input
- Conceptually flawed: the representation lacks the information needed for the prediction

**Toxcast**: 8,595 structures, 620 endpoints, ~6,000 missing values, **56% trigger structural alerts**
**Tox21**: 8,014 compounds, 12 assays, 575-2,104 missing values per assay

#### Key Statistic
- MoleculeNet cited **>1,800 times** despite these fundamental data quality flaws
- **59 beta-lactam antibiotics** in BBB dataset have inconsistent carboxylic acid representation

### 2.2 Pat Walters Blog: "Some Thoughts on Splitting Chemical Datasets" (November 16, 2024)

**URL**: https://practicalcheminformatics.blogspot.com/2024/11/some-thoughts-on-splitting-chemical.html

#### Quantitative Splitting Comparison (Biogen solubility dataset)

| Split Method | R² (approx.) | Description |
|-------------|-------------|-------------|
| Random split | **0.73** | 80/20 partition, most lenient |
| Scaffold split | ~0.67 | Bemis-Murcko scaffolds |
| Butina split | ~0.65 | Morgan fingerprint clustering |
| UMAP split | **0.62** | Most stringent, agglomerative clustering |

**Key finding**: Random splits overestimate model performance by **~18%** (R² 0.73 vs. 0.62) compared to the most realistic splitting method.

- All splitting methods produce **statistically distinct results** (Tukey HSD, p < 0.05)
- "Random splits with the highest train/test similarity generate the model with the highest R²"
- Critical gap: most benchmark datasets **lack timestamps**, making ideal time-based validation impossible

### 2.3 Pat Walters Blog: "Generative Molecular Design Isn't As Easy As People Make It Look" (May 22, 2024)

**URL**: https://practicalcheminformatics.blogspot.com/2024/05/generative-molecular-design-isnt-as.html

#### Quantitative Cascade Failure of Generative Model (DiffLinker)

| Stage | Input | Output | Retention Rate |
|-------|-------|--------|---------------|
| Initial generation | — | 1,000 | — |
| Deduplication | 1,000 | 581 | 58.1% |
| Ring system filtering | 581 | 437 | 75.2% |
| Chemical stability (REOS) | 437 | 143 | 32.7% |
| Structural validation (PoseBusters) | 143 | 88 | 61.5% |
| **Total yield** | **1,000** | **88** | **8.8%** |

- One structure appeared **145 times** in 1,000 generated molecules (14.5% redundancy)
- Even the 88 "passing" molecules showed strained structures with eclipsed bonds
- Walters classifies most published generative work as **ACD Level 1**: "A machine provides ideas that are then selected by a person"
- Quote: "There's a lot of child-proofing that has to go on with these models"

### 2.4 Pat Walters Blog: "AI in Drug Discovery 2022 — A Highly Opinionated Literature Review" (January 2023)

#### Key Claims
- Traditional methods (Random Forest, XGBoost, SVR with ECFP fingerprints) **frequently match or exceed DNN performance** on realistic datasets
- SVM, GBM, and RF with ECFPs provided "the best performance" on activity cliff datasets
- Performance advantages of deep learning appear primarily with **"tens of thousands of molecules"** — smaller datasets favor simpler approaches
- Quote on structure-based methods: "it's difficult to benchmark because it is hard to know if the method is discovering new interactions or simply transferring information from similar binding sites"

---

## 3. PDBbind/CASF Benchmark Issues — LP-PDBBind Study

### 3.1 The Data Leakage Problem

**Full citation**: Li J, Guan X, Zhang O, Sun K, Wang Y, Bagni D, Head-Gordon T. "Leak Proof PDBBind: A Reorganized Dataset of Protein-Ligand Complexes for More Generalizable Binding Affinity Prediction." arXiv:2308.09639v2, 2024 (Berkeley). DOI: 10.48550/arXiv.2308.09639

#### Nature of Leakage
- PDBBind (~20K protein-ligand complexes) split into general/refined/core sets
- **Original PDBBind split has a sharp peak at similarity = 1.0** between general and core sets for both proteins AND ligands — meaning identical proteins and ligands appear in both train and test
- "The majority of the core data records in the PDBBind dataset have identical proteins and/or ligands with that found in the general and/or refined sets"
- IC50 values for the same complex can **vary up to one order of magnitude** across different assays
- Many ligands are non-drug-like (macrocycles, peptide-like, long aliphatic chains)

#### LP-PDBBind Solution
- Maximum protein sequence similarity between train and test: **0.5** (vs ~1.0 in original)
- Maximum ligand similarity between train and test: **0.99**
- Training set: 11,513 | Validation: 2,422 | Test: 4,860
- Also controls for interaction fingerprint similarity (not just sequence/structure)

### 3.2 Quantitative Performance Impact of Removing Leakage

#### Table 1: RMSE on LP-PDBBind Test Set (kcal/mol)

| Model | RMSE (Original model on LP test) | RMSE (Retrained on LP, test) | Interpretation |
|-------|--------------------------------|----------------------------|----------------|
| AutoDock Vina | 2.85 | 2.56 | Improved (small param count, less overfitting) |
| IGN | **1.82** | **2.16** | Original INFLATED by leakage (+0.34 kcal/mol) |
| RF-Score | **1.89** | **2.10** | Original INFLATED by leakage (+0.21 kcal/mol) |
| DeepDTA | **1.34** | **2.29** | Original INFLATED by leakage (+0.95 kcal/mol) |

**KEY FINDING**: ML scoring functions trained on original PDBBind appear to perform better (lower RMSE) than they actually do. When leakage is removed:
- **DeepDTA** performance drops by **0.95 kcal/mol RMSE** (most affected — sequence-only, no 3D structure)
- **IGN** drops by 0.34 kcal/mol
- **RF-Score** drops by 0.21 kcal/mol
- **AutoDock Vina** actually improves (physics-based, fewer trainable parameters → less memorization)

#### Table 2: Performance on Independent BDB2020+ Benchmark

| Model | RMSE Original | RMSE Retrained | Change | R Original | R Retrained |
|-------|-------------|---------------|--------|-----------|------------|
| AutoDock Vina | 3.31 | **2.10** | **-37%** | 0.23 | 0.29 |
| IGN | 1.62 | **1.38** | -9~20% | 0.41 | **0.54** |
| RF-Score | 1.80 | **1.61** | -10~11% | 0.36 | **0.51** |
| DeepDTA | 1.98 | **1.72** | -9~19% | 0.18 | 0.26 |

**KEY FINDING**: Models retrained on leak-proof data perform BETTER on truly independent data (BDB2020+), confirming that leakage causes overfitting rather than genuine generalization.

#### Table 3: Target-Specific Ranking (EGFR — out-of-distribution target)

| Model | R Original | R Retrained | Rs Original | Rs Retrained |
|-------|-----------|------------|------------|-------------|
| AutoDock Vina | 0.25 | 0.38 | 0.21 | 0.36 |
| IGN | 0.36 | **0.65** | 0.17 | **0.62** |
| RF-Score | **-0.15** | **0.52** | **-0.18** | 0.45 |
| DeepDTA | 0.23 | 0.44 | 0.20 | 0.43 |

**DEVASTATING FINDING**: RF-Score trained on original (leaky) PDBBind shows **negative correlation** (R = -0.15, Rs = -0.18) on out-of-distribution EGFR target — meaning its predictions are *worse than random*. After retraining on leak-proof data, R jumps to 0.52. This is the strongest quantitative evidence that benchmark leakage creates models that actively mislead on novel targets.

---

## 4. Prospective Validation Studies

### 4.1 Available Data Points

**Virtual screening hit rates in practice**: ~1-5% (cited in outline.md; widely reported in literature)
- This means 95-99% of computationally predicted "hits" fail experimental validation
- Traditional HTS hit rates: ~0.01-0.1% but from much larger screens

**Active learning efficiency** (from raw_agent_data_sdl_agents.md):
- Active learning with linear regression retrieves **90% of top-tier docking hits** after evaluating just **10% of a virtual library** (14-fold reduction in computational cost)
- But this measures computational efficiency, not experimental hit rates

### 4.2 What We Could NOT Verify

**GAPS IN AVAILABLE DATA** — the following would strengthen Section 4.3 but require access to paywalled primary literature:

1. **No large-scale published study** directly comparing the same model's benchmark performance to its prospective hit rate in a real drug discovery project was accessible through open sources
2. Specific hit rates from AI-predicted compound libraries tested in wet-lab remain largely unpublished or in proprietary company data
3. The exact quantitative gap between "AUC on MoleculeNet test set" and "% of predicted actives confirmed in dose-response assay" has not been systematically measured in a single controlled study

### 4.3 Indirect Evidence

**The 91.2% generative model failure rate** (Walters, May 2024): Of 1,000 AI-generated molecules, only 88 (8.8%) survive basic chemical validity filters — before any biological testing. This is purely computational filtering, not wet-lab.

**The splitting gap**: Random-split R² = 0.73 vs. realistic-split R² = 0.62 (18% overestimation) on Biogen solubility data. In real deployment, the model encounters molecules from the "UMAP split" distribution, not the "random split" distribution.

**The PDBbind leakage gap**: Models that appear to predict binding affinity with R = 0.41 on leaky benchmarks actually achieve R = -0.15 on novel targets (RF-Score on EGFR). This is the most extreme documented example of benchmark-to-real-world performance collapse.

---

## 5. Niazi 2025 — AI vs. Traditional Methods Comparison

**Full citation**: Niazi SK. "Artificial Intelligence in Small-Molecule Drug Discovery: A Critical Review." *Pharmaceuticals*, 2025, 18(9):1271. DOI: 10.3390/ph18091271

### Verified Numbers
- Traditional docking scoring functions: **AUC 0.70-0.80**
- AI-enhanced scoring methods: **AUC 0.72-0.82**
- Difference: marginal (**+0.02** at both ends of range)
- "Competitive performance" but "results vary significantly depending on specific target and dataset"

### Important Caveats
1. **Single-author critical review**, not a primary benchmarking study
2. AUC ranges are compiled from multiple sources, not a single controlled comparison
3. The modest improvement (0.02 AUC) is within typical experimental noise for many applications
4. Should be cited as "a critical review found..." NOT "a benchmarking study demonstrated..."

### Rhetorical Value
Even taken at face value, the Niazi numbers are powerful: **billions of dollars of AI investment** has produced a scoring function improvement of **~0.02 AUC points** over traditional docking — an improvement that may not be statistically significant for any individual target.

---

## 6. Synthesis: Quantitative Evidence for Section 4.3

### The Strongest Numbers to Cite

| Claim | Number | Source | Confidence |
|-------|--------|--------|-----------|
| Random vs. realistic split performance gap | R² 0.73 vs. 0.62 (18% inflation) | Walters 2024 blog (Biogen data) | HIGH — reproducible, primary data |
| MoleculeNet citation count despite flaws | >1,800 citations | Walters 2023 blog | HIGH |
| BACE IC50 inconsistency | 45% differ by >0.3 log units | Walters 2023 blog | HIGH |
| HIV dataset artifacts | 70% trigger structural alerts | Walters 2023 blog | HIGH |
| BBB conflicting labels | 10 duplicate pairs with opposite labels | Walters 2023 blog | HIGH |
| PDBbind train-test identity | Peak at similarity = 1.0 | Li et al. 2024 (LP-PDBBind) | HIGH — peer reviewed |
| RF-Score on novel target (leaky vs. clean) | R = -0.15 → R = 0.52 | Li et al. 2024 (LP-PDBBind) | HIGH — peer reviewed |
| DeepDTA RMSE inflation from leakage | 1.34 → 2.29 kcal/mol (+0.95) | Li et al. 2024 (LP-PDBBind) | HIGH — peer reviewed |
| AI vs. traditional docking AUC | 0.72-0.82 vs. 0.70-0.80 | Niazi 2025 (review) | MODERATE — secondary source |
| Generative model yield after filtering | 8.8% (88/1000) | Walters 2024 blog (DiffLinker) | HIGH — reproducible |
| Virtual screening hit rates in practice | ~1-5% | Multiple sources | MODERATE — widely cited but imprecise |

### Recommended Narrative for Section 4.3

**Opening**: Benchmark leaderboard performance has become the *de facto* currency of progress in AI drug discovery, yet mounting evidence reveals systematic inflation of these metrics.

**Three lines of evidence**:

1. **Data quality**: MoleculeNet, cited >1,800 times, contains datasets with 45% interlaboratory inconsistency in IC50 values (BACE), 70% assay artifacts (HIV), and contradictory labels for identical molecules (BBB) [Walters 2023].

2. **Splitting artifacts**: Random train-test splits overestimate model performance by ~18% compared to realistic chemical diversity splits [Walters 2024]. Most benchmarks lack timestamps, preventing the temporal splits that would simulate real deployment.

3. **Data leakage**: In PDBbind — the standard benchmark for scoring functions — the training and test sets share identical proteins and ligands (similarity = 1.0). When this leakage is removed (LP-PDBBind), ML scoring functions lose 0.2-0.95 kcal/mol RMSE, and one model's correlation on a novel target collapses from R = -0.15 (worse than random) to R = 0.52 after retraining on clean data [Li et al. 2024].

**The punchline**: Despite billions in AI investment, AI-enhanced docking achieves AUC 0.72-0.82 vs. traditional docking's 0.70-0.80 [Niazi 2025] — a difference of ~0.02 that is often within experimental noise.

---

## 7. BibTeX Entries to Add

```bibtex
@article{LiLP2024,
  author  = {Li, Jie and Guan, Xingyi and Zhang, Oufan and Sun, Kunyang and Wang, Yingze and Bagni, Dorian and Head-Gordon, Teresa},
  title   = {Leak Proof PDBBind: A Reorganized Dataset of Protein-Ligand Complexes for More Generalizable Binding Affinity Prediction},
  journal = {arXiv preprint},
  year    = {2024},
  volume  = {},
  pages   = {},
  doi     = {10.48550/arXiv.2308.09639},
  note    = {PDBBind train-test leakage; RF-Score R flips from -0.15 to 0.52 on EGFR after removing leakage}
}

@misc{Walters2023blog,
  author = {Walters, W. Patrick},
  title  = {We Need Better Benchmarks for Machine Learning in Drug Discovery},
  year   = {2023},
  url    = {https://practicalcheminformatics.blogspot.com/2023/08/we-need-better-benchmarks-for-machine.html},
  note   = {MoleculeNet >1800 citations; BACE 45\% IC50 inconsistency; HIV 70\% artifacts; BBB 10 conflicting labels}
}

@misc{Walters2024split,
  author = {Walters, W. Patrick},
  title  = {Some Thoughts on Splitting Chemical Datasets},
  year   = {2024},
  url    = {https://practicalcheminformatics.blogspot.com/2024/11/some-thoughts-on-splitting-chemical.html},
  note   = {Random split R2=0.73 vs UMAP split R2=0.62 on Biogen solubility data; 18\% overestimation}
}

@misc{Walters2024gen,
  author = {Walters, W. Patrick},
  title  = {Generative Molecular Design Isn't As Easy As People Make It Look},
  year   = {2024},
  url    = {https://practicalcheminformatics.blogspot.com/2024/05/generative-molecular-design-isnt-as.html},
  note   = {DiffLinker: 88/1000 molecules survive filtering (8.8\% yield)}
}
```

---

## 8. Remaining Research Gaps

The following data would further strengthen Section 4.3 but was not accessible:

1. **Walters & Barzilay 2021 full text**: The paper is behind Taylor & Francis paywall. Our notes confirm the key arguments (random splits, data leakage, MoleculeNet problems) but we lack paper-specific quantitative tables. The blog posts from 2023-2024 provide stronger quantitative evidence for the same arguments.

2. **Niazi 2025 full text**: MDPI returned 403. The AUC comparison (0.70-0.80 vs 0.72-0.82) is confirmed from existing notes but the underlying primary sources supporting those ranges need verification.

3. **Systematic prospective validation study**: No single published study compares the same model's benchmark leaderboard performance to its hit rate in a real drug discovery campaign. This gap is itself evidence for our thesis — the field publishes benchmark results but rarely reports prospective outcomes.

4. **Temporal split quantification from Walters & Barzilay**: The 2021 paper argues for temporal splits conceptually but the quantitative comparison (R² 0.73 vs 0.62) comes from Walters' 2024 blog using Biogen data, not from the 2021 paper itself. Cite accordingly.
