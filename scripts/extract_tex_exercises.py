import re
from pathlib import Path

tex = Path(r"c:\Users\calculus\Downloads\Understanding_analysis_4.tex")
md = Path(r"c:\Users\calculus\Desktop\数学笔记\Understanding Analysis 习题解答.md")
backup = md.with_suffix('.md.bak')

text = tex.read_text(encoding='utf-8')
# Find lines that start with 习题 or 练习 followed by chapter 4 numbering
pattern = re.compile(r'(?m)^(?:\s*(?:习题|练习)\s*)(4\.(\d+)\.(\d+))(?:[\.。])?\s*(.*)$')
# This captures the numbering in group1 and rest of line in group4
mapping = {}
for m in pattern.finditer(text):
    key = m.group(1)  # e.g., '4.2.1'
    rest = m.group(4).strip()
    # full line
    full = m.group(0).strip()
    mapping[key] = full

print('Found', len(mapping), 'exercises in TeX for chapter 4')

# Read md
md_text = md.read_text(encoding='utf-8')
lines = md_text.splitlines()

out_lines = []
inserted = set()
# pattern to detect md markers like $4.2.1.$ or 4.2.1. etc
md_pat = re.compile(r'\$?\s*(4\.(\d+)\.(\d+))\.\$?')
for line in lines:
    out_lines.append(line)
    m = md_pat.search(line)
    if m:
        key = m.group(1)
        if key in mapping and key not in inserted:
            out_lines.append('')
            out_lines.append('**从 TeX 提取：** ' + mapping[key])
            inserted.add(key)

# For any mapping keys not found in md, append them at end under a new heading
remaining = [k for k in mapping.keys() if k not in inserted]
if remaining:
    out_lines.append('')
    out_lines.append('## 附加：TeX 中未匹配到的习题')
    for k in sorted(remaining):
        out_lines.append('')
        out_lines.append('**' + k + '** ' + mapping[k])

# backup and write
backup.write_text(md_text, encoding='utf-8')
md.write_text('\n'.join(out_lines), encoding='utf-8')
print('Wrote modified MD and backup to', backup)
