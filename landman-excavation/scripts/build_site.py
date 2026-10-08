"""Build the 15-page LandMan Excavation local demo."""
from pathlib import Path

ROOT = Path(r"E:\All Client Websites\demosites\landman-excavation")
PHONE = "(770) 714-4907"
TEL = "+17707144907"
EMAIL = "info@landmanexcavation.com"

SERVICES = [
    ("land-clearing", "Land Clearing", "Selective clearing, stumps, and forestry mulching."),
    ("brush-removal", "Brush Removal", "Briars, vines, saplings, and overgrown fence lines."),
    ("pasture-reclamation", "Pasture Reclamation", "Bring overgrown pasture back to usable ground."),
    ("grading", "Grading", "Pads, drainage, culverts, and finished grade."),
    ("driveway-repair", "Driveway Repair", "Crown, washouts, gravel, and drainage that stays put."),
    ("site-preparation", "Site Preparation", "Barn sites, arenas, access, and building pads."),
]

COUNTIES = [
    "Hall", "Forsyth", "Lumpkin", "Pickens", "White", "Habersham",
    "Stephens", "Franklin", "Banks", "Jackson", "Dawson",
]

FAQS = [
    ("Do I need a permit?",
     "<p>It depends on the scope of the project. Many routine property improvements — brush removal, stump removal, gravel driveway repair, fence line clearing, and selective land clearing — often do not require permits. Projects involving new construction, major grading, retaining walls, streams, or extensive land disturbance may require permits or approvals.</p><p>During the free estimate, LandMan talks through the project and will say if permitting may be necessary. If the work sits outside this scope, Chris will point you in the right direction.</p>"),
    ("Are you insured?",
     "<p>Yes. LandMan Excavation &amp; Grading is insured. Proof of insurance is available on request.</p>"),
    ("Can you remove trees?",
     "<p>Yes — the specialty is small to medium-sized trees, brush, saplings, and selective clearing as part of improving the property. Large, hazardous, or technical removals that need climbing or a crane are referred to a tree service, and LandMan will coordinate with them if you want that. The goal is to improve the property while keeping the trees you want to keep.</p>"),
    ("How much does land clearing cost?",
     "<p>Every property is different. Price depends on the size of the area, the amount of brush and vegetation, the number and size of trees, terrain and access, whether debris is hauled or mulched, and whether you want final grading or restoration. LandMan gives a free on-site estimate so the number matches the land.</p>"),
    ("How long will the project take?",
     "<p>Many smaller jobs — driveway repairs, stump removal, brush clearing — can be finished in a day or two. Larger clearing or grading can take several days. The estimate includes a realistic timeline before work starts.</p>"),
    ("Can you improve an existing driveway?",
     "<p>Yes. Many driveways do not need a full rebuild. The problem is often drainage, crown, washouts, and grade — water running down the driveway instead of off it. LandMan looks at the cause and recommends the most practical fix, including spreading, grading, and compacting gravel.</p>"),
    ("Do you work on horse farms?",
     "<p>Yes. Horse properties need safe, usable space. Work can include pasture reclamation, arena preparation and grading, fence line clearing, drainage, access roads, barn site preparation, and turnout expansion.</p>"),
    ("Can you clear fence lines?",
     "<p>Yes. Fence lines fill in with brush, vines, saplings, and unwanted vegetation. Clearing along an existing fence makes it easier to maintain and gives that edge of the property back.</p>"),
    ("Can you spread gravel?",
     "<p>Yes. New gravel or a refresh on a driveway, parking area, or access road can be spread, graded, and compacted. Grading and drainage matter as much as the stone itself.</p>"),
    ("Do you haul debris away?",
     "<p>Yes. Depending on the job, debris can be hauled, stacked, burned where that is permitted, or forestry-mulched. The estimate covers which option fits the property and the budget.</p>"),
    ("Can I stay on my property while work is being done?",
     "<p>In most cases, yes. LandMan will point out areas to avoid while equipment is running and will keep you informed. Safety comes first.</p>"),
]


def service_links(mobile=False):
    cls = ' class="sub"' if mobile else ""
    items = ['<a href="/services/">All services</a>']
    items += [f'<a href="/services/{slug}/">{name}</a>' for slug, name, _ in SERVICES]
    inner = "".join(items)
    if mobile:
        return f'<div class="sub">{inner}</div>'
    return f"<menu>{''.join(f'<li>{a}</li>' for a in items)}</menu>"


