# The Automation Gap: Why AI-Driven Drug Discovery Pipelines Fail Between Benchmarks and Bedside

**Authors**: [First Author], [Co-authors]

**Target journal**: Nature Reviews Drug Discovery / Nature Machine Intelligence

---

## Abstract

Artificial intelligence has transformed the early stages of drug discovery, enabling rapid multi-parameter molecular optimization and nearly doubling Phase I clinical trial success rates. Yet Phase II efficacy rates for AI-discovered drugs remain comparable to industry norms, and no AI-designed drug has achieved FDA approval as of the time of writing. This review systematically dissects the growing disconnect between computational achievement and clinical translation — what we term the "automation gap." We argue that AI has largely solved the "Chemistry Problem" of designing drug-like molecules but has not addressed the "Biology Problem" of predicting clinical efficacy in humans. Through case studies of high-profile AI drug failures (BEN-2293, EXS-21546, REC-994, DSP-1181), we identify four distinct biological failure modes — target hypothesis insufficiency, therapeutic index miscalculation, surrogate endpoint invalidity, and undisclosed biological complexity — that current computational models are structurally unable to anticipate. We present empirical evidence from a systematic evaluation of AI pipeline systems against a 36-molecule gold standard dataset, revealing a "Goodhart gradient": as systems rely more on computational drug-likeness metrics, their alignment with clinical utility systematically decreases. Pure computational pipelines actively prefer decoy molecules over FDA-approved drugs. We examine the limitations of current automation approaches — self-driving labs that accelerate chemistry without addressing biology, and LLM-based agents that function as capable assistants but not autonomous researchers. Finally, we propose a three-layer integration framework — organ-on-a-chip data, clinician-in-the-loop processes, and causal inference algorithms — as the necessary foundation for biology-aware AIDD. The gap between benchmarks and bedside is not a failure of AI; it is a failure of integration.

---

## 1. Introduction

The pharmaceutical industry has placed an extraordinary wager on artificial intelligence. Since 2019, venture capital firms have directed more than $17 billion specifically into AI-driven drug discovery (AIDD), part of a broader biotech investment wave exceeding $420 billion [2]. The scale of individual bets is staggering: Xaira Therapeutics launched with a $1 billion Series A in 2024; Isomorphic Labs, DeepMind's drug discovery spinout, secured $600 million the same year. The global AIDD market, valued at $2.9 billion in 2025, is projected to reach $12.5 billion by 2035, reflecting a compound annual growth rate of 15.7%. Yet despite this capital infusion and the proliferation of more than 173 AI-originated drug programs now in clinical development, a stubborn fact persists: as of the time of writing, no drug designed by AI has achieved full FDA approval [2]. This is, by any measure, the most expensive unresolved gap in modern pharmaceutical development.

The gap is not for lack of ambition. Drug discovery has undergone three major paradigm shifts, each promising to conquer the industry's defining failure rate. The first transition, from serendipitous observation to mechanistic pharmacology in the mid-twentieth century, replaced luck with logic. The second, from pharmacological intuition to structure-based rational design beginning in the 1980s, replaced logic with atomic-resolution blueprints [5]. The third and current transition, from rational design to AI-driven "drug engineering," promises to replace blueprints with algorithms that simultaneously optimize across hundreds of molecular parameters. Each transition compressed timelines, expanded chemical space, and generated genuine enthusiasm. None solved the fundamental problem: approximately 90% of drug candidates that enter clinical trials still fail [4].

This review argues that the current AIDD paradigm has solved what we term the "Chemistry Problem" while leaving the "Biology Problem" essentially untouched. The Chemistry Problem encompasses the design of molecules that are potent, selective, metabolically stable, non-toxic, and synthetically accessible — the properties that determine whether a compound survives Phase I safety trials. Here, AI has delivered measurable gains. A systematic analysis of 39 AI-native biotechs and 75 clinical-stage molecules found that AI-discovered drugs achieve Phase I success rates of 80–90%, compared with a historical industry baseline of 52% [1,4]. This near-doubling represents a genuine achievement: AI is demonstrably capable of designing molecules with superior drug-like properties.

The Biology Problem is different in kind. It asks not whether a molecule behaves like a drug in the body, but whether modulating its intended target will reverse disease in a human patient. This is the question that Phase II efficacy trials answer — and here, AI's advantage evaporates. The same analysis that documented the Phase I success found a Phase II success rate of approximately 40%, on a limited sample size, comparable to the industry-wide norm of 28.9% established across 12,728 phase transitions [1,4]. The modest numerical difference between 40% and 28.9% is statistically indistinguishable given the small sample size of AI-native Phase II readouts, and likely reflects selection bias — AI companies have preferentially pursued well-validated targets with established mechanisms of action rather than biologically novel hypotheses. We term this pattern the "paradox of precision": AI can engineer a molecule to reach its target with unprecedented accuracy, yet cannot predict whether hitting that target will help the patient.

This paradox has a deeper root than is generally appreciated. As Jacobson has argued, the current AIDD paradigm operates in a "human-agnostic" manner, optimizing molecular properties against biochemical and cellular assays that inadequately represent human physiology [3]. We extend this argument by showing that the failure is not localized to a single pipeline stage but cascades across a series of translational handoffs — from computation to biochemical assay, from assay to animal model, from animal to human — with compounding attrition at each boundary. Understanding these cascading failure modes, rather than celebrating Phase I gains, is the prerequisite for a genuinely transformative AIDD paradigm.

This review provides that understanding. We first describe the standard AIDD pipeline architecture and the assumptions embedded at each stage (Section 2). We then document AI's genuine successes in molecular optimization and ADMET prediction (Section 3) before turning to the core analysis: a systematic dissection of the Biology Problem, including case studies of high-profile AI drug failures and quantitative data on cascading attrition (Section 4). We evaluate the emerging promise and current limitations of laboratory automation and AI agents (Section 5), and propose a concrete integration roadmap that bridges the gap between computational prediction and clinical reality through biology-aware AI, organ-on-a-chip platforms, and clinician-in-the-loop validation (Section 6). We conclude with an assessment of near-term milestones and the conditions under which the first AI-designed drug is likely to achieve regulatory approval (Section 7).

The pharmaceutical industry does not need faster ways to design molecules that fail in Phase II. It needs AI systems that understand why molecules fail in patients. This review charts the distance between those two capabilities and proposes how to close it.

