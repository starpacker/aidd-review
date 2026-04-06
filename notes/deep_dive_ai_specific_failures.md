# Deep Dive: What Is AI-SPECIFIC About AIDD Failure Modes?

> Date: 2026-04-04
> Status: Complete — CRITICAL for differentiating from general drug discovery critique

---

## The Critic's Challenge

"The Biology Problem is not AI-specific — traditional drugs also fail Phase II at ~70%. Your cascading failure (0.003%) applies equally to traditional HTS. What's AI-SPECIFIC about your criticism?"

## The Rebuttal

**While the Biology Problem is universal, AI introduces six categories of failure that do not exist in traditional drug discovery, and amplifies certain existing failure modes through false confidence.**

---

## 1. Six AI-Specific Failure Modes

### 1.1 Illusory Performance (Data Leakage / Benchmark Inflation)
- **Graber et al. 2025 (Nature Machine Intelligence)**: removing PDBbind leakage → ML RMSE increases 42%; nearest-neighbor competitive with DL
- **Guo et al. (ICANN 2024, arXiv 2406.00873)**: even Bemis-Murcko scaffold splits introduce unrealistically high train-test similarities → "Scaffold Splits Overestimate Virtual Screening Performance"
- **Oxford Briefings in Bioinformatics 2025**: data leakage inflates pose RMSD <2Å success rates by **20-60%** and binding-affinity Pearson R by **0.15-0.30**
- **Why AI-specific**: Traditional HTS has no "training set." Screen performance IS real performance. No possibility of data leakage because no model to leak into.

### 1.2 Physically Invalid Predictions
- **PoseBusters (Buttenschoen et al., Chemical Science, 2024)**: AI docking methods (DiffDock, EquiBind, TankBind) generate poses with steric clashes, impossible bond lengths, non-planar aromatics
- **No DL docking method outperformed** classical AutoDock Vina/GOLD when physical validity assessed
- **Why AI-specific**: A medicinal chemist never proposes impossible bond angles. Traditional workflow has built-in physical reality constraints. AI models violate basic physics while appearing to succeed on benchmarks.

### 1.3 Hallucinated/Unsynthesizable Molecules
- Generative models routinely produce unsynthesizable or prohibitively expensive molecules
- Walters 2024: 1,000 DiffLinker molecules → 88 (8.8%) survive basic filters; 1 structure appeared 145 times
- **Why AI-specific**: Traditional medchem proposes modifications the chemist knows how to make. Generation grounded in synthetic feasibility because the chemist IS the generator. AI separates generation from synthesis.

### 1.4 Training Distribution Bias (Hidden)
- >90% training data Ro5-compliant → systematic failure for bRo5
- AlphaFold2: conformations biased toward PDB activation state distribution (55% inactive/37% active for class A GPCRs)
- Generative models biased toward known kinase chemotypes if pre-training data lacks diversity
- **Why AI-specific**: Traditional medchem creativity is NOT bounded by a training distribution. Chemists CAN deliberately explore beyond known space (AbbVie macrocycles, PPI inhibitors). AI models literally cannot generate what they haven't been trained on — and the failures are invisible (never proposed).

### 1.5 Black Box vs Interpretable SAR
- DL: no mechanistic explanation for predictions (Lavecchia, WIREs 2025)
- Traditional SAR: explicit, testable hypotheses ("methyl group fills hydrophobic pocket")
- **Why AI-specific**: When traditional SAR is wrong, chemist diagnoses WHY and learns. When AI SAR is wrong, no feedback on what went wrong → repeated failures in same blind spots. Traditional failures are informative; AI failures are opaque.

### 1.6 Uncalibrated Confidence (No "I Don't Know")
- Standard DL models produce **overconfident predictions for out-of-distribution** samples (PMC9391523; Nature Communications 2025)
- High prediction probabilities even in low-confidence situations → false positives into validation
- Most models lack calibrated uncertainty
- **Why AI-specific**: Traditional medchemists have calibrated intuition — they know when they're guessing. AI models give equally confident predictions whether in-distribution or completely novel → dangerous illusion of certainty.

---

## 2. Breadth vs Depth Tradeoff (AI-Specific Risk)

### Traditional medchem:
- ~100-500 compounds/program
- Deep understanding of each compound's SAR, PK, metabolism, synthesis
- Each modification hypothesis-driven
- **Failures generate mechanistic understanding**

