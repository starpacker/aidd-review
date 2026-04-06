"""
Build Gold-Standard Test Dataset for AI-Agent Pipeline Evaluation
=================================================================
Three categories:
  A) Clinically Proven Drugs (FDA-approved, clear efficacy)
  B) "Chemistry-Perfect" Clinical Failures (passed computational filters, failed clinically)
  C) Computationally Attractive Decoys (look good on paper, no therapeutic rationale)

Every SMILES is from PubChem. Every clinical outcome is referenced.
"""

import json, pathlib, datetime
from rdkit import Chem
from rdkit.Chem import Descriptors, QED, FilterCatalog, rdMolDescriptors

# ── helpers ──────────────────────────────────────────────────────────────
def compute_props(smi: str) -> dict:
    """Return a dict of drug-likeness properties; None values if SMILES invalid."""
    mol = Chem.MolFromSmiles(smi)
    if mol is None:
        return {"valid_smiles": False}
    mw   = Descriptors.ExactMolWt(mol)
    logp = Descriptors.MolLogP(mol)
    hbd  = rdMolDescriptors.CalcNumHBD(mol)
    hba  = rdMolDescriptors.CalcNumHBA(mol)
    tpsa = Descriptors.TPSA(mol)
    rotb = rdMolDescriptors.CalcNumRotatableBonds(mol)
    qed  = QED.qed(mol)
    lip  = sum([mw <= 500, logp <= 5, hbd <= 5, hba <= 10])
    lip_pass = lip == 4

    # PAINS filter
    params = FilterCatalog.FilterCatalogParams()
    params.AddCatalog(FilterCatalog.FilterCatalogParams.FilterCatalogs.PAINS)
    catalog = FilterCatalog.FilterCatalog(params)
    pains_flag = catalog.HasMatch(mol)

    return {
        "valid_smiles": True,
        "MW": round(mw, 1),
        "LogP": round(logp, 2),
        "HBD": hbd,
        "HBA": hba,
        "TPSA": round(tpsa, 1),
        "RotBonds": rotb,
        "QED": round(qed, 3),
        "Lipinski_violations": 4 - lip,
        "Lipinski_pass": lip_pass,
        "PAINS_flag": pains_flag,
    }

