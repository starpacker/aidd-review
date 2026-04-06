"""
Phase 2 - System 3: DruGUI End-to-End Virtual Screening Pipeline
Runs the DruGUI 8-stage pipeline on 36 molecules against EGFR (PDB: 6JX0).
Tests a full structure-based virtual screening workflow.

Requires druGUI conda environment with RDKit, pdbfixer, openmm.
AutoDock Vina optional (has fallback physics-based scoring).
"""

import json
import os
import subprocess
import sys

DATASET_PATH = os.path.join(os.path.dirname(__file__), "agent_evaluation_dataset.json")
DRUGUI_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "DruGUI")
SMILES_FILE = os.path.join(DRUGUI_DIR, "our_36_molecules.txt")
OUTPUT_DIR = os.path.join(DRUGUI_DIR, "output", "egfr_36mol_test")
RESULTS_PATH = os.path.join(os.path.dirname(__file__), "results_drugui.json")

PDB_ID = "6JX0"  # EGFR — Category A has Osimertinib (EGFR inhibitor)


def main():
    # Load dataset for mapping
    with open(DATASET_PATH, encoding='utf-8') as f:
        dataset = json.load(f)

    # Verify SMILES file exists
    if not os.path.exists(SMILES_FILE):
        print("Creating SMILES input file...")
        with open(SMILES_FILE, 'w') as f:
            for mol in dataset:
                f.write(mol['smiles'] + '\n')

    print(f"DruGUI directory: {DRUGUI_DIR}")
    print(f"SMILES file: {SMILES_FILE} ({len(dataset)} molecules)")
    print(f"Target: {PDB_ID} (EGFR)")
    print(f"Output: {OUTPUT_DIR}")
    print()

    # Run DruGUI
    cmd = [
        sys.executable, os.path.join(DRUGUI_DIR, "druGUI.py"),
        "run",
        "--pdb-id", PDB_ID,
        "--smiles-file", SMILES_FILE,
        "--output-dir", OUTPUT_DIR,
        "--top-k", "36",
    ]

    print(f"Running: {' '.join(cmd)}")
    print()

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=1800)

    print("=== STDOUT ===")
    print(result.stdout[-3000:] if len(result.stdout) > 3000 else result.stdout)

    if result.stderr:
        print("=== STDERR ===")
        print(result.stderr[-2000:] if len(result.stderr) > 2000 else result.stderr)

    print(f"\nReturn code: {result.returncode}")

    # Parse DruGUI output
    final_report_json = os.path.join(OUTPUT_DIR, "final_report.json")
    final_report_csv = os.path.join(OUTPUT_DIR, "final_report.csv")
    docking_csv = os.path.join(OUTPUT_DIR, "docking_results.csv")

    results = []

    if os.path.exists(final_report_json):
        print(f"\nParsing {final_report_json}...")
        with open(final_report_json, encoding='utf-8') as f:
            drugui_results = json.load(f)

        # Map DruGUI results back to our dataset
        for mol in dataset:
            smiles = mol['smiles']
            match = None
            for dr in drugui_results:
                if dr.get('smiles') == smiles:
                    match = dr
                    break

            entry = {
                "name": mol["name"],
                "smiles": smiles,
                "category": mol["category"],
            }

            if match:
                entry.update({
                    "vina_score": match.get("vina_score"),
                    "composite_score": match.get("composite_score") or match.get("final_score"),
                    "admet_pass": match.get("admet_pass"),
                    "lipinski_pass": match.get("lipinski_pass"),
                    "sa_score": match.get("sa_score"),
                    "rank": match.get("rank"),
                    "drugui_raw": match,
                })
            else:
                entry["error"] = "Not found in DruGUI output"

            results.append(entry)
    else:
        print(f"\nfinal_report.json not found. Checking for partial outputs...")

        # Try parsing partial outputs
        import csv
        if os.path.exists(docking_csv):
            print(f"Found docking results: {docking_csv}")
            with open(docking_csv) as f:
                reader = csv.DictReader(f)
                docking_data = list(reader)
            print(f"  {len(docking_data)} docking results")
        else:
            docking_data = []

        for mol in dataset:
            entry = {
                "name": mol["name"],
                "smiles": mol["smiles"],
                "category": mol["category"],
                "error": "DruGUI did not complete successfully",
                "return_code": result.returncode,
            }
            # Try to match with partial docking data
            for dr in docking_data:
                if dr.get('smiles') == mol['smiles']:
                    entry["vina_score"] = float(dr.get("vina_score", 0))
                    entry["error"] = "Partial results (docking only)"
                    break
            results.append(entry)

    # Save results
    with open(RESULTS_PATH, "w", encoding='utf-8') as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nResults saved to {RESULTS_PATH}")

    # Summary
    print("\n=== Summary ===")
    for cat in ["A_approved", "B_clinical_failure", "C_decoy"]:
        cat_results = [r for r in results if r["category"] == cat]
        scores = [r.get("composite_score") or r.get("vina_score") for r in cat_results if r.get("composite_score") or r.get("vina_score")]
        if scores:
            scores = [float(s) for s in scores if s is not None]
            if scores:
                avg = sum(scores) / len(scores)
                print(f"{cat}: avg_score={avg:.3f}, n={len(scores)}")
            else:
                print(f"{cat}: no valid scores")
        else:
            errors = sum(1 for r in cat_results if r.get("error"))
            print(f"{cat}: {errors} errors, no scores")


if __name__ == "__main__":
    main()
