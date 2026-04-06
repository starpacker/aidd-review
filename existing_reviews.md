# Landscape of Existing Reviews on AI-Driven Drug Discovery (2023-2026)

> Compiled 2026-04-03. Purpose: identify gaps and differentiation opportunities for our review.

---

## Category 1: General AI in Drug Discovery Overviews

### R1. AI-Driven Drug Discovery: A Comprehensive Review
- **Authors**: Multiple (ACS Omega team)
- **Journal**: ACS Omega, 2025
- **DOI**: 10.1021/acsomega.5c00549
- **Main angle**: Comprehensive survey of AI/ML methodologies (2019-2024) across the entire pipeline — target ID, lead discovery, hit optimization, preclinical safety. Covers deep learning, GNNs, transformers.
- **Gaps**: Primarily a methods taxonomy. Does NOT deeply analyze clinical failure modes, the biology vs. chemistry problem, or the disconnect between benchmark performance and real-world outcomes. No cascading failure analysis.

### R2. Artificial Intelligence in Small-Molecule Drug Discovery: A Critical Review of Methods, Applications, and Real-World Outcomes
- **Authors**: Multiple
- **Journal**: Pharmaceuticals (MDPI), 2025
- **DOI**: PMC12472608
- **Main angle**: Reviews AI from target ID to safety prediction; includes real-world case studies (ISM001-055, DSP-1181). Notes that AI augments rather than replaces traditional methods.
- **Gaps**: Acknowledges the benchmark-vs-reality gap but does not propose a systematic framework for understanding WHY the gap exists. Limited discussion of automation infrastructure and OoC integration.

### R3. Leading AI-Driven Drug Discovery Platforms: 2025 Landscape and Global Outlook
- **Authors**: Multiple
- **Journal**: Pharmacological Research (ScienceDirect), 2025
- **Main angle**: Compares 5 leading AI platform archetypes: generative chemistry, phenomics-first, integrated target-to-design, knowledge-graph repurposing, physics+ML design. Industry/market focus.
- **Gaps**: Platform-centric, business/market oriented. Does NOT analyze clinical translation failures or the biology problem. No discussion of organ-on-chip or wet-lab automation gaps.

### R4. Artificial Intelligence in Drug Development
- **Authors**: Multiple
- **Journal**: Nature Medicine, January 2025
- **Main angle**: State-of-the-art AI applications in small-molecule development — target ID, drug synthesis, clinical trial design. High-profile Nature Medicine publication.
- **Gaps**: Focuses on positive applications rather than systematic failure analysis. Does not deeply cover the Phase II "valley of death" for AI drugs or the automation gap.

### R5. Transformative Role of AI in Drug Discovery and Translational Medicine
- **Authors**: Multiple
- **Journal**: PMC, 2025 (PMC12406033)
- **Main angle**: Broad overview of AI innovations, challenges, and future prospects in drug discovery and translational medicine.
- **Gaps**: Another broad survey. No unique analytical framework; does not distinguish computational validation from clinical outcomes in a systematic way.

### R6. From Lab to Clinic: How AI Is Reshaping Drug Discovery Timelines and Industry Outcomes
- **Authors**: Multiple
- **Journal**: PMC, 2025 (PMC12298131)
- **Main angle**: Focuses on timeline compression — how AI shortens discovery from 4-6 years to 12-18 months. Documents industry outcomes.
- **Gaps**: Emphasizes speed gains but does not adequately address that faster discovery does NOT equal better clinical outcomes. Limited failure analysis.

### R7. AI and ML in Drug Discovery: From Lead Discovery to Clinical Validation (2020-2025)
- **Authors**: Multiple
- **Journal**: ScienceDirect (Computational Biology and Chemistry), 2025
- **Main angle**: Covers the full timeline from lead discovery through clinical validation, with data on AI-derived compounds in trials.
- **Gaps**: Linear pipeline view; does not model cascading failures between stages or the specific domain knowledge gaps (pH, enzymatic hydrolysis, ADMET) that computational papers ignore.

---

## Category 2: Clinical Translation Failures of AI Drug Candidates