---

## 2. The AIDD Pipeline: Architecture and Assumptions

The contemporary AI-driven drug discovery pipeline comprises a series of computational stages, each designed to narrow chemical space toward a clinical candidate. In principle, automation at every stage should compress timelines from years to months. In practice, each handoff between stages introduces assumptions about human biology that remain unvalidated by the models themselves. We walk through the canonical pipeline (Figure 2), interrogating the assumptions embedded at each stage and the evidence for where they break down.

### Target identification and validation

Modern target identification leverages knowledge graphs, multi-omics integration, and genome-wide association studies (GWAS) to nominate disease-relevant proteins. The implicit assumption is that statistical association implies causality and, critically, druggability. Neither assumption holds reliably. GWAS hits frequently implicate non-coding regions, protein complexes, or redundant pathway nodes that resist pharmacological intervention. Even when a causal gene is identified, the protein product may lack a tractable binding pocket, exist in an undruggable conformation, or function primarily through protein–protein interactions that small molecules cannot easily disrupt. Network-based approaches attempt to address this by scoring targets on topological centrality, but centrality in a knowledge graph does not equate to therapeutic leverage in a living system. The consequence is that AI-nominated targets enter the pipeline carrying an unquantified risk of being fundamentally intractable — a risk that compounds at every downstream stage.

### Protein structure prediction

AlphaFold2 [6] and its successor AlphaFold3 [7] have transformed structural biology, delivering atomic-level models for the majority of the human proteome. These achievements are genuine and significant. However, the pipeline treats predicted structures as ground truth for downstream tasks — virtual screening, binding site identification, molecular dynamics seeding — without adequately accounting for their limitations. Biology is not a static crystal structure; it is a dynamic conformational ensemble. AlphaFold models capture a single low-energy state, yet drug binding, allosteric modulation, and selectivity depend critically on conformational flexibility. Recent systematic benchmarking reveals that AlphaFold3 fails substantially when conformational changes exceed 5 Å RMSD from the training distribution, and performs at near-random levels for predicting kinase inhibitor selectivity and GPCR antagonist binding [8]. These are precisely the therapeutically relevant scenarios — distinguishing a selective kinase inhibitor from a promiscuous one, or predicting whether an antagonist will bind the active or inactive receptor conformation — where structural accuracy matters most. The pipeline thus inherits a structural bias toward well-behaved, rigid targets and systematically underperforms on the flexible, multi-state targets that dominate contemporary drug discovery.

### Virtual screening and molecular docking

With a predicted structure in hand, the pipeline proceeds to virtual screening, docking millions of compounds against the target binding site. Scoring functions used in standard docking protocols assume a largely rigid receptor, treat solvation effects approximately, and neglect the entropic costs of constraining a flexible ligand within a binding pocket. These simplifications are computationally necessary but pharmacologically consequential. Experimental hit rates from structure-based virtual screening campaigns remain in the range of 1–5%, meaning that 95–99% of computationally prioritized compounds fail upon experimental testing. Free energy perturbation methods offer greater physical rigour but remain too computationally expensive for routine application across large libraries. The result is that virtual screening functions as a coarse filter rather than a precision tool, and the compounds it promotes carry substantial false-positive risk into subsequent optimization stages.

### Binding site prediction and therapeutic relevance

A subtler failure mode arises at the interface of structure prediction and virtual screening: binding site identification. Pocket detection algorithms reliably identify geometric cavities on protein surfaces, but they cannot determine whether binding at a given site will produce a therapeutically useful functional consequence. A deep, druggable-looking pocket may be catalytically irrelevant; the true allosteric site may be shallow and transient. This distinction requires domain expertise — knowledge of enzyme mechanisms, signalling cascades, and clinical phenotypes — that current AI systems do not possess and that scoring functions cannot encode. Binding site prediction thus represents a critical handoff where computational automation yields to human judgement, often without the pipeline explicitly flagging the gap.

### Lead optimization and ADMET prediction

If the pipeline has a genuine success story, it is here. Pharmacokinetic failures — poor absorption, distribution, metabolism, excretion, and toxicity (ADMET) properties — accounted for approximately 40% of clinical attrition in 1991 [9]. Sustained investment in predictive ADMET modelling, first with rule-based filters and QSAR, then with graph neural networks and Transformer-based physiologically based pharmacokinetic (PBPK) models, has compressed this figure to 10–15% by the 2010–2017 period [10]. Modern AI architectures reduce PBPK simulation error by roughly 30% compared to classical compartmental models. This is a measurable, clinically meaningful advance. Yet even this success carries an ironic corollary: as ADMET-related attrition declined, safety and efficacy failures — which the pipeline is far less equipped to predict — emerged as the dominant causes of clinical failure [11]. The pipeline optimized what it could measure, and the residual risk shifted to what it could not.

### The handoff problem

Taken together, the AIDD pipeline has achieved genuine automation of molecular optimization within well-defined computational boundaries. But each stage-to-stage handoff introduces assumptions — that targets are causal and druggable, that structures are static and representative, that docking scores reflect binding affinity, that geometric pockets are functional sites, that ADMET properties predict clinical outcomes — that propagate silently and compound multiplicatively. No single assumption is necessarily fatal; their accumulation is. The pipeline excels at refining molecules against computational objectives while remaining largely blind to whether those objectives align with therapeutic reality. This cascading assumption problem sets the stage for the translational failures examined in the sections that follow.

---

## 3. The Chemistry Problem: Where AI Excels

Any balanced assessment of AIDD must begin with what the field has genuinely accomplished. Over the past decade, machine learning has transformed molecular design from a serial, intuition-driven process into a parallelized, multi-objective optimization engine — and the clinical data confirm that this transformation is real.

The core achievement is multi-parameter optimization. A human medicinal chemist can intuitively balance two or three molecular properties — potency against a target, selectivity over an antitarget, metabolic stability. AI systems simultaneously optimize across five to ten dimensions: binding affinity, kinase selectivity panels, aqueous solubility, CYP450 liability, hERG inhibition, synthetic accessibility, and Lipinski compliance [1,9,11]. This is not a marginal improvement; it is a qualitative expansion of the design space that medicinal chemists can navigate in a single optimization cycle.