def chrome(active: str) -> str:
    def cur(key):
        return ' aria-current="page"' if active == key else ""

    desktop_links = f"""
      <a href="/"{cur("home")}>Home</a>
      <a href="/about/"{cur("about")}>About</a>
      <div class="nav-drop">
        <button type="button" aria-haspopup="true">Services</button>
        {service_links()}
      </div>
      <a href="/projects/"{cur("projects")}>Projects</a>
      <a href="/property-solutions/"{cur("solutions")}>Solutions</a>
      <a href="/service-area/"{cur("area")}>Service Area</a>
      <a href="/faq/"{cur("faq")}>FAQ</a>
    """
    return f"""
<a class="skip" href="#main">Skip to content</a>
<div class="demo-bar">Local demo preview. <strong>Not indexed.</strong> Photos and copy come from landmanexcavation.com. This is not the live site.</div>
<header class="site-header">
  <div class="wrap header-inner">
    <button class="hamburger" type="button" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
    <a class="brand" href="/" aria-label="LandMan Excavation and Grading home">
      <img src="/assets/images/Landman-Excavation-Grading.jpg" alt="LandMan Excavation and Grading" width="512" height="512">
    </a>
    <nav class="site-nav" aria-label="Primary">{desktop_links}</nav>
    <a class="header-call" href="tel:{TEL}"><small>Call or text</small><strong>{PHONE}</strong></a>
    <a class="btn header-quote" href="/contact/">Free estimate</a>
  </div>
</header>
<div class="scrim"></div>
<nav class="drawer" aria-label="Mobile" inert>
  <div class="drawer-head"><strong>Menu</strong><button class="drawer-close btn" type="button">Close</button></div>
  <a href="/">Home</a>
  <a href="/about/">About</a>
  <a href="/services/">Services</a>
  {service_links(mobile=True)}
  <a href="/projects/">Projects</a>
  <a href="/property-solutions/">Property solutions</a>
  <a href="/horse-properties/">Horse properties</a>
  <a href="/service-area/">Service area</a>
  <a href="/faq/">FAQ</a>
  <a href="/contact/">Contact</a>
  <a href="tel:{TEL}">Call {PHONE}</a>
</nav>
"""


def footer() -> str:
    svc = "".join(f'<li><a href="/services/{slug}/">{name}</a></li>' for slug, name, _ in SERVICES)
    return f"""
<footer class="site-footer">
  <div class="wrap footer-grid">
    <div>
      <img class="footer-logo" src="/assets/images/Landman-Excavation-Grading.jpg" alt="" width="512" height="512">
      <p>LandMan Excavation &amp; Grading helps North Georgia property owners get more use from their land. Chris Chaney. Insured. Locally owned.</p>
      <p><a href="tel:{TEL}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
    <div>
      <h2>Explore</h2>
      <ul>
        <li><a href="/about/">About Chris</a></li>
        <li><a href="/services/">Services</a></li>
        <li><a href="/projects/">Projects</a></li>
        <li><a href="/property-solutions/">Property solutions</a></li>
        <li><a href="/horse-properties/">Horse properties</a></li>
        <li><a href="/service-area/">Service area</a></li>
        <li><a href="/faq/">FAQ</a></li>
        <li><a href="/contact/">Contact</a></li>
      </ul>
    </div>
    <div>
      <h2>Services</h2>
      <ul>{svc}</ul>
    </div>
  </div>
  <div class="wrap fine">
    <span>&copy; <span id="year">2026</span> LandMan Excavation &amp; Grading. Demo preview by Knight Logics.</span>
    <span>North Georgia · Hall, Forsyth, Lumpkin, Pickens, White, Habersham, Stephens, Franklin, Banks, Jackson, Dawson</span>
  </div>
</footer>
<a class="mobile-call" href="tel:{TEL}">Call or text {PHONE}</a>
<script src="/assets/js/main.js"></script>
"""


def form(heading="Request a free estimate", compact=False) -> str:
    counties = "".join(f'<option>{c} County</option>' for c in COUNTIES)
    services = "".join(f'<option>{name}</option>' for _, name, _ in SERVICES)
    services += "<option>Horse property work</option><option>Fence line clearing</option><option>Not sure yet</option>"
    return f"""
<form class="estimate-form form-grid" method="post" action="/contact/">
  <h2>{heading}</h2>
  {'' if compact else '<p>Call, text, or leave the basics. This demo form stays in your browser. It does not email Chris.</p>'}
  <label>Name<input name="name" required autocomplete="name"></label>
  <label>Phone<input name="phone" type="tel" required autocomplete="tel"></label>
  <label>Email<input name="email" type="email" required autocomplete="email"></label>
  <label>County<select name="county"><option value="">Select a county</option>{counties}<option>Other North Georgia</option></select></label>
  <label>What do you need?<select name="service"><option value="">Select a service</option>{services}</select></label>
  <label>About the property<textarea name="message" placeholder="Acreage, access, drainage, driveway, horses, or what you want the land to do."></textarea></label>
  <button class="btn" type="submit">Request a free estimate</button>
  <p class="form-note">Live site phone and email still work: <a href="tel:{TEL}">{PHONE}</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
</form>
<div class="form-ok" role="status"><strong>Saved in this browser only.</strong> Nothing was sent. Call or text {PHONE} to reach LandMan.</div>
"""


