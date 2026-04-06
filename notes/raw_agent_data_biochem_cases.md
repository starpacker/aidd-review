# Raw Agent Data: Biochemistry Domain Cases (pH, Enzymatic Hydrolysis, Solvation, CYP, Species Translation)

> Source: Agent "Research pH enzymatic hydrolysis cases" (2026-04-03)
> Status: Verified — specific drug names, mechanisms, clinical consequences, citations

---

## TOPIC 1: pH-Dependent Solubility Failures

### Dasatinib (Sprycel) — TKI for CML
- Weakly basic BCS Class II, highly pH-dependent solubility
- PPI co-administration reduces bioavailability 40-80%
- Even maximal staggering (22h after PPI): >40% AUC reduction
- **Clinical consequence**: 5-year OS with PPI: 79% vs without: 94% (HR 3.5, 95% CI 2.1-5.3, p<0.0001)
- Despite label warnings, >21% co-prescribed PPIs in practice
- **Why models miss**: Standard ADMET evaluates at pH 7.4, not full GI gradient (pH 1.2-6.8), nor polypharmacy context
- Citations: Eley 2009 J Clin Pharmacol PMID:19395585; Larfors 2023 Eur J Haematol DOI:10.1111/ejh.14059; Andersson 2025 J Clin Pharmacol DOI:10.1002/jcph.6173

### Atazanavir — HIV Protease Inhibitor
- Requires acidic gastric pH for dissolution
- PPI co-admin: **94% reduction in both AUC and Cmax**
- Essentially eliminates therapeutic drug levels
- **Why models miss**: Combined effect of pH on solubility AND P-gp efflux (pH-dependent for atazanavir) = compounding failure
- Citations: Tomilo 2006 Antimicrob Agents Chemother PMID:16503713; Agarwal 2014 Pharm Res PMID:24595498

### Erlotinib (Tarceva) — EGFR Inhibitor for NSCLC
- Plasma concentrations significantly reduced by gastric acid suppressants
- Clinically significant for cancer patients on PPIs for chemo-induced nausea
- Citations: Hilton 2018 Ther Drug Monit PMID:29995672; van Leeuwen 2023 ESMO Open DOI:10.1016/j.esmoop.2023.100831

---

## TOPIC 2: Enzymatic Hydrolysis / Metabolic Instability

### Oseltamivir (Tamiflu) — CES1 Variant-Dependent Activation
- Ethyl ester prodrug requiring CES1 hydrolysis to active metabolite
- CES1 variants (p.Gly143Glu, p.Asp260fs): severe reduction in catalytic efficiency
- Ex vivo: plasma esterases convert up to 31.8% of parent in 4h with wide interindividual variation
- **Additional**: clopidogrel inhibits CES1-mediated oseltamivir activation (drug-drug interaction)
- **Why models miss**: ADMET assumes uniform enzyme expression; CES1 polymorphism not routinely modeled
- Citations: Zhu 2009 Drug Metab Dispos PMID:19022936; Shi 2006 J Pharmacol Exp Ther PMID:16966469

### Species-Dependent Ester Hydrolysis (General Principle)
- CES distribution varies dramatically: rats = high plasma CES; humans/dogs = essentially absent plasma CES
- Human plasma: high butyrylcholinesterase (BChE) instead
- Curcumin diethyl disuccinate prodrug: markedly different hydrolysis rates across species
- **Why models miss**: ADMET trained on single-species data (often rat/mouse), can't predict human ester bond fate
- Citation: Ratnatilaka Na Bhuket 2019 RSC Adv DOI:10.1039/C8RA08594C

---

## TOPIC 3: Solvation and Water-Mediated Interactions