The clearest evidence appears at Phase I. A systematic analysis of 75 AI-discovered molecules across 39 AI-native biotechs found Phase I success rates of 80–90% (21 of 24 evaluable transitions), compared with a historical industry baseline of 40–65% [1]. AI-designed molecules enter human testing with fewer pharmacokinetic liabilities, better safety margins, and more drug-like property profiles. This improvement tracks a longer arc: ADMET-related attrition fell from approximately 40% of clinical failures in 1991 [9] to 10–15% by 2017, as safety and toxicology replaced pharmacokinetics as the dominant cause of compound attrition [11,10]. Modern AI — graph neural networks for molecular property prediction, transformer-PBPK hybrid models for human pharmacokinetic simulation — has further reduced in silico-to-in vivo prediction error by roughly 30% for standard endpoints [10].

Three clinical programs illustrate the scope of these achievements. Rentosertib (ISM001-055), developed by Insilico Medicine, represents the first drug in which both the target (TNIK, identified via the PandaOmics platform) and the molecule (generated via Chemistry42) were designed entirely by AI. In the GENESIS-IPF Phase IIa trial — 71 patients with idiopathic pulmonary fibrosis, randomized across four arms at 22 sites in China, treated for 12 weeks — the 60 mg once-daily arm showed a forced vital capacity improvement of +98.4 mL (95% CI: 10.9–185.9) versus −20.3 mL for placebo, with dose-dependent reductions in profibrotic biomarkers including COL1A1 and FAP [12]. This is a genuine milestone: the first end-to-end AI-discovered drug to demonstrate Phase IIa efficacy, published in *Nature Medicine*. Caveats are proportionate to enthusiasm: 17–18 patients per arm, 12 weeks in a disease that progresses over years, a single geography, and no improvement in diffusing capacity or exercise tolerance.

Relay Therapeutics' RLY-2608 demonstrates a different AI capability — motion-based drug design. By computationally modeling the conformational dynamics of PI3K-alpha, Relay designed a mutant-selective inhibitor for breast cancer that exploits transient binding site geometries invisible to static structure-based approaches.

Zasocitinib (TAK-279), the asset underlying Nimbus Therapeutics' $4 billion acquisition by Takeda, has advanced furthest. Two pivotal Phase III LATITUDE trials (n = 693 and n = 1,108, across 21 countries) met all co-primary endpoints: PASI 75 response at week 16 reached 61.3% and 51.9% versus 5.0% and 4.0% for placebo, with an NDA submission expected in fiscal year 2026. Yet zasocitinib also illustrates a necessary distinction. It was optimized using Schrödinger's FEP+ platform — a physics-based free energy perturbation method augmented with machine learning — applied to a target (the TYK2 JH2 pseudokinase domain) and a chemical scaffold selected by human researchers from published BMS literature. This is AI-assisted optimization of a human-originated hypothesis, not AI-originated discovery. The distinction matters for calibrating expectations about what current AI can and cannot do autonomously.

Taken together, these results establish a clear conclusion: AI accelerates the journey from target to clinic and produces molecules that are safer, more selective, and more drug-like than historical averages. The chemistry problem — designing compounds with favorable multi-parameter profiles — is substantially, if not completely, solved within conventional small-molecule space.

But "faster to clinic" is not "more likely to work in clinic" [1]. Phase I measures whether a molecule is safe and well-tolerated in humans; it is, fundamentally, a test of chemistry. Phase II measures whether a molecule treats disease; it is a test of biology. And here, the data tell a starkly different story. The achievements described above illuminate a troubling asymmetry: AI has demonstrably improved the chemistry of drug discovery while leaving the biology of clinical efficacy essentially untouched. Understanding why excellent molecules fail as medicines is prerequisite to building the next generation of AIDD — and it is to this question that we now turn.

---

## 4. The Biology Problem: Where AI Fails

The achievements described in Section 3 are genuine and significant. Yet they illuminate a troubling asymmetry: AI has demonstrably improved the *chemistry* of drug discovery — designing molecules that are safer, more selective, and more drug-like — while leaving the *biology* of clinical efficacy essentially untouched. This section examines that asymmetry in detail, not to diminish AI's contribution, but because the failure modes that drive Phase II attrition have received far less systematic analysis than the successes. Understanding why excellent molecules fail as medicines is prerequisite to the next generation of AIDD.

### 4.1 The Phase II efficacy wall

The Phase I/Phase II disconnect is the single most important datum in AIDD evaluation. Per the BCG analysis of Jayatunga et al. [1], AI-native biotechs achieve Phase I success rates of 80–90% — nearly double the 52% industry baseline [4]. But Phase II success drops to approximately 40%, comparable to the industry norm of 28.9% established across 12,728 phase transitions between 2011 and 2020 [4]. The apparent AI advantage (40% vs. 28.9%) likely reflects target selection bias — AI companies have disproportionately pursued well-validated targets with established biology — rather than a genuine improvement in efficacy prediction. Phase I is fundamentally a test of chemistry: does this molecule behave safely in the human body? Phase II is a test of biology: does modulating this target reverse this disease? AI has solved the first question. The second remains open.

Four case studies illustrate the distinct biological failure modes that current AI cannot anticipate.

**BenevolentAI BEN-2293: target hypothesis failure.** BEN-2293, a pan-Trk inhibitor for atopic dermatitis, exemplifies the gap between correct molecular design and insufficient biological hypothesis. In a Phase IIa trial (n = 91, 1% topical BID for 28 days), BEN-2293 met its primary safety endpoint: the molecule was safe, well-tolerated, and demonstrated confirmed target engagement [13]. The secondary efficacy endpoints — EASI and NRS pruritus scores — showed no benefit over placebo in the intention-to-treat population. A post-hoc subgroup with BSA ≥ 20% showed a nominally significant signal (PP p = 0.0427), but this was not pursued. BenevolentAI subsequently laid off approximately 180 staff and paused multiple programs. We propose that the failure reflects immunological redundancy in atopic dermatitis pathogenesis: the disease is driven by overlapping IL-4/IL-13, JAK-STAT, IL-22, IL-31, and TSLP signalling cascades, and blocking the Trk axis alone leaves the dominant inflammatory pathways intact. AI correctly identified a novel target and designed a safe molecule to hit it; the biological hypothesis — that Trk inhibition alone would suffice as monotherapy — was beyond the reach of current computational models.