def faq_html(items=None) -> str:
    rows = []
    for q, a in items or FAQS:
        rows.append(f"<details><summary>{q}</summary>{a}</details>")
    return f'<div class="faq-list">{"".join(rows)}</div>'


def for_base(html: str) -> str:
    """Drop leading slashes so a <base> tag works on GitHub Pages and localhost."""
    html = html.replace('href="/"', 'href="./"')
    html = html.replace('href="/', 'href="')
    html = html.replace('src="/', 'src="')
    html = html.replace('action="/', 'action="')
    html = html.replace('poster="/', 'poster="')
    html = html.replace("url('/assets/", "url('assets/")
    html = html.replace('content="/assets/', 'content="assets/')
    return html


def page(path, title, description, active, body, og_image="assets/images/construction-11.jpg"):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <script>
  (function () {{
    var path = location.pathname;
    var marker = "/landman-excavation";
    var idx = path.indexOf(marker);
    var base = idx >= 0 ? path.slice(0, idx + marker.length) + "/" : "/";
    document.write('<base href="' + base + '">');
  }})();
  </script>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="robots" content="noindex, nofollow">
  <meta name="theme-color" content="#000000">
  <link rel="icon" href="/assets/images/cropped-Landman-Excavation-Grading-32x32.jpg">
  <link rel="apple-touch-icon" href="/assets/images/cropped-Landman-Excavation-Grading-180x180.jpg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/css/style.css">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:image" content="{og_image}">
</head>
<body>
{chrome(active)}
<main id="main">
{body}
</main>
{footer()}
</body>
</html>
"""
    html = for_base(html)
    dest = ROOT / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html, encoding="utf-8")
    print(path)


def hero_home():
    cards = []
    images = {
        "land-clearing": ("arttower-land-clearing-208853_1280.jpg", "Backhoe handling a log in a wooded clearing"),
        "brush-removal": ("georgeb2-landscape-7332939_640.jpg", "Mature trees along a wooded creek"),
        "pasture-reclamation": ("rita2000-wheat-9666681_640.jpg", "Open green field under a bright sky"),
        "grading": ("artellliii72-bulldozer-7147988_640.jpg", "Wheel loader spreading soil in an open field"),
        "driveway-repair": ("pexels-rocks-1869970_640.jpg", "Close view of crushed stone"),
        "site-preparation": ("construction-11.jpg", "Tracked excavator on a graded site"),
    }
    for slug, name, blurb in SERVICES:
        src, alt = images[slug]
        cards.append(f"""
        <article class="card">
          <img src="/assets/images/{src}" alt="{alt}">
          <div class="card-body">
            <h3>{name}</h3>
            <p>{blurb}</p>
            <a class="more" href="/services/{slug}/">View {name.lower()}</a>
          </div>
        </article>""")
    steps = [
        ("1", "Reach out", "Call, text, or request a free estimate."),
        ("2", "On-site visit", "Walk the property, talk through the goal, and ask questions."),
        ("3", "Clear estimate", "A straightforward number, with the approach explained."),
        ("4", "Schedule", "You hear what is happening while the work is underway."),
        ("5", "Job complete", "The property is cleaner, more usable, and ready for what comes next."),
    ]
    step_html = "".join(f"<li><strong>{n}</strong><h3>{t}</h3><p>{b}</p></li>" for n, t, b in steps)
    return f"""
<section class="hero">
  <div class="hero-media">
    <img src="/assets/images/construction-11.jpg" alt="">
    <video autoplay muted loop playsinline poster="/assets/images/construction-11.jpg">
      <source src="/assets/video/204667-925250930_small.mp4" type="video/mp4">
    </video>
  </div>
  <div class="hero-shade"></div>
  <div class="wrap hero-grid">
    <div>
      <p class="eyebrow">North Georgia · Excavation &amp; Grading</p>
      <h1>Get more from the land you already own.</h1>
      <p class="lede">At LandMan, the goal isn’t simply to move dirt. It’s to improve the way people enjoy and use their property.</p>
      <div class="hero-actions">
        <a class="btn" href="tel:{TEL}">Call {PHONE}</a>
        <a class="btn btn-ghost" href="/projects/">See project stories</a>
      </div>
    </div>
    <div class="estimate">{form()}</div>
  </div>
</section>
<section class="trust" aria-label="Why LandMan">
  <ul class="wrap">
    <li><span>01</span>Insured</li>
    <li><span>02</span>Experienced equipment operator</li>
    <li><span>03</span>Honest communication</li>
    <li><span>04</span>Locally owned &amp; operated</li>
  </ul>
</section>
<section class="section">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Services</p>
      <h2>Practical work for rural property.</h2>
      <p>Clearing, brush, pasture, grading, driveways, and site prep. LandMan looks at the property first, then recommends the approach that fits how you want to use it.</p>
    </div>
    <div class="cards">{''.join(cards)}</div>
  </div>