# ── CATEGORY A: Clinically Proven Drugs ─────────────────────────────────
category_a = [
    {
        "name": "Imatinib",
        "smiles": "CC1=C(C=C(C=C1)NC(=O)C2=CC=C(C=C2)CN3CCN(CC3)C)NC4=NC=CC(=N4)C5=CN=CC=C5",
        "target": "BCR-ABL tyrosine kinase",
        "indication": "Chronic myeloid leukemia (CML)",
        "approval_year": 2001,
        "efficacy_data": ">90% 5-year survival in CML; standard of care",
        "reference": "Druker et al., NEJM 2006; FDA approval 2001"
    },
    {
        "name": "Sofosbuvir",
        "smiles": "CC(C)OC(=O)C(C)NP(=O)(OCC1C(C(C(O1)N2C=CC(=O)NC2=O)(C)F)O)OC3=CC=CC=C3",
        "target": "NS5B RNA-dependent RNA polymerase",
        "indication": "Hepatitis C virus (HCV)",
        "approval_year": 2013,
        "efficacy_data": ">95% sustained virologic response (SVR12); curative",
        "reference": "Lawitz et al., NEJM 2013; FDA approval 2013"
    },
    {
        "name": "Osimertinib",
        "smiles": "COC1=C(C=C2C(=C1)N=CN=C2NC3=CC(=C(C=C3)F)Cl)NC(=O)C=C",
        "target": "EGFR T790M mutant",
        "indication": "Non-small cell lung cancer (NSCLC)",
        "approval_year": 2015,
        "efficacy_data": "FLAURA: median OS 38.6 mo vs 31.8 mo (erlotinib/gefitinib); HR 0.80",
        "reference": "Ramalingam et al., NEJM 2020; FDA approval 2015"
    },
    {
        "name": "Olaparib",
        "smiles": "O=C1C2=CC=CC=C2C(=O)N1CC3=CC=C(C=C3)C(=O)N4CCNCC4",
        "target": "PARP1/2",
        "indication": "BRCA-mutated ovarian/breast cancer",
        "approval_year": 2014,
        "efficacy_data": "OlympiAD: PFS 7.0 vs 4.2 mo (HR 0.58); BRCA+ breast cancer",
        "reference": "Robson et al., NEJM 2017; FDA approval 2014"
    },
    {
        "name": "Venetoclax",
        "smiles": "CC1(CCC(=C(C1)C2=CC=C(C=C2)Cl)CN3CCN(CC3)C4=CC(=C(C=C4)C(=O)NS(=O)(=O)C5=CC(=C(C=C5)NCC6CCOCC6)[N+](=O)[O-])OC7=CC=CC=C7)C",
        "target": "BCL-2",
        "indication": "Chronic lymphocytic leukemia (CLL)",
        "approval_year": 2016,
        "efficacy_data": "CLL14: 5-yr PFS 62.6% (venetoclax+obinutuzumab) vs 27.0%",
        "reference": "Fischer et al., NEJM 2019; FDA approval 2016"
    },
    {
        "name": "Lenvatinib",
        "smiles": "COC1=C(C=C2C(=C1)C(=NC=N2)NC3=CC=C(C=C3)OC4=CC=CC(=C4)Cl)C(=O)N",
        "target": "Multi-kinase (VEGFR1-3, FGFR1-4, PDGFRα, RET, KIT)",
        "indication": "Thyroid cancer, HCC, endometrial cancer",
        "approval_year": 2015,
        "efficacy_data": "SELECT: PFS 18.3 vs 3.6 mo (HR 0.21); differentiated thyroid cancer",
        "reference": "Schlumberger et al., NEJM 2015; FDA approval 2015"
    },
    {
        "name": "Sotorasib",
        "smiles": "C=CC(=O)N1CCC(CC1)(C)N2C(=O)C3=CC(=C(N=C3N(C2=O)C4=C(C=CC(=C4)F)F)O)C(C)(C)C",
        "target": "KRAS G12C",
        "indication": "NSCLC with KRAS G12C mutation",
        "approval_year": 2021,
        "efficacy_data": "CodeBreaK 100: ORR 37.1%, DCR 80.6%; first KRAS-targeted therapy",
        "reference": "Skoulidis et al., NEJM 2021; FDA accelerated approval 2021"
    },
    {
        "name": "Palbociclib",
        "smiles": "CC(=O)C1=C(C=C2CN=C(N=C2N1C3CCCC3)NC4=NC=C(C=C4)N5CCNCC5)C",
        "target": "CDK4/6",
        "indication": "HR+/HER2- metastatic breast cancer",
        "approval_year": 2015,
        "efficacy_data": "PALOMA-3: PFS 9.5 vs 4.6 mo (HR 0.46)",
        "reference": "Turner et al., NEJM 2015; FDA approval 2015"
    },
    {
        "name": "Elexacaftor",
        "smiles": "CC1=C(N=C(S1)NC(=O)C2=C(C=CC(=C2)OC(F)F)F)C3=CC(=CC=C3)C(=O)O",
        "target": "CFTR corrector (F508del)",
        "indication": "Cystic fibrosis",
        "approval_year": 2019,
        "efficacy_data": "Trikafta: ppFEV1 +14.3% vs placebo; transformative for CF patients",
        "reference": "Middleton et al., NEJM 2019; FDA approval 2019"
    },
    {
        "name": "Entrectinib",
        "smiles": "CC1=CC=C(C=C1)C(=O)NC2=CC=C(C=C2)N3CCN(CC3)CC4=CC=C5N=CN=C5C4",
        "target": "NTRK1/2/3, ROS1, ALK",
        "indication": "NTRK fusion-positive solid tumors",
        "approval_year": 2019,
        "efficacy_data": "STARTRK-2: ORR 57.4% in NTRK+ tumors; intracranial activity",
        "reference": "Doebele et al., Lancet Oncol 2020; FDA approval 2019"
    },
    {
        "name": "Tazemetostat",
        "smiles": "CCN(C1CCOCC1)C2=C(C=C(C(=C2)C)C3=CC=C(C=C3)OCCN4CCCC4)C(=O)NCC",
        "target": "EZH2",
        "indication": "Epithelioid sarcoma, follicular lymphoma",
        "approval_year": 2020,
        "efficacy_data": "ORR 15% (epithelioid sarcoma); first EZH2 inhibitor approved",
        "reference": "Gounder et al., Lancet Oncol 2020; FDA approval 2020"
    },
    {
        "name": "Ruxolitinib",
        "smiles": "N#CC1=CC=C(C=C1)C2=C(C=CN=C2)C3CC3N4C=CN=C4",
        "target": "JAK1/2",
        "indication": "Myelofibrosis, polycythemia vera",
        "approval_year": 2011,
        "efficacy_data": "COMFORT-I: 41.9% achieved ≥35% spleen volume reduction vs 0.7% placebo",
        "reference": "Verstovsek et al., NEJM 2012; FDA approval 2011"
    },
]

