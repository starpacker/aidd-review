# Research Inventory — AIDD Review Paper

> Last updated: 2026-04-03
> Purpose: Comprehensive catalog of all research materials, their depth, and remaining gaps

---

## Section 1: Introduction (~800 words, ~15 refs needed)

### Data Available
| Item | Source | Depth | Status |
|------|--------|-------|--------|
| AIDD market size ($2.9B→$12.5B) | Gemini (Precedence Research) | Secondary | ⚠️ No primary report downloaded |
| AIDD-specific VC ($17B since 2019) | PitchBook via Gemini | Secondary | ⚠️ Corrected from $420B but no primary data |
| Mega-rounds (Xaira $1B, Isomorphic $600M) | Press releases | Primary | ✅ |
| Phase I/II success rates | Jayatunga 2024 (DDT) | Primary paper read | ✅ Full text analyzed |
| BIO 2021 baseline rates | BIO/QLS 2021 report | Primary report | ✅ Key numbers verified |
| 173+ AI drugs in clinical dev | Axis Intelligence 2026 | Secondary | ⚠️ Not verified independently |
| No FDA-approved AI drug | Wilczok & Zhavoronkov 2025 | Primary | ✅ |
| Geographic concentration (CA+MA 60%) | Gemini | Secondary | ⚠️ Unverified |

### Gaps
- [ ] No primary PitchBook/CB Insights data downloaded
- [ ] "173+ AI drugs" number from Axis Intelligence not independently verified
- [ ] Geographic concentration claim needs primary source

### Refs in .bib: Jayatunga2024, Wilczok2025, Jacobson2025, BIO2021, Drews2000 (5/~15)

---

## Section 2: Pipeline Architecture (~800 words, ~20 refs needed)

### Data Available
| Item | Source | Depth | Status |
|------|--------|-------|--------|
| AlphaFold2/3 capabilities | Jumper 2021, Abramson 2024 | Primary papers | ✅ |
| AF3 limitations (kinase, GPCR, RMSD) | Zheng et al. 2025 (bioRxiv) | Deep-read | ✅ Quantitative data |
| ADMET evolution (40%→10-15%) | Kola & Landis 2004, Sun et al. 2022, Waring 2015 | Primary papers | ✅ Cross-verified |
| Virtual screening hit rates | General literature | Secondary | ⚠️ Need specific numbers |
| ADMET ML review | Venkataraman et al. 2025 | Primary | ✅ |
| Computational toxicology | Zhang 2025 (Brief Bioinf) | Primary paper | ✅ But historical vs current ADMET confusion noted |
| Solvation modeling limits | Mobley & Gilson 2017 | Primary paper | ✅ 2.5-2.8 kcal/mol salt effect |

### Gaps
- [ ] Virtual screening hit rates in practice (1-5%) — need primary source
- [ ] Knowledge graph target ID — no specific citation
- [ ] GWAS hits non-causal — need quantitative evidence (what % of GWAS targets are druggable?)

### Refs in .bib: 8/~20

---

## Section 3: Chemistry Problem / Successes (~600 words, ~12 refs needed)

### Data Available
| Item | Source | Depth | Status |
|------|--------|-------|--------|
| Rentosertib Phase IIa | Ren et al., Nature Med 2025 | **Full text PMC** | ✅ Complete clinical data |
| Zasocitinib Phase 2b | Armstrong et al., JAMA Derm 2024 | **Full text PMC** | ✅ AI attribution finding critical |
| Zasocitinib Phase III LATITUDE | Takeda press releases | Secondary | ✅ Key numbers verified |
| RLY-2608 (Relay) | Varkaris et al., Cancer Discov 2024 | Deep-read | ✅ Dynamo platform + Phase 1/2 data |
| Schrodinger FEP+ methodology | Nimbus/Schrodinger publications | Secondary | ⚠️ No primary methods paper read |
| Schneider 2018 MPO | Schneider, NRDD 2018 | Identified | ⚠️ Not deep-read |

### Gaps
- [ ] Rentosertib's complete AI pipeline (TNIK discovery → molecule generation → optimization) — we have overview but not step-by-step
- [ ] Insilico Medicine's Chemistry42/PandaOmics platform — no technical detail
- [ ] FEP+ validation data — Schrodinger published benchmarks, not in our notes

### Refs in .bib: 5/~12

---

## Section 4: Biology Problem / Failures (~1200 words, ~35 refs needed) ★ CORE

