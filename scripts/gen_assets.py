"""Generate the profile README's SVG assets (dark + light).

Text is outlined to paths with fontTools so the SVGs render the same in every
browser without web fonts. Needs Inter Display and JetBrains Mono installed.

    pip install fonttools
    python3 scripts/gen_assets.py
"""
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

OUT = Path(__file__).resolve().parent.parent / "assets"
FONTS = {
    "display": "/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf",
    "display-semi": "/usr/share/fonts/opentype/inter/InterDisplay-SemiBold.otf",
    "mono": "/usr/share/fonts/truetype/jetbrains-mono/JetBrainsMono-Regular.ttf",
    "mono-med": "/usr/share/fonts/truetype/jetbrains-mono/JetBrainsMono-Medium.ttf",
    "mono-bold": "/usr/share/fonts/truetype/jetbrains-mono/JetBrainsMono-Bold.ttf",
}
_cache = {}

THEMES = {
    "dark": dict(bg="#0a0c10", card="#0d1117", line="#262c36", fg="#f0f3f6",
                 muted="#8b949e", faint="#3d444d", accent="#3fb950"),
    "light": dict(bg="#ffffff", card="#ffffff", line="#d1d9e0", fg="#0d1117",
                  muted="#59636e", faint="#c8d1da", accent="#1a7f37"),
}


def font(name):
    if name not in _cache:
        f = TTFont(FONTS[name])
        _cache[name] = (f, f.getGlyphSet(), f.getBestCmap(), f["head"].unitsPerEm)
    return _cache[name]


def measure(text, name, size, track=0.0):
    f, gs, cmap, upm = font(name)
    s = size / upm
    w = sum(gs[cmap[ord(c)]].width * s + track * size for c in text)
    return w - track * size if text else 0


def text_path(text, name, size, x, y, track=0.0, anchor="start"):
    """Return an SVG path 'd' for text with its baseline at (x, y)."""
    f, gs, cmap, upm = font(name)
    s = size / upm
    if anchor != "start":
        w = measure(text, name, size, track)
        x -= w if anchor == "end" else w / 2
    pen = SVGPathPen(gs)
    for c in text:
        g = cmap[ord(c)]
        gs[g].draw(TransformPen(pen, (s, 0, 0, -s, x, y)))
        x += gs[g].width * s + track * size
    return pen.getCommands()


def P(d, fill, extra=""):
    return f'<path d="{d}" fill="{fill}"{extra}/>'


def svg(w, h, title, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'role="img" aria-label="{title}"><title>{title}</title>{body}</svg>\n')


def header(t):
    W, H = 1200, 300
    name = "Brad Flaugher"
    nx, ny, ns = 64, 168, 104
    nw = measure(name, "display", ns, -0.025)
    tag = "SMALL MODELS ON THE DEVICE  /  SOFTWARE FOR SMALL MACHINES"
    body = f'''
<defs>
  <pattern id="dots" width="20" height="20" patternUnits="userSpaceOnUse">
    <circle cx="10" cy="10" r="1.1" fill="{t['fg']}"/>
  </pattern>
  <linearGradient id="fade" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#fff" stop-opacity="0"/>
    <stop offset=".45" stop-color="#fff" stop-opacity=".25"/>
    <stop offset="1" stop-color="#fff" stop-opacity="1"/>
  </linearGradient>
  <mask id="m"><rect width="{W}" height="{H}" fill="url(#fade)"/></mask>
  <linearGradient id="band" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{t['accent']}" stop-opacity="0"/>
    <stop offset=".5" stop-color="{t['accent']}" stop-opacity="1"/>
    <stop offset="1" stop-color="{t['accent']}" stop-opacity="0"/>
  </linearGradient>
  <mask id="dm"><rect width="{W}" height="{H}" fill="url(#dots)"/></mask>
  <clipPath id="c"><rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="14"/></clipPath>
</defs>
<g clip-path="url(#c)">
  <rect width="{W}" height="{H}" fill="{t['card']}"/>
  <rect width="{W}" height="{H}" fill="url(#dots)" opacity=".16" mask="url(#m)"/>
  <g mask="url(#dm)">
    <rect x="-260" y="0" width="260" height="{H}" fill="url(#band)" opacity=".9">
      <animate attributeName="x" values="-260;{W};{W}" keyTimes="0;.55;1" dur="9s" repeatCount="indefinite"/>
    </rect>
  </g>
</g>
<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="{t['line']}"/>
{P(text_path(name, "display", ns, nx, ny, -0.025), t['fg'])}
<rect x="{nx + nw + 14:.1f}" y="{ny - 76}" width="38" height="76" fill="{t['accent']}">
  <animate attributeName="opacity" values="1;1;0;0" keyTimes="0;.5;.5;1" dur="1.1s" repeatCount="indefinite"/>
</rect>
{P(text_path(tag, "mono-med", 15, nx + 4, 226, 0.08), t['muted'])}
'''
    return svg(W, H, "Brad Flaugher. Small models on the device. Software for small machines.", body)


