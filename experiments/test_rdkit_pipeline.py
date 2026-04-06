"""
Comprehensive RDKit Pipeline Test — Simulating ChemCrow/DruGUI-style Evaluation
================================================================================
This script replicates the core computational workflow that AI-agent drug discovery
pipelines use to evaluate molecules. It tests whether these standard computational
metrics can distinguish between:
  - Category A: FDA-approved drugs (true positives)
  - Category B: Clinical failures that passed all computational filters
  - Category C: Computationally attractive decoys with no therapeutic value

Pipeline components (mirroring ChemCrow / DruGUI / typical AI-agent tools):
  1. Drug-likeness scoring (QED, Lipinski, Veber)
  2. Synthetic accessibility (SA Score)
  3. Structural complexity & diversity (fingerprints, scaffold analysis)
  4. ADMET-proxy filters (TPSA, LogP, MW, HBD/HBA ranges)
  5. Similarity to known drug space (Tanimoto to approved drug set)
  6. Pan-assay interference (PAINS) & Brenk filters
  7. Composite "pipeline score" — weighted combination

The key question: Does the composite score rank Category A > B > C?
"""

import json
import pathlib
import numpy as np
import pandas as pd
from collections import OrderedDict

from rdkit import Chem, DataStructs
from rdkit.Chem import (
    Descriptors, QED, AllChem, FilterCatalog,
    rdMolDescriptors, Scaffolds, Fragments
)
from rdkit.Chem.Scaffolds import MurckoScaffold
from rdkit.Contrib.SA_Score import sascorer

# ── Load dataset ──────────────────────────────────────────────────────────
DATA_PATH = pathlib.Path(__file__).parent / "agent_evaluation_dataset.json"
with open(DATA_PATH) as f:
    dataset = json.load(f)

print(f"Loaded {len(dataset)} molecules from dataset")
print(f"  Category A (approved): {sum(1 for m in dataset if m['category'] == 'A_approved')}")
print(f"  Category B (failures): {sum(1 for m in dataset if m['category'] == 'B_clinical_failure')}")
print(f"  Category C (decoys):   {sum(1 for m in dataset if m['category'] == 'C_decoy')}")
print()

# ── Helper functions ──────────────────────────────────────────────────────

def get_mol(smiles):
    """Parse SMILES with error handling."""
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        print(f"  WARNING: Invalid SMILES: {smiles[:50]}...")
    return mol


def sa_score(mol):
    """Synthetic Accessibility Score (1=easy, 10=hard)."""
    try:
        return sascorer.calculateScore(mol)
    except Exception:
        return None


def veber_pass(mol):
    """Veber's oral bioavailability rule: RotBonds <= 10, TPSA <= 140."""
    rotb = rdMolDescriptors.CalcNumRotatableBonds(mol)
    tpsa = Descriptors.TPSA(mol)
    return rotb <= 10 and tpsa <= 140


def ghose_pass(mol):
    """Ghose filter: 160 <= MW <= 480, -0.4 <= LogP <= 5.6, 40 <= MR <= 130, 20 <= atoms <= 70."""
    mw = Descriptors.ExactMolWt(mol)
    logp = Descriptors.MolLogP(mol)
    mr = Descriptors.MolMR(mol)
    natoms = mol.GetNumAtoms()
    return (160 <= mw <= 480 and -0.4 <= logp <= 5.6 and
            40 <= mr <= 130 and 20 <= natoms <= 70)


def egan_pass(mol):
    """Egan's oral absorption model: TPSA <= 131.6, LogP <= 5.88."""
    tpsa = Descriptors.TPSA(mol)
    logp = Descriptors.MolLogP(mol)
    return tpsa <= 131.6 and logp <= 5.88


def muegge_pass(mol):
    """Muegge's pharmacophore point filter (simplified)."""
    mw = Descriptors.ExactMolWt(mol)
    logp = Descriptors.MolLogP(mol)
    tpsa = Descriptors.TPSA(mol)
    hbd = rdMolDescriptors.CalcNumHBD(mol)
    hba = rdMolDescriptors.CalcNumHBA(mol)
    rotb = rdMolDescriptors.CalcNumRotatableBonds(mol)
    rings = rdMolDescriptors.CalcNumRings(mol)
    natoms = mol.GetNumHeavyAtoms()
    return (200 <= mw <= 600 and -2 <= logp <= 5 and tpsa <= 150 and
            hbd <= 5 and hba <= 10 and rotb <= 15 and rings <= 7 and natoms >= 15)