### 4.1 Phase II Efficacy Wall
| Item | Source | Depth | Status |
|------|--------|-------|--------|
| BEN-2293 failure details | BenevolentAI press, FierceBiotech | Secondary | ✅ But press-only, no paper |
| EXS-21546 termination | BusinessWire, Exscientia disclosures | Secondary | ✅ |
| REC-994 SYCAMORE trial | BioPharma Dive, Recursion disclosures | Secondary | ✅ |
| DSP-1181 discontinuation | Press releases | Secondary | ⚠️ Thin — no Phase I data |
| Jayatunga N=75, Phase II ~40% | Jayatunga 2024 full text | Primary | ✅ |
| NRDD termination analysis (3,180 trials) | Bowling et al. 2025 | Deep-read | ✅ Strategic 36%, efficacy 24% |

### 4.2 Cascading Valley of Death
| Item | Source | Depth | Status |
|------|--------|-------|--------|
| pH-dependent failures (dasatinib, atazanavir, erlotinib) | Multiple primary papers | Primary | ✅ Deep with clinical consequences |
| Enzymatic hydrolysis (oseltamivir, species CES) | Zhu 2009, Ratnatilaka 2019 | Primary | ✅ |
| Water-mediated interactions (HIV PI WAT301) | Barillari 1996, Karthik 2008, Sadiq 2018 | Primary | ✅ Deep |
| CYP polymorphisms (clopidogrel, codeine, antidepressants) | Mega 2010, Gasche 2004, PREPARE trial | Primary | ✅ Deep |
| Species translation (TGN1412, FIAU, solanezumab, ximelagatran) | NEJM, PNAS, Expert Opin | Primary | ✅ Deep |
| Ineichen 2024 (5% approval from animal testing) | PLOS Biology full text | Primary | ✅ 122 reviews, 4,443 studies |

### 4.3 Data Quality Crisis
| Item | Source | Depth | Status |
|------|--------|-------|--------|
| Publication bias (Begley 6/53, Prinz 25%) | Begley 2012, Prinz 2011 | Primary | ✅ |
| XAI reviews | Ding 2025, Lavecchia 2025 | Primary papers | ✅ |
| AI ≈ older methods | Niazi 2025 (Pharmaceuticals) | Single-author review | ⚠️ Not primary benchmarking |
| Generative model stability (>98.5%) | Tang et al. 2024 | Primary | ✅ |
| Benchmark limitations | Walters & Barzilay 2021 | Identified | 🔴 NOT deep-read — numbers missing |

### 4.4 Protein Dynamics Gap
| Item | Source | Depth | Status |
|------|--------|-------|--------|
| AF3 failures quantified | Zheng 2025 | Deep-read | ✅ |
| EGFR T790M | Yun 2008 | Primary | ✅ |
| Protein dynamics | Boehr 2009 | Primary | ✅ |
| Complex modalities (ASO) | Crooke 2021 | Primary | ✅ |
| ADC challenges | No specific citation | Missing | 🔴 Need ADC-specific AI limitation reference |

### Gaps
- [ ] BEN-2293: no peer-reviewed paper, only press releases
- [ ] DSP-1181: very thin — no Phase I data, no failure mechanism
- [ ] Benchmark-to-bedside gap: need SPECIFIC NUMBERS from Walters 2021
- [ ] ADC/complex modality AI limitations: no specific citation
- [ ] 🔴 **NO first-hand experimental validation** of any claim in this section

### Refs in .bib: ~15/~35

---

## Section 5: Automation Mirage (~800 words, ~20 refs needed)

### 5.1 Self-Driving Labs
| Item | Source | Depth | Status |
|------|--------|-------|--------|
| Tom et al. 2024 (100-page review) | Chemical Reviews | Deep-read | ✅ |
| Graff et al. 2021 (MolPAL) | Chemical Science | Primary | ✅ 94.8% from 2.4% |
| Novartis MicroCycle | Tom 2024 | Secondary | ✅ |
| Exscientia stats (70%/80%) | AWS case study | ⚠️ Self-reported marketing | ✅ Caveated |
| SiLA 2 / AnIML adoption | Tom 2024 | Qualitative | ⚠️ No adoption stats |

### 5.2 Fragmentation
| Item | Source | Depth | Status |
|------|--------|-------|--------|
| Hardware integration challenge | Tom 2024 | Qualitative | ✅ But no % quantification |
| "Last mile" problem | Tom 2024 | Qualitative | ⚠️ Thin |

### 5.3 LLM Agents
| Item | Source | Depth | Status |
|------|--------|-------|--------|
| ChemCrow | Bran et al., NMI 2024 | Deep-read + code analysis | ✅ |
| Coscientist | Boiko et al., Nature 2023 | Deep-read + code analysis | ✅ |
| ChemToolAgent | arXiv 2024 / NAACL 2025 | Deep-read | ✅ Key finding: tools hurt general reasoning |
| DruGUI pipeline | clawrxiv + GitHub | Code analysis | ✅ |
| ADMET-AI | Swanson et al., Bioinf 2024 | Code analysis | ✅ But R² claim unverified |
| Reproducibility crisis (3/4 repos) | Our code analysis | Primary observation | ✅ |

