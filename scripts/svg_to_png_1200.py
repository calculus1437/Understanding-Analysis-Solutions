from pathlib import Path
import sys
try:
    import cairosvg
except Exception as e:
    print('CAIROSVG_MISSING', e)
    sys.exit(1)

src = Path(r"c:\Users\calculus\Desktop\数学笔记\diagram_hier2_adjusted.svg")
out = Path(r"c:\Users\calculus\Desktop\数学笔记\diagram_hier2_1200dpi.png")

if not src.exists():
    print('SRC_MISSING', src)
    sys.exit(2)

# Convert SVG to PNG at 1200 DPI
cairosvg.svg2png(url=str(src), write_to=str(out), dpi=1200)
print('WROTE', out)