def get_brenk_filter():
    """Brenk structural alert filter."""
    params = FilterCatalog.FilterCatalogParams()
    params.AddCatalog(FilterCatalog.FilterCatalogParams.FilterCatalogs.BRENK)
    return FilterCatalog.FilterCatalog(params)


def get_pains_filter():
    """PAINS filter."""
    params = FilterCatalog.FilterCatalogParams()
    params.AddCatalog(FilterCatalog.FilterCatalogParams.FilterCatalogs.PAINS)
    return FilterCatalog.FilterCatalog(params)


def compute_fingerprint(mol, radius=2, nbits=2048):
    """Morgan fingerprint (ECFP4 equivalent)."""
    return AllChem.GetMorganFingerprintAsBitVect(mol, radius, nBits=nbits)


def fsp3(mol):
    """Fraction of sp3 carbons — higher often correlates with clinical success."""
    return rdMolDescriptors.CalcFractionCSP3(mol)


def num_stereocenters(mol):
    """Number of stereocenters — complexity indicator."""
    return rdMolDescriptors.CalcNumAtomStereoCenters(mol)


def aromatic_ring_count(mol):
    """Number of aromatic rings."""
    ri = mol.GetRingInfo()
    aromatic = 0
    for ring in ri.BondRings():
        if all(mol.GetBondWithIdx(idx).GetIsAromatic() for idx in ring):
            aromatic += 1
    return aromatic


# ── Build reference drug set for similarity comparison ────────────────────
# Use Category A as reference (what a pipeline would compare against)
# Also build a broader reference from well-known drugs
REFERENCE_DRUGS_SMILES = [
    "CC(=O)OC1=CC=CC=C1C(=O)O",  # Aspirin
    "CC(=O)NC1=CC=C(C=C1)O",     # Acetaminophen
    "CC12CCC3C(C1CCC2O)CCC4=CC(=O)CCC34C",  # Testosterone
    "CC1=CC=C(C=C1)C2=CC(=NN2C3=CC=C(C=C3)S(=O)(=O)N)C(F)(F)F",  # Celecoxib
    "CN1C=NC2=C1C(=O)N(C(=O)N2C)C",  # Caffeine
    "CC(C)CC1=CC=C(C=C1)C(C)C(=O)O",  # Ibuprofen
    "OC(=O)C1=CC=CC=C1O",         # Salicylic acid
    "C1=CC=C(C=C1)C(=O)O",       # Benzoic acid
    "CC(C)NCC(O)C1=CC=C(O)C(O)=C1",  # Isoproterenol
    "CCOC(=O)C1=CC=CC=C1N",      # Benzocaine
]


# ── Main evaluation pipeline ─────────────────────────────────────────────

