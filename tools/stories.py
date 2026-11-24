"""Every story on the page, as reported on Monday 23 November 2026 (UTC). docs/sources.md has the links.

tag: CONFIRMED = two or more outlets; OFFICIAL = on the record from the body named; REPORTED = one outlet;
CLAIM = one side's word, not independently confirmed.
"""

DATE = "Monday 23 November 2026"

REGIONS = {  # key: (label, colour)
    "eu": ("Europe", "#2457a3"),
    "me": ("Middle East", "#b42318"),
    "af": ("Africa", "#b45309"),
    "sa": ("South Asia", "#15803d"),
    "ea": ("East & SE Asia", "#0e7490"),
    "ca": ("Central Asia", "#7a4b12"),
    "na": ("North America", "#6d28d9"),
    "la": ("Latin America", "#be185d"),
    "oc": ("Oceania", "#0369a1"),
    "gl": ("World", "#374151"),
}

# Three leads, drawn large. pic names a drawing in tools/pictures.py.
LEADS = [
    dict(n=1, region="af", place="BENGHAZI, LIBYA", field="WAR AT SEA", tag="OFFICIAL",
         lon=20.07, lat=32.12, pic="warship", big="7 SEA DRONES", small="CORVETTE MERKURY SUNK",
         head="Ukraine says its drones sank a Russian warship",
         dek="Zelensky: 7 drones hit the corvette Merkury and the ship Angara. "
             "Moscow vows “painful consequences”.",
         src="Al Jazeera · BBC · The Guardian"),
    dict(n=2, region="sa", place="NEW DELHI, INDIA", field="DIPLOMACY", tag="OFFICIAL",
         lon=77.2, lat=28.6, pic="handshake", big="$1.62bn", small="FOR NEPAL'S REBUILD",
         head="India pledges $1.62bn to help Nepal rebuild",
         dek="Modi hosts Nepal's new PM Balendra Shah on his first trip abroad; "
             "aid follows August's glacier floods.",
         src="BBC · Al Jazeera · Reuters"),
    dict(n=3, region="eu", place="BRUSSELS, BELGIUM", field="LABOUR", tag="CONFIRMED",
         lon=4.35, lat=50.85, pic="grounded", big="0 FLIGHTS", small="07:00–21:00 LOCAL",
         head="Austerity strike grounds every flight in Belgium",
         dek="Air traffic halted at Brussels and Charleroi; the Brussels metro stops as "
             "marchers fill the capital.",
         src="BBC · Al Jazeera · AFP"),
]

# Ten drawn cards.
CARDS = [
    dict(n=4, region="eu", place="BRUSSELS · EU", field="SANCTIONS", tag="OFFICIAL",
         lon=4.35, lat=50.85, pic="swift", big="22nd", small="60 BANKS OFF SWIFT",
         head="EU proposes 22nd round of Russia sanctions",
         dek="Also bans Russian sports teams",
         src="AP · Al Jazeera"),
    dict(n=5, region="me", place="QOM, IRAN", field="RIGHTS", tag="CONFIRMED",
         lon=50.88, lat=34.64, pic="mic", big="74 LASHES", small="CARRIED OUT MONDAY",
         head="Iran carries out flogging of singer Ahmadi",
         dek="Sentence for her 2024 unveiled concert",
         src="BBC · AFP"),
    dict(n=6, region="me", place="HODEIDAH, YEMEN", field="WAR", tag="REPORTED",
         lon=42.95, lat=14.8, pic="mast", big="8 KILLED", small="17 HURT · SANAA OFFICIALS",
         head="Air raids hit a telecoms site in Hodeidah",
         dek="Houthi media later said 10 dead",
         src="Al Jazeera"),
    dict(n=8, region="ea", place="SEOUL, S. KOREA", field="MARKETS", tag="CONFIRMED",
         lon=126.98, lat=37.57, pic="chartdown", big="−3.3%", small="KOSPI · −5.8% AT WORST",
         head="Seoul stocks slide 3.3% on AI fears",
         dek="Samsung −3.1%, SK Hynix −2.5%",
         src="Al Jazeera · Reuters"),
    dict(n=10, region="ea", place="MYANMAR · UK", field="RIGHTS", tag="OFFICIAL",
         lon=96.1, lat=19.75, pic="gavel", big="5 GENERALS", small="SANCTIONED BY UK",
         head="UK sanctions Myanmar's top brass over Rohingya",
         dek="London recognises the genocide",
         src="BBC · UK Foreign Office"),
    dict(n=12, region="la", place="CÚCUTA, COLOMBIA", field="CONFLICT", tag="REPORTED",
         lon=-72.5, lat=7.89, pic="drone", big="3 HURT", small="INCLUDING A BABY",
         head="Drone strikes a police base in Cúcuta",
         dek="An 18-month-old among the hurt",
         src="AP · Al Jazeera"),
    dict(n=13, region="oc", place="WELLINGTON, NZ", field="CRICKET", tag="CONFIRMED",
         lon=174.78, lat=-41.29, pic="cricket", big="239/5", small="MATCH DRAWN",
         head="New Zealand bat out a draw with India",
         dek="Mitchell 49 not out on day five",
         src="Reuters", brief=("Wellington", "NZ bat out a draw with India, 239/5")),
    dict(n=11, region="eu", place="MADRID, SPAIN", field="LAW", tag="CONFIRMED",
         lon=-3.7, lat=40.42, pic="amnesty", big="AMNESTY", small="CARLES PUIGDEMONT",
         head="Spain's top court clears Puigdemont",
         dek="Ends the 2017 independence cases",
         src="CNN · AFP", brief=("Spain", "top court grants Puigdemont amnesty")),
]

