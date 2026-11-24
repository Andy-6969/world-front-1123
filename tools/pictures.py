"""Flat SVG drawings, one per story picture. Each function takes the box width and height (in CSS px) and
returns SVG markup for that box. The scene sits on the left; the right side is kept calm so the big
number drawn over it (in HTML) stays readable."""

NAVY = "#14213d"
SEA = "#1d4e89"
SKY = "#dbe8f5"
SAND = "#efe2c4"
INK = "#1b1b1b"
RED = "#c62828"
ORANGE = "#f08a24"
YELLOW = "#ffd23f"
GREEN = "#2e7d32"
GREY = "#8a8f98"


def svg(w, h, body, bg):
    return (f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg">'
            f'<rect width="{w}" height="{h}" fill="{bg}"/>{body}</svg>')


def warship(w, h):
    sea_y = h * 0.62
    b = [f'<rect y="{sea_y}" width="{w}" height="{h - sea_y}" fill="{SEA}"/>',
         # night harbour sky glow
         f'<circle cx="{w * 0.08}" cy="{h * 0.2}" r="{h * 0.08}" fill="#f4e9c8"/>',
         # capsized hull, tilted, half under water
         f'<g transform="translate({w * 0.12},{sea_y - h * 0.05}) rotate(-17)">'
         f'<path d="M0 0 L{w * 0.36} 0 L{w * 0.32} {h * 0.16} L{w * 0.03} {h * 0.16} Z" fill="#6b7280"/>'
         f'<rect x="{w * 0.1}" y="{-h * 0.12}" width="{w * 0.12}" height="{h * 0.12}" fill="#4b5563"/>'
         f'<rect x="{w * 0.14}" y="{-h * 0.22}" width="{w * 0.025}" height="{h * 0.1}" fill="#4b5563"/></g>',
         # smoke and fire
         f'<circle cx="{w * 0.25}" cy="{h * 0.3}" r="{h * 0.13}" fill="#4b5563" opacity=".75"/>',
         f'<circle cx="{w * 0.33}" cy="{h * 0.22}" r="{h * 0.1}" fill="#6b7280" opacity=".7"/>',
         f'<path d="M{w * 0.22} {sea_y - 2} q{w * 0.02} {-h * 0.2} {w * 0.05} {-h * 0.08} q{w * 0.01} {-h * 0.14} '
         f'{w * 0.04} {-h * 0.02} q{w * 0.02} {-h * 0.12} {w * 0.03} {h * 0.1} Z" fill="{ORANGE}"/>']
    # seven drone wakes converging on the hull
    for i in range(7):
        y = sea_y + 6 + i * (h - sea_y - 10) / 6.5
        x0 = w * 0.46 + (i % 3) * 6
        b.append(f'<path d="M{x0 + w * 0.12} {y} L{x0} {y - 2}" stroke="#ffffff" stroke-width="1.6" opacity=".85"/>')
        b.append(f'<path d="M{x0 - 7} {y - 2} l8 -2.5 l0 5 Z" fill="{YELLOW}"/>')
    return svg(w, h, "".join(b), "#24324d")