def evaluate_molecule(mol, name, smiles, pains_cat, brenk_cat, ref_fps):
    """Run full pipeline on a single molecule. Returns dict of all scores."""
    if mol is None:
        return {"name": name, "valid": False}

    results = OrderedDict()
    results["name"] = name
    results["smiles"] = smiles
    results["valid"] = True

    # 1. Basic descriptors
    results["MW"] = round(Descriptors.ExactMolWt(mol), 1)
    results["LogP"] = round(Descriptors.MolLogP(mol), 2)
    results["HBD"] = rdMolDescriptors.CalcNumHBD(mol)
    results["HBA"] = rdMolDescriptors.CalcNumHBA(mol)
    results["TPSA"] = round(Descriptors.TPSA(mol), 1)
    results["RotBonds"] = rdMolDescriptors.CalcNumRotatableBonds(mol)
    results["HeavyAtoms"] = mol.GetNumHeavyAtoms()
    results["Rings"] = rdMolDescriptors.CalcNumRings(mol)
    results["AromaticRings"] = aromatic_ring_count(mol)

    # 2. Drug-likeness scores
    results["QED"] = round(QED.qed(mol), 4)
    results["SA_Score"] = round(sa_score(mol), 3) if sa_score(mol) else None
    results["Fsp3"] = round(fsp3(mol), 3)
    results["NumStereocenters"] = num_stereocenters(mol)

    # 3. Filter compliance
    lip_v = sum([
        results["MW"] > 500, results["LogP"] > 5,
        results["HBD"] > 5, results["HBA"] > 10
    ])
    results["Lipinski_violations"] = lip_v
    results["Lipinski_pass"] = lip_v == 0
    results["Veber_pass"] = veber_pass(mol)
    results["Ghose_pass"] = ghose_pass(mol)
    results["Egan_pass"] = egan_pass(mol)
    results["Muegge_pass"] = muegge_pass(mol)
    results["filters_passed"] = sum([
        results["Lipinski_pass"], results["Veber_pass"],
        results["Ghose_pass"], results["Egan_pass"], results["Muegge_pass"]
    ])

    # 4. Structural alerts
    results["PAINS_flag"] = pains_cat.HasMatch(mol)
    results["Brenk_flag"] = brenk_cat.HasMatch(mol)

    # 5. Similarity to reference drug space
    fp = compute_fingerprint(mol)
    similarities = [DataStructs.TanimotoSimilarity(fp, ref_fp) for ref_fp in ref_fps]
    results["max_drug_similarity"] = round(max(similarities), 4)
    results["mean_drug_similarity"] = round(np.mean(similarities), 4)

    # 6. Normalized composite scores
    # QED component (0-1, higher = more drug-like)
    qed_score = results["QED"]

    # SA component: normalize to 0-1 (SA 1=easy → 1.0, SA 10=hard → 0.0)
    sa_norm = max(0, (10 - (results["SA_Score"] or 5)) / 9)

    # Filter compliance score (0-1)
    filter_score = results["filters_passed"] / 5.0

    # Similarity score (already 0-1)
    sim_score = results["max_drug_similarity"]

    # No structural alerts (binary penalty)
    alert_penalty = 0.0
    if results["PAINS_flag"]:
        alert_penalty += 0.15
    if results["Brenk_flag"]:
        alert_penalty += 0.10

    # Composite score — weighted average (mimics typical pipeline ranking)
    # These weights reflect what AI-agent pipelines typically emphasize
    composite = (
        0.30 * qed_score +
        0.15 * sa_norm +
        0.25 * filter_score +
        0.20 * sim_score +
        0.10 * 1.0  # baseline
        - alert_penalty
    )
    results["score_qed"] = round(qed_score, 4)
    results["score_sa"] = round(sa_norm, 4)
    results["score_filters"] = round(filter_score, 4)
    results["score_similarity"] = round(sim_score, 4)
    results["score_alert_penalty"] = round(alert_penalty, 4)
    results["composite_score"] = round(composite, 4)

    return results