</section>
<section class="section" style="background:#fff">
  <div class="wrap split">
    <div class="prose">
      <p class="eyebrow">The LandMan</p>
      <h2>Chris Chaney treats the property like it is his own.</h2>
      <p>Chris brings decades of hands-on work, practical problem-solving, and respect for someone else’s land. He grew up with family roots in farming, then owned a small business, managed pipeline and grading projects, ran heavy equipment, and later flew as a professional pilot.</p>
      <p class="pull">Preparation, safety, communication, and doing the job right the first time.</p>
      <p>Whether the job is an overgrown pasture, drainage, a driveway, clearing, or getting a property ready for its next use, the standard stays the same: practical solutions, clear communication, and care.</p>
      <a class="btn" href="/about/">About Chris</a>
    </div>
    <img src="/assets/images/arttower-land-clearing-208853_1280.jpg" alt="Backhoe working among trees in a clearing">
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Process</p>
      <h2>Straightforward from the first call.</h2>
    </div>
    <ol class="steps">{step_html}</ol>
  </div>
</section>
<section class="section promise">
  <div class="wrap">
    <p class="eyebrow">The LandMan promise</p>
    <h2>Show up. Say what will happen. Finish the job.</h2>
    <p>We treat your property with the same care we’d expect on our own. Real, practical solutions, work until the job is completed, and respect for your hard-earned dollar.</p>
    <a class="btn" href="/contact/">Talk about your property</a>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">FAQ</p>
      <h2>Common questions, answered the way LandMan answers them.</h2>
    </div>
    {faq_html(FAQS[:4])}
    <p style="margin-top:16px"><a class="btn" href="/faq/">All questions</a></p>
  </div>
</section>
"""


def service_body(slug, name, lede, paras, includes, image, alt, related):
    inc = "".join(f"<li>{item}</li>" for item in includes)
    rel = "".join(f'<li><a href="/services/{s}/">{n}</a></li>' for s, n in related)
    body_paras = "".join(f"<p>{p}</p>" for p in paras)
    return f"""
<section class="page-hero" style="background-image:url('/assets/images/{image}')">
  <div class="wrap">
    <p class="crumbs"><a href="/">Home</a> · <a href="/services/">Services</a></p>
    <h1>{name}</h1>
    <p>{lede}</p>
  </div>
</section>
<section class="section">
  <div class="wrap layout">
    <article class="prose">
      {body_paras}
      <h2>How a job starts</h2>
      <p>Call or text {PHONE}, or request a visit. Chris walks the property, talks through what you want the land to do, and sends a straightforward estimate before anything is scheduled.</p>
      <p>Related work: {', '.join(n for _, n in related)}.</p>
    </article>
    <aside class="sidecard">
      <h2>On this kind of job</h2>
      <ul>{inc}</ul>
      <a class="btn" href="/contact/">Request an estimate</a>
      <p>Or call <a href="tel:{TEL}">{PHONE}</a></p>
      <h2>Related</h2>
      <ul>{rel}</ul>
    </aside>
  </div>
