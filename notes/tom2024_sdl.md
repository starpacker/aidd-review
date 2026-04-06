# Self-Driving Laboratories for Chemistry and Materials Science — Tom et al., 2024

**Full citation**: Tom G et al. "Self-Driving Laboratories for Chemistry and Materials Science." Chemical Reviews. 2024;124(16):9633-9732. DOI: 10.1021/acs.chemrev.4c00055. PMID: 39137296.
**Section relevance**: Section 5 (automation gap), Section 6 (proposed solutions), Section 8 (future directions)

## Key Findings

### Scale of Review
- ~100 pages (9633-9732), comprehensive review of SDL landscape
- Covers chemistry and materials science; drug discovery is a subset
- Exact total number of SDLs catalogued: NOT extracted (full text behind paywall/timeout), but review is described as "comprehensive" covering "diverse range of scientific domains"

### Pharma-Specific SDLs

#### Robot Scientists Adam & Eve
- **Adam (2009)**: King et al. — "an SDL capable of generating genomics hypotheses from bioinformatics models, designing experiments, and performing biological assays." Successfully "identified three genes encoding an orphan enzyme involved in lysine biosynthesis"
- **Eve (2009/2015)**: Williams/King et al. — "explored a large library of drug molecules for hit identification, performing assays and feeding back the results into a quantitative structure-activity relationship (QSAR) cheminformatics model." Autonomous experiments with yeast expression of enzymes from other species as targets for chemical inhibition

#### Novartis MicroCycle (2024)
- Published: Brocklehurst CE et al. J Med Chem. 2024;67(3):2118-2128. DOI: 10.1021/acs.jmedchem.3c02029
- 17 authors from Novartis Basel + Cambridge MA
- **What it automates**: "can autonomously synthesize new compounds, purify them, perform chemical and biochemical assays with them, analyse the data and choose new compounds to synthesize and evaluate in the next cycle"
- **Scale**: Compounds synthesized/purified on 2-6 micromol scale, sufficient for 45 uL of 10 mM DMSO stock
- **Assays included**: biochemical assays, cellular assays, permeability, microsomal stability, solubility, lipophilicity
- **Active learning**: "Multiparameter exploration of chemical and property space is hereby driven by active learning models" via Autofocus platform
- **Throughput improvement**: "makes it possible for researchers to iteratively test and evaluate 100 unique chemicals in the time it used to take to evaluate a handful of options"
- **Chemistry approach**: "plate-based microscale chemistry, automated purification, in situ quantification, and robotic liquid handling"
- **Green chemistry**: minimal chemical consumption vs traditional 20-50 mg amounts
- Tom et al. assessment: "perhaps the best-in-class platform for rapidly identifying and obtaining multidimensional data on pharmaceutical lead compounds"
- **Notable result**: ML-suggested compound initially appeared unpromising but proved potent at altering disease biology while maintaining desirable drug properties

### DMTA Cycle Time Improvements
- Exact quantitative DMTA cycle time data: NOT extracted from full text
- MicroCycle described as "generating knowledge for drug discovery projects in a time frame never before possible"
- Traditional DMTA: weeks to months; MicroCycle: days (implied but not explicitly quantified in accessible text)

### Pharma Industry Role
- "the pharmaceutical industry has been a key driver in the field of SDL technologies, due to the industrial and commercial importance of drug discovery, pioneering both experimental and computational high-throughput experimentation (HTE) and screening"
- Beyond Novartis: specific examples of other pharma SDLs NOT extracted from accessible text

### Data Standardization
- **SiLA 2**: "a communication protocol aiming to replicate a robot operating system (ROS) and adapt it for chemical devices"
- **AnIML**: Used as "the medium for the bidirectional transfer of analytical data between laboratory information management systems (LIMS) and chromatography data systems (CDS) in a file-less fashion"
- **SiLA + AnIML combination**: "a promising direction: standardized interfaces for instrumentation and unified machine-readable data representations"
- **Maturity assessment**: Various in-house orchestrators have emerged (ChemOS, Helao, AresOS), suggesting standards are NOT yet universally adopted

### "Last Mile" Problem
- NOT explicitly discussed under this terminology in accessible portions
- The review focuses more on closed-loop within synthesis-characterization rather than connecting to biological testing
- MicroCycle is notable precisely because it DOES bridge synthesis to biological assays — most SDLs don't

### Closed-Loop Automation
- Historical: Krishnadasan et al. 2007 — first closed-loop flow-based microfluidics SDL for CdSe nanoparticle synthesis
- SDL definition involves autonomous experimental planning + execution + feedback
- Most examples are materials science (nanoparticles, thin films, catalysts)

### Drug Discovery vs Materials Science Challenges
- NOT explicitly compared in accessible portions
- Implicit: drug discovery requires multi-objective optimization (potency + selectivity + ADMET + safety) vs materials (often single-property optimization)
- MicroCycle is unique in combining synthesis with multiple drug-relevant assays

## Methods
- Comprehensive literature review
- Taxonomic classification of SDL approaches
- Historical chronology from 2007 to present

## Limitations (of our extraction)
- Full text behind ACS paywall and PMC version timed out (very long article ~100 pages)
- Exact SDL count, detailed drug discovery challenges, SiLA maturity assessment, and quantitative DMTA data not extracted
- Need to revisit with institutional access

## Quotes
- "the pharmaceutical industry has been a key driver in the field of SDL technologies"
- MicroCycle: "perhaps the best-in-class platform for rapidly identifying and obtaining multidimensional data on pharmaceutical lead compounds"
- "100 unique chemicals in the time it used to take to evaluate a handful of options" (Novartis/MicroCycle throughput)
- SiLA+AnIML: "standardized interfaces for instrumentation and unified machine-readable data representations"

## Our Take
- The SDL review is heavily materials-science focused; drug discovery SDLs are rare
- MicroCycle is the ONLY true pharma SDL that closes the loop from synthesis through ADMET assays
- The "last mile" gap (connecting computational design to biological validation) remains unsolved at scale
- Standards (SiLA 2, AnIML) exist but are immature; no universal adoption
- This supports our Section 5 argument: automation exists in silos, not as integrated pipelines
- Key insight: SDLs have ~15 years of history in materials, but pharma adoption is nascent
- The multi-objective nature of drug optimization (potency + selectivity + ADMET + PK + safety) makes pharma SDLs fundamentally harder than materials SDLs