def main():
    print("=" * 70)
    print("RDKit Comprehensive Pipeline — ChemCrow/DruGUI Simulation")
    print("=" * 70)
    print()

    # Initialize filters
    pains_cat = get_pains_filter()
    brenk_cat = get_brenk_filter()

    # Build reference fingerprints (from reference drugs + Category A)
    ref_fps = []
    for smi in REFERENCE_DRUGS_SMILES:
        mol = Chem.MolFromSmiles(smi)
        if mol:
            ref_fps.append(compute_fingerprint(mol))

    # Also add Category A molecules as reference
    for entry in dataset:
        if entry["category"] == "A_approved":
            mol = Chem.MolFromSmiles(entry["smiles"])
            if mol:
                ref_fps.append(compute_fingerprint(mol))

    print(f"Reference drug fingerprints: {len(ref_fps)}")
    print()

    # Evaluate all molecules
    results = []
    for entry in dataset:
        mol = get_mol(entry["smiles"])
        r = evaluate_molecule(mol, entry["name"], entry["smiles"],
                              pains_cat, brenk_cat, ref_fps)
        r["category"] = entry["category"]
        r["category_label"] = {
            "A_approved": "A: Approved",
            "B_clinical_failure": "B: Clinical Failure",
            "C_decoy": "C: Decoy"
        }.get(entry["category"], entry["category"])
        results.append(r)
        print(f"  {r['category_label']:25s} | {r['name']:20s} | "
              f"QED={r.get('QED','N/A'):>6} | SA={r.get('SA_Score','N/A'):>6} | "
              f"Filters={r.get('filters_passed','N/A')}/5 | "
              f"Composite={r.get('composite_score','N/A'):>7}")

    # ── Summary statistics ────────────────────────────────────────────────
    print()
    print("=" * 70)
    print("SUMMARY STATISTICS BY CATEGORY")
    print("=" * 70)

    df = pd.DataFrame(results)
    valid_df = df[df["valid"] == True].copy()

    for cat in ["A_approved", "B_clinical_failure", "C_decoy"]:
        cat_df = valid_df[valid_df["category"] == cat]
        label = cat_df["category_label"].iloc[0]
        print(f"\n--- {label} (n={len(cat_df)}) ---")
        for col in ["QED", "SA_Score", "Fsp3", "composite_score",
                     "filters_passed", "max_drug_similarity",
                     "Lipinski_pass", "Veber_pass", "PAINS_flag", "Brenk_flag"]:
            if col in cat_df.columns:
                if cat_df[col].dtype == bool:
                    print(f"  {col:25s}: {cat_df[col].sum()}/{len(cat_df)} "
                          f"({cat_df[col].mean()*100:.0f}%)")
                else:
                    vals = cat_df[col].dropna()
                    print(f"  {col:25s}: mean={vals.mean():.3f}, "
                          f"std={vals.std():.3f}, "
                          f"min={vals.min():.3f}, max={vals.max():.3f}")

    # ── Key discrimination test ───────────────────────────────────────────
    print()
    print("=" * 70)
    print("DISCRIMINATION ANALYSIS")
    print("=" * 70)

    from scipy import stats

    cat_a = valid_df[valid_df["category"] == "A_approved"]["composite_score"]
    cat_b = valid_df[valid_df["category"] == "B_clinical_failure"]["composite_score"]
    cat_c = valid_df[valid_df["category"] == "C_decoy"]["composite_score"]

    # Kruskal-Wallis test (non-parametric ANOVA)
    h_stat, p_kw = stats.kruskal(cat_a, cat_b, cat_c)
    print(f"\nKruskal-Wallis test (H={h_stat:.3f}, p={p_kw:.4f})")

    # Pairwise Mann-Whitney U tests
    for label_pair, (g1, g2) in [
        ("A vs B", (cat_a, cat_b)),
        ("A vs C", (cat_a, cat_c)),
        ("B vs C", (cat_b, cat_c)),
    ]:
        u_stat, p_val = stats.mannwhitneyu(g1, g2, alternative='two-sided')
        print(f"  Mann-Whitney {label_pair}: U={u_stat:.1f}, p={p_val:.4f}")

    print(f"\nComposite score means:")
    print(f"  Category A (approved):  {cat_a.mean():.4f} +/- {cat_a.std():.4f}")
    print(f"  Category B (failures):  {cat_b.mean():.4f} +/- {cat_b.std():.4f}")
    print(f"  Category C (decoys):    {cat_c.mean():.4f} +/- {cat_c.std():.4f}")

    # ROC-AUC: Can pipeline distinguish A from B?
    from sklearn.metrics import roc_auc_score
    # A vs B (can pipeline tell approved from clinical failures?)
    ab_labels = [1]*len(cat_a) + [0]*len(cat_b)
    ab_scores = list(cat_a) + list(cat_b)
    try:
        auc_ab = roc_auc_score(ab_labels, ab_scores)
        print(f"\n  ROC-AUC (A vs B — approved vs failures): {auc_ab:.4f}")
        if auc_ab < 0.6:
            print(f"    → NEAR RANDOM: Pipeline CANNOT distinguish approved drugs from clinical failures")
        elif auc_ab < 0.7:
            print(f"    → POOR: Weak discrimination between approved and failed drugs")
        else:
            print(f"    → MODERATE+: Some discrimination ability")
    except Exception as e:
        print(f"  ROC-AUC (A vs B) error: {e}")

    # A vs C (can pipeline tell approved from decoys?)
    ac_labels = [1]*len(cat_a) + [0]*len(cat_c)
    ac_scores = list(cat_a) + list(cat_c)
    try:
        auc_ac = roc_auc_score(ac_labels, ac_scores)
        print(f"  ROC-AUC (A vs C — approved vs decoys):   {auc_ac:.4f}")
        if auc_ac < 0.5:
            print(f"    → INVERTED: Pipeline actually PREFERS decoys over approved drugs!")
        elif auc_ac < 0.6:
            print(f"    → NEAR RANDOM: Pipeline CANNOT distinguish approved drugs from decoys")
        else:
            print(f"    → Some discrimination")
    except Exception as e:
        print(f"  ROC-AUC (A vs C) error: {e}")

    # B vs C (can pipeline tell clinical failures from decoys?)
    bc_labels = [0]*len(cat_b) + [1]*len(cat_c)  # Note: neither is "good"
    bc_scores = list(cat_b) + list(cat_c)
    try:
        auc_bc = roc_auc_score(bc_labels, bc_scores)
        print(f"  ROC-AUC (B vs C — failures vs decoys):   {auc_bc:.4f}")
    except Exception as e:
        print(f"  ROC-AUC (B vs C) error: {e}")

    # ── The critical finding ──────────────────────────────────────────────
    print()
    print("=" * 70)
    print("CRITICAL FINDING FOR REVIEW PAPER")
    print("=" * 70)

    # Check if decoys score higher than approved drugs
    if cat_c.mean() > cat_a.mean():
        print("\n*** DECOYS SCORE HIGHER THAN APPROVED DRUGS ***")
        print("This directly supports the review's thesis: computational metrics")
        print("are INVERSELY correlated with clinical utility in many cases.")
    elif abs(cat_a.mean() - cat_b.mean()) < 0.1:
        print("\n*** APPROVED AND FAILED DRUGS ARE INDISTINGUISHABLE ***")
        print("The pipeline cannot differentiate between drugs that work")
        print("and drugs that failed in clinical trials.")

    if cat_c.mean() > cat_b.mean():
        print("\nDecoys > Clinical Failures — meaningless molecules score BEST")

    print(f"\nRanking by composite score (expected: A > B > C):")
    means = {"A": cat_a.mean(), "B": cat_b.mean(), "C": cat_c.mean()}
    ranked = sorted(means.items(), key=lambda x: x[1], reverse=True)
    print(f"  Actual ranking: {' > '.join(f'Cat {k} ({v:.4f})' for k, v in ranked)}")
    expected = ["A", "B", "C"]
    actual = [k for k, v in ranked]
    if actual != expected:
        print(f"  *** INCORRECT RANKING — expected A > B > C ***")
    else:
        print(f"  Ranking matches expected order (but check effect sizes)")

    # ── Save results ──────────────────────────────────────────────────────
    output_path = pathlib.Path(__file__).parent / "results_rdkit_pipeline.json"
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nResults saved to {output_path}")

    # Save summary stats
    summary = {
        "pipeline": "RDKit Comprehensive (ChemCrow/DruGUI simulation)",
        "n_molecules": len(results),
        "composite_score_means": {
            "A_approved": round(cat_a.mean(), 4),
            "B_clinical_failure": round(cat_b.mean(), 4),
            "C_decoy": round(cat_c.mean(), 4),
        },
        "composite_score_std": {
            "A_approved": round(cat_a.std(), 4),
            "B_clinical_failure": round(cat_b.std(), 4),
            "C_decoy": round(cat_c.std(), 4),
        },
        "roc_auc": {
            "A_vs_B": round(auc_ab, 4) if 'auc_ab' in dir() else None,
            "A_vs_C": round(auc_ac, 4) if 'auc_ac' in dir() else None,
            "B_vs_C": round(auc_bc, 4) if 'auc_bc' in dir() else None,
        },
        "kruskal_wallis": {"H": round(h_stat, 3), "p": round(p_kw, 4)},
        "critical_finding": (
            "Decoys score higher than approved drugs"
            if cat_c.mean() > cat_a.mean()
            else "Approved and failed drugs are near-indistinguishable"
            if abs(cat_a.mean() - cat_b.mean()) < 0.1
            else f"Ranking: {' > '.join(k for k, v in ranked)}"
        ),
    }
    summary_path = pathlib.Path(__file__).parent / "results_rdkit_pipeline_summary.json"
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"Summary saved to {summary_path}")

    return df


if __name__ == "__main__":
    df = main()
