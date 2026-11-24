"""Write out/front.html: the whole front page for Monday 23 November 2026 as HTML, CSS and inline SVG.

The world map's coastline comes from Natural Earth's ne_110m_land.geojson (public domain), read from the
folder named by NE_DIR; it is not committed. Run tools/render.ps1 to turn the page into entry.png.
"""
import html
import json
import math
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pictures import DRAW  # noqa: E402
from stories import BRIEFS, CARDS, DATE, LEADS, LEFT_OUT, REGIONS, TIMELINE  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "out")

TAG_CLASS = {"CONFIRMED": "t-conf", "OFFICIAL": "t-off", "REPORTED": "t-rep", "CLAIM": "t-claim"}

# layout knobs (a variant can override them through the VARIANT environment variable, as JSON)
K = dict(lead_pic=96, card_pic=62, cards=8, card_cols=4, head_lead=22.5, head_card=17.5, brief_font=12.6,
         briefs=27, brief_cols=3, brief_src=0, dek_lead=13.4, dek_card=12.8, sub_size=20,
         date_size=70, map=1, map_side="right", map_w=206, map_h=150)
K.update(json.loads(os.environ.get("VARIANT", "{}")))

# What this variant shows: the first K['cards'] cards are drawn, the rest drop into the short list;
# every story is then numbered in page order (leads, cards, list).
SEL_LEADS = [dict(s) for s in LEADS]
SEL_CARDS = [dict(s) for s in CARDS[:K["cards"]]]
SEL_BRIEFS = [(0, c["region"], c["brief"][0], c["brief"][1], c["tag"], c["src"]) for c in CARDS[K["cards"]:]]
def spread(pool, n):
    """Keep n short items, taking one region at a time so a short list still spans the world;
    the kept items stay in their original order."""
    by_region = {}
    for i, b in enumerate(pool):
        by_region.setdefault(b[1], []).append(i)
    keep, queues = set(), list(by_region.values())
    while len(keep) < min(n, len(pool)):
        for q in queues:
            if q and len(keep) < n:
                keep.add(q.pop(0))
    return [b for i, b in enumerate(pool) if i in keep]


SEL_BRIEFS = spread(SEL_BRIEFS + list(BRIEFS), K["briefs"])
for i, s in enumerate(SEL_LEADS + SEL_CARDS):
    s["n"] = i + 1


def esc(s):
    return html.escape(s, quote=False)


def tag(t):
    return f'<span class="tag {TAG_CLASS[t]}">{t}</span>'


def counts():
    c = Counter(s["region"] for s in SEL_LEADS + SEL_CARDS)
    c.update(b[1] for b in SEL_BRIEFS)
    return c


def total():
    return len(SEL_LEADS) + len(SEL_CARDS) + len(SEL_BRIEFS)


def fields():
    f = {s["field"].split(" · ")[0] for s in SEL_LEADS + SEL_CARDS}
    return len(f) + 4  # + energy, crime, tech and disaster that only appear among the briefs


# ---------- map ----------
def land_paths(w, h):
    ne = os.environ.get("NE_DIR")
    if not ne:
        sys.exit("set NE_DIR to a folder holding ne_110m_land.geojson")
    with open(os.path.join(ne, "ne_110m_land.geojson"), encoding="utf-8") as f:
        geo = json.load(f)
    proj = projector(w, h)
    out = []
    for feat in geo["features"]:
        g = feat["geometry"]
        polys = [g["coordinates"]] if g["type"] == "Polygon" else g["coordinates"]
        for poly in polys:
            ring = poly[0]
            pts, last = [], None
            for lon, lat in ring:
                if lat < -58:
                    continue
                x, y = proj(lon, lat)
                if last is None or abs(x - last[0]) + abs(y - last[1]) > 0.8:
                    pts.append(f"{x:.1f},{y:.1f}")
                    last = (x, y)
            if len(pts) > 2:
                out.append("M" + " L".join(pts) + "Z")
    return " ".join(out)


def projector(w, h):
    lon0, lon1, lat0, lat1 = -168.0, 190.0, -56.0, 76.0

    def p(lon, lat):
        if lon < lon0:
            lon += 360
        x = (lon - lon0) / (lon1 - lon0) * w
        # a light Miller-style stretch so Europe is not squashed
        def m(a):
            return 1.25 * math.log(math.tan(math.pi / 4 + 0.4 * math.radians(a)))
        y = (m(lat1) - m(lat)) / (m(lat1) - m(lat0)) * h
        return x, y

    return p