def chip(w, h):
    s = h * 0.6
    x, y = w * 0.07, h * 0.2
    pins = "".join(
        f'<rect x="{x + s * (0.12 + i * 0.16)}" y="{y - s * 0.12}" width="{s * 0.06}" height="{s * 0.12}" fill="#9aa4b2"/>'
        f'<rect x="{x + s * (0.12 + i * 0.16)}" y="{y + s}" width="{s * 0.06}" height="{s * 0.12}" fill="#9aa4b2"/>'
        for i in range(5))
    # rising line from the chip toward the right
    pts = [(w * 0.08, h * 0.95), (w * 0.2, h * 0.86), (w * 0.3, h * 0.9), (w * 0.42, h * 0.62),
           (w * 0.5, h * 0.4), (w * 0.56, h * 0.18)]
    line = " ".join(f"{a:.1f},{b:.1f}" for a, b in pts)
    body = (pins + f'<rect x="{x}" y="{y}" width="{s}" height="{s}" rx="4" fill="#1f2937"/>'
            f'<rect x="{x + s * 0.2}" y="{y + s * 0.2}" width="{s * 0.6}" height="{s * 0.6}" fill="#76b900"/>'
            f'<text x="{x + s / 2}" y="{y + s * 0.59}" font-family="Bahnschrift,Arial" font-weight="700" '
            f'font-size="{s * 0.2}" text-anchor="middle" fill="#0b1d05">GPU</text>'
            f'<polyline points="{line}" fill="none" stroke="#16a34a" stroke-width="4" stroke-linejoin="round"/>'
            f'<path d="M{w * 0.56 - 9} {h * 0.2} L{w * 0.57} {h * 0.08} L{w * 0.6} {h * 0.25} Z" fill="#16a34a"/>')
    return svg(w, h, body, "#e8f3e0")


def grounded(w, h):
    body = [f'<rect y="{h * 0.72}" width="{w}" height="{h * 0.28}" fill="#9ca3af"/>',
            f'<rect y="{h * 0.83}" width="{w}" height="3" fill="#f9fafb" opacity=".8"/>']
    for k, (px, sc) in enumerate(((w * 0.04, 1.0), (w * 0.3, 0.75))):
        u = h * 0.18 * sc
        base = h * 0.72
        body.append(
            f'<g transform="translate({px},{base - u * 1.6})">'
            f'<rect x="0" y="{u * 0.6}" width="{u * 5.2}" height="{u * 0.8}" rx="{u * 0.4}" fill="#f3f4f6" stroke="#6b7280"/>'
            f'<path d="M{u * 0.2} {u * 0.6} L{u * 0.5} {-u * 0.3} L{u * 1.1} {-u * 0.3} L{u * 1.2} {u * 0.6} Z" fill="#c62828"/>'
            f'<path d="M{u * 2} {u * 1.0} L{u * 3.4} {u * 1.0} L{u * 2.3} {u * 1.9} L{u * 1.6} {u * 1.9} Z" fill="#9ca3af"/>'
            f'<circle cx="{u * 1.4}" cy="{u * 1.6}" r="{u * 0.18}" fill="{INK}"/>'
            f'<circle cx="{u * 4.2}" cy="{u * 1.6}" r="{u * 0.18}" fill="{INK}"/></g>')
    # strike placard
    body.append(f'<rect x="{w * 0.08}" y="{h * 0.08}" width="{w * 0.26}" height="{h * 0.2}" fill="{RED}"/>'
                f'<text x="{w * 0.21}" y="{h * 0.225}" font-family="Bahnschrift,Arial" font-weight="700" '
                f'font-size="{h * 0.13}" text-anchor="middle" fill="#fff">STRIKE</text>')
    return svg(w, h, "".join(body), "#cfe0ef")


def swift(w, h):
    cx, cy, r = h * 0.55, h * 0.5, h * 0.33
    stars = "".join(
        f'<circle cx="{cx + r * __import__("math").cos(i * 0.5236):.1f}" '
        f'cy="{cy + r * __import__("math").sin(i * 0.5236):.1f}" r="{h * 0.045}" fill="{YELLOW}"/>'
        for i in range(12))
    bank = (f'<g transform="translate({h * 1.15},{h * 0.2})">'
            f'<path d="M0 {h * 0.18} L{h * 0.42} 0 L{h * 0.84} {h * 0.18} Z" fill="#475569"/>'
            + "".join(f'<rect x="{h * (0.08 + i * 0.2)}" y="{h * 0.2}" width="{h * 0.09}" height="{h * 0.34}" fill="#64748b"/>'
                      for i in range(4))
            + f'<rect x="0" y="{h * 0.54}" width="{h * 0.84}" height="{h * 0.07}" fill="#475569"/>'
            f'<path d="M-4 {h * 0.62} L{h * 0.9} -2" stroke="{RED}" stroke-width="5"/></g>')
    return svg(w, h, f'<rect width="{h * 1.1}" height="{h}" fill="#1e3a8a"/>' + stars + bank, "#e5e7eb")


