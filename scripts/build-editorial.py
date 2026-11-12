#!/usr/bin/env python3
"""Build original GitHub-compatible SVG plates around unchanged UI captures.

Standard library only. Nested SVG viewBoxes focus the original JPEG; no UI text
or numeric values are painted over. The raw bytes remain in docs/editorial/raw.
"""
from pathlib import Path
from html import escape
import base64
import json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets/editorial'
RAW = ROOT / 'docs/editorial/raw'
OUT.mkdir(parents=True, exist_ok=True)

PALETTES = {
    'light': ('#F4F1E9', '#1D2421', '#C6422A', '#DEDCD3'),
    'dark': ('#0D1117', '#F0F1EC', '#F1775C', '#30363D'),
}

def text(x, y, value, size=24, weight=400, color='ink'):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{color}">{escape(value)}</text>'

def plate(name, theme, height, title, captures, footer, narrow=False):
    paper, ink, accent, muted = PALETTES[theme]
    width = 600 if narrow else 1200
    defs, content, image_ids = [], [], {}
    for i, (filename, viewbox, box) in enumerate(captures):
        if filename not in image_ids:
            data = base64.b64encode((RAW / filename).read_bytes()).decode()
            image_ids[filename] = f'shot{i}'
            defs.append(f'<image id="shot{i}" width="1265" height="712" href="data:image/jpeg;base64,{data}"/>')
        image_id = image_ids[filename]
        vx, vy, vw, vh = viewbox
        x, y, w, h = box
        content.append(f'<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="{vx} {vy} {vw} {vh}" overflow="hidden"><use href="#{image_id}"/></svg>')
    size = 31 if narrow else 48
    content.insert(0, text(24 if narrow else 40, 57 if narrow else 72, title, size, 700))
    if name == 'eval' and not narrow:
        content.extend([text(40,135,'Original',26,600),text(40,347,'Revision',26,600),text(640,135,'Human judgment',26,600)])
    content.append(text(24 if narrow else 40, height-24, footer, 17 if narrow else 22))
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">Unchanged product screenshots, cropped with SVG viewBoxes. Constructed demonstration material; no model calls. Details and original captures: docs/editorial/SOURCES.md.</desc>
<defs>{''.join(defs)}</defs><rect width="{width}" height="{height}" fill="{paper}"/>
<g font-family="Helvetica Neue, Helvetica, Arial, sans-serif" fill="{ink}">{''.join(content).replace('fill="ink"',f'fill="{ink}"')}</g></svg>'''
    suffix = '-narrow' if narrow else ''
    (OUT/f'{name}{suffix}-{theme}.svg').write_text(svg)

def cover(theme, narrow=False):
    paper, ink, accent, muted = PALETTES[theme]
    pieces = [
        text(40, 132, 'Andy Zhang', 108, 700),
        text(44, 192, 'Agent / Evaluation / Growth', 28, 400),
        text(44, 252, '张千羽', 32, 600),
        text(942, 49, 'Judgment', 24, 500),
        f'<path d="M942 203V76h143v127Z" fill="none" stroke="{ink}" stroke-width="7"/>',
        f'<path d="M980 241V114h143v127Z" fill="none" stroke="{accent}" stroke-width="7"/>',
        text(980, 280, 'Verification', 24, 500, accent),
    ]
    width, height = 1200, 320
    if narrow:
        width, height = 600, 260
        pieces = [text(24, 98, 'Andy Zhang', 72, 700),text(27,145,'Agent / Evaluation / Growth',24),text(27,218,'张千羽',32,600),f'<path d="M464 217v-82h82v82Z" fill="none" stroke="{ink}" stroke-width="5"/>',f'<path d="M483 236v-82h82v82Z" fill="none" stroke="{accent}" stroke-width="5"/>']
    suffix = '-narrow' if narrow else ''
    (OUT/f'cover{suffix}-{theme}.svg').write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc"><title id="title">Andy Zhang · 张千羽</title><desc id="desc">Agent, Evaluation, Growth. Judgment connected to verification through one deliberately displaced frame.</desc><rect width="{width}" height="{height}" fill="{paper}"/><g font-family="Helvetica Neue, Helvetica, Arial, PingFang SC, Microsoft YaHei, sans-serif" fill="{ink}">{''.join(pieces).replace('fill="ink"',f'fill="{ink}"')}</g></svg>''')

for theme in PALETTES:
    cover(theme)
    cover(theme, narrow=True)
    plate('eval', theme, 720, 'Read. Question. Revise.', [
        ('eval-review.jpg',(208,250,495,100),(40,155,520,105)),
        ('eval-diff.jpg',(208,245,495,245),(40,370,520,257)),
        ('eval-review.jpg',(725,90,493,100),(640,155,520,105)),
        ('eval-review.jpg',(725,338,493,319),(640,290,520,337)),
    ], 'Manual notes stay separate from model scores.')
    plate('eval', theme, 1090, 'Read. Question. Revise.', [
        ('eval-diff.jpg',(208,205,495,280),(24,90,552,312)),
        ('eval-review.jpg',(725,90,493,565),(24,420,552,632)),
    ], 'Constructed text / Manual review / No model call', narrow=True)
    plate('taste', theme, 620, 'Same content. Different context.', [
        ('taste-scene.jpg',(96,182,1045,435),(40,110,1120,466)),
    ], 'Personal / Work — viewing a comparison saves no preference.')
    plate('bundle', theme, 700, 'Growth has a cost.', [
        ('bundle-ledger.jpg',(392,270,825,395),(40,110,1120,536)),
    ], 'Synthetic orders / Conditional gross margin / Not business results')
    plate('rag', theme, 920, 'A number needs a source.', [
        ('rag-numeric.jpg',(311,108,570,459),(40,110,700,564)),
        ('rag-numeric.jpg',(920,22,300,235),(780,110,380,298)),
        ('rag-condition.jpg',(311,140,565,100),(40,680,1120,198)),
    ], 'Rule checks flag a review need; they do not verify meaning.')
    plate('rag', theme, 940, 'A number needs a source.', [
        ('rag-numeric.jpg',(920,84,300,112),(24,85,552,206)),
        ('rag-numeric.jpg',(311,108,570,459),(24,320,552,445)),
        ('rag-condition.jpg',(311,140,565,100),(24,800,552,98)),
    ], 'A changed date makes the old citation stale.', narrow=True)

print(json.dumps({p.name:p.stat().st_size for p in OUT.glob('*.svg')}, indent=2))