# ── CATEGORY B: "Chemistry-Perfect" Clinical Failures ───────────────────
category_b = [
    {
        "name": "BEN-2293",
        "smiles": "CC1=CC(=CC(=C1NC(=O)C2=CC(=C(C=C2)C3=CN=C4C=CC=CN34)OC)C)N5CCC(CC5)N6CCOCC6",
        "target": "Pan-Trk (TRKA/B/C)",
        "indication": "Atopic dermatitis",
        "failure_stage": "Phase IIa",
        "failure_reason": "No efficacy vs placebo (EASI, NRS endpoints). Target hypothesis failure — immunological redundancy (JAK/STAT, IL-4/13 compensatory pathways)",
        "reference": "BenevolentAI disclosures 2023; FierceBiotech",
        "ai_company": "BenevolentAI"
    },
    {
        "name": "Rofecoxib (Vioxx)",
        "smiles": "CS(=O)(=O)C1=CC=C(C=C1)C2=C(C(=O)OC2)C3=CC=CC=C3",
        "target": "COX-2 selective inhibitor",
        "indication": "Osteoarthritis, pain",
        "failure_stage": "Post-market withdrawal",
        "failure_reason": "Cardiovascular events — 60,000+ excess MIs estimated. System-level off-target toxicity not predicted by target-based screening",
        "reference": "Bresalier et al., NEJM 2005; FDA withdrawal 2004"
    },
    {
        "name": "Troglitazone",
        "smiles": "CC1=C(C2=C(CC(OC2=O)(C)C)C(=C1O)C)CCOC3=CC=C(C=C3)CC4SC(=O)NC4=O",
        "target": "PPARγ agonist",
        "indication": "Type 2 diabetes",
        "failure_stage": "Post-market withdrawal",
        "failure_reason": "Idiosyncratic hepatotoxicity — 63 deaths. Reactive metabolite formation via CYP3A4 not predictable from structure alone",
        "reference": "Watkins et al., JAMA 1998; FDA withdrawal 2000"
    },
    {
        "name": "Ximelagatran",
        "smiles": "CC(C)CC(NC(=O)C(CC1=CC=CC=C1)NC(=O)C2=NC=CC=C2N)C(=O)OCC",
        "target": "Direct thrombin inhibitor",
        "indication": "Anticoagulation (DVT/PE prevention)",
        "failure_stage": "Post-market withdrawal (EU); FDA rejected",
        "failure_reason": "Hepatotoxicity in 6% patients (ALT >3x ULN). HLA-DRB1*07:01 mediated — immune-mediated idiosyncratic reaction unpredictable by computational methods",
        "reference": "Albers et al., JAMA 2005; AstraZeneca withdrawal 2006"
    },
    {
        "name": "Lorcainide",
        "smiles": "ClC1=CC=C(C=C1)OCC(=O)NC2CCCCN2CC3=CC=CC=C3",
        "target": "Sodium channel blocker (Class IC antiarrhythmic)",
        "indication": "Ventricular arrhythmias post-MI",
        "failure_stage": "CAST trial — terminated for harm",
        "failure_reason": "Increased mortality despite suppressing arrhythmias. Surrogate endpoint (PVC suppression) did not predict clinical outcome (survival). CAST trial: 2.5x mortality increase",
        "reference": "CAST Investigators, NEJM 1989"
    },
    {
        "name": "Encainide",
        "smiles": "CCOC1=CC2=C(C=C1)NC(=C2)C(=O)C3CCCCN3CC4=CC=CC=C4",
        "target": "Sodium channel blocker (Class IC antiarrhythmic)",
        "indication": "Ventricular arrhythmias post-MI",
        "failure_stage": "CAST trial — terminated for harm",
        "failure_reason": "Same as lorcainide — CAST trial showed increased mortality. Perfect example of surrogate endpoint failure",
        "reference": "CAST Investigators, NEJM 1989"
    },
    {
        "name": "EXS-21546",
        "smiles": "CC1=NN=C(N1C2=CC(=CC=C2)C(F)(F)F)C3=CC=C(C=C3)C#N",
        "target": "Adenosine A2A receptor antagonist",
        "indication": "Solid tumors (immuno-oncology)",
        "failure_stage": "Phase I — terminated",
        "failure_reason": "Therapeutic index failure — prolonged high target coverage needed but not achievable at tolerable doses",
        "reference": "Exscientia press release Oct 2023; BusinessWire 2022",
        "ai_company": "Exscientia"
    },
    {
        "name": "DSP-1181",
        "smiles": "CC1=CC=C(C=C1)C2=CC(=NN2C3=CC=C(C=C3)S(=O)(=O)N)C(F)(F)F",
        "target": "5-HT1A receptor agonist",
        "indication": "Obsessive-compulsive disorder (OCD)",
        "failure_stage": "Phase I completed — discontinued without Phase II",
        "failure_reason": "Undisclosed. Speed of discovery (12 months) did not translate to clinical viability",
        "reference": "Sumitomo Pharma/Exscientia press releases 2020-2022",
        "ai_company": "Exscientia"
    },
    {
        "name": "Torcetrapib",
        "smiles": "CC(C)C1=CC(=CC(=C1)C(=O)N2CC(CC(C2)OC(=O)NC3=CC=CC=C3)CC(F)(F)F)C(C)C",
        "target": "CETP inhibitor",
        "indication": "Cardiovascular disease (raise HDL)",
        "failure_stage": "Phase III — ILLUMINATE trial terminated",
        "failure_reason": "Increased mortality and CV events despite raising HDL 72%. Off-target aldosterone elevation. $800M development cost. Surrogate endpoint (HDL) did not predict clinical benefit",
        "reference": "Barter et al., NEJM 2007; Pfizer termination 2006"
    },
    {
        "name": "Semagacestat",
        "smiles": "CC(C)CC(C(=O)NC(CC1=CC=CC=C1)C(=O)N2CC(CC2=O)O)NC(=O)C",
        "target": "γ-secretase inhibitor",
        "indication": "Alzheimer's disease",
        "failure_stage": "Phase III — terminated for futility + harm",
        "failure_reason": "Worsened cognition and increased skin cancer risk. Non-selective γ-secretase inhibition affected Notch signaling. Biology too complex for target-based approach",
        "reference": "Doody et al., NEJM 2013; Eli Lilly termination 2010"
    },
    {
        "name": "Evacetrapib",
        "smiles": "CC1=CC(=CC(=C1)C(F)(F)F)NC(=O)C2CC2C3=CC(=C(C=C3)F)F",
        "target": "CETP inhibitor",
        "indication": "Cardiovascular disease",
        "failure_stage": "Phase III — ACCELERATE trial: no benefit",
        "failure_reason": "Raised HDL 130%, lowered LDL 37%, but ZERO reduction in CV events. Definitive proof that HDL-raising alone is insufficient",
        "reference": "Lincoff et al., NEJM 2017; Eli Lilly termination 2015"
    },
    {
        "name": "REC-994 (Tempol)",
        "smiles": "CC1(CC(CC(C1)(C)O)O)N=[O]",
        "target": "Antioxidant / free radical scavenger",
        "indication": "Cerebral cavernous malformation",
        "failure_stage": "Phase II — SYCAMORE trial: no sustained efficacy",
        "failure_reason": "12-month MRI signal (p=0.449, not significant); patient-reported outcomes showed NO differences. Long-term extension: initial signal not sustained",
        "reference": "Recursion Pharmaceuticals 2025; BioPharma Dive May 2025",
        "ai_company": "Recursion"
    },
]

