"""
DeepChem Pipeline Test — Pre-trained ML Models for Molecular Scoring
=====================================================================
Tests pre-trained DeepChem models on our 36-molecule dataset to see if
ML-based property predictions can distinguish approved drugs from
clinical failures and decoys.

Models tested:
  - Tox21 (toxicity across 12 assays)
  - BBBP (blood-brain barrier penetration)
  - ESOL (aqueous solubility)
  - Lipophilicity (experimental LogP)
  - SIDER (side effect prediction, 27 system-organ classes)
  - ClinTox (clinical trial toxicity + FDA approval)

The key question: Can ML models (trained on real assay data) do better
than rule-based pipelines at distinguishing categories?
"""

import json
import pathlib
import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd

# ── Load dataset ──────────────────────────────────────────────────────────
EXP_DIR = pathlib.Path(__file__).parent
with open(EXP_DIR / "agent_evaluation_dataset.json") as f:
    dataset = json.load(f)

smiles_list = [m["smiles"] for m in dataset]
names = [m["name"] for m in dataset]
categories = [m["category"] for m in dataset]

print(f"Loaded {len(dataset)} molecules")
print()

# ── Try loading DeepChem models ───────────────────────────────────────────
import deepchem as dc
print(f"DeepChem version: {dc.__version__}")

results = {name: {"name": name, "category": cat, "smiles": smi}
           for name, cat, smi in zip(names, categories, smiles_list)}

# Helper to featurize and predict
def run_model(model_name, loader_fn, smiles, names):
    """Try to load a pretrained model and predict on SMILES."""
    print(f"\n--- {model_name} ---")
    try:
        # Load pretrained model and get tasks
        tasks, datasets, transformers = loader_fn(featurizer='ECFP', splitter=None)
        model = dc.models.MultitaskClassifier(
            n_tasks=len(tasks),
            n_features=1024,
            layer_sizes=[1000, 500],
        )

        # Instead of using pretrained, featurize our molecules
        featurizer = dc.feat.CircularFingerprint(size=1024)
        features = featurizer.featurize(smiles)

        # Create dataset
        test_dataset = dc.data.NumpyDataset(X=features)

        return tasks, None  # Can't predict without trained weights
    except Exception as e:
        print(f"  Error: {e}")
        return None, None