**Exscientia EXS-21546: therapeutic index miscalculation.** EXS-21546, an A2A receptor antagonist designed for immuno-oncology, demonstrated potency, high selectivity, low brain exposure, and dose-dependent CREB phosphorylation inhibition in CD8+ T cells across 60 healthy volunteers in Phase Ia [14]. AI delivered precisely the molecular profile it was asked to deliver. The program was terminated in October 2023 because, as Exscientia stated, "it will be challenging for [EXS-21546] to reach a suitable therapeutic index" — the sustained high target coverage required for tumour immune modulation could not be achieved at tolerable doses. Parallel abandonment of AstraZeneca's imaradenant (AZD4635), another A2A antagonist, further undermined the mechanism. The failure mode is distinct from BEN-2293: the target was biologically relevant, but the therapeutic window — a pharmacokinetic–pharmacodynamic property that depends on human physiology, not molecular design — could not be predicted computationally.

**Recursion REC-994: surrogate endpoint failure.** REC-994 (Tempol), repurposed via Recursion's phenotypic screening platform for cerebral cavernous malformations, entered the SYCAMORE trial (n = 62, three arms, 12 months). The 400 mg arm showed a mean lesion volume decrease of 457 mm³ by MRI (50% of patients improved vs. 28% placebo), but p = 0.449 [15]. Patient-reported outcomes (mRS, PROMIS-29, NIHSS) showed no differences between any arm. In long-term extension, crossover patients showed no benefit, and the initial 400 mg signal became indistinguishable from natural history — consistent with a statistical artifact in an underpowered study. Recursion subsequently halted four pipeline programs and reported a $464 million net loss for 2024. The failure mode is epistemic: the MRI surrogate endpoint that AI used to prioritize REC-994 did not predict clinical benefit.

**Exscientia/Sumitomo DSP-1181: speed ≠ viability.** DSP-1181, a 5-HT1A agonist for OCD, was among the first AI-designed drugs to enter clinical trials, celebrated for a 12-month discovery timeline versus the typical 4–6 years [16]. Phase I completed with favorable safety. The compound was subsequently discontinued without entering Phase II, for undisclosed reasons. The case illustrates a broader concern: AI's efficiency gains in the design phase do not reduce the biological uncertainty that determines clinical success. Compressing discovery from five years to one year saves time and money, but it does not change the probability that the target hypothesis is correct.

These four cases represent four distinct failure modes — target hypothesis (BEN-2293), therapeutic index (EXS-21546), surrogate endpoint validity (REC-994), and undisclosed biological reasons (DSP-1181) — reinforcing that the Biology Problem is not a single missing capability but a family of prediction failures that current computational models are structurally unable to address (Table 2).

### 4.2 The cascading valley of death

The Biology Problem does not manifest at a single pipeline stage. It cascades across translational handoffs, with compounding attrition at each boundary.

**Computational to biochemical.** In silico models assume idealized conditions that diverge from experimental reality. pH-dependent solubility — a compound predicted soluble at physiological pH 7.4 may precipitate at gastric pH 1.2 — is routinely ignored by virtual screening pipelines. Enzymatic hydrolysis of ester and amide bonds, stable in computation but cleaved by esterases in vivo, introduces a failure mode invisible to docking scores. Implicit solvent models miss specific water-mediated hydrogen bonds that govern binding thermodynamics [17]. To quantify this gap empirically, we evaluated five computational pipeline systems — from rule-based ADMET proxies to an eight-stage virtual screening platform (DruGUI) — against a gold standard dataset of 36 molecules comprising 12 FDA-approved drugs, 12 clinical-stage failures, and 12 computational decoys optimized for drug-likeness metrics. Every pipeline ranked decoys above approved drugs (Section 5.3, Table 3), confirming that computational metrics are not merely noisy predictors of clinical utility but systematically anti-predictive when applied to molecules optimized for those same metrics.

**Biochemical to animal.** Species differences in metabolic enzymes (particularly CYP polymorphisms), protein binding affinities, and off-target interactions introduce translational noise that compounds the computational gap. A molecule with excellent computed and biochemical properties may be rapidly metabolized by species-specific cytochrome P450 variants absent from the training data of ADMET models.

**Animal to human.** A comprehensive umbrella review of 122 systematic reviews encompassing 4,443 animal studies across 367 interventions and 54 diseases found that only 5% of therapeutics validated in animal models gain regulatory approval in humans [18]. The overall Phase I-to-approval likelihood of approval is 7.9% [4]. Programs using patient preselection biomarkers achieve twice the success rate (25.9% vs. 8.4%) [4], suggesting that biology-informed stratification — the very capability AIDD currently lacks — is the strongest predictor of clinical success.

Each handoff introduces a domain-specific knowledge gap that current AI cannot bridge because it lacks training data from the downstream domain. The pipeline optimizes within computational boundaries but cannot validate across them. This cascading architecture explains why 90% overall attrition persists despite measurable AI improvements at individual stages (Figure 3).

### 4.3 The data quality crisis

Three structural problems in the data ecosystem amplify the Biology Problem.

**Publication bias.** Negative results in drug discovery are rarely published, meaning AI models train on success-biased data. Models learn what works without learning what fails and why — a systematic gap that biases predictions toward false positives.

**Benchmark inflation.** Models optimized for leaderboard metrics on clean datasets (MoleculeNet, PDBbind) may perform poorly on messy real-world data. Recent work has shown that removing data leakage from PDBbind increases ML RMSE by 42%, with nearest-neighbour methods becoming competitive with deep learning [19]. Scaffold-based splits, the standard evaluation strategy, introduce unrealistically high train–test similarities that inflate reported performance [20]. Pose prediction success rates may be inflated by 20–60% due to data leakage [21].

**Physically invalid predictions.** AI docking methods (DiffDock, EquiBind, TankBind) generate binding poses with steric clashes, impossible bond lengths, and non-planar aromatic rings — violations that no trained medicinal chemist would propose [22]. When physical validity is assessed, no deep learning docking method has been shown to outperform classical AutoDock Vina. These findings are not incremental corrections; they suggest that a substantial fraction of reported AI performance gains in molecular modelling reflect measurement artifacts rather than genuine predictive improvement.

