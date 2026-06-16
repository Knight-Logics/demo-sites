#!/usr/bin/env python3
"""Generate service area hub and location landing pages from data/service-areas.json."""

from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "service-areas.json"
HUB = ROOT / "about-us" / "locations-we-serve"
BASE = HUB

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,300;0,400;0,500;0,700;0,900;1,400;1,700&family=Roboto+Slab:wght@400;600;700;800;900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" />
  <script>
(function () {{
  var path = location.pathname;
  var marker = '/roof-monsters/';
  var idx = path.indexOf(marker);
  window.__RM_BASE__ = idx >= 0 ? path.slice(0, idx + marker.length) : '/';
  document.write('<base href="' + window.__RM_BASE__ + '">');
}})();
  </script>
  <link rel="stylesheet" href="assets/css/style.css" />
</head>
<body>
  <div id="site-header-include"></div>
"""

FOOT = """
  <div id="site-footer-include"></div>
  <script src="includes.js"></script>
  <script src="assets/js/main.js"></script>
</body>
</html>
"""


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def area_url(slug: str) -> str:
    return f"about-us/locations-we-serve/{slug}/"


def cta_block(short: str) -> str:
    return f"""
  <section class="service-cta-section">
    <div class="container service-cta-grid">
      <div class="service-cta-content">
        <p class="section-eyebrow">Get Started</p>
        <h2>Schedule Your Free Roofing Consultation in <span class="accent">{esc(short)}</span></h2>
        <p>Contact Roof Monsters today for a free estimate. We'll inspect your roof, explain your options clearly, and help you protect your property with confidence.</p>
        <div class="cta-features">
          <div class="cta-feature"><i class="fa-solid fa-check-circle"></i> Free roof inspections</div>
          <div class="cta-feature"><i class="fa-solid fa-check-circle"></i> 15-year workmanship warranty</div>
          <div class="cta-feature"><i class="fa-solid fa-check-circle"></i> Storm damage specialists</div>
        </div>
        <a href="tel:7274393869" class="btn btn-primary u-mt-20"><i class="fa-solid fa-phone"></i> Call (727) 439-3869</a>
      </div>
      <div class="cta-form-card">
        <h3>Request a Free Estimate</h3>
        <form class="estimate-form">
          <div class="form-row">
            <div class="form-group">
              <label>Name</label>
              <input type="text" name="name" placeholder="Your name" required />
            </div>
            <div class="form-group">
              <label>Email</label>
              <input type="email" name="email" placeholder="you@email.com" required />
            </div>
          </div>
          <div class="form-group">
            <label>Phone</label>
            <input type="tel" name="phone" placeholder="(727) 000-0000" />
          </div>
          <div class="form-group">
            <label>Property Address</label>
            <input type="text" name="address" placeholder="{esc(short)} address" />
          </div>
          <div class="form-group">
            <label>Message</label>
            <textarea name="message" rows="3" placeholder="Tell us about your roofing needs"></textarea>
          </div>
          <button type="submit" class="btn-submit">Send Request</button>
        </form>
      </div>
    </div>
  </section>
"""


def services_block(short: str) -> str:
    return f"""
        <h3>Roofing Services We Provide</h3>
        <div class="benefits-list">
          <div class="benefit-item"><i class="fa-solid fa-check-circle"></i><p><strong>Roof Installation &amp; Replacement</strong> — New construction and re-roof projects using premium shingles and proven installation methods.</p></div>
          <div class="benefit-item"><i class="fa-solid fa-check-circle"></i><p><strong>Repairs &amp; Maintenance</strong> — Fast leak diagnosis, flashing repairs, and preventative maintenance to extend roof life.</p></div>
          <div class="benefit-item"><i class="fa-solid fa-check-circle"></i><p><strong>Storm &amp; Emergency Response</strong> — Tarping, insurance documentation support, and permanent repairs after severe weather.</p></div>
          <div class="benefit-item"><i class="fa-solid fa-check-circle"></i><p><strong>Free Inspections</strong> — No-pressure assessments with honest recommendations for {esc(short)} property owners.</p></div>
        </div>