### HIV-1 Protease Inhibitors — WAT301 (Conserved Flap Water)
- Conserved structural water WAT301 mediates H-bonds between flap tips (Ile50/Ile50') and all peptidomimetic inhibitors (saquinavir, indinavir, ritonavir, nelfinavir)
- Acts as H-bond acceptor for flap NH groups AND H-bond donor to inhibitor carbonyls
- QM/MM: H-bond interactions through WAT301 overcome inhibitor strain
- In multidrug-resistant variants: WAT301 displaced = resistance mechanism invisible to implicit solvent docking
- **Why models miss**: Standard docking (AutoDock, Glide default) uses implicit solvent, misses ~3-5 kcal/mol WAT301 contribution
- Citations: Barillari 1996 JACS PMID:8789192; Karthik & Bhakat 2008 J Mol Model PMID:18351589; Sadiq 2018 JCTC PMC:6219750

### General Evidence — 85% of Complexes Have Bridging Waters
- Systematic PDB analysis: >85% of protein-ligand structures have ≥1 bridging water, mean 3.5 per complex
- Displacing/disrupting water bridges during lead optimization routinely yields less active inhibitors
- 2025 review: "Water in drug design: pitfalls and good practices"
- Citations: Expert Opin Drug Discov 2025 DOI:10.1080/17460441.2025.2497912; Krimmer 2023 JCIM PMC:9970846

---

## TOPIC 4: CYP Polymorphism-Related Failures

### Clopidogrel (Plavix) / CYP2C19 — Stent Thrombosis Deaths
- Prodrug requiring CYP2C19 activation
- Poor/intermediate metabolizers: 2-15% of population (up to 30% East Asian)
- Meta-analysis >9,000 patients: HR 1.57 for MACE; **HR 2.81 for stent thrombosis** in PM/IM
- Case report: simultaneous two-vessel subacute stent thrombosis from CYP2C19 polymorphism
- FDA black box warning 2010
- **Why models miss**: ADMET predicts which CYPs metabolize a compound, NOT pharmacogenomic consequences on clinical outcomes
- Citations: Mega 2010 JAMA PMC:3048820; Lee 2022 Clin Pharmacol Ther DOI:10.1002/cpt.2526; Kariyanna PMC:4983389

### Codeine / CYP2D6 — Pediatric Deaths
- Prodrug activated to morphine by CYP2D6
- Ultra-rapid metabolizers (>2 functional copies, 1-10%): excessive morphine production
- Multiple pediatric deaths after routine tonsillectomy/adenoidectomy
- Breastfed infant death from nursing mother who was UM
- **Why models miss**: Models predict metabolic pathway correctly but NOT population-level enzyme activity variation consequences
- Citations: Gasche 2004 NEJM DOI:10.1056/NEJMoa041888; Kelly 2013 NEJM DOI:10.1056/NEJMp1302454; FDA Black Box 2013

### Antidepressants / CYP2C19+CYP2D6 — 47% Mismatch
- 46.7% of MDD outpatients had phenotype-drug mismatch
- ~30% higher side-effect scores from week 8 onward
- PREPARE trial (first large European RCT): preemptive pharmacogenomics → 30% reduction in clinically relevant ADRs
- Citations: Swen et al. (PREPARE) Frontiers Pharmacol 2024; Nature Transl Psych 2024

---

## TOPIC 5: Species-Specific Translation Failures

### TGN1412 — Catastrophic Cytokine Storm (2006)
- CD28 superagonist antibody, dose 500x below safe animal dose
- Within 90 min: all 6 volunteers → life-threatening cytokine storm, multi-organ failure, ICU
- Mechanism: CD28 expressed on human CD4+ effector memory T-cells but NOT on equivalent cells in cynomolgus/rhesus macaques
- Animal binding affinity was similar → structural homology was MISLEADING
- **Why models miss**: Species-specific immune cell receptor expression patterns not in computational toxicity models
- Citations: Suntharalingam 2006 NEJM 355:1018-1028; Eastwood 2010 J Immunol PMC:2990151

### Fialuridine (FIAU) — 5 Deaths from Hepatotoxicity (1993)
- Antiviral for HBV, passed all preclinical species at 100x human doses
- Phase II: 7/15 severe hepatic failure + lactic acidosis; 5 died, 2 liver transplants
- Mechanism: human hENT1 has PEXN motif → mitochondrial targeting → mtDNA disruption; mouse/rat ENT1 has PAXS motif → no mitochondrial localization
- Motif swap experimentally confirmed causality
- **Why models miss**: Subcellular transporter localization difference across species = invisible to in silico
- Citations: McKenzie 1995 NEJM 333:1099-1105 PMID:7565947; Lee 2006 J Biol Chem PMID:16595656; Xu 2014 PLoS Med PMC:3988005

### Solanezumab & Bapineuzumab — Alzheimer's Translation Failure
- Both showed robust efficacy in transgenic mouse models (PDAPP, Tg2576)
- Both failed definitively in Phase III humans (solanezumab: 3 major trials; bapineuzumab: ARIA + no benefit)
- Transgenic mice overexpress APP mutations → artificial amyloid; lack tau pathology, neuroinflammation, neurodegeneration of human AD
- **Why models miss**: Disease biology fundamentally different across species
- Citations: Bhatt 2024 Expert Opin Drug Discov DOI:10.1080/17460441.2024.2348142; Salloway J Transl Med 2024

### Ximelagatran — Unpredicted Human Hepatotoxicity
- Direct thrombin inhibitor, no hepatotoxicity in ANY preclinical species
- Humans: 6% ALT >3x ULN, 3.4% >5x ULN → market withdrawal
- Associated with specific HLA alleles (DRB1*07, DQA1*02) = immune-mediated idiosyncratic
- **Why models miss**: HLA-mediated idiosyncratic toxicity is inherently species-specific
- Citation: Keisu & Andersson 2010 Bentham Science PMID:20020269

---

## Summary Table

| Topic | Drug | Mechanism Missed | Clinical Consequence | Key Citation |
|-------|------|-----------------|---------------------|-------------|
| pH solubility | Dasatinib | GI pH gradient + PPI | 5yr OS 79% vs 94% (HR 3.5) | Larfors 2023 |
| pH solubility | Atazanavir | pH dissolution + P-gp | 94% AUC reduction | Tomilo 2006 |
| Ester hydrolysis | Oseltamivir | CES1 polymorphism | Impaired activation | Zhu 2009 |
| Water interactions | HIV-1 PI (WAT301) | Bridging water in 85% complexes | Drug resistance | Karthik 2008 |
| CYP polymorphism | Clopidogrel/CYP2C19 | PM genotype | HR 2.81 stent thrombosis | Mega 2010 |
| CYP polymorphism | Codeine/CYP2D6 | UM genotype | Pediatric deaths | Gasche NEJM 2004 |
| Species translation | TGN1412 | CD28 cell-type distribution | Cytokine storm 6/6 | Eastwood 2010 |
| Species translation | Fialuridine | hENT1 mito targeting | 5 deaths, 2 transplants | McKenzie NEJM 1995 |
| Species translation | Solanezumab | Transgenic ≠ human AD | Phase III x3 failure | Bhatt 2024 |
| Species translation | Ximelagatran | HLA-mediated idiosyncratic | Market withdrawal | Keisu 2010 |