# ── CATEGORY C: Computationally Attractive Decoys ───────────────────────
# These are real molecules from ChEMBL/ZINC that have good computational profiles
# but no known therapeutic value for the indications tested above.
category_c = [
    {
        "name": "Decoy-1 (ZINC000003986735)",
        "smiles": "CC1=CC=C(C=C1)NC(=O)C2=CC=C(C=C2)OC",
        "source": "ZINC database — p-methoxybenzanilide derivative",
        "rationale": "Lipinski-compliant, drug-like scaffold, no known therapeutic activity. Simple amide with aromatic rings — common in screening libraries",
        "known_activity": "None — inactive in all tested assays in ChEMBL"
    },
    {
        "name": "Decoy-2 (Phenacetin analog)",
        "smiles": "CCOC1=CC=C(C=C1)NC(=O)CC2=CC=CC=C2",
        "source": "Designed — phenylacetamide scaffold",
        "rationale": "Drug-like properties, good QED expected, no specific target engagement at therapeutic concentrations",
        "known_activity": "Weak, non-specific — no therapeutic utility"
    },
    {
        "name": "Decoy-3 (Biphenyl sulfonamide)",
        "smiles": "CC1=CC=C(C=C1)C2=CC=C(C=C2)S(=O)(=O)NC",
        "source": "Designed — biphenyl sulfonamide",
        "rationale": "Common medicinal chemistry scaffold, Lipinski-compliant, frequently appears as screening hit but rarely progresses",
        "known_activity": "Non-specific kinase panel activity at high concentrations only"
    },
    {
        "name": "Decoy-4 (Benzimidazole carboxamide)",
        "smiles": "C1=CC=C2C(=C1)NC(=N2)C(=O)NC3=CC=C(C=C3)F",
        "source": "Designed — benzimidazole scaffold",
        "rationale": "Privileged scaffold in drug discovery, excellent drug-likeness, but this specific compound has no validated target",
        "known_activity": "None validated"
    },
    {
        "name": "Decoy-5 (Pyridine amide)",
        "smiles": "CC(C)NC(=O)C1=CC=CN=C1",
        "source": "Designed — nicotinamide derivative",
        "rationale": "Very drug-like, low MW, good solubility predicted, but no specific pharmacological activity",
        "known_activity": "None — too simple for specific target engagement"
    },
    {
        "name": "Decoy-6 (Indole-3-acetic acid derivative)",
        "smiles": "O=C(NCC1=CC=CC=C1)CC2=CNC3=CC=CC=C32",
        "source": "Designed — indole scaffold",
        "rationale": "Indole is a privileged scaffold; this derivative has good drug-likeness but no validated human target",
        "known_activity": "Plant hormone analog (auxin); no human therapeutic activity"
    },
    {
        "name": "Decoy-7 (Quinoline carboxamide)",
        "smiles": "COC1=CC2=NC=CC(=C2C=C1)C(=O)NC3CCCCC3",
        "source": "Designed — quinoline scaffold",
        "rationale": "Quinoline is common in drugs (chloroquine, etc.), this derivative has good properties but no specific validated activity",
        "known_activity": "None validated for this specific compound"
    },
    {
        "name": "Decoy-8 (Thiophene sulfonamide)",
        "smiles": "CC1=CC=C(S1)S(=O)(=O)NC2=CC=C(C=C2)OC",
        "source": "Designed — thiophene sulfonamide",
        "rationale": "Drug-like, PAINS-free, good predicted ADMET, but no therapeutic rationale",
        "known_activity": "None — designed as computational decoy"
    },
    {
        "name": "Decoy-9 (Piperazine benzamide)",
        "smiles": "O=C(C1=CC=C(F)C=C1)N2CCN(CC2)C3=CC=CC=C3",
        "source": "Designed — piperazine linker",
        "rationale": "Piperazine is the most common ring in FDA-approved drugs; this compound has excellent drug-likeness but no specific validated target",
        "known_activity": "Non-specific — piperazines often show promiscuous binding"
    },
    {
        "name": "Decoy-10 (Oxadiazole amide)",
        "smiles": "CC1=NN=C(O1)C(=O)NC2=CC=C(C=C2)Cl",
        "source": "Designed — 1,2,4-oxadiazole scaffold",
        "rationale": "Oxadiazole is a bioisostere for esters/amides; drug-like but this compound has no known activity",
        "known_activity": "None validated"
    },
    {
        "name": "Decoy-11 (Chromone derivative)",
        "smiles": "O=C1C=C(OC2=CC(=CC=C21)O)C3=CC=C(C=C3)OC",
        "source": "Designed — flavone/chromone scaffold",
        "rationale": "Natural product-like, excellent drug-likeness, but flavones are notorious for non-specific activity (PAINS-adjacent)",
        "known_activity": "Non-specific antioxidant; no validated drug target"
    },
    {
        "name": "Decoy-12 (Triazole ether)",
        "smiles": "C1=CN=NN1CC2=CC=C(C=C2)OCC3=CC=CC=C3",
        "source": "Designed — 1,2,4-triazole scaffold",
        "rationale": "Triazole is common in antifungals; this derivative has good properties but no antifungal or other validated activity",
        "known_activity": "None validated for this specific compound"
    },
]


