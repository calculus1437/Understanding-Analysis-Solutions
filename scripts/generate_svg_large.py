#!/usr/bin/env python3
"""
Read a DOT file (default: diagram_portrait.dot), increase node font size/margins,
write diagram_portrait_large.dot and print paths. Does not invoke Graphviz so you
can inspect the DOT first if you want. Usage:

python generate_svg_large.py [input.dot] [output.dot]

"""
import re
import sys
from pathlib import Path

ROOT = Path(r"c:\Users\calculus\Desktop\数学笔记")
INPUT = ROOT / "diagram_portrait.dot"
OUTPUT = ROOT / "diagram_portrait_large.dot"

if len(sys.argv) > 1:
    INPUT = Path(sys.argv[1])
if len(sys.argv) > 2:
    OUTPUT = Path(sys.argv[2])

text = INPUT.read_text(encoding='utf-8')

# Replace the node default attributes block
# match a line starting with optional space then node [ ... ];
node_re = re.compile(r"^\s*node\s*\[.*?\];\s*$", flags=re.M | re.S)
new_node = '  node [shape=box, style=rounded, fontsize=18, margin="0.45,0.45", fontname="Microsoft YaHei", fixedsize=false];\n'
if node_re.search(text):
    text = node_re.sub(new_node, text)
else:
    # insert after graph [...] header block - simpler: put near top after graph header
    text = text.replace('\n\n', '\n' + new_node + '\n', 1)

# Also increase label fontsize for clusters (cluster label uses label attribute) by adding a cluster style
# Note: keep cluster label text as-is to avoid accidental syntax changes.
# If needed later, we can add cluster-level fontsize attributes per-cluster.

OUTPUT.write_text(text, encoding='utf-8')
print(f'Wrote modified DOT to: {OUTPUT}')
print('Now run Graphviz to produce SVG:')
print(f'  & "C:\\Program Files\\Graphviz\\bin\\dot.exe" -Tsvg "{OUTPUT}" -o "{OUTPUT.with_suffix(".svg")}"')