"""


def why_block(short: str, name: str) -> str:
    return f"""
  <section class="why-choose-section section-pad">
    <div class="container">
      <div class="section-header">
        <span class="section-eyebrow">Why Roof Monsters</span>
        <h2>Why {esc(short)} Property Owners <span class="accent">Choose Us</span></h2>
        <p class="section-desc">Local expertise, premium materials, and a customer-first process from the first call through final walkthrough.</p>
      </div>
      <div class="why-choose-grid">
        <div class="why-card">
          <div class="why-num"><i class="fa-solid fa-map-location-dot"></i></div>
          <h4>Local Knowledge</h4>
          <p>We understand regional building codes, HOA requirements, and the roofing systems that perform best in {esc(name)}.</p>
        </div>
        <div class="why-card">
          <div class="why-num"><i class="fa-solid fa-shield-halved"></i></div>
          <h4>Licensed &amp; Insured</h4>
          <p>Florida-licensed roofing and building contractor. Roofing licenses CCC1335398, CCC052490. Building license CBC015719. Fully insured on every project.</p>
        </div>
        <div class="why-card">
          <div class="why-num"><i class="fa-solid fa-house-chimney"></i></div>
          <h4>Family Owned Since 1988</h4>
          <p>Florida natives serving Florida — honest communication and craftsmanship you can count on year after year.</p>
        </div>
      </div>
    </div>
  </section>
"""


def featured_cities_html(area: dict) -> str:
    items = []
    for city in area.get("featuredCities", []):
        name = city["name"]
        slug = city.get("slug")
        note = city.get("note", "")
        badge = f' <span class="area-city-badge">{esc(note)}</span>' if note else ""
        if slug:
            items.append(
                f'<a class="area-city-link" href="{area_url(slug)}">{esc(name)}{badge}</a>'
            )
        else:
            items.append(f'<span class="area-city-link area-city-link--text">{esc(name)}</span>')
    grid = "\n        ".join(items)
    extra = area.get("additionalCommunities", [])
    extra_html = ""
    if extra:
        joined = ", ".join(esc(c) for c in extra)
        extra_html = f"""
      <p class="area-more-communities"><strong>Also serving communities such as:</strong> {joined} — and elsewhere in {esc(area["shortName"])}.</p>"""
    return f"""
  <section class="area-coverage-section section-pad section-bg-white">
    <div class="container">
      <div class="section-header">
        <span class="section-eyebrow">Service Coverage</span>
        <h2>Full <span class="accent">{esc(area["shortName"])}</span> Coverage</h2>
      </div>
      <p class="area-coverage-note">{esc(area.get("coverageStatement", ""))}</p>
      <div class="area-city-grid">
        {grid}
      </div>{extra_html}
    </div>
  </section>
"""


def city_page(area: dict, config: dict) -> str:
    name = area["name"]
    short = area["shortName"]
    hq = config["headquarters"]
    title = f"Roofing Company in {name} | Roof Monsters"
    description = (
        f"Roof Monsters provides roof repair, replacement, inspections, and storm damage "
        f"services in {name}. Dunedin-based, family owned Tampa Bay roofing since 1988."
    )

    hq_note = ""
    if area.get("isHeadquarters"):
        hq_note = f"""
        <p class="area-local-note area-local-note--hq"><strong>Company headquarters:</strong> Roof Monsters is based in {esc(hq["city"])}, {esc(hq["state"])} — serving {esc(area["county"])} and the greater Tampa Bay area since 1988.</p>"""
    elif area.get("countySlug"):
        county_link = area_url(area["countySlug"])
        hq_note = f"""
        <p class="area-local-note">Based in <strong>{esc(hq["city"])}</strong>, we regularly serve {esc(short)} and neighboring communities. This city page highlights a common service zone within our full <a href="{county_link}">{esc(area["county"])}</a> coverage.</p>"""

    nearby = area.get("nearbyCities", [])
    nearby_html = ""
    if nearby:
        joined = ", ".join(esc(c) for c in nearby)
        nearby_html = f'<p class="area-nearby"><strong>Nearby communities we also serve:</strong> {joined}.</p>'

    local_detail = area.get("localDetail", "")
    local_para = f"<p>{esc(local_detail)}</p>" if local_detail else ""

    return HEAD.format(title=esc(title), description=esc(description)) + f"""
  <section class="page-hero">
    <div class="container">
      <h1>Roofing in <span class="accent">{esc(short)}</span></h1>
      <nav class="breadcrumb" aria-label="breadcrumb">
        <a href="/">Home</a>
        <i class="fa-solid fa-chevron-right"></i>
        <a href="/about-us/locations-we-serve/">Service Areas</a>
        <i class="fa-solid fa-chevron-right"></i>
        <span>{esc(name)}</span>
      </nav>
    </div>
  </section>

  <section class="service-intro-section section-pad">
    <div class="container service-intro-grid">
      <div class="service-intro-content">
        <span class="section-eyebrow">{"Headquarters City" if area.get("isHeadquarters") else "Local Roofing Experts"}</span>
        <h2>Trusted Roofing Services in {esc(name)}</h2>
        <p>{esc(area["blurb"])} Roof Monsters brings nearly four decades of Florida roofing experience to every project, with clear estimates, quality materials, and crews who know how Gulf Coast weather affects your roof.</p>
        {local_para}
        {hq_note}
        {nearby_html}
        {services_block(short)}
      </div>
      <div class="service-intro-img">
        <img src="/assets/images/gallery/completed-03.webp" alt="Completed roofing project in {esc(short)}" />
      </div>
    </div>
  </section>