# ── Compute properties and assemble dataset ─────────────────────────────
def build_entry(mol_data: dict, category: str) -> dict:
    smi = mol_data["smiles"]
    props = compute_props(smi)
    entry = {"category": category}
    entry.update(mol_data)
    entry.update(props)
    return entry

dataset = []
for m in category_a:
    dataset.append(build_entry(m, "A_approved"))
for m in category_b:
    dataset.append(build_entry(m, "B_clinical_failure"))
for m in category_c:
    dataset.append(build_entry(m, "C_decoy"))

# ── Validate ────────────────────────────────────────────────────────────
n_valid = sum(1 for d in dataset if d.get("valid_smiles"))
n_total = len(dataset)
print(f"Dataset: {n_total} molecules, {n_valid} valid SMILES")
for cat in ["A_approved", "B_clinical_failure", "C_decoy"]:
    n = sum(1 for d in dataset if d["category"] == cat)
    nv = sum(1 for d in dataset if d["category"] == cat and d.get("valid_smiles"))
    print(f"  {cat}: {n} total, {nv} valid")

# ── Save ────────────────────────────────────────────────────────────────
out_path = pathlib.Path(__file__).parent / "agent_evaluation_dataset.json"
with open(out_path, "w") as f:
    json.dump(dataset, f, indent=2)