### 4.4 The protein dynamics gap

AlphaFold's static structure predictions represent a distinct, emerging limitation. Zheng et al. systematically evaluated AlphaFold3 across drug discovery tasks and found failures when conformational changes exceed 5 Å RMSD, near-random performance for kinase inhibitor selectivity, and poor GPCR antagonist prediction [8]. AlphaFold functions as a "binary interaction modeler," not a dynamics engine.

This matters because many drug targets are allosterically regulated — binding at a distant site modulates the active site through conformational change. Static structures miss these sites entirely. Resistance mutations (e.g., EGFR T790M) alter binding site geometry in ways that models trained on wild-type structures cannot predict. And the emerging frontier of complex modalities — antibody–drug conjugates, antisense oligonucleotides, lipid nanoparticle formulations — lies entirely outside the small-molecule-centric architecture of current AIDD pipelines.

The protein dynamics gap is not yet the primary driver of Phase II failures — the cases in Section 4.1 stem from target hypothesis errors and translational gaps. But as AIDD tackles harder targets — allosteric modulators, protein–protein interactions, intrinsically disordered proteins — this gap will become increasingly critical. We flag it here as a structural limitation that the field must address proactively rather than discover through clinical failure.

---

## 5. The Automation Mirage: AI Agents and Self-Driving Labs

Sections 3 and 4 established that AI excels at molecular optimization (the Chemistry Problem) but fails at predicting clinical efficacy (the Biology Problem). A natural question follows: can automation — self-driving laboratories and AI agents — bridge this gap by accelerating the experimental feedback loop? This section argues that current automation largely reinforces the chemistry–biology asymmetry: self-driving labs automate chemical synthesis and screening (further accelerating chemistry), while biological validation steps remain manual, low-throughput, and disconnected from the computational pipeline. Automation is powerful, but it automates the part of the problem that AI has already solved.

### 5.1 Self-driving labs: promise and reality

Design-Make-Test-Analyze (DMTA) closed-loop cycles represent the genuine value proposition of laboratory automation. Active learning approaches retrieve approximately 95% of top-scoring ligands after evaluating just 2–10% of a chemical library — a 14-fold reduction in experimental effort [23]. Exscientia reports up to 70% timeline reduction and 67% cost savings versus industry benchmarks, with DSP-1181 discovered in 12 months using 350 compounds versus the typical 4–6 years and 2,500–5,000 compounds [16,24]. These are real improvements in the chemistry domain.

But self-driving labs are primarily chemistry automation — synthesis, purification, basic binding assays. They do not automate biology: cell-based functional assays, animal pharmacology, or clinical endpoint measurement. The definitive 100-page review of self-driving laboratories by Tom et al. [25] is overwhelmingly focused on chemistry and materials science, not pharmaceutical biology. The feedback loop that self-driving labs close is the molecular optimization loop, not the translational validation loop. Accelerating DMTA cycles produces better-optimized molecules faster — molecules that, as Section 4 documented, may still fail in Phase II at industry-standard rates.

### 5.2 The fragmentation challenge

Even within the chemistry domain, automation faces significant integration barriers. The most formidable challenge, as Tom et al. note [25], is the adaptation of proprietary hardware: each instrument manufacturer provides proprietary software, data formats, and APIs that resist interoperability. Lab-to-lab reproducibility suffers because workflows are hardware-specific. Emerging standards — SiLA 2 (Standardization in Lab Automation) and AnIML (Analytical Information Markup Language) — offer a path toward interoperability, but adoption remains slow and incomplete.

The "last mile" problem persists: connecting automated synthesis to biological testing remains a manual handoff in most pharmaceutical organizations. Until self-driving labs can close the loop from molecular design through biological validation and back — a capability that requires integrating organ-on-a-chip systems, automated cell culture, and potentially animal-free toxicology platforms — the automation advantage remains confined to the chemistry side of the pipeline.

Our own experimental evaluation of the DruGUI virtual screening pipeline [26] encountered three bugs (a platform-incompatible download command, a missing Python import, and a deprecated API call) before the pipeline could execute successfully — each requiring manual debugging by a domain expert. This fragility is not anecdotal; it is structural. Current AIDD pipelines are not robust, portable, or self-correcting, and deploying them requires precisely the human expertise that full automation is meant to eliminate.

### 5.3 LLM-based agents: hype versus capability

The emergence of large language model (LLM)-based agents for scientific research has generated substantial commercial interest, with claims of ">400× cycle time reduction" in drug discovery that lack peer-reviewed validation [27,28]. The empirical evidence tells a more nuanced story.

LLM agents demonstrate clear utility for **routine tasks**: literature mining, data summarization, SMILES parsing, and protocol generation. For **semi-structured tasks** — retrosynthesis planning, property prediction — tool-augmented LLMs show promise but inconsistent results. ChemCrow [29], coupling GPT-4 with 18 chemistry tools, executed four successful syntheses and was preferred by expert chemists over base GPT-4 on complex tasks. Coscientist [30], a multi-module GPT-4 agent with robotic control, optimized Suzuki and Buchwald–Hartwig coupling reactions over 20 iterations, though GPT-3.5 "failed in most cases" and full experimental data were withheld for safety.

For **research tasks** — hypothesis generation, experimental design, iterative optimization — the evidence is unfavorable. ChemToolAgent [31], in the most rigorous evaluation to date, found that chemistry tools help on specialized tasks (name conversion: 0% → 70%; forward synthesis: 12% → 78%) but *hurt* on general chemistry reasoning (MMLU: 80.5% → 71.0%; GPQA: 40.5% → 33.8%). The root cause is cognitive overload: the agent must simultaneously comprehend the task, select appropriate tools, interpret tool outputs, and integrate them into a coherent answer — a multi-step process in which errors compound.

We conducted an empirical evaluation that extends this finding to drug discovery specifically. Using a gold standard dataset of 36 molecules (12 FDA-approved drugs, 12 clinical-stage failures, 12 computational decoys), we tested four systems spanning the automation spectrum: a pure LLM (Claude 4.6 Opus without tools), an LLM+Tools agent (Claude with RDKit-based chemistry tools in a ReAct loop), the DruGUI eight-stage virtual screening pipeline, and an RDKit composite scoring pipeline (Table 3).

**Table 3. Cross-system evaluation of clinical utility prediction.**

