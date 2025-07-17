
### `1_prepare_ligands/clean_and_generate3d.py`

```python
from rdkit import Chem
from rdkit.Chem import AllChem
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

supplier = Chem.SDMolSupplier(input_file, removeHs=False)
writer = Chem.SDWriter(output_file)

total = 0
skipped = 0
written = 0

for mol in supplier:
    total += 1
    if mol is None or not mol.GetNumConformers() == 0:
        skipped += 1
        continue
    try:
        AllChem.EmbedMolecule(mol)
        AllChem.UFFOptimizeMolecule(mol)
        writer.write(mol)
        written += 1
    except:
        skipped += 1

print(f"Total molecules: {total}")
print(f"Skipped molecules: {skipped}")
print(f"Written to output: {written}")
