#!/usr/bin/env python3
"""
Increase node and cluster label font sizes in a DOT file and write a new DOT.
Usage: python make_svg_xl.py [input.dot] [output.dot]

This script:
- Sets node fontsize to 28 and margin to 0.6
- Adds fontsize and labelfontsize attributes inside each cluster block
- Preserves labels and other node attributes
"""
import re
import sys
from pathlib import Path

ROOT = Path(r"c:\Users\calculus\Desktop\数学笔记")
INPUT = ROOT / "diagram_portrait_large.dot"
OUTPUT = ROOT / "diagram_portrait_xl.dot"

if len(sys.argv) > 1:
    INPUT = Path(sys.argv[1])
if len(sys.argv) > 2:
    OUTPUT = Path(sys.argv[2])

text = INPUT.read_text(encoding='utf-8')

# Replace node default attributes block safely
text = re.sub(r"^\s*node\s*\[.*?\];\s*$",
              '  node [shape=box, style=rounded, fontsize=28, margin="0.6,0.6", fontname="Microsoft YaHei", fixedsize=false];\n',
              text,
              flags=re.M | re.S)

# Insert cluster fontsize / labelfontsize inside each subgraph cluster_{n} block
# We'll find 'subgraph cluster_X {' and insert lines after that line
lines = text.splitlines()
out_lines = []
cluster_re = re.compile(r"^\s*subgraph\s+cluster_\d+\s*{\s*$")
inserted = 0
for i, ln in enumerate(lines):
    out_lines.append(ln)
    if cluster_re.match(ln):
        # insert cluster label fontsize attributes
        out_lines.append('    // cluster label sizing added by make_svg_xl.py')
        out_lines.append('    fontsize=20;')
        out_lines.append('    labelfontsize=20;')
        out_lines.append('    labelfontname="Microsoft YaHei";')
        inserted += 1

new_text = '\n'.join(out_lines) + '\n'
OUTPUT.write_text(new_text, encoding='utf-8')
print(f'Wrote XL DOT to: {OUTPUT} (inserted cluster attrs in {inserted} clusters)')
print('To render SVG:')
print(f'  & "C:\\Program Files\\Graphviz\\bin\\dot.exe" -Tsvg "{OUTPUT}" -o "{OUTPUT.with_suffix(".svg")}"')