### AI-driven:
- 10M-500M virtual compounds screened
- Shallow computational evaluation of each
- Prioritization by scoring functions with known limitations
- **Failures generate training data but not necessarily understanding**

### Unique risk:
- Traditional fails **deep** (you know why compound #237 didn't work)
- AI fails **wide** (screened 10M but can't explain why top 100 hits all failed in assay)
- "Breadth without understanding" is fundamentally new

---

## 3. Speed-to-Clinic Risk (AI-Amplified)

- DSP-1181: 12 months discovery → Phase I → discontinued (faster ≠ better)
- Chemistry World critique: AI "like selling a car by highlighting its windows roll up quickly"
- Derek Lowe: "Speeding up screening is nice, but clinical failure is the real problem — all that other stuff is a roundoff error"
- AI compresses preclinical timelines 30-40% but **no evidence this translates to better clinical outcomes**
- Concern: speed creates pressure to skip validation steps traditional programs perform because they have more time

---

## 4. Organizational Integration Gap (AI-Specific)

- Traditional: integrated teams (medchemists + pharmacologists + biologists + clinicians) in same org
- AI: CS/ML teams often separate from biology teams
- CAS 2025: "connecting chemistry and biology teams requires more than shared data standards — demands unified governance structures"
- Frontiers in Bioinformatics 2023: "hype from executive leadership can lead to expectation-reward error, severing trust between computational and bench scientists"
- **Input data generation, AI execution, and validation often fall within separate groups**

---

## 5. Leading Critics' Views

### Derek Lowe (In the Pipeline, Science/AAAS):
- "The problems we want to solve are **almost inversely proportional to AI's ability to solve them**"
- "Better target selection and human toxicity prediction kill most programs... not yet within AI's reach"
- "The synthetic organic chemistry literature is a mess" — AI trained on biased, inconsistent data
- Self-described "short-term pessimist, long-term optimist"

### Pat Walters (Relay Therapeutics):
- Nature Machine Intelligence 2024: "absence of standardized datasets has led to a **growing gap between perceived progress and real-world impact**"
- Walters & Murcko (Nature Biotechnology, 2020): generative models produce "close structural analogs of known actives" — novelty overstated
- PoseBusters: AI docking generates physically invalid poses
- Called for industry-led initiative to critically assess ML for real-world drug discovery

### Anthony Nicholls (OpenEye):
- Applied quality criteria to 728 structures for docking validation → **only 17% acceptable**
- Validation data itself is compromised → models trained on flawed structures

---

## 6. The Correct Framing for the Paper

**"The Biology Problem is universal, but AI introduces novel failure modes upstream that compound the universal problem downstream. Traditional drugs fail in Phase II because biology is hard. AI drugs fail in Phase II because biology is hard AND because computational artifacts upstream create a false sense of confidence that the chemistry problem has been more thoroughly solved than it actually has."**

**More concisely**: "Traditional drug discovery fails honestly — each failure teaches something. AI drug discovery can fail opaquely — not through fraud, but through systematic methodological artifacts (data leakage, distribution bias, uncalibrated confidence) that create an illusion of progress where none exists."

---

## 7. Implications for Outline Structure

### Add to Section 4.3 (Data Quality Crisis):
- PoseBusters evidence (physically invalid predictions)
- Leakage quantification (20-60% inflation)
- Uncalibrated confidence as a new subsection

### Add to Section 5 (Automation Mirage) — reframe as:
- Automation **amplifies** AI-specific failure modes: faster screening of more molecules with less understanding per molecule
- SDL automation addresses chemistry (what AI already solved) not biology (what remains unsolved)

### Add to Introduction:
- The "six AI-specific failure modes" as a preview of the unique contribution this review makes
- Traditional drug discovery critique exists (plenty of reviews); AI-SPECIFIC failure analysis does NOT exist

---

## Key New References

- Buttenschoen et al., Chemical Science, 2024 — PoseBusters
- Guo et al., arXiv 2406.00873 / ICANN 2024 — scaffold splits overestimate
- Oxford Briefings in Bioinformatics 2025 — leakage quantification (20-60%)
- Walters & Murcko, Nature Biotechnology, 2020 — generative model novelty critique
- Walters, Nature Machine Intelligence, 2024 — perceived vs real progress gap