### R8. How Successful Are AI-Discovered Drugs in Clinical Trials? A First Analysis and Emerging Lessons
- **Authors**: Jayatunga et al.
- **Journal**: Drug Discovery Today, 2024
- **DOI**: 10.1016/j.drudis.2024.103946 (PubMed: 38692505)
- **Main angle**: LANDMARK PAPER. First systematic analysis of AI-discovered drugs in clinical trials. Found ~300 AI-native biotechs, 67 drugs in clinical development. Phase I success: 80-90% vs. industry 40-65%. Phase II: drops back to ~28-40%, matching industry norms.
- **Gaps**: Quantifies the problem but does not deeply explain WHY Phase II drops. Limited discussion of the biology problem, target validation failures, or the role of preclinical model inadequacy. No proposed solutions.
- **KEY COMPETITOR**: Most directly relevant to our thesis. We must cite and differentiate from this paper.

### R9. The AI Drug Revolution Needs a Revolution
- **Authors**: Jacobson, R.D.
- **Journal**: npj Drug Discovery, 2025
- **DOI**: 10.1038/s44386-025-00013-6
- **Main angle**: CRITICAL PERSPECTIVE. Argues AI drug revolution is limited by "human-agnostic" approach. Scientists should leverage AI to measure human responses during preclinical stages. Need for functional human data including variability.
- **Gaps**: A perspective/opinion piece rather than comprehensive review. Does not provide detailed pipeline analysis, quantitative failure data, or concrete solutions beyond "incorporate human data." No discussion of automation or OoC.
- **KEY COMPETITOR**: Very close to our thesis. We must acknowledge and extend this argument with concrete data and solutions.

### R10. Progress, Pitfalls, and Impact of AI-Driven Clinical Trials
- **Authors**: Wilczok
- **Journal**: Clinical Pharmacology & Therapeutics (Wiley), 2025
- **DOI**: 10.1002/cpt.3542
- **Main angle**: Focuses on AI's role IN clinical trials (trial design, patient selection, digital twins) rather than AI-discovered drugs in trials. Discusses pitfalls of AI-optimized trial design.
- **Gaps**: Different focus — about AI for trial optimization, not about AI-designed molecules failing in trials. Does not address the computational-to-clinical translation gap for drug candidates themselves.

### R11. Has AI Reshaped Drug Discovery, or Is There Still a Long Way to Go?
- **Authors**: Shree Harini et al.
- **Journal**: Drug Development Research (Wiley), 2026
- **Main angle**: Critical assessment of whether AI has genuinely reshaped drug discovery or whether hype exceeds reality. Timely 2026 publication.
- **Gaps**: Not yet fully analyzed. Likely a broad perspective piece; need to check if it provides systematic failure analysis.

---

## Category 3: Generative AI for Molecular Design

### R12. Generative AI for Drug Discovery and Protein Design: The Next Frontier
- **Authors**: Multiple
- **Journal**: ScienceDirect (Current Opinion in Structural Biology), 2025
- **Main angle**: Reviews generative models (VAEs, GANs, transformers, diffusion models) for molecular and protein design. Covers PropMolFlow and other recent architectures.
- **Gaps**: Focuses on computational methods and benchmarks. Does NOT address whether generated molecules succeed in real biological testing, let alone clinical trials. Classic "CS paper ignoring biology" problem.

### R13. Generative AI for the Design of Molecules: Advances and Challenges
- **Authors**: Multiple
- **Journal**: Journal of Chemical Information and Modeling (ACS), 2025
- **DOI**: 10.1021/acs.jcim.5c02234
- **Main angle**: Technical review of generative methods for molecule design. Discusses advances and challenges in synthetic accessibility, target engagement.
- **Gaps**: Acknowledges challenges but from a computational perspective. Does not discuss the gap between generated molecules that look good in silico and their performance in wet-lab validation or clinical settings.

### R14. Large Language Models for Drug Discovery and Development
- **Authors**: Multiple
- **Journal**: Cell Patterns, 2025
- **Main angle**: Explores transformative impact of LLMs across drug discovery pipeline — from literature mining to molecular generation.
- **Gaps**: Focused on LLM capabilities; does not critically assess limitations in translating LLM-generated hypotheses to clinical outcomes. No wet-lab validation discussion.

