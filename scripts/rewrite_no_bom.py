from pathlib import Path
p=Path(r'c:\Users\calculus\Desktop\数学笔记\diagram_portrait_xxl.dot')
s=p.read_text(encoding='utf-8-sig')
p.write_text(s,encoding='utf-8')
print('rewrote without BOM:', p)