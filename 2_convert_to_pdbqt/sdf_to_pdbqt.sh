### `2_convert_to_pdbqt/sdf_to_pdbqt.sh`

```bash
#!/bin/bash

INPUT_DIR="$1"
OUTPUT_DIR="$2"

mkdir -p "$OUTPUT_DIR"

for file in "$INPUT_DIR"/*.sdf; do
    base=$(basename "$file" .sdf)
    obabel "$file" -O "$OUTPUT_DIR/$base.pdbqt"
done