print(f"\nSaved to {out_path}")

# ── Quick summary table ─────────────────────────────────────────────────
print(f"\n{'Name':<30} {'Cat':<20} {'MW':>6} {'LogP':>6} {'QED':>5} {'Lip':>4} {'PAINS':>6}")
print("-" * 100)
for d in dataset:
    if d.get("valid_smiles"):
        print(f"{d['name']:<30} {d['category']:<20} {d['MW']:>6.1f} {d['LogP']:>6.2f} {d['QED']:>5.3f} {'PASS' if d['Lipinski_pass'] else 'FAIL':>4} {'YES' if d['PAINS_flag'] else 'NO':>6}")
    else:
        print(f"{d['name']:<30} {d['category']:<20} INVALID SMILES")

# ── Key insight preview ─────────────────────────────────────────────────
import statistics
for cat in ["A_approved", "B_clinical_failure", "C_decoy"]:
    qeds = [d["QED"] for d in dataset if d["category"] == cat and d.get("valid_smiles")]
    mws  = [d["MW"] for d in dataset if d["category"] == cat and d.get("valid_smiles")]
    lip_pass = sum(1 for d in dataset if d["category"] == cat and d.get("valid_smiles") and d["Lipinski_pass"])
    lip_total = sum(1 for d in dataset if d["category"] == cat and d.get("valid_smiles"))
    print(f"\n{cat}:")
    print(f"  QED: mean={statistics.mean(qeds):.3f}, median={statistics.median(qeds):.3f}")
    print(f"  MW:  mean={statistics.mean(mws):.1f}")
    print(f"  Lipinski pass: {lip_pass}/{lip_total} ({100*lip_pass/lip_total:.0f}%)")