def mic(w, h):
    body = (f'<rect x="{h * 0.5}" y="{h * 0.15}" width="{h * 0.26}" height="{h * 0.4}" rx="{h * 0.13}" fill="#374151"/>'
            f'<path d="M{h * 0.42} {h * 0.38} q0 {h * 0.3} {h * 0.21} {h * 0.3} q{h * 0.21} 0 {h * 0.21} {-h * 0.3}" '
            f'fill="none" stroke="#374151" stroke-width="3"/>'
            f'<rect x="{h * 0.615}" y="{h * 0.68}" width="3" height="{h * 0.2}" fill="#374151"/>'
            f'<rect x="{h * 0.45}" y="{h * 0.86}" width="{h * 0.36}" height="3" fill="#374151"/>'
            # loose headscarf, crossed out, on the left
            f'<path d="M{h * 0.06} {h * 0.62} q{h * 0.12} {-h * 0.5} {h * 0.26} 0 Z" fill="#7c3aed" opacity=".85"/>'
            f'<path d="M{h * 0.02} {h * 0.2} L{h * 0.36} {h * 0.7}" stroke="{RED}" stroke-width="3.5"/>')
    return svg(w, h, body, "#f3e8e8")


def mast(w, h):
    body = (f'<rect y="{h * 0.8}" width="{w}" height="{h * 0.2}" fill="#d6c7a1"/>'
            f'<path d="M{h * 0.45} {h * 0.8} L{h * 0.62} {h * 0.1} L{h * 0.79} {h * 0.8}" fill="none" stroke="#374151" stroke-width="3"/>'
            f'<path d="M{h * 0.5} {h * 0.6} L{h * 0.74} {h * 0.6} M{h * 0.55} {h * 0.4} L{h * 0.7} {h * 0.4}" stroke="#374151" stroke-width="2"/>'
            f'<circle cx="{h * 0.62}" cy="{h * 0.1}" r="{h * 0.05}" fill="{RED}"/>'
            f'<circle cx="{h * 0.25}" cy="{h * 0.62}" r="{h * 0.2}" fill="{ORANGE}"/>'
            f'<circle cx="{h * 0.25}" cy="{h * 0.62}" r="{h * 0.1}" fill="{YELLOW}"/>'
            f'<circle cx="{h * 0.2}" cy="{h * 0.3}" r="{h * 0.14}" fill="#6b7280" opacity=".7"/>')
    return svg(w, h, body, "#f6e7cf")


def handshake(w, h):
    # two flags meeting: India (saffron/white/green) and Nepal (crimson pennant)
    body = (f'<rect x="{h * 0.08}" y="{h * 0.18}" width="{h * 0.6}" height="{h * 0.14}" fill="#ff9933"/>'
            f'<rect x="{h * 0.08}" y="{h * 0.32}" width="{h * 0.6}" height="{h * 0.14}" fill="#ffffff"/>'
            f'<rect x="{h * 0.08}" y="{h * 0.46}" width="{h * 0.6}" height="{h * 0.14}" fill="#138808"/>'
            f'<circle cx="{h * 0.38}" cy="{h * 0.39}" r="{h * 0.05}" fill="none" stroke="#000080" stroke-width="1.5"/>'
            f'<rect x="{h * 0.06}" y="{h * 0.16}" width="2" height="{h * 0.72}" fill="#4b5563"/>'
            f'<path d="M{h * 0.86} {h * 0.16} L{h * 1.26} {h * 0.36} L{h * 0.98} {h * 0.36} L{h * 1.26} {h * 0.62} '
            f'L{h * 0.86} {h * 0.62} Z" fill="#dc143c" stroke="#003893" stroke-width="2.5"/>'
            f'<rect x="{h * 0.84}" y="{h * 0.16}" width="2" height="{h * 0.72}" fill="#4b5563"/>')
    return svg(w, h, body, "#eef2e6")