</section>
"""


PAGES_SERVICES = {
    "land-clearing": dict(
        lede="Small, medium, and larger acreage — cleared with the trees you want left standing.",
        image="arttower-land-clearing-208853_1280.jpg",
        alt="Backhoe handling a log in a wooded clearing",
        includes=["Small, medium, and large acreage", "Brush and stump removal or grinding", "Selective tree clearing", "Forestry mulching", "Pasture restoration as part of the clear"],
        paras=[
            "Land clearing at LandMan is selective. The work is brush, saplings, and small to medium trees that are in the way of pasture, access, a homesite, or a fence — not a blank wipe of every trunk on the place.",
            "If a tree is large, hazardous, or needs climbing or a crane, that is a tree service’s job. LandMan will say so and can coordinate with a crew you trust. The point is a property you can use, with the trees you meant to keep still there.",
            "Debris can be hauled, stacked, burned where that is allowed, or mulched in place. The estimate says which one fits the acreage, the access, and the budget.",
        ],
        related=[("brush-removal", "Brush removal"), ("pasture-reclamation", "Pasture reclamation"), ("site-preparation", "Site preparation")],
    ),
    "brush-removal": dict(
        lede="Briars, vines, and saplings cleared so fence lines and edges are usable again.",
        image="georgeb2-landscape-7332939_640.jpg",
        alt="Mature trees along a wooded creek",
        includes=["Brush, vines, and saplings", "Fence line clearing", "Easement edges", "Haul-off, stacking, or mulching"],
        paras=[
            "Brush takes a fence line, a field edge, or a path back faster than most owners can keep up with. LandMan cuts that growth out so you can see the fence, walk the line, and mow or maintain what is left.",
            "This is the same practical standard as the rest of the work: keep what you want, remove what is in the way, and leave the ground ready for the next use. Storm cleanup and overgrown easements sit in this same conversation.",
            "On the visit, Chris will say whether the brush should be hauled, stacked, burned where permitted, or forestry-mulched. You should not have to guess what the pile will look like when the machine leaves.",
        ],
        related=[("land-clearing", "Land clearing"), ("pasture-reclamation", "Pasture reclamation"), ("grading", "Grading")],
    ),
    "pasture-reclamation": dict(
        lede="Overgrown pasture brought back for mowing, grazing, or horses.",
        image="rita2000-wheat-9666681_640.jpg",
        alt="Open green field under a bright sky",
        includes=["Brush and young trees in the field", "Fence line clearing", "Access for equipment", "Ground ready to mow, graze, or reseed"],
        paras=[
            "Open land does not stay open. Briars, invasive growth, and young trees take over pasture until it is hard to mow and unsafe for horses or other livestock. Reclamation is how LandMan gives that ground back.",
            "The work is selective removal, fence line clearing, better access, and a finish you can maintain. It is not just “knock it down.” The estimate covers what gets removed, what stays, and whether you want the ground ready for grass.",
            "Horse properties are a regular part of this work: turnout, barn approaches, and fields that have gone to brush. See the horse properties page if that is the use you have in mind.",
        ],
        related=[("brush-removal", "Brush removal"), ("land-clearing", "Land clearing"), ("grading", "Grading")],
    ),
    "grading": dict(
        lede="Pads, drainage, culverts, and driveways shaped so water goes where it should.",
        image="artellliii72-bulldozer-7147988_640.jpg",
        alt="Wheel loader spreading soil in an open field",
        includes=["Building pads", "Drainage and culverts", "Driveway grade", "Final shape around barns and arenas"],
        paras=[
            "Grading is how a property sheds water and how equipment, trucks, and animals move across it. LandMan reads the way the land already drains, then cuts and fills so the new shape works with that, not against it.",
            "Jobs include building pads, drainage corrections, culverts, driveway grade, and the finish around a barn or arena. A French drain, a reshaped hillside, or a crown that finally pushes rain off a road all start with the same walk of the property.",
            "You get the plan in the estimate: what moves, where it goes, and what “done” looks like. Standing water, muddy pasture, and a driveway that guts itself every storm are the usual reasons people call.",
        ],
        related=[("driveway-repair", "Driveway repair"), ("site-preparation", "Site preparation"), ("land-clearing", "Land clearing")],
    ),
    "driveway-repair": dict(
        lede="Fix the washouts and the crown before you buy another load of gravel.",
        image="pexels-rocks-1869970_640.jpg",
        alt="Close view of crushed stone",
        includes=["Reshape the crown", "Fill washouts", "Correct drainage", "Spread, grade, and compact gravel"],
        paras=[
            "A lot of gravel driveways do not need to be rebuilt. They need the water sent off the road. Ruts, potholes, and washouts usually come from a flat or backwards crown, a low spot, or runoff aimed down the lane.",
            "LandMan looks at the cause, then reshapes the road, fills the cuts, and — when stone is actually the missing piece — spreads, grades, and compacts gravel for a driveway, parking area, or access road.",
            "New gravel on a bad grade is a short repair. The estimate will say whether you need stone, drainage, or both, and what a realistic timeline looks like. Smaller driveway jobs are often a day or two.",
        ],
        related=[("grading", "Grading"), ("site-preparation", "Site preparation"), ("brush-removal", "Brush removal")],
    ),
    "site-preparation": dict(
        lede="Pads, barn sites, arenas, and access — ready for what you build next.",
        image="construction-23.jpg",
        alt="Wheel loader working a soil pile at a site",
        includes=["Building pads", "Barn site preparation", "Arena prep and repair", "Access roads and easements"],
        paras=[
            "Site prep is the step between raw land and the thing you actually want there: a barn, an arena, a pad, a parking area, or a road you can drive in the rain. LandMan clears what is in the way, shapes the ground, and leaves a surface you can build on or maintain.",
            "Rural jobs on this list include fence line clearing, access roads, easement clearing, and arena grading — new or repaired. Horse properties often combine a pad, drainage, and turnout in one visit plan.",
            "If the project steps into permits, streams, or retaining walls, Chris will say so on the estimate instead of guessing. Work outside this scope gets a straight referral.",
        ],
        related=[("grading", "Grading"), ("land-clearing", "Land clearing"), ("driveway-repair", "Driveway repair")],
    ),
}


def build():
    page("index.html",
         "LandMan Excavation & Grading | North Georgia",
         "LandMan Excavation and Grading helps North Georgia property owners clear land, reclaim pasture, grade, and repair driveways. Call (770) 714-4907.",
         "home", hero_home())

    page("about/index.html",
         "About Chris Chaney | LandMan Excavation & Grading",
         "Chris Chaney runs LandMan Excavation and Grading in North Georgia. Farming roots, heavy equipment, and a pilot’s habit of preparation.",
         "about", f"""