# Short items: (n, region, place, text, tag, source)
BRIEFS = [
    (14, "eu", "Russia", "drones hit 2 oil refineries", "REPORTED", "Kyiv Independent"),
    (15, "eu", "Kyiv region", "Dymer death toll rises to 11", "OFFICIAL", "regional gov."),
    (16, "eu", "Estonia", "Moscow warns of “open war”", "CLAIM", "Russian MFA"),
    (18, "eu", "Germany", "bomb threats at 450 schools", "OFFICIAL", "police"),
    (20, "eu", "UK", "Capita shares crash 70%", "CONFIRMED", "Guardian"),
    (21, "eu", "UK", "PM Burnham sells EU deal to MPs", "OFFICIAL", "BBC"),
    (22, "eu", "Europe", "gas price jumps 4% on cold snap", "CONFIRMED", "Guardian"),
    (19, "eu", "Denmark", "court backs “ghetto law” evictions", "CONFIRMED", "Reuters"),
    (23, "eu", "Rome", "hunger-striking student dies", "REPORTED", "Fanpage"),
    (24, "me", "Türkiye", "PKK quits 14 more Iraq bases", "OFFICIAL", "AFP"),
    (25, "me", "Istanbul", "police hunt a loose lioness", "CONFIRMED", "AFP · AP"),
    (26, "me", "Iran", "vows to fight US blockade", "OFFICIAL", "AJ"),
    (27, "me", "Iran", "new US sanctions on banks", "OFFICIAL", "US Treasury"),
    (28, "me", "Gaza", "strike kills UN aid worker", "CONFIRMED", "UNRWA"),
    (29, "me", "Gaza", "Oxfam: 99% of strip polluted", "REPORTED", "Oxfam"),
    (30, "af", "Libya", "UN seeks Benghazi inquiry", "OFFICIAL", "Guardian"),
    (31, "af", "Nigeria", "bill to decriminalise suicide bid", "REPORTED", "BBC"),
    (32, "ea", "Indonesia", "factory fire: 24 body bags", "CONFIRMED", "Reuters"),
    (33, "sa", "Bangladesh", "garment pay offer rejected", "CONFIRMED", "AJ"),
    (34, "sa", "Pakistan", "truck crash in Punjab kills 7", "REPORTED", "Xinhua"),
    (35, "ca", "Tajikistan", "moves to quit the ICC", "CONFIRMED", "Reuters"),
    (36, "oc", "Vanuatu", "M6.5 quake at sea", "OFFICIAL", "USGS"),
    (37, "oc", "Australia", "Jetstar refund class action", "REPORTED", "Guardian"),
    (38, "na", "US", "2 states sue SpaceX over Grok", "CONFIRMED", "AP"),
    (39, "na", "Iowa", "Army blast paused for court", "OFFICIAL", "AJ"),
    (40, "na", "US", "Rep. Jimmy Gomez to resign", "CONFIRMED", "BBC"),
    (42, "na", "Quebec", "MNAs must swear oath to King", "REPORTED", "AFP"),
    (43, "na", "New York", "e-bike fares capped at $3.65", "OFFICIAL", "Guardian"),
    (44, "gl", "COP31", "calls to end consensus rule", "REPORTED", "Guardian"),
]

# The day in UTC, for the strip under the date.
TIMELINE = [
    ("02:40", "Vanuatu M6.5"),
    ("06:00", "Belgian skies shut"),
    ("06:30", "Kospi −3.3%"),
    ("~07:30", "Libya strike claim"),
    ("~13:40", "Nepal aid pledge"),
    ("~21:00", "Myanmar sanctions"),
]

# Left out on purpose: first reported on another day.
LEFT_OUT = [
    ("Sunday 22 November", "COP31's collapse, the Dymer strike itself, Alcaraz's ATP title, Márquez's 8th crown"),
    ("Friday 20 November", "the capture of “Chapo Isidro”"),
]