### Gaps
- [ ] No SDL cost data comparison (pharma vs materials SDL investment)
- [ ] 🔴 **Have not actually run any code** — claims based on repo inspection only
- [ ] Agent hallucination rates in chemistry: need specific numbers beyond ChemToolAgent
- [ ] No pharma company SDL beyond Novartis MicroCycle identified

### Refs in .bib: ~8/~20

---

## Section 6: Bridging the Gap (~1100 words, ~25 refs needed)

### 6.1 Better Preclinical Models
| Item | Source | Depth | Status |
|------|--------|-------|--------|
| Emulate Liver-Chip (87% sensitivity) | Ewart et al. 2022 | Primary | ✅ |
| DILITracer (82.34%) | Tan et al. 2025 | Primary | ✅ |
| Tak et al. (95.2% on OoC+CNN) | Front Bioeng 2024 | Primary | ✅ |
| FDA Modernization Act 2.0 | S.5002 text | Primary legislation | ✅ |
| FDA AI guidance (Jan 2025) | Federal Register | Primary | ✅ Excludes discovery |
| FDA animal phase-out (Apr 2025) | Press release | Primary | ✅ |
| ARPA-H CATALYST ($21M) | Press release | Secondary | ⚠️ No results |
| LivHeart multi-organ | Ferrari 2023 | Primary | ✅ |
| Emulate AVA (96-channel) | Company press | Secondary | ⚠️ No published ML data |
| OoC+AI silo claim | Our analysis | Novel claim | 🔴 Needs quantitative backing |

### 6.2 Human-AI Collaboration
| Item | Source | Depth | Status |
|------|--------|-------|--------|
| Jacobson 2025 argument | npj Drug Discov | Deep-read | ✅ |
| Cross-disciplinary teams | Schuhmacher 2023 NRDD | Identified | ⚠️ Different paper from originally cited |
| Clinician-in-the-loop | General concept | No specific citation | 🔴 Need specific examples |

### 6.3 Technical Roadmap
| Item | Source | Depth | Status |
|------|--------|-------|--------|
| Causal inference | Pearl 2009, Feuerriegel 2024 | Identified | 🔴 Thin — no drug discovery examples |
| Multi-omics | Hasin 2017 | Old reference | 🔴 Need 2024-2026 update |
| xAI | Ding 2025, Lavecchia 2025 | Primary | ✅ |
| Digital twins | Silva & Vale 2025 | One review | 🔴 Need more evidence |
| Benchmark reform | Walters & Barzilay 2021 | Identified | 🔴 Not deep-read |

### Gaps
- [ ] 🔴 OoC+AI silo claim lacks quantitative evidence (e.g., publication overlap analysis)
- [ ] 🔴 Causal inference examples in drug discovery very thin
- [ ] 🔴 Multi-omics section relies on 2017 reference
- [ ] 🔴 Digital twins: only one citation
- [ ] Clinician-in-the-loop: no published workflow example
- [ ] No mention of federated learning for multi-site drug data

### Refs in .bib: ~10/~25

---

## Section 7: Outlook (~500 words, ~8 refs needed)

### Data Available
| Item | Source | Depth | Status |
|------|--------|-------|--------|
| Rentosertib timeline | Nature Med 2025 | Primary | ✅ |
| Zasocitinib NDA timeline | Takeda guidance | Secondary | ✅ |
| RLY-2608 Phase 3 | Relay press | Secondary | ✅ |
| AI attribution debate | Our analysis + zasocitinib paper | Primary observation | ✅ |

### Gaps
- [ ] "15-20 AI-originated Phase III readouts in 2026" — unverified claim
- [ ] Need comprehensive list of AI drugs approaching pivotal trials

### Refs in .bib: 3/~8

---

## Cross-Cutting Gaps (Priority Order)

### 🔴 Critical — Must Address Before Drafting
1. **No first-hand experiments run** — ADMET-AI, DruGUI, ChemCrow all inspected but never executed
2. **Benchmark gap not quantified** — Walters 2021 not deep-read; no specific random vs temporal split numbers
3. **Causal inference in drug discovery** — Section 6.3 is hand-wavy; need concrete examples
4. **OoC+AI silo quantification** — unique contribution claim but evidence is anecdotal
5. **References.bib at ~75/~135** — need ~60 more entries

### 🟡 Important — Would Strengthen Paper
6. Multi-omics integration post-2017 updates
7. Digital twins evidence beyond one review
8. ADC/oligonucleotide AI limitations
9. Pharma SDL examples beyond Novartis
10. PitchBook primary data for investment claims

### 🟢 Nice to Have
11. Geographic concentration primary data
12. BEN-2293 peer-reviewed paper (may not exist)
13. Full Insilico Chemistry42 technical details
14. SiLA 2 adoption statistics