<section class="page-hero" style="background-image:url('/assets/images/arttower-land-clearing-208853_1280.jpg')">
  <div class="wrap">
    <p class="crumbs"><a href="/">Home</a> · About</p>
    <h1>Meet the LandMan.</h1>
    <p>Practical solutions for property you can actually use.</p>
  </div>
</section>
<section class="section">
  <div class="wrap split">
    <article class="prose">
      <p class="eyebrow">Chris Chaney</p>
      <h2>Some careers are built behind a desk. This one was built on responsibility.</h2>
      <p>Chris grew up with a strong work ethic and family roots in farming. He learned early to take care of equipment and to respect another person’s property.</p>
      <p>Before aviation, he owned and operated a small business and managed commercial pipeline and grading projects, working with heavy equipment. That work taught planning, communication, and doing a job safely the first time.</p>
      <p>His years as a professional pilot asked for the same things at a higher level: preparation, attention, safety, and accountability. Those habits came back to the land. Between flights and after, he kept helping friends, family, and neighbors with drainage, grading, and clearing.</p>
      <p class="pull">Treat every property as if it were his own.</p>
      <p>LandMan Excavation &amp; Grading is that standard, full time. The goal is not simply to move dirt. It is to improve the way people enjoy and use their property.</p>
    </article>
    <img src="/assets/images/Landman-Excavation-Grading.jpg" alt="LandMan Excavation and Grading logo with an excavator">
  </div>
</section>
<section class="section" style="background:#fff">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">Process</p><h2>Five steps, then the machine shows up.</h2></div>
    <ol class="steps">
      <li><strong>1</strong><h3>Reach out</h3><p>Call, text, or request a free estimate.</p></li>
      <li><strong>2</strong><h3>On-site visit</h3><p>Walk the property and talk through the goal.</p></li>
      <li><strong>3</strong><h3>Clear estimate</h3><p>A straightforward price and a clear approach.</p></li>
      <li><strong>4</strong><h3>Schedule</h3><p>Updates while the work is underway.</p></li>
      <li><strong>5</strong><h3>Job complete</h3><p>Cleaner, more usable, ready for what is next.</p></li>
    </ol>
  </div>
</section>
""")

    cards = []
    for slug, name, blurb in SERVICES:
        meta = PAGES_SERVICES[slug]
        cards.append(f"""<article class="card"><img src="/assets/images/{meta['image']}" alt="{meta['alt']}"><div class="card-body"><h3>{name}</h3><p>{blurb}</p><a class="more" href="/services/{slug}/">Read {name.lower()}</a></div></article>""")
    page("services/index.html",
         "Services | LandMan Excavation & Grading",
         "Land clearing, brush removal, pasture reclamation, grading, driveway repair, and site preparation for North Georgia property owners.",
         "services", f"""
<section class="page-hero" style="background-image:url('/assets/images/construction-23.jpg')">
  <div class="wrap">
    <p class="crumbs"><a href="/">Home</a> · Services</p>
    <h1>Services built around the property.</h1>
    <p>Reclaim space, fix access, correct drainage, restore a driveway, or prepare a site.</p>
  </div>
</section>
<section class="section"><div class="wrap"><div class="cards">{''.join(cards)}</div></div></section>
<section class="section" style="background:#fff">
  <div class="wrap prose">
    <h2>Also on rural places</h2>
    <p>Fence line clearing, access roads, easement clearing, storm cleanup, drainage corrections, and arena grading — new or repaired — sit alongside the six services above. Horse properties have their own page because the mix of pasture, fence, drainage, and barn pad is its own job.</p>
    <p><a class="btn" href="/horse-properties/">Horse properties</a> <a class="btn" href="/property-solutions/" style="margin-left:8px">Property solutions</a></p>
  </div>
</section>
""")

    for slug, name, blurb in SERVICES:
        meta = PAGES_SERVICES[slug]
        page(f"services/{slug}/index.html",
             f"{name} | LandMan Excavation & Grading",
             f"{name} in North Georgia from LandMan Excavation and Grading. Free on-site estimate. Call {PHONE}.",
             "services",
             service_body(slug, name, meta["lede"], meta["paras"], meta["includes"], meta["image"], meta["alt"], meta["related"]))

    projects = [
        ("French drain installation", "construction-11.jpg", "Tracked excavator on a work site",
         "Every heavy rain left standing water around the pool and backyard. The area stayed muddy, unusable, and washed out after storms.",
         "After reading the property’s natural drainage, LandMan excavated and installed over 120 feet of French drain, surrounded it with drainage stone, and restored the area so it blended with the landscape.",
         ["Standing water eliminated", "Drainage restored", "Yard usable again", "Surrounding landscaping protected"]),
        ("Five large stumps removed", "arttower-land-clearing-208853_1280.jpg", "Equipment working in a wooded clearing",
         "Years after several large trees came down, five oversized stumps still occupied space, made mowing difficult, and blocked a future garden.",
         "Each stump was excavated and removed, not just cut flush. The holes were backfilled, graded, and prepared for grass or a garden.",
         ["Easier mowing", "More useful ground", "Ready for landscaping or fencing"]),
        ("Pasture expansion and barn grading", "artellliii72-bulldozer-7147988_640.jpg", "Loader spreading soil across a field",
         "A hillside beside a mini barn limited access, wasted pasture, and made mowing hard. The uneven ground also limited future livestock use.",
         "LandMan lowered the hillside, moved soil to the opposite side of the barn, and built a smooth grade around the structure. The finish was prepared for grass so the pasture could expand.",
         ["More usable pasture", "Better equipment access", "Improved drainage", "Easier mowing"]),
        ("Front entrance cleaned up", "georgeb2-landscape-7332939_640.jpg", "Wooded landscape with mature trees",
         "Years of overgrown landscaping hid the home’s entrance. Mature shrubs crowded the house, crepe myrtles had taken over, and the front approach had no definition.",
         "The overgrown landscape came out. Existing trees were selectively trimmed and reshaped, new mulch beds went in, a staircase was built, and a paver and pea-gravel walkway set the entrance.",
         ["Clearer curb appeal", "Easier maintenance", "Better access", "A defined first impression"]),
    ]
    blocks = []
    for title, img, alt, challenge, solution, results in projects:
        checks = "".join(f"<li>{r}</li>" for r in results)
        blocks.append(f"""