### R15. Large Language Models and Their Applications in Drug Discovery: A Primer
- **Authors**: Lu et al.
- **Journal**: Clinical and Translational Science (Wiley), 2025
- **DOI**: 10.1111/cts.70205
- **Main angle**: Primer on LLM applications for clinical pharmacology and translational medicine audiences.
- **Gaps**: Introductory primer rather than critical review. Does not address failure modes or the gap between computational and clinical performance.

---

## Category 4: Self-Driving Labs / Automated Drug Discovery

### R16. Self-Driving Laboratories for Chemistry and Materials Science
- **Authors**: Tom, G. et al.
- **Journal**: Chemical Reviews, 2024 (Vol. 124, Issue 16, pp. 9633-9732)
- **DOI**: 10.1021/acs.chemrev.4c00055
- **Main angle**: DEFINITIVE REVIEW (100 pages). In-depth analysis of SDL technology — hardware, software, integration, applications across chemistry, materials science, genomics. Covers active learning, Bayesian optimization.
- **Gaps**: Primarily chemistry/materials science focused, NOT drug discovery-centric. Does not deeply address the pharma-specific challenges of integrating SDLs into drug discovery pipelines (ADMET, biology, clinical translation). Limited discussion of the gap between automated synthesis and biological validation.
- **KEY REFERENCE**: Must cite as the definitive SDL review.

### R17. Autonomous 'Self-Driving' Laboratories: A Review of Technology
- **Authors**: Multiple
- **Journal**: Royal Society Open Science, 2025
- **Main angle**: Reviews SDL technology for chemistry, materials, and biological sciences. Notes that today's most capable SDLs automate nearly the entire scientific method.
- **Gaps**: Broad technology review. Does not specifically address drug discovery clinical translation or the fragmentation problem in pharma lab integration.

### R18. AI Agents in Drug Discovery
- **Authors**: Multiple
- **Journal**: arXiv, 2025 (arXiv:2510.27130)
- **Main angle**: Reviews evolution from rule-based systems to agentic AI in drug discovery. Discusses autonomous agents that can reason from literature to executable automation code, with claimed >400x reduction in cycle time.
- **Gaps**: Optimistic about agent capabilities. Does not adequately address that autonomous labs have NOT yet demonstrated ability to discover validated drug candidates independently. Limited discussion of failure modes.

### R19. The Agentic Era: Why Biopharma Must Embrace AI That Acts, Not Just Informs
- **Authors**: Multiple
- **Journal**: PMC, 2025 (PMC12048886)
- **Main angle**: Argues biopharma needs agentic AI that takes action, not just provides information. Forward-looking perspective.
- **Gaps**: Advocacy piece rather than critical analysis. Does not discuss current limitations of agentic systems or provide failure case studies.

### R20. Agentic AI and the Rise of In Silico Team Science in Biomedical Research
- **Authors**: Multiple
- **Journal**: Nature Biotechnology, 2026
- **Main angle**: Discusses how agentic AI enables "team science" in silico — multiple AI agents collaborating on research tasks. Very recent Nature Biotech publication.
- **Gaps**: Forward-looking; likely does not address the gap between in silico team science and real-world drug discovery outcomes.

---

## Category 5: Organ-on-Chip for Drug Testing

### R21. Revolutionizing Drug Evaluation System with Organ-on-a-Chip and Artificial Intelligence: A Critical Review
- **Authors**: Multiple
- **Journal**: Biomicrofluidics (AIP), November 2025
- **Main angle**: Critical review of integrating OoC with AI for drug evaluation. Discusses how AI enhances processing and predictive capabilities of OoC platforms.
- **Gaps**: Focused on OoC+AI integration but from a bioengineering perspective. Does NOT connect to the broader drug discovery pipeline failures or discuss how OoC could specifically address the Phase II efficacy wall.

### R22. When AI Meets Organoids and Organs-on-Chips: Game-Changer for Drug Discovery?
- **Authors**: Multiple
- **Journal**: The Innovation: Life, 2024
- **Main angle**: Explores synergies between AI, organoids, and OoC systems. Argues this integration could be a "game-changer" for drug discovery.
- **Gaps**: Optimistic framing. Does not critically assess scalability limitations, standardization challenges, or the current disconnect between OoC and AIDD communities.

