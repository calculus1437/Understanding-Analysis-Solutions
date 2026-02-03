from pathlib import Path
candidates = ['utf-8-sig','utf-8','gb18030','gbk','cp936','latin1']
src = Path(r'c:\Users\calculus\Desktop\数学笔记\```mermaid.md')
dst = Path(r'c:\Users\calculus\Desktop\数学笔记\mermaid_utf.md')
bytes_data = src.read_bytes()
for enc in candidates:
    try:
        text = bytes_data.decode(enc)
        dst.write_text(text, encoding='utf-8')
        print('written with', enc)
        break
    except Exception as e:
        print('failed', enc, e)
else:
    print('no encoding succeeded')