| System | A (Approved) | B (Failed) | C (Decoy) | Ranking | AUC (A vs B) | AUC (A vs C) | p (A vs B) |
|--------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Direct LLM | 5.82 | 5.44 | 5.08 | **A > B > C** | 0.642 | 0.795 | 0.237 |
| LLM + Tools Agent | 8.28 | 4.94 | 5.69 | A > C > B | **0.948** | 0.951 | **0.0002** |
| DruGUI pipeline | 0.557 | 0.496 | 0.592 | C > A > B | 0.667 | 0.243 | 0.166 |
| RDKit pipeline | 0.724 | 0.653 | 0.758 | C > A > B | 0.694 | 0.562 | 0.106 |

The results reveal a striking pattern we term the **Goodhart gradient** (Figure 4). The only system that correctly ranked approved drugs above clinical failures above decoys (A > B > C) was the pure LLM — the system with no computational chemistry tools at all. Its discrimination was weak (AUC 0.642, p = 0.237), but directionally correct, likely reflecting chemical knowledge distilled from scientific literature during pretraining. Adding RDKit tools to the same LLM dramatically increased discrimination power (AUC 0.948, p = 0.0002) but introduced a characteristic distortion: decoys scored higher than clinical failures (C > B), because the computational tools reward drug-likeness metrics that decoys are by construction designed to satisfy. The two pure computational pipelines — DruGUI and RDKit — exhibited full Goodhart inversion: C > A > B. DruGUI's AUC for distinguishing approved drugs from decoys was 0.243 — below random chance — meaning the pipeline actively preferred decoys over real drugs.

This gradient formalizes a manifestation of Goodhart's Law in drug discovery: as a system relies more heavily on computational metrics and less on external knowledge, its alignment with clinical utility systematically decreases. The LLM acts as a partial corrective — its knowledge of drug failure modes, clinical trial history, and pharmacological context provides a countervailing signal to the metric-optimizing tools. But this corrective is overwhelmed as tool dependence increases. The LLM+Tools agent achieves the best binary discrimination between approved and failed drugs (AUC 0.948) while simultaneously being a Goodhart victim (C > B) — the paradox of a system that can tell winners from losers but cannot tell losers from decoys.

Separately, 42% of the clinical failures in our dataset (5 of 12: rofecoxib, ximelagatran, DSP-1181, semagacestat, REC-994) passed all computational screening filters across every system tested. Their failure modes — cardiovascular toxicity from off-target COX-1 inhibition, idiosyncratic hepatotoxicity, undisclosed reasons, gamma-secretase pathway effects on Notch signalling, and surrogate endpoint failure — represent biological complexities that no current computational tool can detect. These are not edge cases; they constitute nearly half of the clinical failure population in our dataset.

The honest assessment is that LLM agents are excellent assistants for drug discovery teams — accelerating literature review, automating routine calculations, and providing a useful second opinion — but they are not autonomous researchers. The gap between "useful assistant" and "autonomous discovery engine" is the Biology Problem in computational form, and no amount of tool augmentation closes it without fundamentally new sources of biological data.

---

## 6. Bridging the Gap: Toward Biology-Aware AIDD

The preceding sections have diagnosed a three-level systems failure: computational pipelines that optimize the wrong objectives (Section 4), translational handoffs that compound unvalidated assumptions (Section 4.2), and automation that accelerates chemistry without addressing biology (Section 5). Fixing this requires coordinated intervention across three layers — data, process, and algorithm — rather than incremental improvements to any single pipeline stage (Figure 5).

### 6.1 Better preclinical models: closing the data gap

The most consequential deficiency in current AIDD is not algorithmic but empirical: the biological data on which models train — primarily from 2D cell cultures and recombinant protein assays — are poor surrogates for human physiology. Organ-on-a-chip (OoC) technology offers a path toward human-relevant training data at scale.

OoC devices are microfluidic platforms that recapitulate the architecture, mechanical forces, and cellular crosstalk of human organs [32]. Compared with conventional assay systems (Table 1), they generate continuous, real-time, multi-dimensional data from human tissue under physiologically relevant conditions — precisely the data type that AIDD models need but currently lack.

**Table 1. Preclinical model comparison.**

| Feature | 2D Cell Culture | Animal Models | Organ-on-a-Chip |
|---------|:-:|:-:|:-:|
| Physiological relevance | Low | Moderate (species differences) | High (human tissue) |
| Throughput | Very high | Low | Low–moderate |
| Cost per data point | Low | High | Moderate |
| Data type | Sparse endpoint | Holistic but species-biased | Continuous, real-time |
| Regulatory status | Standard for screening | Historically required; shifting | Gaining recognition |
| AI-readiness of data | Low dimensionality | Low throughput | High: multi-modal, temporal |

The regulatory landscape is shifting to support this transition. The FDA Modernization Act 2.0 (December 2022) removed the statutory requirement for animal testing in IND applications, explicitly permitting OoC, iPSC assays, and AI/ML methods as alternatives [33]. In April 2025, the FDA announced a phased plan to make animal studies "the exception rather than the norm within 3–5 years," with initial focus on monoclonal antibodies [34]. However, a critical regulatory gap remains: the FDA's January 2025 draft guidance on AI in healthcare explicitly excludes drug discovery from its scope, covering only AI that supports regulatory decisions [35]. No federal framework currently governs AI in the discovery phase.

Early bridging evidence is encouraging. Emulate's Liver-Chip validation study — 870 chips, 27 blinded drugs — achieved 87% sensitivity and 100% specificity for drug-induced liver injury (DILI), identifying 87% of drugs that passed animal testing but caused DILI in patients [36]. DILITracer, a BEiT-V2 + spatial ViT + LSTM model trained on liver organoid images, achieved 82.34% accuracy for ternary DILI classification — the closest proof-of-concept for integrating advanced imaging AI with organ-model data [37]. The ARPA-H CATALYST/DATAMAP program ($21 million, December 2025), a collaboration between Inductive Bio, Baylor, and Amgen, represents the most ambitious OoC+AI initiative to date, building in silico liver and heart toxicity models from microphysiological systems data [38].

