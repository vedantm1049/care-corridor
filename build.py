"""Build the two views of Care Corridor from one source file.

    python3 build.py

Writes index.html (provider view) and insurers.html (insurer view).
The only differences are the AUD flag and the page title; everything
else, including every number, comes from src/care-corridor.html.
"""
from pathlib import Path

ROOT = Path(__file__).parent
SRC = (ROOT / "src" / "care-corridor.html").read_text(encoding="utf-8")
HEAD = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<style>[hidden]{display:none!important}img{max-width:100%}</style>')

VIEWS = {
    "index.html": ("trudoc", "Care Corridor for Providers"),
    "insurers.html": ("insurer", "Care Corridor for Insurers"),
}

for name, (aud, title) in VIEWS.items():
    page = SRC.replace('const AUD="trudoc";', f'const AUD="{aud}";')
    page = page.replace("<title>Care Corridor for Providers</title>", f"<title>{title}</title>")
    (ROOT / name).write_text(HEAD + page + "</html>", encoding="utf-8")
    print("wrote", name)
