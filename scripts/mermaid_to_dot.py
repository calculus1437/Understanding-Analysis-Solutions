#!/usr/bin/env python3
"""
Simple converter: mermaid-ish -> Graphviz DOT
- Parses `subgraph` blocks as clusters
- Parses node definitions like `A1[Label<br>more]`
- Parses edges like `A1 --> B1` or `数学海洋 --> 启蒙港湾`

Not a full mermaid parser, but enough for your document structure.
"""
import re
import html
import sys
from pathlib import Path

# Paths
ROOT = Path(r"c:\Users\calculus\Desktop\数学笔记")
INPUT = ROOT / "```mermaid.md"
OUTPUT = ROOT / "diagram.dot"

if len(sys.argv) > 1:
    INPUT = Path(sys.argv[1])
if len(sys.argv) > 2:
    OUTPUT = Path(sys.argv[2])

subgraph_re = re.compile(r"^\s*subgraph\s+(\S+)\s*\[(.*)\]")
node_re = re.compile(r"^\s*([^\[\s]+)\s*\[(.*?)\]\s*$")
edge_re = re.compile(r"^\s*([^\s-]+)\s*--+>\s*([^\s\[]+)\s*")
classdef_re = re.compile(r"^\s*classDef\s+(\S+)\s+(.*)")
class_apply_re = re.compile(r"^\s*class\s+(\S+)\s+(\S+)")

clusters = []  # list of (id, title, nodes)
cluster_map = {}  # id -> index
nodes = {}  # node_id -> label
node_cluster = {}  # node_id -> cluster_index
edges = []  # (from, to)

cur_cluster = None
cur_cluster_title = None

# helper to clean label: replace <br> with \n, unescape html entities
def clean_label(s):
    s = s.strip()
    s = s.replace("<br>", "\\n").replace("<br/>", "\\n").replace("<br />", "\\n")
    s = html.unescape(s)
    return s

text = INPUT.read_text(encoding='utf-8-sig')
lines = text.splitlines()
for ln in lines:
    # parse classDef lines like: classDef ocean fill:#1e88e5,stroke:#0d47a1,stroke-width:4px,color:#fff,font-size:16px
    mcd = classdef_re.match(ln)
    if mcd:
        cname = mcd.group(1).strip()
        props = mcd.group(2).strip()
        # parse key:val pairs separated by commas
        style = {}
        for part in props.split(','):
            if ':' in part:
                k, v = part.split(':', 1)
                style[k.strip()] = v.strip()
        # store raw hex colors or values
        try:
            class_styles
        except NameError:
            class_styles = {}
        class_styles[cname] = style
        continue
    # parse class application lines like: class 启蒙港湾 harbor
    mca = class_apply_re.match(ln)
    if mca:
        target = mca.group(1).strip()
        cname = mca.group(2).strip()
        try:
            class_map
        except NameError:
            class_map = {}
        class_map[target] = cname
        continue
    # subgraph start
    m = subgraph_re.match(ln)
    if m:
        cid = m.group(1)
        title = m.group(2).strip()
        # remove surrounding quotes if present
        if (title.startswith('"') and title.endswith('"')) or (title.startswith("'") and title.endswith("'")):
            title = title[1:-1]
        title = clean_label(title)
        cur_cluster = cid
        idx = len(clusters)
        clusters.append((cid, title, []))
        cluster_map[cid] = idx
        continue
    # end lines
    if ln.strip() == 'end':
        cur_cluster = None
        cur_cluster_title = None
        continue
    # node definitions
    m = node_re.match(ln)
    if m:
        nid, lab = m.group(1).strip(), m.group(2).strip()
        lab = clean_label(lab)
        nodes[nid] = lab
        if cur_cluster is not None:
            node_cluster[nid] = cluster_map[cur_cluster]
            clusters[cluster_map[cur_cluster]][2].append(nid)
        continue
    # edges
    m = edge_re.match(ln)
    if m:
        a, b = m.group(1).strip(), m.group(2).strip()
        edges.append((a, b))
        continue
    # also allow lines like '数学海洋 --> 启蒙港湾' with non-ascii ids
    if '-->' in ln:
        parts = ln.split('-->')
        if len(parts) >= 2:
            a = parts[0].strip()
            b = parts[1].strip()
            # drop trailing annotations after b (like [label]) if any
            b = b.split()[0]
            a = a.split()[0]
            edges.append((a, b))