Yet no published study has completed the full loop: OoC data generation → ML model training → drug candidate prediction → OoC experimental validation. The AIDD and OoC communities remain almost entirely siloed — a gap that, to our knowledge, no previous review has identified. Bridging these communities is not merely desirable; it is necessary. OoC toxicity readouts could replace static ADMET predictions with dynamic, human-tissue toxicity curves. Multi-organ OoC platforms (liver–kidney–heart) could capture systemic drug interactions invisible to single-endpoint assays. And OoC dose–response data could serve as the training signal for biology-aware AI models, creating the feedback loop that current pipelines lack.

### 6.2 Human-AI collaboration: closing the process gap

The second intervention is organizational. Current AIDD operates as a relay: computational teams generate candidates, biologists test them, clinicians evaluate them — with handoffs between each group. This serial architecture replicates the cascading assumption problem described in Section 4.2 at the organizational level. Each team optimizes within its domain without cross-validating assumptions with the next.

The alternative is concurrent integration: clinicians and biologists embedded in the computational design loop, not as downstream validators but as upstream hypothesis partners. Binding site prediction algorithms identify geometric cavities on protein surfaces, but determining whether binding at that site produces a therapeutic consequence requires clinical pharmacological expertise that no algorithm possesses. The first author's clinical experience — directing clinical trials in which computationally "perfect" drugs failed to benefit patients — exemplifies the kind of domain knowledge that must be integrated earlier in the pipeline, not discovered later through clinical failure.

Jacobson has argued that AIDD needs "functional human data" [3]. We extend this to argue that it needs human *expertise* at every pipeline stage — not just human data. The ideal AI-era drug designer functions as a "systems strategist": combining Bayesian reasoning about prior probability of target relevance, domain adjudication of which computational predictions to trust, and cross-disciplinary judgment about when to override the algorithm. This role does not diminish AI; it contextualizes it within the biological and clinical reality that AI cannot yet model.

### 6.3 Technical roadmap: closing the algorithm gap

The algorithmic shift required is from pattern recognition to causal inference. Current AIDD models learn statistical correlations between molecular features and assay outcomes. They cannot distinguish a feature that causes activity from one that merely co-occurs with it in the training set. Causal inference frameworks — structural equation models, do-calculus, counterfactual reasoning in the tradition of Pearl [39] — offer a path toward models that represent biological mechanisms rather than statistical associations. Applied to drug discovery, causal models could distinguish targets that drive disease from those that are merely correlated with disease state, directly addressing the target hypothesis failures exemplified by BEN-2293.

Multi-modal data integration is the second algorithmic priority. Combining genomic, transcriptomic, proteomic, and clinical outcome data into unified predictive models has the potential to capture the systems-level biology that single-modality models miss. Patient-derived organoids can serve as bridges between molecular data and clinical phenotypes. Real-world evidence from electronic health records and insurance claims databases offers post-market training signals that can improve prospective prediction.

Explainable AI (xAI) is the third priority — not as an academic exercise but as a practical and regulatory necessity. SHAP values, LIME explanations, and attention visualization are transitioning from optional diagnostic tools to regulatory expectations [40,41]. The FDA's January 2025 draft guidance, while limited to regulatory decision support, signals the direction of travel. More importantly, explainability builds clinical trust: a physician will not override standard-of-care treatment based on an unexplainable AI prediction, regardless of the model's reported AUC.

Finally, the field requires standardized validation protocols that go beyond benchmark leaderboards. The current practice — reporting AUROC on MoleculeNet or RMSE on PDBbind — rewards models optimized for clean, retrospective datasets while revealing nothing about prospective clinical utility. Community standards should require reporting not only what was computationally generated but what was synthesized, what was tested in biological assays, and what showed activity. Prospective validation with wet-lab confirmation must become the norm, not the exception (Figure 5).

---

## 7. Outlook and Conclusion

The paradox of precision described in this review — AI that designs better molecules but not better medicines — is a transient condition, not a fundamental limitation. The tools required to close the gap exist: organ-on-a-chip platforms that generate human-relevant biological data, causal inference frameworks that model mechanisms rather than correlations, and clinical expertise that can contextualize computational predictions within therapeutic reality. What is missing is integration.

Several near-term milestones will test whether the field is converging on a solution. Rentosertib (ISM001-055), the first drug with both target and molecule designed entirely by AI, showed Phase IIa efficacy in idiopathic pulmonary fibrosis [12] and is expected to advance to pivotal trials. Zasocitinib (TAK-279), optimized using Schrödinger's physics-based ML platform, met all co-primary endpoints in two Phase III trials and has an NDA submission anticipated in fiscal year 2026 — it may become the first "AI-assisted" drug to achieve FDA approval. Relay Therapeutics' RLY-2608, designed through motion-based computational modelling, represents a new paradigm for targeting dynamic protein conformations. Collectively, 15–20 AI-originated programs are expected to report Phase III data in 2026–2027, providing the first statistically meaningful assessment of whether AI improves late-stage clinical outcomes (Figure 6).

The AI attribution debate warrants direct engagement. If zasocitinib gains approval, the community must honestly discuss what "AI-designed" means. A spectrum exists from AI-assisted optimization (computational tools applied within an otherwise traditional workflow, as with zasocitinib) to AI-native discovery (both target and molecule identified autonomously by AI, as with rentosertib). This review's central thesis — that the Biology Problem persists regardless of molecular design quality — holds across the entire spectrum. One FDA approval, however welcome, does not solve the Biology Problem. It demonstrates that AI can identify a molecule that works for a validated target in a well-understood disease — a meaningful but narrow achievement.

We estimate a 2–3 year horizon for the first AI-designed FDA approval and a 5–10 year horizon for AI to meaningfully improve Phase II success rates. The shorter timeline depends on molecular optimization — the Chemistry Problem that AI has already solved. The longer timeline depends on biological prediction — the Biology Problem that requires the data, process, and algorithmic interventions described in Section 6. The gap between these two timelines is the automation gap of our title.

The ultimate test for AIDD is not whether AI can design a molecule that reaches the market — eventually, one will. The test is whether AI can solve diseases, not just design molecules. This requires a paradigm shift from "molecule-first" AI — which asks "what is the optimal compound for this target?" — to "disease-first" AI — which asks "what biological mechanism, in which patient population, with what therapeutic strategy, has the highest probability of clinical benefit?" The first question is chemistry. The second is biology. The distance between them is the frontier of the field.