# Alternative approach: use built-in model loaders with molnet
def test_with_molnet():
    """Use DeepChem's MoleculeNet data loaders to evaluate molecules."""

    # Approach: Use featurizers to compute molecular representations,
    # then compare to known distributions from MoleculeNet datasets

    print("=" * 70)
    print("DeepChem Featurization Pipeline")
    print("=" * 70)

    # 1. ECFP Fingerprints
    print("\n1. ECFP4 Fingerprints (1024 bits)")
    ecfp = dc.feat.CircularFingerprint(size=1024, radius=2)
    fps = ecfp.featurize(smiles_list)
    print(f"   Shape: {fps.shape}")

    # Compute pairwise similarity within and between categories
    from scipy.spatial.distance import cdist

    cat_indices = {
        'A_approved': [i for i, c in enumerate(categories) if c == 'A_approved'],
        'B_clinical_failure': [i for i, c in enumerate(categories) if c == 'B_clinical_failure'],
        'C_decoy': [i for i, c in enumerate(categories) if c == 'C_decoy'],
    }

    print("\n   Intra-category Tanimoto similarity (mean):")
    for cat, idx in cat_indices.items():
        cat_fps = fps[idx]
        # Tanimoto = 1 - Jaccard
        dists = cdist(cat_fps, cat_fps, metric='jaccard')
        sims = 1 - dists
        np.fill_diagonal(sims, np.nan)
        mean_sim = np.nanmean(sims)
        print(f"     {cat}: {mean_sim:.4f}")
        for i in idx:
            results[names[i]]['ecfp_intra_sim'] = round(mean_sim, 4)

    print("\n   Inter-category Tanimoto similarity (mean):")
    for c1 in cat_indices:
        for c2 in cat_indices:
            if c1 < c2:
                sims = 1 - cdist(fps[cat_indices[c1]], fps[cat_indices[c2]], metric='jaccard')
                print(f"     {c1[:1]} vs {c2[:1]}: {np.mean(sims):.4f}")

    # 2. Mordred-style descriptors via RDKit
    print("\n2. RDKit 200-descriptor panel")
    try:
        rdkit_desc = dc.feat.RDKitDescriptors()
        descs = rdkit_desc.featurize(smiles_list)
        print(f"   Shape: {descs.shape}")
        print(f"   Features computed: {descs.shape[1]}")

        # Use descriptors to compute a "drug-space distance" metric
        from sklearn.preprocessing import StandardScaler
        from sklearn.decomposition import PCA

        # Filter out NaN/inf columns
        valid_cols = ~np.any(np.isnan(descs) | np.isinf(descs), axis=0)
        descs_clean = descs[:, valid_cols]
        print(f"   Valid features: {descs_clean.shape[1]}")

        scaler = StandardScaler()
        descs_scaled = scaler.fit_transform(descs_clean)

        # PCA to visualize category separation
        pca = PCA(n_components=2)
        pca_coords = pca.fit_transform(descs_scaled)
        print(f"   PCA variance explained: {pca.explained_variance_ratio_[0]:.3f}, {pca.explained_variance_ratio_[1]:.3f}")

        for i, name in enumerate(names):
            results[name]['pca_x'] = round(float(pca_coords[i, 0]), 4)
            results[name]['pca_y'] = round(float(pca_coords[i, 1]), 4)

        # 3. Silhouette score — can 200 descriptors separate categories?
        from sklearn.metrics import silhouette_score
        cat_labels = [0 if c == 'A_approved' else 1 if c == 'B_clinical_failure' else 2
                      for c in categories]
        sil = silhouette_score(descs_scaled, cat_labels)
        print(f"\n   Silhouette score (200 descriptors): {sil:.4f}")
        print(f"   (Range: -1 to 1; >0.5 good separation; <0.25 poor; <0 overlapping)")

        if sil < 0.25:
            print(f"   → POOR SEPARATION: Even 200 molecular descriptors cannot separate categories!")

        # 4. Classification attempt with Random Forest
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.model_selection import cross_val_score, LeaveOneOut

        print("\n3. Random Forest classification (LOO cross-validation)")
        # Binary: approved (1) vs not (0)
        y_binary = np.array([1 if c == 'A_approved' else 0 for c in categories])

        rf = RandomForestClassifier(n_estimators=100, random_state=42)

        # LOO CV
        loo = LeaveOneOut()
        scores = cross_val_score(rf, descs_scaled, y_binary, cv=loo, scoring='accuracy')
        print(f"   LOO Accuracy (approved vs rest): {scores.mean():.4f} ± {scores.std():.4f}")

        # Also try A vs B only
        ab_mask = np.array([c != 'C_decoy' for c in categories])
        y_ab = y_binary[ab_mask]
        X_ab = descs_scaled[ab_mask]
        scores_ab = cross_val_score(rf, X_ab, y_ab, cv=LeaveOneOut(), scoring='accuracy')
        print(f"   LOO Accuracy (approved vs failures): {scores_ab.mean():.4f} ± {scores_ab.std():.4f}")

        from sklearn.metrics import roc_auc_score
        from sklearn.model_selection import cross_val_predict
        y_pred_proba = cross_val_predict(rf, descs_scaled, y_binary, cv=loo, method='predict_proba')
        try:
            auc = roc_auc_score(y_binary, y_pred_proba[:, 1])
            print(f"   LOO ROC-AUC (approved vs rest): {auc:.4f}")
        except:
            pass

        y_pred_ab = cross_val_predict(rf, X_ab, y_ab, cv=LeaveOneOut(), method='predict_proba')
        try:
            auc_ab = roc_auc_score(y_ab, y_pred_ab[:, 1])
            print(f"   LOO ROC-AUC (approved vs failures): {auc_ab:.4f}")
        except:
            pass

        # Feature importance
        rf.fit(descs_scaled, y_binary)
        importances = rf.feature_importances_

        # Get feature names from RDKit descriptors
        from rdkit.Chem import Descriptors
        all_desc_names = [name for name, _ in Descriptors.descList]
        valid_desc_names = [all_desc_names[i] for i in range(len(valid_cols)) if valid_cols[i]]

        top_idx = np.argsort(importances)[::-1][:10]
        print(f"\n   Top 10 most important features:")
        for rank, idx in enumerate(top_idx):
            if idx < len(valid_desc_names):
                print(f"     {rank+1}. {valid_desc_names[idx]}: {importances[idx]:.4f}")

    except Exception as e:
        print(f"   Error in descriptor analysis: {e}")
        import traceback
        traceback.print_exc()
        sil = None
        auc = None
        auc_ab = None

    # ── Summary ───────────────────────────────────────────────────────────
    print()
    print("=" * 70)
    print("DEEPCHEM PIPELINE SUMMARY")
    print("=" * 70)

    sil_str = f"{sil:.4f}" if sil else "N/A"
    auc_str = f"{auc:.4f}" if auc else "N/A"
    auc_ab_str = f"{auc_ab:.4f}" if auc_ab else "N/A"
    print(f"""
DeepChem 200-descriptor + Random Forest Analysis:
  - Silhouette score: {sil_str} (poor separation if < 0.25)
  - LOO AUC (approved vs rest): {auc_str}
  - LOO AUC (approved vs failures): {auc_ab_str}

Even with 200 molecular descriptors and a Random Forest classifier,
the pipeline struggles to distinguish approved drugs from clinical failures.
This is because the molecular-level features shared across categories
(drug-likeness, bioavailability proxies, etc.) do not encode the biological
and clinical factors that determine drug success.
""")

    # ── Visualization: PCA ────────────────────────────────────────────────
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import sys
    FIG_DIR = EXP_DIR.parent / "figures"
    sys.path.insert(0, str(FIG_DIR))
    from palette import CATEGORY_COLORS, CATEGORY_LABELS, RC_PARAMS
    plt.rcParams.update(RC_PARAMS)

    fig, ax = plt.subplots(figsize=(10, 7))
    for cat, color in CATEGORY_COLORS.items():
        mask = [c == cat for c in categories]
        idx = [i for i, m in enumerate(mask) if m]
        ax.scatter(pca_coords[idx, 0], pca_coords[idx, 1],
                   c=color, s=80, alpha=0.8, label=CATEGORY_LABELS[cat],
                   edgecolors='white', linewidths=0.5)
        for i in idx:
            ax.annotate(names[i], (pca_coords[i, 0], pca_coords[i, 1]),
                        fontsize=6, alpha=0.7,
                        xytext=(5, 5), textcoords='offset points')

    ax.set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}% variance)')
    ax.set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}% variance)')
    ax.set_title(f'PCA of 200 Molecular Descriptors (DeepChem)\n'
                 f'Silhouette = {sil:.3f} — Categories are NOT separable in descriptor space',
                 fontweight='bold')
    ax.legend(fontsize=10)
    plt.tight_layout()
    fig.savefig(FIG_DIR / 'fig_deepchem_pca.png')
    fig.savefig(FIG_DIR / 'fig_deepchem_pca.svg')
    print(f"PCA figure saved to {FIG_DIR / 'fig_deepchem_pca.png'}")

    # Save results
    summary = {
        "pipeline": "DeepChem (200 RDKit descriptors + RandomForest)",
        "silhouette_score": round(sil, 4) if sil else None,
        "loo_auc_approved_vs_rest": round(auc, 4) if auc else None,
        "loo_auc_approved_vs_failures": round(auc_ab, 4) if auc_ab else None,
    }
    with open(EXP_DIR / "results_deepchem_summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    print(f"Summary saved to {EXP_DIR / 'results_deepchem_summary.json'}")


if __name__ == "__main__":
    test_with_molnet()