### R23. Organoids and Organs-on-Chips: Recent Advances, Applications in Drug Development, and Regulatory Challenges
- **Authors**: Multiple
- **Journal**: ScienceDirect, 2025
- **Main angle**: Reviews recent advances in organoids and OoC for drug development, including regulatory landscape (FDA Modernization Act).
- **Gaps**: Regulatory and technology focus. Limited discussion of AI integration or how OoC data could train ML models to improve clinical predictions.

---

## Category 6: ADMET and Specific Technical Reviews

### R24. Leveraging Machine Learning Models in Evaluating ADMET Properties
- **Authors**: Multiple
- **Journal**: ADMET and DMPK, 2025 (PMC12205928)
- **Main angle**: Reviews ML models for ADMET prediction — random forest, gradient boosting, deep learning. Notes ML outperforms traditional QSAR.
- **Gaps**: Technical ADMET focus only. Does not discuss the broader pipeline context or how ADMET prediction failures cascade into clinical failures.

### R25. AlphaFold3 in Drug Discovery: Capabilities, Limitations, and Applications
- **Authors**: Multiple
- **Journal**: bioRxiv, 2025
- **Main angle**: Comprehensive assessment of AF3 for drug discovery. Documents limitations: struggles with conformational changes >5A RMSD, GPCR selectivity issues, stereochemistry, dynamics.
- **Gaps**: AlphaFold-specific. Does not connect to broader pipeline failures or clinical translation challenges.

### R26. Review of AlphaFold 3: Transformative Advances in Drug Design and Therapeutics
- **Authors**: Multiple
- **Journal**: PMC, 2024 (PMC11292590)
- **Main angle**: Reviews AF3's transformative impact on drug design, including protein-ligand interaction prediction.
- **Gaps**: Largely positive assessment. Limited critical analysis of real-world limitations or integration challenges with downstream drug development.

---

## Gap Analysis: Where Our Review Fits

### What existing reviews cover well:
1. **Methods taxonomy** — AI/ML techniques are exhaustively catalogued (R1, R2, R5, R7)
2. **Platform landscape** — Commercial AIDD platforms are mapped (R3)
3. **SDL technology** — Self-driving lab hardware/software is comprehensively reviewed (R16, R17)
4. **OoC engineering** — Organ-on-chip fabrication and biosensing advances are documented (R21-23)
5. **Clinical trial statistics** — Phase I vs II success rates are quantified (R8)
6. **Generative models** — VAEs, GANs, diffusion models are thoroughly covered (R12, R13)

### What NO existing review adequately covers (OUR GAPS TO EXPLOIT):

1. **Cascading failure analysis across pipeline stages**: No review systematically traces HOW failures propagate from target selection -> molecular design -> ADMET -> preclinical -> clinical. Reviews treat stages in isolation.

2. **The "Chemistry Problem vs. Biology Problem" framing**: Jayatunga (R8) quantifies Phase II drop-off; Jacobson (R9) argues for human data. But NOBODY provides a systematic analysis of WHY solving the chemistry problem (Phase I success) does NOT solve the biology problem (Phase II failure). This is our core thesis.

3. **CS-Biochemistry knowledge gap**: No review critically examines how computational researchers' lack of domain expertise (pH dependence, enzymatic hydrolysis, protein dynamics beyond static snapshots, tissue-specific metabolism) leads to models that perform well on benchmarks but fail in practice.

4. **Honest assessment of AI agent capabilities**: Reviews on agentic AI (R18-20) are either advocacy pieces or arxiv preprints. No critical, evidence-based assessment of what AI agents CAN and CANNOT do in drug discovery, with concrete failure examples.

5. **OoC-AIDD integration gap**: Reviews on OoC (R21-23) and AIDD (R1-7) exist in separate universes. Nobody has written about how OoC can specifically address the Phase II efficacy wall, or how the disconnect between these communities hurts clinical translation.

6. **Automation fragmentation in pharma**: The SDL reviews (R16-17) focus on chemistry/materials. Nobody has written about the specific challenges of integrating automated systems across the pharma drug discovery pipeline (synthesis -> assay -> ADMET -> in vivo -> clinical), including vendor fragmentation, data standardization (SiLA 2, AnIML), and the "last mile" problem.

7. **Clinical perspective on computational claims**: No existing review is written from the perspective of someone with clinical trial experience examining computational claims. Our first author's clinical background (hospital director, clinical trial center director) provides a unique voice that pure CS or pure chemistry reviews lack.

