#!/usr/bin/env python3
"""
Convert the mermaid-ish file to a self-contained HTML that uses Viz.js to render DOT.
Produces vertical layout (rankdir=TB). No Graphviz required.
"""
import re
import html
from pathlib import Path
import json

ROOT = Path(r"c:\Users\calculus\Desktop\数学笔记")
INPUT = ROOT / "```mermaid.md"
OUTPUT_HTML = ROOT / "diagram.html"

subgraph_re = re.compile(r"^\s*subgraph\s+(\S+)\s*\[(.*)\]")
node_re = re.compile(r"^\s*([^\[\s]+)\s*\[(.*?)\]\s*$")
edge_re = re.compile(r"^\s*([^\s-]+)\s*--+>\s*([^\s\[]+)\s*")

clusters = []  # list of (id, title, nodes)
cluster_map = {}
nodes = {}
node_cluster = {}
edges = []
cur_cluster = None


def clean_label(s):
    s = s.strip()
    s = s.replace("<br>", "\\n").replace("<br/>", "\\n").replace("<br />", "\\n")
    s = html.unescape(s)
    return s

text = INPUT.read_text(encoding='utf-8')
lines = text.splitlines()
for ln in lines:
    m = subgraph_re.match(ln)
    if m:
        cid = m.group(1)
        title = m.group(2).strip()
        if (title.startswith('"') and title.endswith('"')) or (title.startswith("'") and title.endswith("'")):
            title = title[1:-1]
        title = clean_label(title)
        cur_cluster = cid
        idx = len(clusters)
        clusters.append([cid, title, []])
        cluster_map[cid] = idx
        continue
    if ln.strip() == 'end':
        cur_cluster = None
        continue
    m = node_re.match(ln)
    if m:
        nid, lab = m.group(1).strip(), m.group(2).strip()
        lab = clean_label(lab)
        nodes[nid] = lab
        if cur_cluster is not None:
            node_cluster[nid] = cluster_map[cur_cluster]
            clusters[cluster_map[cur_cluster]][2].append(nid)
        continue
    if '-->' in ln:
        parts = ln.split('-->')
        if len(parts) >= 2:
            a = parts[0].strip().split()[0]
            b = parts[1].strip().split()[0]
            edges.append((a, b))

# build DOT string with top-down layout
lines_dot = []
lines_dot.append('digraph MathMap {')
lines_dot.append('  rankdir=TB;')
lines_dot.append('  node [shape=box, style=rounded, fontsize=12, margin="0.2,0.2"];')
lines_dot.append('  edge [arrowsize=0.8];')
lines_dot.append('')
for i, (cid, title, cnodes) in enumerate(clusters):
    cluster_name = f'cluster_{i}'
    lines_dot.append(f'  subgraph {cluster_name} {{')
    lines_dot.append(f'    label="{title}";')
    lines_dot.append('    color="#cccccc";')
    for nid in cnodes:
        label = nodes.get(nid, nid).replace('"', '\\"')
        lines_dot.append(f'    "{nid}" [label="{label}"];')
    lines_dot.append('  }')
    lines_dot.append('')
# nodes outside clusters
for nid, lab in nodes.items():
    if nid not in node_cluster:
        lab2 = lab.replace('"', '\\"')
        lines_dot.append(f'  "{nid}" [label="{lab2}"];')
lines_dot.append('')
for a, b in edges:
    lines_dot.append(f'  "{a}" -> "{b}";')
lines_dot.append('}')

dot_text = '\n'.join(lines_dot)

# create HTML embedding Viz.js and the DOT
html_template = f'''<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <title>Math Diagram (Graphviz via Viz.js)</title>
  <style>body {{ font-family: sans-serif; margin: 8px; }}</style>
  <script src="https://unpkg.com/viz.js@2.1.2/dist/viz.js"></script>
  <script src="https://unpkg.com/viz.js@2.1.2/dist/full.render.js"></script>
</head>
<body>
  <h2>数学知识地图（Graphviz via Viz.js）</h2>
  <div id="diagram">Rendering...</div>
  <script>
    const dot = {json.dumps(dot_text)};
    const viz = new Viz();
    viz.renderSVGElement(dot)
      .then(function(element) {{
        const container = document.getElementById('diagram');
        container.innerHTML = '';
        container.appendChild(element);
      }})
      .catch(error => {{
        document.getElementById('diagram').textContent = 'Render error: ' + error;
        console.error(error);
      }});
  </script>
</body>
</html>
'''

OUTPUT_HTML.write_text(html_template, encoding='utf-8')
print(f'Wrote HTML to: {OUTPUT_HTML}')
''