#!/usr/bin/env python3
"""Regenerate sitemap.xml from folder structure (index.html pages)."""
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://roofmonsters.co"
SKIP = {"partials", "scripts", "assets", "GROWTH-ROADMAP-PROPOSAL.html"}

def collect_urls() -> list[str]:
    urls = []
    if (ROOT / "index.html").exists():
        urls.append(f"{BASE}/")

    for index in sorted(ROOT.rglob("index.html")):
        if index.parent == ROOT:
            continue
        rel = index.parent.relative_to(ROOT)
        if rel.parts[0] in SKIP or any(p.startswith(".") for p in rel.parts):
            continue
        path = "/" + "/".join(rel.parts) + "/"
        urls.append(f"{BASE}{path}")

    return sorted(set(urls), key=lambda u: (u.count("/"), u))

def main() -> None:
    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    for loc in collect_urls():
        ET.SubElement(ET.SubElement(urlset, "url"), "loc").text = loc

    tree = ET.ElementTree(urlset)
    ET.indent(tree, space="  ")
    tree.write(ROOT / "sitemap.xml", encoding="UTF-8", xml_declaration=True)
    print(f"Wrote {len(collect_urls())} URLs to sitemap.xml")

if __name__ == "__main__":
    main()