---

## Category 7: Subtopic-Specific Reviews (Added 2026-04-03)

### R27. Wilczok D, Zhavoronkov A. "Progress, Pitfalls, and Impact of AI-Driven Clinical Trials"
- **Journal**: Clinical Pharmacology & Therapeutics, 2024. DOI: 10.1002/cpt.3542
- **Main angle**: No AI-discovered drugs have achieved clinical approval as of 2024. Identifies three AI business models (repurposing, new molecules for known targets, novel molecules for novel targets). Non-technical barriers: lack of industry standards/benchmarks, insufficient AI + traditional expertise integration.
- **Gap for us**: Aligns with our cascading failure thesis. We extend with deeper clinical perspective and quantitative pipeline-stage analysis.
- **Note**: Overlaps with R10 but has distinct co-author (Zhavoronkov/Insilico Medicine) and clinical trial focus.

### R28. Tang X, Dai H, Knight E, Wu F, Li Y, Li T, Gerstein M. "A survey of generative AI for de novo drug design: new frontiers in molecule and protein generation"
- **Journal**: Briefings in Bioinformatics, 2024. DOI: 10.1093/bib/bbae338
- **Main angle**: Comprehensive survey of VAEs, GANs, autoregressive transformers, diffusion models. Evolution from 1D SMILES to 2D graphs to 3D structures. Diffusion models achieve >98.5% atom stability. Notes >150 AI small-molecule drugs initiated. Equivariant GNNs as key architecture.
- **Gap for us**: Focuses on architectures without addressing synthesizability, ADMET compliance, or clinical translation of generated molecules.

### R29. "Diffusion Models in De Novo Drug Design"
- **Journal**: Journal of Chemical Information and Modeling, 2024. DOI: 10.1021/acs.jcim.4c01107
- **Main angle**: Dedicated diffusion model review for structure-based drug design: target-specific molecular generation, molecular docking, protein-ligand dynamics. Key challenge: chemical synthesizability of generated molecules.
- **Gap for us**: Does not connect computational generation quality to downstream biological/clinical outcomes.

### R30. "Diffusion Models at the Drug Discovery Frontier: A Review on Generating Small Molecules versus Therapeutic Peptides"
- **Journal**: Biology (MDPI), 2025.
- **Main angle**: Distinguishes small-molecule vs. peptide generation challenges. Small molecules: synthesizability. Peptides: proteolytic stability, folding, immunogenicity. Identifies data sparsity, lack of physics integration, unreliable metrics, scalability limitations.
- **Gap for us**: Useful for our section on generative model limitations. We can cite their physics-integration critique.

### R31. "Computational drug design in the artificial intelligence era: A systematic review of molecular representations, generative architectures, and performance assessment"
- **Journal**: Pharmacological Reviews, 2025.
- **Main angle**: Unified framework categorizing generative methods by drug representation (1D/2D/3D) and model type (VAE, GAN, RL, diffusion). Clarifies which models suit which molecular data types. Comprehensive evaluation methodology.
- **Gap for us**: Excellent methodological reference but does not address real-world validation or clinical outcomes.

### R32. Bran AM, Cox S, Schilter O, Baldassari C, White AD, Schwaller P. "ChemCrow: Augmenting large-language models with chemistry tools"
- **Journal**: Nature Machine Intelligence, 2024. DOI: 10.1038/s42256-024-00832-8
- **Main angle**: Original ChemCrow paper. GPT-4 + 18 chemistry tools. Autonomously planned insect repellent synthesis, organocatalysts, discovered novel chromophore. Proof-of-concept for tool-augmented LLM chemistry agents.
- **Gap for us**: Narrow proof-of-concept tasks, not real drug discovery workflows. Does not address regulatory requirements, scaling, or full AIDD pipeline.

### R33. Boiko DA, MacKnight R, Kline B, Gomes G. "Autonomous chemical research with large language models"
- **Journal**: Nature, 2023. DOI: 10.1038/s41586-023-06792-0
- **Main angle**: Coscientist. Multi-LLM agent automating experiment design, planning, and execution via robotic platforms. Web search, code execution, lab instrument control. High-impact Nature publication.
- **Gap for us**: Proof-of-concept. Neither ChemCrow nor Coscientist address the full AIDD pipeline, regulatory context, or scaling to real drug discovery.

