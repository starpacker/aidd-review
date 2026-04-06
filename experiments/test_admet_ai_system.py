"""
Phase 2 - System 4: ADMET-AI (SOTA ML ADMET Predictor)
Uses Chemprop GNN to predict 41 ADMET endpoints for each molecule.
Tests whether ML-based ADMET prediction can distinguish A/B/C categories.
"""

import json
import os
import sys

DATASET_PATH = os.path.join(os.path.dirname(__file__), "agent_evaluation_dataset.json")
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "results_admet_ai_system.json")


def main():
    print("Loading ADMET-AI model...")
    from admet_ai import ADMETModel
    model = ADMETModel()
    print("Model loaded successfully.")

    with open(DATASET_PATH, encoding='utf-8') as f:
        dataset = json.load(f)

    print(f"Evaluating {len(dataset)} molecules across 41 ADMET endpoints...")

    results = []
    for i, mol in enumerate(dataset):
        name = mol["name"]
        smiles = mol["smiles"]
        category = mol["category"]
        print(f"[{i+1}/{len(dataset)}] {name} ({category})")

        try:
            preds = model.predict(smiles=smiles)

            # preds is a dict of endpoint -> value
            # Convert to serializable format
            pred_dict = {}
            for k, v in preds.items():
                try:
                    pred_dict[k] = float(v)
                except (TypeError, ValueError):
                    pred_dict[k] = str(v)

            entry = {
                "name": name,
                "smiles": smiles,
                "category": category,
                "num_endpoints": len(pred_dict),
                "predictions": pred_dict,
            }

            # Compute summary safety metrics
            # Key toxicity endpoints (higher = more toxic for classification endpoints)
            tox_keys = [k for k in pred_dict if any(t in k.lower() for t in ['tox', 'herg', 'ames', 'dili', 'ld50', 'carci'])]
            safety_keys = [k for k in pred_dict if any(t in k.lower() for t in ['hia', 'bioavail', 'caco', 'solub', 'perm'])]

            entry["toxicity_flags"] = {k: pred_dict[k] for k in tox_keys}
            entry["safety_flags"] = {k: pred_dict[k] for k in safety_keys}

        except Exception as e:
            print(f"  ERROR: {e}")
            entry = {
                "name": name,
                "smiles": smiles,
                "category": category,
                "num_endpoints": 0,
                "predictions": {},
                "error": str(e),
            }

        results.append(entry)

    # Save full results
    with open(OUTPUT_PATH, "w", encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {OUTPUT_PATH}")

    # Summary statistics
    print("\n=== Summary ===")
    for cat in ["A_approved", "B_clinical_failure", "C_decoy"]:
        cat_results = [r for r in results if r["category"] == cat and r.get("num_endpoints", 0) > 0]
        if cat_results:
            # Average over all shared endpoints
            all_keys = set()
            for r in cat_results:
                all_keys.update(r["predictions"].keys())

            print(f"\n{cat} ({len(cat_results)} molecules, {len(all_keys)} endpoints):")

            # Show key clinical endpoints
            key_endpoints = ['ClinTox', 'hERG', 'AMES', 'DILI', 'HIA_Hou', 'Caco2_Wang',
                           'BBB_Martins', 'Bioavailability_Ma', 'Lipophilicity_AstraZeneca',
                           'Solubility_AqSolDB', 'CYP2D6_Veith', 'CYP3A4_Veith']

            for ep in key_endpoints:
                vals = [r["predictions"].get(ep) for r in cat_results if ep in r.get("predictions", {})]
                if vals:
                    vals = [v for v in vals if v is not None]
                    if vals:
                        avg = sum(vals) / len(vals)
                        print(f"  {ep}: mean={avg:.3f} (n={len(vals)})")


if __name__ == "__main__":
    main()