STATS = [
    ("98.8%", "ROUTING ACCURACY", "divid3, 582 held-out queries"),
    ("11.8M", "PARAMETERS", "post-training, in the browser"),
    ("1.7B", "PARAMETERS", "genaro, on the phone"),
    ("0", "SERVERS", "every model runs on the device"),
]


def stats(t):
    W, H = 1200, 180
    cw = W / len(STATS)
    parts = [f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="14" fill="{t["card"]}" stroke="{t["line"]}"/>']
    for i, (num, label, sub) in enumerate(STATS):
        x = i * cw
        if i:
            parts.append(f'<line x1="{x}" y1="28" x2="{x}" y2="{H-28}" stroke="{t["line"]}"/>')
        d0 = i * 0.12
        g = (f'<g opacity="1"><animate attributeName="opacity" values="0;0;1;1" '
             f'keyTimes="0;{d0/1.6:.3f};{(d0+0.5)/1.6:.3f};1" dur="1.6s" fill="freeze"/>')
        g += f'<rect x="{x+36}" y="34" width="18" height="3" fill="{t["accent"]}"/>'
        g += P(text_path(num, "display-semi", 58, x + 34, 106, -0.02), t['fg'])
        g += P(text_path(label, "mono-bold", 12.5, x + 36, 134, 0.1), t['fg'])
        g += P(text_path(sub, "mono", 12.5, x + 36, 155, 0), t['muted'])
        parts.append(g + "</g>")
    alt = ". ".join(f"{n} {l.lower()}: {s}" for n, l, s in STATS)
    return svg(W, H, alt, "".join(parts))


SECTIONS = ["ON DEVICE", "GAME BOY", "ANDROID", "BOOK"]


def section(t, i, label):
    W, H = 1200, 40
    num = f"{i:02d}"
    x = 2
    body = P(text_path(num, "mono-bold", 15, x, 26, 0.1), t['accent'])
    lx = x + measure(num, "mono-bold", 15, 0.1) + 18
    body += P(text_path(label, "mono-bold", 15, lx, 26, 0.16), t['fg'])
    ex = lx + measure(label, "mono-bold", 15, 0.16) + 22
    body += f'<line x1="{ex:.1f}" y1="21" x2="{W-2}" y2="21" stroke="{t["faint"]}"/>'
    return svg(W, H, f"{num} {label.title()}", body)


def main():
    OUT.mkdir(exist_ok=True)
    for theme, t in THEMES.items():
        (OUT / f"header-{theme}.svg").write_text(header(t))
        (OUT / f"stats-{theme}.svg").write_text(stats(t))
        for i, s in enumerate(SECTIONS, 1):
            slug = s.lower().replace(" ", "-")
            (OUT / f"section-{slug}-{theme}.svg").write_text(section(t, i, s))
    print("wrote", sorted(p.name for p in OUT.glob("*.svg")))


if __name__ == "__main__":
    main()