""" + why_block(short, name) + cta_block(short) + FOOT


def county_page(area: dict, config: dict) -> str:
    name = area["name"]
    short = area["shortName"]
    hq = config["headquarters"]
    title = f"Roofing Company in {name} | Roof Monsters"
    description = (
        f"Roof Monsters serves all of {name} with roof repair, replacement, inspections, and storm damage services. "
        f"Headquartered in {hq['city']}, FL. Family owned since 1988."
    )

    return HEAD.format(title=esc(title), description=esc(description)) + f"""
  <section class="page-hero">
    <div class="container">
      <h1>Roofing in <span class="accent">{esc(short)}</span></h1>
      <nav class="breadcrumb" aria-label="breadcrumb">
        <a href="/">Home</a>
        <i class="fa-solid fa-chevron-right"></i>
        <a href="/about-us/locations-we-serve/">Service Areas</a>
        <i class="fa-solid fa-chevron-right"></i>
        <span>{esc(name)}</span>
      </nav>
    </div>
  </section>

  <section class="service-intro-section section-pad">
    <div class="container service-intro-grid">
      <div class="service-intro-content">
        <span class="section-eyebrow">County-Wide Service</span>
        <h2>Trusted Roofing Throughout {esc(name)}</h2>
        <p>{esc(area["blurb"])} Our Dunedin headquarters puts Pinellas and the wider Tampa Bay region within practical reach for inspections, repairs, and full replacements.</p>
        <p class="area-coverage-note area-coverage-note--inline">{esc(area.get("coverageStatement", ""))}</p>
        {services_block(short)}
      </div>
      <div class="service-intro-img">
        <img src="/assets/images/gallery/completed-03.webp" alt="Completed roofing project in {esc(short)}" />
      </div>
    </div>
  </section>
