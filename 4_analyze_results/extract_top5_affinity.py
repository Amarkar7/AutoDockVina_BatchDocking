### `4_analyze_results/extract_top5_affinity.py`

```python
import os
import glob
import sys

log_dir = sys.argv[1]
affinities = []

for filepath in glob.glob(os.path.join(log_dir, "*.log")):
    with open(filepath) as f:
        for line in f:
            if "REMARK VINA RESULT:" in line:
                affinity = float(line.split()[3])
                affinities.append((os.path.basename(filepath), affinity))
                break

top5 = sorted(affinities, key=lambda x: x[1])[:5]

print("Top 5 ligands by binding affinity:")
for name, affinity in top5:
    print(f"{name}: {affinity} kcal/mol")