NUDGE = {3: (5, -4), 4: (-4, 6), 9: (2, 7), 11: (-6, 0), 5: (3, 3), 6: (-2, 4), 2: (0, 0)}


def world_map(w, h):
    proj = projector(w, h)
    pins = []
    for s in SEL_LEADS + SEL_CARDS:
        x, y = proj(s["lon"], s["lat"])
        dx, dy = NUDGE.get(s["n"], (0, 0))
        col = REGIONS[s["region"]][1]
        r = 7.2 if s["n"] <= 3 else 6.2
        pins.append(f'<circle cx="{x + dx:.1f}" cy="{y + dy:.1f}" r="{r}" fill="{col}" stroke="#fff" stroke-width="1.2"/>'
                    f'<text x="{x + dx:.1f}" y="{y + dy + 3.2:.1f}" font-size="{8.6 if s["n"] < 10 else 7.6}" '
                    f'text-anchor="middle" fill="#fff" font-family="Bahnschrift,Arial" font-weight="700">{s["n"]}</text>')
    return (f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg">'
            f'<rect width="{w}" height="{h}" fill="#dfe9f2"/>'
            f'<path d="{land_paths(w, h)}" fill="#e9dfc8" stroke="#b9a983" stroke-width=".5"/>'
            + "".join(pins) + "</svg>")


# ---------- blocks ----------
def lead_html(s, width):
    pic = DRAW[s["pic"]](width, K["lead_pic"])
    col = REGIONS[s["region"]][1]
    return f"""
<div class="lead">
  <div class="pic" style="height:{K['lead_pic']}px">{pic}
    <div class="over big-lead"><b>{esc(s['big'])}</b><i>{esc(s['small'])}</i></div></div>
  <div class="meta"><span class="num" style="background:{col}">{s['n']}</span>
    <span class="place" style="color:{col}">{esc(s['place'])} · {esc(s['field'])}</span>{tag(s['tag'])}</div>
  <h2>{esc(s['head'])}</h2>
  <p class="dek">{esc(s['dek'])}</p>
  {f'<p class="src">{esc(s["src"])}</p>' if K['brief_src'] else ''}
</div>"""


def card_html(s, width):
    pic = DRAW[s["pic"]](width, K["card_pic"])
    col = REGIONS[s["region"]][1]
    return f"""
<div class="card">
  <div class="pic" style="height:{K['card_pic']}px">{pic}
    <div class="over big-card"><b>{esc(s['big'])}</b><i>{esc(s['small'])}</i></div></div>
  <div class="meta"><span class="num" style="background:{col}">{s['n']}</span>
    <span class="place" style="color:{col}">{esc(s['place'])}</span>{tag(s['tag'])}</div>
  <h3>{esc(s['head'])}</h3>
  <p class="dek">{esc(s['dek'])}</p>
</div>"""


def brief_html(n, b):
    _, reg, place, text, t, src = b  # numbered in page order, after the leads and cards
    col = REGIONS[reg][1]
    mark = ' <span class="tag t-claim">CLAIM</span>' if t == "CLAIM" else ""
    source = f' <span class="bs">{esc(src)}</span>' if K["brief_src"] else ""
    return (f'<li><span class="bn" style="color:{col}">{n}</span><b style="color:{col}">{esc(place)}:</b> '
            f'{esc(text)}{mark}{source}</li>')


