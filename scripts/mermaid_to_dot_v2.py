#!/usr/bin/env python3
import re, html, sys
from pathlib import Path

# Input/output
INPUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(r"c:\Users\calculus\Desktop\数学笔记\mermaid_clean.md")
OUTPUT = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(r"c:\Users\calculus\Desktop\数学笔记\diagram_hier2.dot")

subgraph_re = re.compile(r"^\s*subgraph\s+(\S+)\s*\[(.*)\]")
node_re = re.compile(r"^\s*([^\[\s]+)\s*\[(.*?)\]\s*$")
edge_re = re.compile(r"^\s*([^\s-]+)\s*--+>\s*([^\s\[]+)\s*")
classdef_re = re.compile(r"^\s*classDef\s+(\S+)\s+(.*)")
class_apply_re = re.compile(r"^\s*class\s+(\S+)\s+(\S+)")

clusters=[]
cluster_map={}
nodes={}
node_cluster={}
edges=[]

def clean_label(s):
    s=s.strip()
    s=s.replace('<br>','\\n').replace('<br/>','\\n').replace('<br />','\\n')
    s=html.unescape(s)
    return s

text = INPUT.read_text(encoding='utf-8-sig')
for ln in text.splitlines():
    m = classdef_re.match(ln)
    if m:
        continue
    m = class_apply_re.match(ln)
    if m:
        continue
    m = subgraph_re.match(ln)
    if m:
        cid = m.group(1)
        title = m.group(2).strip()
        if (title.startswith('"') and title.endswith('"')) or (title.startswith("'") and title.endswith("'")):
            title = title[1:-1]
        title = clean_label(title)
        idx = len(clusters)
        clusters.append((cid,title,[]))
        cluster_map[cid]=idx
        cur=cid
        continue
    if ln.strip()=='end':
        cur=None
        continue
    m = node_re.match(ln)
    if m:
        nid,lab=m.group(1).strip(),m.group(2).strip()
        lab=clean_label(lab)
        nodes[nid]=lab
        if 'cur' in locals() and cur is not None:
            node_cluster[nid]=cluster_map[cur]
            clusters[cluster_map[cur]][2].append(nid)
        continue
    m = edge_re.match(ln)
    if m:
        a,b=m.group(1).strip(),m.group(2).strip()
        edges.append((a,b))
        continue
    if '-->' in ln:
        parts=ln.split('-->')
        if len(parts)>=2:
            a=parts[0].strip().split()[0]
            b=parts[1].strip().split()[0]
            edges.append((a,b))

# ensure referenced nodes exist
for a,b in list(edges):
    if a not in nodes: nodes[a]=a
    if b not in nodes: nodes[b]=b

# top layer names to hide as separate nodes
top_layer_names = ['数学海洋','启蒙港湾','基础海洋','专业深海','研究前沿','大师领域','未知深渊']

with OUTPUT.open('w',encoding='utf-8') as f:
    f.write('digraph MathMap {\n')
    f.write('  rankdir=TB;\n')
    f.write('  graph [fontname="Microsoft YaHei", fontsize=16, nodesep=1.0, ranksep=1.5, splines=true, overlap=false, ratio=fill, size="200,200!"];\n')
    f.write('  node [shape=box, style=rounded, fontsize=16, margin="0.15,0.15", fontname="Microsoft YaHei"];\n')
    f.write('  edge [arrowsize=0.7, fontname="Microsoft YaHei"];\n\n')

    # clusters with label and an internal anchor point (so cluster encloses it)
    for i,(cid,title,cnodes) in enumerate(clusters):
        f.write(f'  subgraph cluster_{i} {{\n')
        lab=title.replace('"','\\"')
        f.write(f'    label="{lab}";\n')
        f.write('    labelfontname="Microsoft YaHei";\n')
        f.write('    labelfontsize=16;\n')
        f.write('    labelloc="t";\n')
        f.write('    labeljust="c";\n')
        f.write('    margin="0.2";\n')
        f.write('    color="#cccccc";\n')
        # anchor inside cluster
        f.write(f'    "__anchor_{i}" [label="", shape=point, width=0.01, height=0.01, style=invis];\n')
        for nid in cnodes:
            lab2 = nodes.get(nid,nid).replace('"','\\"')
            f.write(f'    "{nid}" [label="{lab2}"];\n')
        f.write('  }\n\n')

    # nodes outside clusters (skip top layer nav nodes)
    for nid,lab in nodes.items():
        if nid not in node_cluster and nid not in top_layer_names:
            lab_esc = lab.replace('"','\\"')
            f.write('  "' + nid + '" [label="' + lab_esc + '"];\\n')
    f.write('\n')

    # edges with lighter style for inter-cluster
    for a,b in edges:
        a_q=f'"{a}"'
        b_q=f'"{b}"'
        a_idx=node_cluster.get(a,None)
        b_idx=node_cluster.get(b,None)
        attrs=[]
        if a_idx is not None and b_idx is not None and a_idx!=b_idx:
            attrs.extend(['constraint=false','color="#888888"','arrowsize=0.6','penwidth=0.6'])
        elif a_idx is None or b_idx is None:
            attrs.extend(['constraint=false','color="#888888"','arrowsize=0.6','penwidth=0.6'])
        attr = (' ['+','.join(attrs)+']') if attrs else ''
        f.write(f'  {a_q} -> {b_q}{attr};\n')
    f.write('\n')

    # chain anchors and add visible light edges between them to show top-level flow
    for i in range(len(clusters)-1):
        f.write(f'  "__anchor_{i}" -> "__anchor_{i+1}" [color="#666666", penwidth=0.8, arrowsize=0.7];\n')
    f.write('\n')

    f.write('}\n')

print('Wrote DOT to', OUTPUT)