<article class="project">
  <img src="/assets/images/{img}" alt="{alt}">
  <div class="project-body">
    <h3>{title}</h3>
    <p class="kicker">Customer challenge</p>
    <p>{challenge}</p>
    <p class="kicker">The LandMan solution</p>
    <p>{solution}</p>
    <ul class="checks">{checks}</ul>
  </div>
</article>""")
    page("projects/index.html",
         "Projects | LandMan Excavation & Grading",
         "Drainage, stump removal, pasture grading, and entrance work from LandMan Excavation and Grading.",
         "projects", f"""
<section class="page-hero" style="background-image:url('/assets/images/construction-34.jpg')">
  <div class="wrap">
    <p class="crumbs"><a href="/">Home</a> · Projects</p>
    <h1>Featured projects.</h1>
    <p>Real challenges, the fix, and what the property could do afterward. Photos on this demo are the images from the live site, used as section art — not labeled as before-and-after proof.</p>
  </div>
</section>
<section class="section"><div class="wrap">{''.join(blocks)}</div></section>
<section class="section promise"><div class="wrap"><h2>The promise on every one of these.</h2><p>Show up, communicate, and leave the property more usable than you found it.</p><a class="btn" href="/contact/">Start with an estimate</a></div></section>
""")

    solutions = [
        ("There’s an old stump in the way",
         "Maybe the tree came down years ago. The stump is still there, in the way of the mower and of whatever you wanted that corner to become.",
         "LandMan removes the stump, backfills, and leaves it ready for grass, landscaping, fencing, or the next idea."),
        ("The pasture is overgrown",
         "Briars, brush, and young trees take pasture until it is hard to maintain or unsafe for horses and livestock.",
         "Selective removal, fence line clearing, better access, and ground prepared for mowing, grazing, or reseeding."),
        ("The driveway washes out",
         "Ruts and potholes after every rain are usually a grade and drainage problem. Another load of gravel alone rarely fixes it.",
         "Find the cause — crown, drainage, or both — then reshape the road so it holds up and looks like a driveway again."),
        ("Part of the property is unusable",
         "An old stump, brush, uneven ground, poor drainage, or years of neglect can park a whole section of land.",
         "A practical plan for a larger yard, room for horses, better access, parking, or space for a later project."),
        ("You need room for horses",
         "Usable pasture disappears fast. Turnout, fence lines, and a dry path to the barn matter more than a cleared postcard.",
         "Reclaim pasture, expand turnout, clear fence lines, improve drainage, and prepare an arena or barn site."),
        ("You need better drainage",
         "Standing water ruins driveways, turns pasture to mud, feeds erosion, and can work against a foundation over time.",
         "Read how the property already sheds water, then move it away from the problem without fighting the land."),
    ]
    sol_html = "".join(f"<article class='solution'><h3>{t}</h3><p>{p}</p><p><strong>LandMan:</strong> {s}</p></article>" for t, p, s in solutions)
    page("property-solutions/index.html",
         "Property Solutions | LandMan Excavation & Grading",
         "Common North Georgia property problems — stumps, brush, driveways, drainage, and horse pasture — and how LandMan approaches them.",
         "solutions", f"""
<section class="page-hero" style="background-image:url('/assets/images/georgeb2-landscape-7332939_640.jpg')">
  <div class="wrap">
    <p class="crumbs"><a href="/">Home</a> · Property solutions</p>
    <h1>Not every problem arrives with an obvious fix.</h1>
    <p>Start with what the land is doing. Then pick the work that changes how you use it.</p>
  </div>
