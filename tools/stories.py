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
         lon=50.88, lat=34.64, pic="mic", big="74 LASHES", small="FOR SINGING UNVEILED",
         head="Iran flogs singer who performed without hijab",
         dek="Parastoo Ahmadi, 29, and 4 of her team",
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
    (14, "eu", "Russia", "Ukrainian drones hit Perm and Novoshakhtinsk refineries", "REPORTED", "Kyiv Independent"),
    (15, "eu", "Kyiv region", "Dymer toll from Sunday's strike rises to 11", "OFFICIAL", "regional gov."),
    (16, "eu", "Estonia", "Moscow says Tallinn is near “open war”", "CLAIM", "Russian MFA"),
    (18, "eu", "Germany", "emailed bomb threats hit 450 schools; Denmark too", "OFFICIAL", "police"),
    (20, "eu", "UK", "Capita shares crash 70% as its CEO quits", "CONFIRMED", "Guardian"),
    (21, "eu", "UK", "PM Burnham sells EU deal to MPs as “£17bn” boost", "OFFICIAL", "BBC"),
    (22, "eu", "Europe", "gas jumps 4% to €92.50 on cold-snap fears", "CONFIRMED", "Guardian"),
    (19, "eu", "Denmark", "Supreme Court backs “ghetto law” evictions", "CONFIRMED", "Reuters"),
    (23, "eu", "Rome", "student on hunger strike over housing dies", "REPORTED", "Fanpage"),
    (24, "me", "Türkiye", "PKK leaves 14 more bases in Iraq, MIT says", "OFFICIAL", "AFP"),
    (25, "me", "Istanbul", "police hunt a lioness in Sarıyer woods", "CONFIRMED", "AFP · AP"),
    (26, "me", "Iran", "vows “all available means” against US blockade", "OFFICIAL", "AJ"),
    (27, "me", "Iran", "US sanctions 24+ shadow-banking fronts", "OFFICIAL", "US Treasury"),
    (28, "me", "Gaza", "strike kills UNRWA worker at a well", "CONFIRMED", "UNRWA"),
    (29, "me", "Gaza", "Oxfam: war pollution reaches 99% of the strip", "REPORTED", "Oxfam"),
    (30, "af", "Libya", "UN mission seeks inquiry into Benghazi blasts", "OFFICIAL", "Guardian"),
    (31, "af", "Nigeria", "Tinubu asks to end jail for attempted suicide", "REPORTED", "BBC"),
    (32, "ea", "Indonesia", "candy-factory fire: 24 body bags recovered", "CONFIRMED", "Reuters"),
    (33, "sa", "Bangladesh", "garment workers reject owners' pay offer", "CONFIRMED", "AJ"),
    (34, "sa", "Pakistan", "truck overturns in Punjab, 7 killed", "REPORTED", "Xinhua"),
    (35, "ca", "Tajikistan", "begins quitting the ICC, 4th since US push", "CONFIRMED", "Reuters"),
    (36, "oc", "Vanuatu", "M6.5 earthquake at sea, 02:40 UTC", "OFFICIAL", "USGS"),
    (37, "oc", "Australia", "Jetstar refund class action open to 1m flyers", "REPORTED", "Guardian"),
    (38, "na", "Virginia, Oregon", "sue SpaceX over Grok's sexual images", "CONFIRMED", "AP"),
    (39, "na", "Iowa", "Trump pauses Army lead-azide blast for court", "OFFICIAL", "AJ"),
    (40, "na", "Washington", "Rep. Jimmy Gomez to resign on 1 December", "CONFIRMED", "BBC"),
    (42, "na", "Quebec", "court: MNAs must swear oath to the King", "REPORTED", "AFP"),
    (43, "na", "New York", "e-bike rides capped at $3.65 from January", "OFFICIAL", "Guardian"),
    (44, "gl", "COP31", "Gore and experts urge end to consensus rule", "REPORTED", "Guardian"),
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
