#!/usr/bin/env python3
"""
Strip coloring from an existing diagram.dot and set portrait layout attributes.
Writes `diagram_portrait.dot` beside the source file.
Usage: python dot_portrait.py [input.dot] [output.dot]
"""
import re
import sys
from pathlib import Path

ROOT = Path(r"c:\Users\calculus\Desktop\数学笔记")
INPUT = ROOT / "diagram.dot"
OUTPUT = ROOT / "diagram_portrait.dot"

if len(sys.argv) > 1:
    INPUT = Path(sys.argv[1])
if len(sys.argv) > 2:
    OUTPUT = Path(sys.argv[2])

text = INPUT.read_text(encoding='utf-8')

# Replace graph[...] header with portrait-friendly attributes
new_graph_attrs = ('graph [fontname="Microsoft YaHei", fontsize=12, '
                   'nodesep=0.6, ranksep=0.9, splines=true, ratio=fill, size="8,14!"];')
text, nsub = re.subn(r'graph \[.*?\];', new_graph_attrs, text, flags=re.S)

# Remove fillcolor and style=filled and penwidth lines (cancel coloring)
text = re.sub(r'\s*style=filled;\n', '\n', text)
text = re.sub(r'\s*fillcolor="[^"]*";\n', '', text)
text = re.sub(r'\s*penwidth=[0-9\.]+;\n', '', text)

# Optionally normalize cluster color to a subtle gray (or remove color lines)
# Here we replace explicit color lines inside clusters with a light gray border
text = re.sub(r'\s*color="#[0-9a-fA-F]+";\n', '    color="#cccccc";\n', text)

# Ensure rankdir=TB exists
if 'rankdir=' not in text:
    text = text.replace('digraph MathMap {\n', 'digraph MathMap {\n  rankdir=TB;\n')

OUTPUT.write_text(text, encoding='utf-8')
print(f'Wrote portrait DOT to: {OUTPUT} (replaced {nsub} graph header)')