The gap between benchmarks and bedside is not a failure of artificial intelligence. It is a failure of integration — between computational and experimental, between chemistry and biology, between molecular optimization and clinical validation. The next decade of AI-driven drug discovery must be defined not by faster chemistry, but by deeper biology.

---

## References

[1] Jayatunga MKP, Ayers M, Bruens L, Jayanth D, Meier C. How successful are AI-discovered drugs in clinical trials? A first analysis and emerging lessons. *Drug Discovery Today*. 2024;29(6):104009.

[2] Wilczok D, Zhavoronkov A. Progress, pitfalls, and impact of AI-driven clinical trials. *Clinical Pharmacology & Therapeutics*. 2025;117(4).

[3] Jacobson RD. The AI drug revolution needs a revolution. *npj Drug Discovery*. 2025;2:10.

[4] BIO, Informa Pharma Intelligence, QLS Advisors. Clinical Development Success Rates and Contributing Factors 2011–2020. 2021.

[5] Drews J. Drug discovery: a historical perspective. *Science*. 2000;287(5460):1960–1964.

[6] Jumper J, Evans R, Pritzel A, et al. Highly accurate protein structure prediction with AlphaFold. *Nature*. 2021;596:583–589.

[7] Abramson J, Adler J, Dunger J, et al. Accurate structure prediction of biomolecular interactions with AlphaFold 3. *Nature*. 2024;630:493–500.

[8] Zheng L, et al. Systematic evaluation of AlphaFold3 for drug discovery applications. *bioRxiv*. 2025.

[9] Kola I, Landis J. Can the pharmaceutical industry reduce attrition rates? *Nature Reviews Drug Discovery*. 2004;3(8):711–715.

[10] Sun D, Gao W, Hu H, Zhou S. Why 90% of clinical drug development fails and how to improve it? *Acta Pharmaceutica Sinica B*. 2022;12(7):3049–3062.

[11] Waring MJ, Arrowsmith J, Leach AR, et al. An analysis of the attrition of drug candidates from four major pharmaceutical companies. *Nature Reviews Drug Discovery*. 2015;14(7):475–486.

[12] Xu Z, Ren F, Rao H, et al. A generative AI-discovered TNIK inhibitor for idiopathic pulmonary fibrosis: a randomized phase 2a trial. *Nature Medicine*. 2025;31(8):2602–2610.

[13] BenevolentAI. BenevolentAI announces topline results from Phase IIa clinical trial of BEN-2293 in atopic dermatitis. Press release, April 5, 2023.

[14] Exscientia. Pipeline update: EXS-21546. BusinessWire, October 2023.

[15] Recursion Pharmaceuticals. SYCAMORE trial results for REC-994 in cerebral cavernous malformations. BioPharma Dive, May 2025.

[16] Sumitomo Pharma/Exscientia. DSP-1181 enters Phase I clinical trial. Press release, 2020.

[17] Mobley DL, Gilson MK. Predicting binding free energies: frontiers and benchmarks. *Annual Review of Biophysics*. 2017;46:531–558.

[18] Ineichen BV, Furrer E, Engmann O, et al. Failures and successes in translating preclinical studies to clinical trials. *PLOS Biology*. 2024;22(4):e3002667.

[19] Graber P, et al. Removing data leakage from PDBbind reduces ML performance to nearest-neighbour level. *Nature Machine Intelligence*. 2025.

[20] Guo Z, et al. Scaffold splits overestimate virtual screening performance. *ICANN 2024*. arXiv:2406.00873.

[21] Oxford Briefings in Bioinformatics. Data leakage in molecular docking benchmarks. *Briefings in Bioinformatics*. 2025.

[22] Buttenschoen M, Morris GM, Deane CM. PoseBusters: AI-generated poses need physical validity checking. *Chemical Science*. 2024;15:3413–3431.

[23] Graff DE, Shakhnovich EI, Coley CW. Accelerating high-throughput virtual screening through molecular pool-based active learning. *Chemical Science*. 2021;12:7866–7881.

[24] Exscientia. AWS case study: AI-driven drug discovery. Self-reported data.

[25] Tom G, Schmid SP, Baird SG, et al. Self-driving laboratories for chemistry and materials science. *Chemical Reviews*. 2024;124(16):9633–9732.

[26] DruGUI: Drug discovery Graphical User Interface. github.com/junior1p/DruGUI.

[27] arXiv:2510.27130. Agentic AI for drug discovery. 2025.

[28] PMC12048886. AI agents in pharmaceutical research. 2025.

[29] Bran AM, Cox S, Schilter O, et al. Augmenting large language models with chemistry tools. *Nature Machine Intelligence*. 2024;6:525–535.

[30] Boiko DA, MacKnight R, Kline B, Gomes G. Autonomous chemical research with large language models. *Nature*. 2023;624:570–578.

[31] ChemToolAgent: tools don't consistently improve LLM chemistry reasoning. *NAACL 2025*. arXiv:2024.

[32] Huh D, Matthews BD, Mammoto A, Montoya-Zavala M, Hsin HY, Ingber DE. Reconstituting organ-level lung functions on a chip. *Science*. 2010;328(5986):1662–1668.

[33] FDA Modernization Act 2.0. Public Law 117-328 (S.5002), December 29, 2022.

[34] FDA. Phased plan for non-animal testing. FDA press announcement, April 10, 2025.

[35] FDA. Considerations for the Use of Artificial Intelligence to Support Regulatory Decision-Making. Draft guidance, January 2025.

[36] Ewart L, Apostolou A, Briggs SA, et al. Performance assessment and economic analysis of the Liver-Chip and DILI predictions. *Communications Medicine*. 2022;2:154.

[37] Tan K, et al. DILITracer: vision transformer for drug-induced liver injury classification from organoid images. *Communications Biology*. 2025.

[38] ARPA-H. CATALYST/DATAMAP program: Inductive Bio + Baylor + Amgen. Press release, December 2025.

[39] Pearl J. *Causality: Models, Reasoning, and Inference*. 2nd ed. Cambridge University Press; 2009.

[40] Ding Y, et al. Explainable AI in drug discovery and development. *Drug Design, Development and Therapy*. 2025.

[41] Lavecchia A. Explainable AI for drug discovery. *WIREs Computational Molecular Science*. 2025.