""" + featured_cities_html(area) + why_block(short, name) + cta_block(short) + FOOT


def hub_page(config: dict, cities: list[dict], counties: list[dict]) -> str:
    hq = config["headquarters"]
    counties_label = ", ".join(config["serviceCounties"])

    city_cards = []
    for area in cities:
        badge = ' <span class="area-card-badge">HQ</span>' if area.get("isHeadquarters") else ""
        city_cards.append(f"""
        <div class="service-page-card">
          <div class="spc-icon"><i class="fa-solid fa-location-dot"></i></div>
          <h3>{esc(area["name"].replace(", FL", ", Florida"))}{badge}</h3>
          <p>{esc(area["blurb"])}</p>
          <a href="{area_url(area["slug"])}" class="service-link">View {esc(area["shortName"])} <i class="fa-solid fa-arrow-right"></i></a>
        </div>""")

    county_cards = []
    for area in counties:
        featured = ", ".join(c["name"] for c in area.get("featuredCities", [])[:4])
        county_cards.append(f"""
        <div class="service-page-card">
          <div class="spc-icon"><i class="fa-solid fa-map"></i></div>
          <h3>{esc(area["name"].replace(", FL", ", Florida"))}</h3>
          <p><strong>Full county coverage.</strong> {esc(area["blurb"])} Featured communities include {esc(featured)}.</p>
          <a href="{area_url(area["slug"])}" class="service-link">View {esc(area["shortName"])} <i class="fa-solid fa-arrow-right"></i></a>
        </div>""")

    return HEAD.format(
        title="Locations We Serve | Roof Monsters — Tampa Bay Roofing",
        description=(
            f"Roof Monsters is headquartered in {hq['city']}, FL and serves all of Pasco, Pinellas, "
            "Hernando, Hillsborough, and Manatee County with expert roofing services."
        ),
    ) + f"""
  <section class="page-hero">
    <div class="container">
      <h1>Locations We <span class="accent">Serve</span></h1>
      <nav class="breadcrumb" aria-label="breadcrumb">
        <a href="/">Home</a>
        <i class="fa-solid fa-chevron-right"></i>
        <a href="/about-us/">About Us</a>
        <i class="fa-solid fa-chevron-right"></i>
        <span>Locations We Serve</span>
      </nav>
    </div>
  </section>

  <section class="service-intro-section section-pad">
    <div class="container service-intro-grid">
      <div class="service-intro-content">
        <span class="section-eyebrow">Dunedin Headquarters · Tampa Bay</span>
        <h2>Serving All of Tampa Bay — From Our Home Base in Dunedin</h2>
        <p>Roof Monsters is headquartered in <strong>{esc(hq["city"])}, Florida</strong> and provides roofing across <strong>{esc(counties_label)}</strong> — the same five-county Tampa Bay territory published on roofmonsters.co.</p>
        <p>{esc(config.get("coverageDisclaimer", ""))}</p>
        <p>City pages focus on high-intent local searches in Pinellas and select neighboring markets. County pages explain whole-county service and link to featured communities within our typical project radius.</p>

        <h3>Why Choose Roof Monsters in Florida?</h3>
        <div class="benefits-list">
          <div class="benefit-item"><i class="fa-solid fa-check-circle"></i><p><strong>Dunedin-Based Operations</strong> — Fast response across Pinellas and the wider bay area from a local headquarters, not a national call center.</p></div>
          <div class="benefit-item"><i class="fa-solid fa-check-circle"></i><p><strong>County-Wide Coverage</strong> — We serve all of Pasco, Pinellas, Hernando, Hillsborough, and Manatee Counties.</p></div>
          <div class="benefit-item"><i class="fa-solid fa-check-circle"></i><p><strong>HOA &amp; Property Manager Support</strong> — Documentation, scheduling, and communication tailored for communities and managers (CAM experience on staff).</p></div>
        </div>
      </div>
      <div class="service-intro-img">
        <img src="/assets/images/gallery/completed-01.webp" alt="Roof Monsters crew serving Tampa Bay from Dunedin" />
      </div>
    </div>
  </section>

  <section class="services-page-section section-pad section-bg-white">
    <div class="container">
      <div class="section-header">
        <span class="section-eyebrow">Pinellas Cities</span>
        <h2>City Pages — <span class="accent">Pinellas &amp; Select Markets</span></h2>
        <p class="section-desc">Local landing pages for communities we serve frequently from Dunedin. Every Pinellas city is part of our full county coverage.</p>
      </div>
      <div class="services-page-grid">
        {"".join(city_cards)}
      </div>
    </div>
  </section>

  <section class="services-page-section section-pad">
    <div class="container">
      <div class="section-header">
        <span class="section-eyebrow">County Coverage</span>
        <h2>Full-County <span class="accent">Service Areas</span></h2>
        <p class="section-desc">Each county page confirms whole-county service and highlights cities within our typical Tampa Bay project radius.</p>
      </div>
      <div class="services-page-grid">
        {"".join(county_cards)}
      </div>
    </div>
  </section>

  <section class="atlas-banner bg-atlas-banner-shingles">
    <div class="atlas-overlay"></div>
    <div class="container atlas-inner">
      <div class="atlas-content">
        <p class="section-eyebrow">Contact Us Today</p>
        <h2>Ready for Expert Roofing in <span class="accent">Your Area?</span></h2>
        <p>Trust Roof Monsters for roofing solutions tailored to your location — from Dunedin to every county we serve across Tampa Bay.</p>
        <a href="/contact-us/" class="btn btn-primary u-mt-20">Get A Free Estimate</a>
      </div>
      <div class="atlas-stat">
        <div class="atlas-num">10,000 +</div>
        <div class="atlas-label">Happy Clients All Over The Bay Area!</div>
      </div>
    </div>
  </section>
""" + FOOT


def main() -> None:
    config = json.loads(DATA.read_text(encoding="utf-8"))
    areas = config["areas"]
    cities = [a for a in areas if a["type"] == "city"]
    counties = [a for a in areas if a["type"] == "county"]

    (HUB / "index.html").write_text(hub_page(config, cities, counties), encoding="utf-8")
    print(f"Wrote {HUB / 'index.html'}")

    for area in areas:
        out_dir = BASE / area["slug"]
        out_dir.mkdir(parents=True, exist_ok=True)
        if area["type"] == "city":
            content = city_page(area, config)
        else:
            content = county_page(area, config)
        (out_dir / "index.html").write_text(content, encoding="utf-8")
        print(f"Wrote {out_dir / 'index.html'}")


if __name__ == "__main__":
    main()