</section>
<section class="section"><div class="wrap"><div class="solutions">{sol_html}</div></div></section>
""")

    page("horse-properties/index.html",
         "Horse Properties | LandMan Excavation & Grading",
         "Pasture reclamation, arena grading, fence lines, drainage, access roads, and barn pads for North Georgia horse properties.",
         "horse", f"""
<section class="page-hero" style="background-image:url('/assets/images/georgialens-horse-4492201_640.jpg')">
  <div class="wrap">
    <p class="crumbs"><a href="/">Home</a> · Horse properties</p>
    <h1>Room for horses, and ground that stays usable.</h1>
    <p>Safe, functional space for the horses and for the people taking care of them.</p>
  </div>
</section>
<section class="section">
  <div class="wrap split">
    <article class="prose">
      <p>Horse properties have a short list of things that actually matter: pasture you can turn out on, fence you can maintain, a path that does not turn to soup, and a barn or arena site that drains. LandMan works that list.</p>
      <ul>
        <li>Pasture reclamation</li>
        <li>Arena preparation and grading, new or repaired</li>
        <li>Fence line clearing</li>
        <li>Drainage improvements</li>
        <li>Access roads</li>
        <li>Barn site preparation</li>
        <li>Turnout expansion</li>
      </ul>
      <p>Whether you are bringing a first horse home or opening more of an existing farm, the visit is about how you use the place day to day. The estimate says what gets cleared, what gets graded, and what you will be able to maintain after the machines leave.</p>
      <a class="btn" href="/contact/">Talk through the farm</a>
    </article>
    <img src="/assets/images/georgialens-horse-4492201_640.jpg" alt="White horse standing in a green pasture">
  </div>
</section>
""")

    county_html = "".join(f"<li>{c} County</li>" for c in COUNTIES)
    page("service-area/index.html",
         "North Georgia Service Area | LandMan Excavation & Grading",
         "LandMan Excavation and Grading serves North Georgia, including Hall, Forsyth, Lumpkin, Pickens, White, Habersham, Stephens, Franklin, Banks, Jackson, and Dawson counties.",
         "area", f"""
<section class="page-hero" style="background-image:url('/assets/images/rita2000-wheat-9666681_640.jpg')">
  <div class="wrap">
    <p class="crumbs"><a href="/">Home</a> · Service area</p>
    <h1>North Georgia.</h1>
    <p>The live site lists these counties. If you are nearby and not sure, call — the estimate visit is how LandMan decides.</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <ul class="counties">{county_html}</ul>
    <div class="prose" style="margin-top:28px">
      <p>Hall, Forsyth, Lumpkin, Pickens, White, Habersham, Stephens, Franklin, Banks, Jackson, and Dawson. No street address is published on the current site. The way to start is a call, a text, or a note: {PHONE} · {EMAIL}.</p>
      <a class="btn" href="/contact/">Request a visit</a>
    </div>
  </div>
</section>
""")

    page("faq/index.html",
         "FAQ | LandMan Excavation & Grading",
         "Permits, insurance, tree size, cost, timing, driveways, horse farms, fence lines, gravel, debris, and staying on site during the work.",
         "faq", f"""
<section class="page-hero" style="background-image:url('/assets/images/construction-11.jpg')">
  <div class="wrap">
    <p class="crumbs"><a href="/">Home</a> · FAQ</p>
    <h1>Questions owners actually ask.</h1>
    <p>Answers from the LandMan site, in one place.</p>
  </div>
</section>
<section class="section"><div class="wrap">{faq_html()}</div></section>
""")

    page("contact/index.html",
         "Contact | LandMan Excavation & Grading",
         "Call or text LandMan Excavation and Grading at (770) 714-4907 or email info@landmanexcavation.com. Free on-site estimate in North Georgia.",
         "contact", f"""
<section class="page-hero" style="background-image:url('/assets/images/construction-23.jpg')">
  <div class="wrap">
    <p class="crumbs"><a href="/">Home</a> · Contact</p>
    <h1>Let’s talk about your property.</h1>
    <p>{PHONE} · {EMAIL}</p>
  </div>
</section>
<section class="section">
  <div class="wrap layout">
    <div class="estimate">{form("Get in touch")}</div>
    <aside class="sidecard">
      <h2>Direct</h2>
      <p><a href="tel:{TEL}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <h2>Service area</h2>
      <p>North Georgia, including Hall, Forsyth, Lumpkin, Pickens, White, Habersham, Stephens, Franklin, Banks, Jackson, and Dawson Counties.</p>
      <a class="btn" href="/service-area/">See counties</a>
    </aside>
  </div>
</section>
""")

    robots = """User-agent: *
Disallow: /
"""
    (ROOT / "robots.txt").write_text(robots, encoding="utf-8")
    html_files = list(ROOT.rglob("index.html"))
    print("PAGES", len(html_files))
    if len(html_files) != 15:
        raise SystemExit(f"expected 15 pages, found {len(html_files)}")


if __name__ == "__main__":
    build()