def chartdown(w, h):
    pts = [(h * 0.08, h * 0.2), (h * 0.3, h * 0.3), (h * 0.5, h * 0.25), (h * 0.7, h * 0.55),
           (h * 0.9, h * 0.48), (h * 1.15, h * 0.82)]
    line = " ".join(f"{a:.1f},{b:.1f}" for a, b in pts)
    grid = "".join(f'<rect x="0" y="{h * k}" width="{h * 1.3}" height="1" fill="#cbd5e1"/>' for k in (0.25, 0.5, 0.75))
    body = (grid + f'<polyline points="{line}" fill="none" stroke="{RED}" stroke-width="4" stroke-linejoin="round"/>'
            f'<path d="M{h * 1.08} {h * 0.86} L{h * 1.22} {h * 0.9} L{h * 1.18} {h * 0.72} Z" fill="{RED}"/>')
    return svg(w, h, body, "#eef2f7")


def trophy(w, h):
    body = (f'<circle cx="{h * 0.55}" cy="{h * 0.3}" r="{h * 0.2}" fill="#2b6cb0"/>'
            f'<path d="M{h * 0.4} {h * 0.22} q{h * 0.15} {h * 0.06} {h * 0.3} 0 M{h * 0.38} {h * 0.36} q{h * 0.17} {h * 0.07} {h * 0.34} 0" '
            f'stroke="#9ae6b4" stroke-width="2" fill="none"/>'
            f'<path d="M{h * 0.45} {h * 0.48} L{h * 0.65} {h * 0.48} L{h * 0.6} {h * 0.72} L{h * 0.5} {h * 0.72} Z" fill="#d4a017"/>'
            f'<rect x="{h * 0.38}" y="{h * 0.72}" width="{h * 0.34}" height="{h * 0.14}" fill="#8b6b12"/>'
            f'<circle cx="{h * 1.05}" cy="{h * 0.55}" r="{h * 0.16}" fill="#fff" stroke="{INK}" stroke-width="1.5"/>'
            f'<path d="M{h * 1.0} {h * 0.47} l{h * 0.1} 0 l{h * 0.03} {h * 0.09} l{-h * 0.08} {h * 0.06} l{-h * 0.08} {-h * 0.06} Z" fill="{INK}"/>')
    return svg(w, h, body, "#e6f0e8")


def gavel(w, h):
    body = (f'<g transform="rotate(-28 {h * 0.6} {h * 0.5})">'
            f'<rect x="{h * 0.3}" y="{h * 0.3}" width="{h * 0.6}" height="{h * 0.26}" rx="4" fill="#7c4a1e"/>'
            f'<rect x="{h * 0.56}" y="{h * 0.56}" width="{h * 0.08}" height="{h * 0.45}" fill="#a16207"/></g>'
            f'<rect x="{h * 0.15}" y="{h * 0.82}" width="{h * 0.6}" height="{h * 0.1}" fill="#7c4a1e"/>'
            # Myanmar flag stripes, small
            f'<rect x="{h * 1.0}" y="{h * 0.2}" width="{h * 0.5}" height="{h * 0.12}" fill="#fecb00"/>'
            f'<rect x="{h * 1.0}" y="{h * 0.32}" width="{h * 0.5}" height="{h * 0.12}" fill="#34b233"/>'
            f'<rect x="{h * 1.0}" y="{h * 0.44}" width="{h * 0.5}" height="{h * 0.12}" fill="#ea2839"/>')
    return svg(w, h, body, "#f1ede4")