### R34. "ChemToolAgent: The Impact of Tools on Language Agents for Chemistry Problem Solving"
- **Journal**: arXiv, 2024. arXiv:2411.07228
- **Main angle**: Tool augmentation does NOT consistently outperform base LLMs. Tools help for specialized tasks (synthesis prediction) but not for general chemistry reasoning. Important nuance for honest agent assessment.
- **Gap for us**: Supports our argument that AI agent capabilities are overstated in drug discovery contexts.

### R35. Silva A, Vale N. "Digital Twins in Personalized Medicine: Bridging Innovation and Clinical Reality"
- **Journal**: Journal of Personalized Medicine, 2025. DOI: 10.3390/jpm15110503
- **Main angle**: Reviews digital twins in cardiology, oncology, neurology, pharmacogenomics. Key finding: very few in routine clinical practice — most limited to pilots. Barriers: regulatory ambiguity, interoperability, ethics, computational infrastructure, algorithmic bias. RCTs inadequate for validating adaptive AI systems.
- **Gap for us**: Directly supports our bench-to-bedside gap thesis. We integrate with our clinical trial expertise.

### R36. "Digital twins, synthetic patient data, and in-silico trials: can they empower paediatric clinical trials?"
- **Journal**: Lancet Digital Health, 2025.
- **Main angle**: Focused on paediatric trials. Synthetic patient data and in-silico trials for populations where traditional trials are difficult.
- **Gap for us**: Niche application. We can cite for digital twin limitations in special populations.

### R37. Ding Q, Yao R, Bai Y, Da L, Wang Y, Xiang R, Jiang X, Zhai F. "Explainable Artificial Intelligence in the Field of Drug Research"
- **Journal**: Drug Design, Development and Therapy, 2025. DOI: 10.2147/DDDT.S525171
- **Main angle**: Bibliometric analysis of 573 XAI publications. Rapid growth since 2018. SHAP and attention mechanisms dominate. Persistent tension between accuracy and interpretability. No unified standards for interpretability validity assessment.
- **Gap for us**: We can argue XAI is necessary for regulatory acceptance and clinical trust, not just a technical nicety.

### R38. Lavecchia A. "Explainable Artificial Intelligence in Drug Discovery: Bridging Predictive Power and Mechanistic Insight"
- **Journal**: WIREs Computational Molecular Science, 2025. DOI: 10.1002/wcms.70049
- **Main angle**: Core XAI techniques (SHAP, LIME, saliency maps, attention, counterfactuals, causal inference). Black-box opacity limits pharmaceutical acceptance. XAI as bridge between prediction and mechanistic understanding.
- **Gap for us**: We connect interpretability requirements to regulatory/clinical decision-making, not just model transparency.

### R39. Venkataraman M, Rao GC, Madavareddi JK, Maddi SR. "Leveraging machine learning models in evaluating ADMET properties for drug discovery and development"
- **Journal**: ADMET & DMPK, 2025. DOI: 10.5599/admet.2772
- **Main angle**: ML outperforms QSAR for ADMET. Both classical (RF, SVM) and DL (GNN, transformers) effective, some >90% accuracy on specific endpoints. Multi-task learning as promising paradigm. Persistent challenges: data quality, interpretability, regulatory acceptance.
- **Gap for us**: Does not address domain-specific pitfalls (pH-dependent solubility, enzymatic hydrolysis, protein binding shifts) that our review uniquely highlights.

---

### Differentiation strategy for our review:
- **Title angle**: "Why AIDD pipelines fail in practice: the automation gap between benchmarks and bedside"
- **Unique contribution**: First review to systematically analyze cascading failures across the AIDD pipeline from a clinical perspective, proposing concrete solutions including OoC integration, standardized automation, and biology-first AI approaches.
- **Key differentiators vs. closest competitors**:
  - vs. Jayatunga (R8): We EXPLAIN why, not just quantify
  - vs. Jacobson (R9): We provide systematic analysis, not just a perspective
  - vs. Tom (R16): We focus on pharma, not materials science
  - vs. OoC reviews (R21-23): We connect OoC to AIDD pipeline failures