def page():
    c = counts()
    regions_used = [k for k in REGIONS if c[k]]
    chips = "".join(f'<span class="chip" style="background:{REGIONS[k][1]}">{REGIONS[k][0]} <b>{c[k]}</b></span>'
                    for k in regions_used)
    tl = "".join(f'<span class="ev"><b>{t}</b> {esc(e)}</span>' for t, e in TIMELINE)
    lead_w = (1024 - 2 * 16 - 2 * 12) // 3
    card_w = (1024 - 2 * 16 - (K["card_cols"] - 1) * 10) // K["card_cols"]
    leads = "".join(lead_html(s, lead_w) for s in SEL_LEADS)
    cards = "".join(card_html(s, card_w) for s in SEL_CARDS)
    first = len(SEL_LEADS) + len(SEL_CARDS) + 1
    items = [brief_html(first + i, b) for i, b in enumerate(SEL_BRIEFS)]
    per = -(-len(items) // K["brief_cols"])
    cols = "".join(f"<ul>{''.join(items[i * per:(i + 1) * per])}</ul>" for i in range(K["brief_cols"]))
    mapbox = (f'<div class="mapbox"><h4>WHERE IT HAPPENED</h4>'
              f'{world_map(K["map_w"], K["map_h"])}</div>') if K["map"] else ""
    left = " · ".join(f'<b>{d}:</b> {esc(t)}' for d, t in LEFT_OUT)
    n_regions = len([k for k in regions_used if k != "gl"])
    subtitle = "  •  ".join([
        "Ukraine says it sank a Russian warship",
        "India pledges $1.62bn to Nepal",
        "Belgium grounded by strike"])
    return f"""<!doctype html><html><head><meta charset="utf-8"><title>{DATE}</title><style>
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1024px;height:1024px;overflow:hidden;background:#f6f1e6;color:#161616;
  font-family:"Segoe UI",Arial,sans-serif}}
.top{{height:22px;background:#14213d;color:#fff;display:flex;justify-content:space-between;align-items:center;
  padding:0 14px;font:700 11.5px Bahnschrift,Arial;letter-spacing:.06em}}
.top .r b{{color:#ffd23f}}
.date{{text-align:center;font:700 {K['date_size']}px/1 Georgia,"Times New Roman",serif;letter-spacing:-.01em;
  color:#14213d;margin-top:7px;white-space:nowrap}}
.sub{{text-align:center;color:#b42318;font:700 {K['sub_size']}px "Segoe UI",Arial;margin-top:5px;white-space:nowrap}}
.band{{display:flex;gap:6px;justify-content:center;margin:8px 16px 0}}
.chip{{color:#fff;font:700 12px Bahnschrift,Arial;padding:2px 7px;border-radius:3px;white-space:nowrap}}
.chip b{{background:rgba(255,255,255,.25);padding:0 4px;border-radius:2px;margin-left:2px}}
.tl{{margin:7px 16px 0;background:#14213d;color:#fff;display:flex;align-items:center;height:28px;
  font:600 13.2px "Segoe UI",Arial;border-radius:3px;overflow:hidden}}
.tl .lab{{background:#ffd23f;color:#14213d;font:700 12px Bahnschrift,Arial;padding:0 9px;height:100%;
  display:flex;align-items:center;letter-spacing:.05em}}
.tl .ev{{flex:1;padding-left:9px;border-left:2px solid #ffd23f;margin-left:7px;white-space:nowrap}}
.tl .ev b{{color:#ffd23f;font-family:Bahnschrift,Arial}}
.leads{{display:flex;gap:12px;margin:9px 16px 0}}
.lead{{width:{lead_w}px}}
.pic{{position:relative;overflow:hidden;border-radius:3px;border:1px solid #c9bfa8}}
.pic svg{{display:block;width:100%;height:100%}}
.over{{position:absolute;right:8px;bottom:6px;text-align:right;display:flex;flex-direction:column;align-items:flex-end}}
.over b{{font:700 {K['lead_pic'] * 0.3:.0f}px/1 Bahnschrift,Arial;color:#fff;background:#14213d;padding:2px 7px 1px;border-radius:3px}}
.over i{{font:700 13px Bahnschrift,Arial;font-style:normal;color:#14213d;background:#ffd23f;padding:1px 6px;margin-top:3px;
  border-radius:2px;letter-spacing:.03em}}
.big-card b{{font-size:{K['card_pic'] * 0.37:.0f}px}}
.big-card i{{font-size:11.5px}}
.meta{{display:flex;align-items:center;gap:5px;margin-top:5px;white-space:nowrap}}
.num{{color:#fff;font:700 12px Bahnschrift,Arial;min-width:18px;height:18px;border-radius:50%;display:inline-flex;
  align-items:center;justify-content:center}}
.place{{font:700 13.2px Bahnschrift,Arial;letter-spacing:.02em;flex:1;overflow:hidden;text-overflow:ellipsis}}
.tag{{font:700 10.5px Bahnschrift,Arial;letter-spacing:.05em;padding:1px 4px;border-radius:2px;border:1.2px solid}}
.t-conf{{color:#166534;border-color:#166534;background:#ecfdf3}}
.t-off{{color:#1e3a8a;border-color:#1e3a8a;background:#eef4ff}}
.t-rep{{color:#4b5563;border-color:#4b5563;background:#f3f4f6}}
.t-claim{{color:#b45309;border-color:#b45309;background:#fff7e6}}
h2{{font:700 {K['head_lead']}px/1.12 Georgia,serif;margin-top:4px;color:#111}}
h3{{font:700 {K['head_card']}px/1.14 Georgia,serif;margin-top:3px;color:#111}}
.dek{{font-size:{K['dek_lead']}px;line-height:1.3;margin-top:4px;color:#2b2b2b}}
.card .dek{{font-size:{K['dek_card']}px;margin-top:2px}}
.src{{font-size:10px;color:#6b6b6b;margin-top:3px}}
.sec{{margin:9px 16px 0;border-top:2.5px solid #14213d;padding-top:3px;font:700 12px Bahnschrift,Arial;letter-spacing:.06em;
  color:#14213d}}
.sec span{{font:400 11.5px "Segoe UI",Arial;color:#555;letter-spacing:0;margin-left:6px}}
.cards{{display:grid;grid-template-columns:repeat({K['card_cols']},1fr);gap:8px 10px;margin:4px 16px 0}}
.bottom{{display:flex;gap:14px;margin:9px 16px 0;border-top:2.5px solid #14213d;padding-top:5px}}
.mapbox{{width:{K['map_w']}px;flex:none}}
.mapbox h4,.also h4{{font:700 12.5px Bahnschrift,Arial;letter-spacing:.06em;color:#14213d;margin-bottom:3px}}
.mapbox h4 span,.also h4 span{{color:#b42318}}
.mapbox svg{{display:block;border:1px solid #c9bfa8;border-radius:3px}}
.key{{font-size:10.3px;color:#333;margin-top:3px;line-height:1.35}}
.also{{flex:1}}
.also .cols{{display:flex;gap:14px}}
.also ul{{list-style:none;flex:1}}
.also li{{font-size:{K['brief_font']}px;line-height:1.3;white-space:nowrap}}
.bn{{font:700 11.5px Bahnschrift,Arial;display:inline-block;width:19px}}
.bs{{color:#8a8a8a;font-size:9.6px}}
.check{{margin:7px 16px 0;border:2px solid #b42318;border-radius:3px;display:flex;align-items:stretch;background:#fffaf3}}
.check .lab{{background:#b42318;color:#fff;font:700 12px/1.15 Bahnschrift,Arial;padding:5px 8px;display:flex;align-items:center;
  text-align:center;letter-spacing:.05em}}
.check .txt{{padding:4px 9px;font-size:12.4px;line-height:1.35}}
.check .txt b{{color:#b42318}}
.legend{{margin:4px 16px 0;display:flex;gap:10px;align-items:center;font-size:10.2px;color:#444}}
.legend .sp{{flex:1}}
</style></head><body>
<div class="top"><span>THE WORLD IN ONE DAY</span>
  <span class="r"><b>{total()} STORIES</b> · {n_regions} REGIONS · {fields()} FIELDS · EVERY ONE REPORTED ON {DATE.upper()} (UTC)</span></div>
<div class="date">{DATE}</div>
<div class="sub">{esc(subtitle)}</div>
<div class="band">{chips}</div>
<div class="tl"><span class="lab">UTC</span>{tl}</div>
<div class="leads">{leads}</div>
<div class="sec">THE DAY IN {len(SEL_CARDS)} MORE<span>Monday's other big stories, across {len({s['region'] for s in SEL_CARDS})} regions</span></div>
<div class="cards">{cards}</div>
<div class="bottom">
  {mapbox if K.get('map_side') != 'right' else ''}
  <div class="also"><h4>ALSO ON MONDAY 23 NOVEMBER <span>— {len(SEL_BRIEFS)} MORE STORIES</span></h4>
    <div class="cols">{cols}</div></div>
  {mapbox if K.get('map_side') == 'right' else ''}
</div>
<div class="check"><div class="lab">DATE<br>CHECK</div><div class="txt">Every story here happened, or was first reported, on
  <b>Monday 23 November 2026</b> (UTC). <b>Left out as other days' news:</b> {left}.</div></div>
<div class="legend">{tag("CONFIRMED")} 2+ outlets {tag("OFFICIAL")} on the record {tag("REPORTED")} one outlet
  {tag("CLAIM")} one side's word<span class="sp"></span>Times UTC · pictures and map drawn in code, not photos</div>
</body></html>"""


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "front.html"), "w", encoding="utf-8") as f:
        f.write(page())
    print(f"out/front.html: {total()} stories, regions {dict(counts())}")
