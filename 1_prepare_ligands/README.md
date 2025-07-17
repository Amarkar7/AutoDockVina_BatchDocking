# Step 1: Clean Ligands and Generate 3D Structures

This script uses RDKit to:
- Remove molecules with stereochemistry issues
- Generate 3D conformations
- Save the cleaned output to a new SDF file

## Usage

```bash
python clean_and_generate3d.py input.sdf output_cleaned.sdf