# produce DOT
with OUTPUT.open('w', encoding='utf-8') as f:
    f.write('digraph MathMap {\n')
    # Use top-to-bottom layout (vertical) and set fonts that support Chinese
    # layout and spacing adjustments to improve balance (not fully vertical/horizontal)
    f.write('  rankdir=TB;\n')
    # set very large uniform fonts (user requested 256) and increase spacing
    f.write('  graph [fontname="Microsoft YaHei", fontsize=128, nodesep=3.0, ranksep=4.0, splines=true, overlap=false, ratio=fill, size="200,200!"];\n')
    f.write('  node [shape=box, style=rounded, fontsize=128, margin="1.5,1.5", fontname="Microsoft YaHei", fixedsize=false];\n')
    f.write('  edge [arrowsize=0.8, fontname="Microsoft YaHei"];\n\n')

    # ensure any node referenced by edges but not explicitly defined gets a default label
    for a, b in edges:
        if a not in nodes:
            nodes[a] = a
        if b not in nodes:
            nodes[b] = b

    # clusters
    for i, (cid, title, cnodes) in enumerate(clusters):
        cluster_name = f'cluster_{i}'
        f.write(f'  subgraph {cluster_name} {{\n')
        # larger cluster label for readability; no fill/color (no dyeing)
        lab = title.replace('"', '\\"')
        f.write(f'    label="{lab}";\n')
        # align cluster title at top and center it so title aligns with content
        f.write('    labelfontname="Microsoft YaHei";\n')
        f.write('    labelfontsize=128;\n')
        f.write('    labelloc="t";\n')
        f.write('    labeljust="c";\n')
        f.write('    margin="0.6";\n')
        f.write('    color="#cccccc";\n')
        # write an invisible anchor inside the cluster to help enforce vertical ordering
        f.write(f'    "__anchor_{i}" [label="", shape=point, width=0, height=0, style=invis];\n')
        # write nodes inside cluster
        for nid in cnodes:
            label = nodes.get(nid, nid)
            label = label.replace('"', '\\"')
            f.write(f'    "{nid}" [label="{label}"];\n')
        # do not force strict vertical stacking; allow Graphviz to balance layout
        f.write('  }\n\n')

    # nodes defined outside clusters
    for nid, lab in nodes.items():
        if nid not in node_cluster:
            lab2 = lab.replace('"', '\\"')
            f.write(f'  "{nid}" [label="{lab2}"];\n')
    f.write('\n')

    # edges: mark cross-cluster edges with constraint=false so layout can distribute more evenly
    for a, b in edges:
        a_q = f'"{a}"'
        b_q = f'"{b}"'
        attr = ''
        try:
            a_idx = node_cluster.get(a, None)
            b_idx = node_cluster.get(b, None)
        except Exception:
            a_idx = None
            b_idx = None
        # if nodes are in different clusters (or one is outside), relax rank constraint
        if a_idx is not None and b_idx is not None and a_idx != b_idx:
            attr = ' [constraint=false]'
        elif a_idx is None or b_idx is None:
            # edge involving top-level nodes: relax to allow better packing
            attr = ' [constraint=false]'
        f.write(f'  {a_q} -> {b_q}{attr};\n')
    f.write('\n')
    # Chain the invisible anchors between clusters to enforce vertical ordering of layers
    # anchors were created inside each cluster above, so only chain them here
    for i in range(len(clusters) - 1):
        # use constraint=true and a high weight so dot respects the vertical order
        f.write(f'  "__anchor_{i}" -> "__anchor_{i+1}" [style=invis, weight=100, constraint=true];\n')
    f.write('\n')
    f.write('}\n')

print(f'Wrote DOT to: {OUTPUT}')
