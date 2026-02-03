#!/usr/bin/env python3
"""
Make an extra-large SVG-friendly DOT by increasing node font size and enforcing
larger node box sizes so text becomes clearly readable.

Usage: python make_svg_xxl.py [input.dot] [output.dot]

This script:
- Sets graph nodesep/ranksep larger for more spacing
- Sets node defaults to fontsize=36, margin larger, and fixed width/height
- Writes `diagram_portrait_xxl.dot` by default
"""
import re
import sys
from pathlib import Path

ROOT = Path(r"c:\Users\calculus\Desktop\数学笔记")
INPUT = ROOT / "diagram_portrait_xl.dot"
OUTPUT = ROOT / "diagram_portrait_xxl.dot"

if len(sys.argv) > 1:
    INPUT = Path(sys.argv[1])
if len(sys.argv) > 2:
    OUTPUT = Path(sys.argv[2])

text = INPUT.read_text(encoding='utf-8')

# Increase overall spacing
text = re.sub(r'(graph \[.*?\])',
              'graph [fontname="Microsoft YaHei", fontsize=14, nodesep=1.2, ranksep=1.4, splines=true, ratio=fill, size="8,14!"]',
              text, flags=re.S)

# Replace node default attributes to enforce bigger boxes and larger text
text = re.sub(r'^\s*node\s*\[.*?\];\s*$',
              '  node [shape=box, style=rounded, fontsize=36, margin="0.8,0.8", fontname="Microsoft YaHei", fixedsize=true, width=4.0, height=1.8];',
              text, flags=re.M | re.S)

OUTPUT.write_text(text, encoding='utf-8')
print(f'Wrote XXL DOT to: {OUTPUT}')
print('Render command:')
print(f'  & "C:\\Program Files\\Graphviz\\bin\\dot.exe" -Tsvg "{OUTPUT}" -o "{OUTPUT.with_suffix(".svg")}"')