def amnesty(w, h):
    stripes = "".join(f'<rect x="{h * 0.08}" y="{h * (0.14 + i * 0.16)}" width="{h * 0.9}" height="{h * 0.08}" fill="#da121a"/>'
                      for i in range(4))
    body = (f'<rect x="{h * 0.08}" y="{h * 0.1}" width="{h * 0.9}" height="{h * 0.7}" fill="#fcdd09"/>' + stripes +
            f'<path d="M{h * 0.7} {h * 0.62} l{h * 0.12} {h * 0.12} l{h * 0.26} {-h * 0.3}" fill="none" stroke="{GREEN}" stroke-width="6"/>')
    return svg(w, h, body, "#f3efe2")


def drone(w, h):
    body = (f'<rect x="{h * 0.1}" y="{h * 0.55}" width="{h * 0.9}" height="{h * 0.4}" fill="#64748b"/>'
            f'<rect x="{h * 0.35}" y="{h * 0.45}" width="{h * 0.4}" height="{h * 0.1}" fill="#1e3a8a"/>'
            f'<text x="{h * 0.55}" y="{h * 0.53}" font-family="Bahnschrift,Arial" font-weight="700" font-size="{h * 0.09}" '
            f'text-anchor="middle" fill="#fff">POLICE</text>'
            f'<rect x="{h * 0.22}" y="{h * 0.68}" width="{h * 0.14}" height="{h * 0.14}" fill="#cbd5e1"/>'
            f'<rect x="{h * 0.72}" y="{h * 0.68}" width="{h * 0.14}" height="{h * 0.14}" fill="#cbd5e1"/>'
            f'<circle cx="{h * 0.85}" cy="{h * 0.5}" r="{h * 0.12}" fill="{ORANGE}"/>'
            f'<g transform="translate({h * 1.05},{h * 0.12})"><rect x="0" y="{h * 0.05}" width="{h * 0.3}" height="{h * 0.06}" fill="{INK}"/>'
            f'<rect x="{h * 0.1}" y="{h * 0.08}" width="{h * 0.1}" height="{h * 0.08}" fill="{INK}"/>'
            f'<rect x="{-h * 0.04}" y="0" width="{h * 0.12}" height="{h * 0.03}" fill="{INK}"/>'
            f'<rect x="{h * 0.22}" y="0" width="{h * 0.12}" height="{h * 0.03}" fill="{INK}"/></g>'
            f'<path d="M{h * 1.1} {h * 0.3} L{h * 0.9} {h * 0.45}" stroke="{INK}" stroke-dasharray="3 3" stroke-width="1.5"/>')
    return svg(w, h, body, "#e5e7eb")


def cricket(w, h):
    body = (f'<rect y="{h * 0.55}" width="{w}" height="{h * 0.45}" fill="#7cb342"/>'
            f'<rect x="{h * 0.3}" y="{h * 0.55}" width="{h * 0.5}" height="{h * 0.45}" fill="#d7ccc8"/>'
            f'<rect x="{h * 0.5}" y="{h * 0.3}" width="3" height="{h * 0.3}" fill="#f5f5f5"/>'
            f'<rect x="{h * 0.56}" y="{h * 0.3}" width="3" height="{h * 0.3}" fill="#f5f5f5"/>'
            f'<rect x="{h * 0.62}" y="{h * 0.3}" width="3" height="{h * 0.3}" fill="#f5f5f5"/>'
            f'<g transform="rotate(35 {h * 0.25} {h * 0.4})"><rect x="{h * 0.2}" y="{h * 0.1}" width="{h * 0.1}" height="{h * 0.5}" rx="3" fill="#c49a6c"/></g>'
            f'<circle cx="{h * 0.95}" cy="{h * 0.35}" r="{h * 0.06}" fill="{RED}"/>')
    return svg(w, h, body, "#cfe8f7")


DRAW = dict(warship=warship, chip=chip, grounded=grounded, swift=swift, mic=mic, mast=mast,
            handshake=handshake, chartdown=chartdown, trophy=trophy, gavel=gavel, amnesty=amnesty,
            drone=drone, cricket=cricket)
