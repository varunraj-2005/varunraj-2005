"""
Generates periodic-table-style SVG 'element' cards for the tech stack section
of the README, in the black/toxic-green 'laboratory dossier' palette.
Run once locally: python3 scripts/make_elements.py
Output: assets/elements/*.svg
"""
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "elements")
os.makedirs(OUT, exist_ok=True)

BG = "#0b0d0a"
BORDER = "#39ff14"
BORDER_DIM = "#1f7a0c"
SYMBOL_COLOR = "#39ff14"
NUM_COLOR = "#ffc400"
NAME_COLOR = "#e8ffe0"
MASS_COLOR = "#5fae3f"

# (atomic_number, symbol, full_name, "mass" reused as proficiency tag)
ELEMENTS = [
    (1,  "Jv", "Java",        "OOP"),
    (2,  "Py", "Python",      "AI/ML"),
    (3,  "Js", "JavaScript",  "Web"),
    (4,  "C",  "C",           "Core"),
    (5,  "Nd", "Node.js",     "Backend"),
    (6,  "Mn", "MERN",        "Stack"),
    (7,  "Ma", "MEAN",        "Stack"),
    (8,  "Sq", "SQL",         "MySQL"),
    (9,  "Mo", "MongoDB",     "NoSQL"),
    (10, "Gt", "Git/GitHub",  "VCS"),
]

CARD_W, CARD_H = 140, 160

TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <defs>
    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="2.2" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <rect x="2" y="2" width="{wi}" height="{hi}" rx="10" fill="{bg}" stroke="{border}" stroke-width="2"/>
  <rect x="6" y="6" width="{wi6}" height="{hi6}" rx="7" fill="none" stroke="{border_dim}" stroke-width="1"/>
  <text x="14" y="26" font-family="'Courier New', monospace" font-size="14" font-weight="bold" fill="{num_color}">{num:02d}</text>
  <text x="{cx}" y="82" font-family="'Courier New', monospace" font-size="40" font-weight="bold" fill="{symbol_color}" text-anchor="middle" filter="url(#glow)">{symbol}</text>
  <text x="{cx}" y="112" font-family="'Courier New', monospace" font-size="13" fill="{name_color}" text-anchor="middle">{name}</text>
  <text x="{cx}" y="132" font-family="'Courier New', monospace" font-size="11" fill="{mass_color}" text-anchor="middle">{tag}</text>
</svg>
"""

for num, symbol, name, tag in ELEMENTS:
    svg = TEMPLATE.format(
        w=CARD_W, h=CARD_H, wi=CARD_W - 4, hi=CARD_H - 4,
        wi6=CARD_W - 12, hi6=CARD_H - 12,
        bg=BG, border=BORDER, border_dim=BORDER_DIM,
        num=num, num_color=NUM_COLOR,
        cx=CARD_W // 2, symbol=symbol, symbol_color=SYMBOL_COLOR,
        name=name, name_color=NAME_COLOR,
        tag=tag, mass_color=MASS_COLOR,
    )
    fname = name.lower().replace("/", "-").replace(".", "").replace(" ", "-") + ".svg"
    with open(os.path.join(OUT, fname), "w") as f:
        f.write(svg)
    print("wrote", fname)
