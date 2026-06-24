#!/usr/bin/env python3
"""Regenerate sitemap.xml from folder structure (index.html pages)."""
from __future__ import annotations

import argparse
import json
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "data" / "site-seo.json"
SKIP = {"partials", "scripts", "assets", "data", "GROWTH-ROADMAP-PROPOSAL.html"}


def resolve_base(value: str | None) -> str:
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    if not value or value == "production":
        return config["productionBase"].rstrip("/")
    if value == "demo":
        return config["demoBase"].rstrip("/")
    return value.rstrip("/")


def collect_urls(base: str) -> list[str]:
    urls = []
    if (ROOT / "index.html").exists():
        urls.append(f"{base}/")

    for index in sorted(ROOT.rglob("index.html")):
        if index.parent == ROOT:
            continue
        rel = index.parent.relative_to(ROOT)
        if rel.parts[0] in SKIP or any(p.startswith(".") for p in rel.parts):
            continue
        path = "/" + "/".join(rel.parts) + "/"
        urls.append(f"{base}{path}")

    return sorted(set(urls), key=lambda u: (u.count("/"), u))


def main() -> None:
    parser = argparse.ArgumentParser(description="Build sitemap.xml for Roof Monsters")
    parser.add_argument(
        "--base",
        default="production",
        help="production | demo | full URL (default: production)",
    )
    args = parser.parse_args()
    base = resolve_base(args.base)
    urls = collect_urls(base)

    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    for loc in urls:
        ET.SubElement(ET.SubElement(urlset, "url"), "loc").text = loc

    tree = ET.ElementTree(urlset)
    ET.indent(tree, space="  ")
    tree.write(ROOT / "sitemap.xml", encoding="UTF-8", xml_declaration=True)
    print(f"Wrote {len(urls)} URLs to sitemap.xml (base: {base})")


if __name__ == "__main__":
    main()
