#!/usr/bin/env python3
"""Act_ive De_sk — static site generator.

Renders every page from shared templates so navigation, footer and legal
details stay identical across the site. Output is plain static HTML that
Vercel serves directly; there is no build step at deploy time.

Run:  python3 tools/build.py
"""
import os, html, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

COMPANY_NO = "13461733"
REG_OFFICE = ("Penny Lane Business Centre, 374 Smithdown Road, "
              "Liverpool, L15 5AN")
INSTAGRAM = "https://www.instagram.com/activedesk.co.uk/"
LINKEDIN = "https://uk.linkedin.com/company/active-desk-ltd"
EMAIL = "hello@activedesk.co.uk"

# --- Shared frame specification, verbatim from all four brochures ----------
FRAME_SPEC = [
    ("Height adjustment (frame only)", "580–1230mm"),
    ("Frame width adjustment range", "1200mm to 2000mm"),
    ("Frame arm length", "585mm"),
    ("Height adjustable method", "Electric, dual motor"),
    ("Control switch", "Digital display (3 settings)"),
    ("Speed", "38mm/s"),
    ("Motors / noise level", "&lt;50dB"),
    ("Maximum load capacity", "125kg"),
    ("Anti-collision", "Yes"),
    ("Life (cycles at full rated load)", "10,000"),
    ("Frame colours", "White &amp; Black"),
    ("Frame finish", "Steel (powder coated)"),
    ("Voltage input", "AC 100–240V 50/60Hz 450VA"),
    ("Voltage output", "23V 13A"),
    ("CE compliance", "BS EN 527-1"),
    ("Warranty", "10 years"),
]

CONTROLLER = ["Digital height display", "Time reminder to stand up",
              "3 programmable presets", "Anti-collision"]

PRODUCTS = [
    {
        "slug": "the-expressive", "sku": "A_1", "name": "The Expressive",
        "level": "Entry level", "material": "25mm MFC laminate",
        "tagline": "For those who love to express themselves.",
        "intro": ("The Expressive is our entry-level desk for those creative people who love to "
                  "get down and express their beautiful colourful self to the world. Honestly, I "
                  "don't think you will be working from this desk, but more like busting moves, "
                  "chatting, collaborating and expressing your unique gift into the world."),
        "quote": "Here's to the high fiving and busting moves at your desk — what back pain!",
        "desktop": ("The Expressive desktop is made from hardwearing laminate, so it can withstand "
                    "any battering you may throw at it. It comes in 10 standard colourful colours — "
                    "but don't let that stop you asking for more."),
        "spec": [("Desktop", "25mm MDF/MFC laminate"), ("Desk bottom", "White laminate balancer")],
        "features": ["Abrasion, impact and scratch-resistant", "Moisture-resistant surface",
                     "Food-safe and hygienic", "Lightfast", "Durable and easy to maintain",
                     "Also available MED-certified", "Antibacterial properties (tested to JIS Z 2801)"],
        "decors": ["White", "Cashmere", "Dark Grey", "Field Grey", "Granite Grey",
                   "Black", "Toffee", "Rose", "Grey", "Ice Blue"],
        "hero": "expressive-lifestyle-01",
        "gallery": ["expressive-lifestyle-02", "expressive-lifestyle-03", "detail-controller-blue"],
    },
    {
        "slug": "the-naturalist", "sku": "A_2", "name": "The Naturalist",
        "level": "Mid level", "material": "25mm MFC woodgrain",
        "tagline": "For those who love the natural things in life.",
        "intro": ("The Naturalist is our mid-range desk for those naturalists out there who want to "
                  "be nurtured by nature's beauty. Work from this desk and you will feel like you "
                  "have been transported into the beautiful English countryside. All you need now "
                  "is a blanket, a couple of glasses and a bottle opener."),
        "quote": "For those people who love the natural things in life.",
        "desktop": ("The Naturalist desktop is made from woodgrain reproduction laminates and "
                    "decorative faced boards. Each woodgrain has been carefully chosen for its "
                    "unique authentic character and colour grain."),
        "spec": [("Desktop", "25mm MDF/MFC laminate"), ("Desk bottom", "MDF/MFC laminate")],
        "features": ["Abrasion, impact and scratch-resistant", "Moisture-resistant surface",
                     "Food-safe and hygienic", "Lightfast", "Durable and easy to maintain",
                     "Also available MED-certified", "Antibacterial properties (tested to JIS Z 2801)"],
        "decors": ["Lisa Oak", "Maple", "Natural Dijon Walnut", "Ellmau Beech", "Laguna Oak",
                   "Walnut Opera", "Verona Cherry", "Nebraska Oak", "Tobacco Walnut", "Light Sorano Oak"],
        "hero": "naturalist-lifestyle-02",
        "gallery": ["naturalist-lifestyle-01", "naturalist-lifestyle-03", "detail-controller-wood"],
    },
    {
        "slug": "the-smooth-operator", "sku": "A_3", "name": "The Smooth Operator",
        "level": "High level", "material": "19mm Perfectsense matt",
        "tagline": "For those cool cats and smooth criminals out there.",
        "intro": ("The Smooth Operator is our high-level desk for those cool cats and smooth "
                  "criminals out there. Success comes easy at this desk as you perform your tasks "
                  "with great skill and grace, through your cool, collected, charming and "
                  "persuasive manner. Just don't forget to wipe that speck of dust off the desk "
                  "before you leave."),
        "quote": "A range of ultra smooth touch desk tops.",
        "desktop": ("The Smooth Operator desktop is made from Perfectsense lacquered chipboard matt. "
                    "The low gloss gives the desk a beautiful smooth, natural velvety finish, and "
                    "the anti-fingerprint properties are a plus — though obviously not necessary "
                    "for the clean Smooth Operator."),
        "spec": [("Desktop", "19mm lacquered chipboard matt")],
        "features": ["Textured, matt, velvety surface", "Anti-fingerprint properties",
                     "Scratch and micro-scratch resistance", "Elegant finish", "Easy to clean",
                     "Heat resistant", "Antibacterial properties (tested to JIS Z 2801)"],
        "decors": ["Stone Green", "Taupe Grey", "Pebble Grey", "Premium White", "Light Grey",
                   "Inigo Blue", "Cubanit Grey", "Cashmere", "Angora Grey", "Black"],
        "hero": "smooth-operator-lifestyle-01",
        "gallery": ["smooth-operator-lifestyle-02", "smooth-operator-lifestyle-03", "detail-controller-matt"],
    },
    {
        "slug": "the-perfectionist", "sku": "A_4", "name": "The Perfectionist",
        "level": "Premium", "material": "6mm solid surface on 18mm ply",
        "tagline": "For those who strive to create perfection.",
        "intro": ("The Perfectionist is our premium desk for those perfectionists out there who "
                  "want nothing else but sheer class. Work from this desk and you will feel like "
                  "you have won the lottery — well, I guess you would not be working if you won "
                  "the lottery, but you know what I mean. Pure class."),
        "quote": "Don't let the haters get to you — indulge yourself.",
        "desktop": ("The Perfectionist top layer is a delicate composition of 6mm acrylic, minerals "
                    "and natural pigments that combine to create a smooth, non-porous, "
                    "thermoformable and visually seamless solid surface finish. The top is bonded "
                    "onto 18mm real Latvian plywood, clear lacquered to give a natural finish — "
                    "leaving only perfection."),
        "spec": [("Desktop", "6mm solid surface material"),
                 ("Desk bottom", "18mm Latvian birch plywood, clear lacquer finish")],
        "features": ["Resistant to scratching, chipping and denting with daily wear",
                     "Colour and texture run through the entire thickness and cannot wear away",
                     "Non-porous — no tiny openings or pores on the surface",
                     "Stain and bacteria resistant", "Low maintenance and chemical resistant",
                     "Built to last, and warranted for 10 years"],
        "decors": ["Sapphire", "Alpine White", "Ivory White", "Grey", "Suede", "Babylon Grey",
                   "Stone Green", "Taupe Grey"],
        "hero": "perfectionist-lifestyle-01",
        "gallery": ["perfectionist-lifestyle-02", "detail-controller-solid", "frame-single-white"],
    },
]

TESTIMONIALS = [
    ("Excellent value, great design, speed of installation and immediate positive impact!",
     "Will Lewis", ""),
    ("We were surprised by the increased energy levels and productivity! Increased collaboration "
     "by people being on their feet more, and the cost and quality was amazing!",
     "Phil Thompson", ""),
    ("The end result was amazing and my entire team have commented favourably on their look, quiet "
     "movement and modern look and feel our office now has. I myself was on the fence, but I "
     "wouldn't hesitate now!", "Derek Knowles", "Operations Director"),
    ("Act_ive De_sk has truly transformed our office environment! Their electric stand-up desks are "
     "not only of exceptional quality but also offered at a competitive price!", "Cameron Watson", ""),
]

NAV = [("/products", "Products"), ("/stories", "Stories"),
       ("/sustainability", "Sustainability"), ("/story", "Our Story"), ("/contact", "Contact")]


def wordmark(cls=""):
    return (f'<span class="wordmark {cls}">Act<span class="wordmark__rule" aria-hidden="true">'
            f'</span>ive De<span class="wordmark__rule" aria-hidden="true"></span>sk</span>')


def head(title, desc, path, solid_nav=False):
    def nav_item(href, label):
        current = ' aria-current="page"' if path.startswith(href) else ''
        return f'<a class="nav__link" href="{href}"{current}>{label}</a>'
    nav_links = "".join(nav_item(h, l) for h, l in NAV)
    drawer_products = "".join(
        f'<a href="/products/{p["slug"]}">{p["sku"]} · {p["name"]}</a>' for p in PRODUCTS)
    drawer_links = "".join(f'<a href="{href}">{label}</a>' for href, label in NAV if href != "/products")
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:locale" content="en_GB">
<meta name="theme-color" content="#ffffff">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;600;700;800&family=Instrument+Sans:wght@400;500;600&display=swap">
<link rel="stylesheet" href="/assets/css/site.css">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<div class="progress" data-progress aria-hidden="true"></div>
<header class="nav{' is-solid' if solid_nav else ''}" data-nav>
  <div class="shell shell--wide nav__inner">
    <a class="wordmark" href="/" aria-label="Act_ive De_sk home">Act<span class="wordmark__rule" aria-hidden="true"></span>ive De<span class="wordmark__rule" aria-hidden="true"></span>sk</a>
    <nav class="nav__links" aria-label="Primary">{nav_links}</nav>
    <div class="nav__actions">
      <a class="btn btn--sm nav__cta" href="/contact#dealer" data-event="dealer_enquiry">Become a dealer</a>
      <button class="menu-btn" type="button" data-menu aria-expanded="false" aria-controls="drawer" aria-label="Menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>
<div class="drawer" id="drawer" data-drawer>
  <a href="/products">Products</a>
  <div class="drawer__sub">{drawer_products}</div>
  {drawer_links}
  <div class="drawer__foot"><a class="btn" href="/contact#dealer">Become a dealer</a></div>
</div>
<main id="main">
"""


def foot():
    prod_links = "".join(f'<li><a href="/products/{p["slug"]}">{p["name"]}</a></li>' for p in PRODUCTS)
    return f"""</main>
<footer class="footer">
  <div class="shell shell--wide">
    <div class="footer__grid">
      <div class="footer__brand">
        {wordmark()}
        <p style="margin-top:1rem;max-width:24ch">Work Smarter. Be Healthier. Live Happier.</p>
      </div>
      <div><h2>Products</h2><ul>{prod_links}<li><a href="/products">Compare all four</a></li></ul></div>
      <div><h2>Company</h2><ul>
        <li><a href="/stories">Stories</a></li>
        <li><a href="/sustainability">Sustainability</a></li>
        <li><a href="/story">Our story</a></li>
        <li><a href="/contact">Contact</a></li>
      </ul></div>
      <div><h2>Connect</h2><ul>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><a href="{INSTAGRAM}" rel="noopener">Instagram</a></li>
        <li><a href="{LINKEDIN}" rel="noopener">LinkedIn</a></li>
        <li><a href="/contact#dealer">Become a dealer</a></li>
      </ul></div>
    </div>
    <div class="footer__legal">
      <p class="footer__reg">Act_ive De_sk® is a registered trademark of ACTIVEDESK LIMITED, a company
        registered in England and Wales, company number {COMPANY_NO}. Registered office: {REG_OFFICE}.</p>
      <ul class="footer__links">
        <li><a href="/privacy">Privacy</a></li>
        <li><a href="/terms">Terms</a></li>
        <li><a href="/cookies">Cookies</a></li>
        <li>&copy; <span data-year>2026</span> ACTIVEDESK LIMITED</li>
      </ul>
    </div>
  </div>
</footer>
<script src="/assets/js/site.js" defer></script>
</body>
</html>
"""


def write(path, body):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(body)
    print("  ", path)


def img(name, alt, cls="", loading="lazy", sizes=None):
    s = f' sizes="{sizes}"' if sizes else ""
    return (f'<img src="/assets/img/{name}.jpg" alt="{alt}" class="{cls}" '
            f'loading="{loading}" decoding="async"{s}>')


def spec_table(rows, caption, first_col="Specification", second_col="Detail"):
    body = "".join(f'<tr><th scope="row">{k}</th><td>{v}</td></tr>' for k, v in rows)
    return f"""<div class="tablewrap"><table class="spec">
<caption>{caption}</caption>
<thead><tr><th scope="col">{first_col}</th><th scope="col">{second_col}</th></tr></thead>
<tbody>{body}</tbody></table></div>"""


def testimonial_rail():
    items = ""
    for quote, name, role in TESTIMONIALS:
        role_html = f"<span>{role}</span>" if role else ""
        items += (f'<figure class="quote"><p class="quote__mark" aria-hidden="true">"</p>'
                  f'<blockquote>{quote}</blockquote>'
                  f'<figcaption>{name}{role_html}</figcaption></figure>')
    return f'<div class="rail">{items}</div>'


def trust_bar():
    stats = [("2", "decades of workplace design"), ("15,000", "hours space planning"),
             ("£15m", "of furniture specified"), ("1,000+", "commercial projects")]
    items = "".join(
        f'<div class="trustbar__item"><p class="trustbar__num" data-count-text="{n}">{n}</p>'
        f'<p class="trustbar__label">{l}</p></div>' for n, l in stats)
    return f'<section class="trustbar"><div class="shell shell--wide"><div class="trustbar__grid">{items}</div></div></section>'


def marquee():
    real = ["OBI"]
    chips = "".join(f'<span class="logo-chip">{r}</span>' for r in real)
    chips += "".join('<span class="logo-chip logo-chip--placeholder">Client logo</span>' for _ in range(6))
    return (f'<div class="marquee"><div class="marquee__track">{chips}{chips}</div></div>')


def cta_band(title, primary=("/contact#dealer", "Become a dealer"),
             secondary=("/products", "Explore the products")):
    return f"""<section class="section section--ink">
  <div class="shell cta reveal">
    <p class="eyebrow eyebrow--centre">Get started</p>
    <h2 class="cta__title" style="margin-top:1.25rem">{title}</h2>
    <div class="cta__actions">
      <a class="btn btn--invert" href="{primary[0]}" data-event="dealer_enquiry">{primary[1]}</a>
      <a class="btn btn--ghost-invert" href="{secondary[0]}">{secondary[1]}</a>
    </div>
  </div>
</section>"""


# ==========================================================================
# HOME
# ==========================================================================
def build_home():
    cards = ""
    for p in PRODUCTS:
        cards += f"""<a class="card" href="/products/{p['slug']}" data-event="tier_view">
  <div class="card__media">{img(p['hero'], p['name'] + ' electric sit stand desk')}</div>
  <div class="card__body">
    <p class="card__meta">{p['sku']} · {p['level']}</p>
    <h3 class="card__title">{p['name']}</h3>
    <p class="card__text">{p['tagline']}</p>
    <span class="card__more">View desk</span>
  </div>
</a>"""

    body = f"""<section class="hero">
  <div class="shell shell--wide hero__grid">
    <div>
      <p class="eyebrow">Electric sit stand desks</p>
      <h1 class="hero__title"><span>Work Smarter.</span><span>Be Healthier.</span><span>Live Happier.</span></h1>
      <p class="hero__lede">Complete ergonomic solutions for maintaining consistent productivity and
        efficiency while ensuring employee health and well-being.</p>
      <div class="hero__actions">
        <a class="btn" href="/products">Explore the products</a>
        <a class="btn btn--ghost" href="/contact#dealer" data-event="dealer_enquiry">Become a dealer</a>
      </div>
    </div>
    <div class="hero__media">{img('naturalist-lifestyle-02', 'The Naturalist sit stand desk at standing height', loading='eager')}</div>
  </div>
</section>

{trust_bar()}

<section class="section section--tight">
  <div class="shell shell--wide">
    <p class="eyebrow eyebrow--centre" style="margin-bottom:0.5rem">Specified and installed for</p>
    {marquee()}
    <p style="text-align:center;color:var(--ink-3);font-size:var(--step--2)">Client logos to be supplied</p>
  </div>
</section>

<section class="rise" data-rise>
  <div class="rise__track" data-rise-track>
    <div class="rise__pin">
      <div class="shell shell--wide rise__grid">
        <div class="rise__stack">
          {img('gallery-04', 'The Naturalist sit stand desk raised to standing height')}
          <p class="rise__readout" data-height><span>Frame height</span>580mm</p>
        </div>
        <div class="rise__stages" data-rise-stages>
          <div class="rise__stage is-current" data-stage="0">
            <p class="eyebrow">Sit</p>
            <h2 class="rise__title">Where most of the day goes.</h2>
            <p class="rise__copy">Seated, static, hour after hour. It is the default position of
              modern work, and the one the body was never built to hold.</p>
          </div>
          <div class="rise__stage" data-stage="1">
            <p class="eyebrow">Transition</p>
            <h2 class="rise__title">Dual motor. Quiet as a mouse.</h2>
            <p class="rise__copy">38mm per second, under 50 decibels, with three programmable
              presets — so you change position without breaking your thought, or your colleague's.</p>
          </div>
          <div class="rise__stage" data-stage="2">
            <p class="eyebrow">Stand</p>
            <h2 class="rise__title">Get Up Stand Up, Stand up for your life!</h2>
            <p class="rise__copy">580 to 1230 millimetres of travel, rated for 10,000 cycles at full
              load and warranted for ten years. Built for the habit, not the novelty.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--ash">
  <div class="shell shell--wide">
    <div class="section__head reveal"><p class="eyebrow">The range</p>
      <h2 class="section__title">Four desks. Four characters.</h2>
      <p class="section__lede">The same serious frame under every one. What changes is the desktop —
        and who you are.</p>
    </div>
    <div class="cards cards--4 reveal-group">{cards}</div>
    <p style="margin-top:2.5rem" class="reveal"><a class="btn btn--ghost" href="/products">Compare all four</a></p>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="split">
      <div class="reveal">
        <p class="eyebrow">The problem</p>
        <h2 class="section__title">A silent killer, sitting under your team right now.</h2>
        <div class="prose" style="margin-top:1.5rem">
          <p>The impact of prolonged sitting from sedentary working conditions is having a
            detrimental impact on businesses and people's lives. Conditions associated with
            prolonged sitting include cardiovascular disease, some forms of cancer, type 2 diabetes,
            and back, shoulder and neck pain.</p>
          <p>Often these conditions don't catch up with people until middle to old age — and that's
            when it's too late, as they turn into chronic conditions from years of unhealthy habits.</p>
          <p><strong>We have your back.</strong></p>
        </div>
      </div>
      <div class="prose reveal">
        <p><strong>The British Medical Journal states:</strong> "Spending large amounts of time
          sitting or lounging around during the day is linked to around 70,000 deaths per year in
          the UK and the NHS spends more than £0.7bn per year treating the health consequences."</p>
        <p><strong>And the cost to business, according to Get A Move On:</strong> "An estimated 6.9
          million working days are lost in the UK due to work-related musculoskeletal problems and
          the cost of poor mental health to UK business is estimated to be an astonishing £35bn
          annually."</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--ink">
  <div class="shell">
    <div class="section__head section__head--centre reveal">
      <p class="eyebrow eyebrow--centre">Why we exist</p>
      <h2 class="section__title" style="font-size:var(--step-3)">"My stepfather's chronic back pain
        which took his life, not cancer, was the catalyst for the seed to be born"</h2>
      <p class="section__lede">By_ James C Scott, Founder</p>
      <p style="margin-top:2.25rem"><a class="btn btn--invert" href="/story">Read the founder story</a></p>
    </div>
  </div>
</section>

<section class="section">
  <div class="shell shell--wide">
    <div class="section__head reveal"><p class="eyebrow">Proof</p>
      <h2 class="section__title">What people say once the desks are in.</h2></div>
    <div class="reveal">{testimonial_rail()}</div>
    <p style="margin-top:2rem" class="reveal"><a class="btn btn--ghost" href="/stories">Read the client stories</a></p>
  </div>
</section>

<section class="section section--ash">
  <div class="shell">
    <div class="split split--flip">
      <div class="split__media reveal">
        <div class="globe" aria-hidden="true">
          <div class="globe__spin">
            <div class="globe__ring"></div>
            <div class="globe__lat" style="top:25%"></div>
            <div class="globe__lat" style="top:50%"></div>
            <div class="globe__lat" style="top:75%"></div>
            <div class="globe__lon" style="width:0;left:50%"></div>
            <div class="globe__lon" style="width:50%;left:25%;border-right:1px solid currentColor;border-left:1px solid currentColor"></div>
          </div>
        </div>
      </div>
      <div class="reveal">
        <p class="eyebrow">Sustainability</p>
        <h2 class="section__title">Saving our environment one desk at a time.</h2>
        <p class="section__lede">Reuse, reduce and sustain. Desks built to last ten years, screens
          made locally and carbon neutral, and a recycling programme rather than a skip.</p>
        <p style="margin-top:2rem"><a class="btn btn--ghost" href="/sustainability">How we do it</a></p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="shell shell--wide">
    <div class="section__head reveal"><p class="eyebrow">How we work with you</p>
      <h2 class="section__title">Try it first. Then hold us to the date.</h2></div>
    <div class="cards cards--3 reveal-group">
      <div class="card"><div class="card__body">
        <p class="card__meta">No obligation</p><h3 class="card__title">Free trial desk</h3>
        <p class="card__text">A two-week loan period with no obligation to purchase. Put a desk in
          front of the people who will actually use it.</p>
        <a class="card__more" href="/contact#trial" data-event="trial_request">Request a trial</a>
      </div></div>
      <div class="card"><div class="card__body">
        <p class="card__meta">Guaranteed</p><h3 class="card__title">21 days delivery and install</h3>
        <p class="card__text">Delivered and installed within 21 days, guaranteed — and the guarantee
          carries a penalty clause in your favour if we miss it.</p>
      </div></div>
      <div class="card"><div class="card__body">
        <p class="card__meta">At no cost</p><h3 class="card__title">Space planning and design</h3>
        <p class="card__text">Free building appraisal, free space planning, and a free design service
          to match desk finishes to your brand.</p>
        <a class="card__more" href="/contact#samples" data-event="sample_request">Request samples</a>
      </div></div>
    </div>
  </div>
</section>

{cta_band("Ready to create a more productive workplace, a healthier team and business growth?")}
"""
    write("index.html", head("Act_ive De_sk® | Quality Affordable Sit Stand Desks",
                             "Electric sit stand desks for UK workplaces. Four desks, over 40 standard "
                             "finishes, 21-day delivery and install guaranteed.", "/") + body + foot())


# ==========================================================================
# PRODUCTS INDEX + DETAIL PAGES
# ==========================================================================
def build_products():
    cards = ""
    for p in PRODUCTS:
        cards += f"""<a class="card" href="/products/{p['slug']}" data-event="tier_view">
  <div class="card__media">{img(p['hero'], p['name'] + ' electric sit stand desk')}</div>
  <div class="card__body">
    <p class="card__meta">{p['sku']} · {p['level']}</p>
    <h3 class="card__title">{p['name']}</h3>
    <p class="card__text">{p['tagline']}</p>
    <p class="card__meta" style="color:var(--ink-2);text-transform:none;letter-spacing:0">{p['material']}</p>
    <span class="card__more">View desk</span>
  </div>
</a>"""

    compare_head = "".join(f'<th scope="col">{p["sku"]}<br>{p["name"]}</th>' for p in PRODUCTS)
    rows = [
        ("Level", [p["level"] for p in PRODUCTS]),
        ("Desktop", [p["spec"][0][1] for p in PRODUCTS]),
        ("Character", [p["tagline"] for p in PRODUCTS]),
        ("Standard decors", [str(len(p["decors"])) for p in PRODUCTS]),
    ]
    compare_rows = ""
    for label, vals in rows:
        compare_rows += f'<tr><th scope="row">{label}</th>' + "".join(f"<td>{v}</td>" for v in vals) + "</tr>"
    shared = ("Every desk shares the same frame: dual motor, 580–1230mm height adjustment, "
              "125kg load, under 50dB, 10,000 cycles, 10-year warranty.")
    compare_rows += f'<tr><th scope="row">Shared frame</th><td colspan="4">{shared}</td></tr>'
    compare_rows += ('<tr><th scope="row">Price</th><td colspan="4">On enquiry — '
                     '<a href="/contact">talk to us about your project</a></td></tr>')

    body = f"""<section class="pagehead">
  <div class="shell shell--wide">
    <p class="eyebrow">Products</p>
    <h1 class="pagehead__title">Four desks. Four characters.</h1>
    <p class="pagehead__lede">The tier names are not spec labels — they are personalities. Pick the
      one that matches the people who will sit, and stand, at it every day.</p>
  </div>
</section>

<section class="section section--tight">
  <div class="shell shell--wide"><div class="cards cards--4 reveal-group">{cards}</div></div>
</section>

<section class="section section--ash">
  <div class="shell shell--wide">
    <div class="section__head reveal"><p class="eyebrow">Compare</p>
      <h2 class="section__title">Side by side.</h2></div>
    <div class="reveal"><div class="tablewrap"><table class="spec">
      <caption>The four Act_ive De_sk desks compared</caption>
      <thead><tr><th scope="col">Specification</th>{compare_head}</tr></thead>
      <tbody>{compare_rows}</tbody></table></div></div>
  </div>
</section>

<section class="section">
  <div class="shell shell--wide">
    <div class="section__head reveal"><p class="eyebrow">Shared engineering</p>
      <h2 class="section__title">One frame under all four.</h2>
      <p class="section__lede">Our lifting columns are made by one of the world's top three
        manufacturers, built for commercial office environments and covered for ten years.</p>
    </div>
    <div class="split">
      <div class="reveal">{spec_table(FRAME_SPEC, "Frame specification")}</div>
      <div class="reveal">
        <figure class="figure figure--ash">{img('frame-double-black', 'Back-to-back dual motor sit stand desk frame in black')}</figure>
        <figure class="figure figure--ash" style="margin-top:1rem">{img('frame-single-white', 'Single sit stand desk frame in white')}</figure>
        <p style="margin-top:1.25rem;color:var(--ink-2);font-size:var(--step--1)">Available single or
          back-to-back, dual motor or on each leg. Controller: {", ".join(CONTROLLER).lower()}.</p>
      </div>
    </div>
  </div>
</section>

{cta_band("Not sure which desk suits your workplace?", ("/contact#samples", "Request samples"), ("/contact", "Talk to us"))}
"""
    write("products.html", head("Products | Act_ive De_sk®",
                                "The four Act_ive De_sk electric sit stand desks compared: The Expressive, "
                                "The Naturalist, The Smooth Operator and The Perfectionist.",
                                "/products", solid_nav=True) + body + foot())

    for i, p in enumerate(PRODUCTS):
        build_product(p, PRODUCTS[(i + 1) % len(PRODUCTS)])


def build_product(p, nxt):
    features = "".join(f"<li>{f}</li>" for f in p["features"])
    decors = "".join(f"<li>{d}</li>" for d in p["decors"])
    gallery = "".join(
        f'<figure class="figure figure--ash">{img(g, p["name"] + " sit stand desk")}</figure>'
        for g in p["gallery"])
    desktop_spec = spec_table(p["spec"] + [("Standard decors", str(len(p["decors"])))],
                              "Desktop specification")

    ld = {
        "expressive": "the-expressive",
    }
    body = f"""<section class="pagehead">
  <div class="shell shell--wide">
    <p class="eyebrow">{p['sku']} · {p['level']}</p>
    <h1 class="pagehead__title">{p['name']}</h1>
    <p class="pagehead__lede">{p['tagline']}</p>
  </div>
</section>

<section class="section section--tight">
  <div class="shell shell--wide split">
    <div class="split__media reveal">
      <figure class="figure figure--ash">{img(p['hero'], p['name'] + ' electric sit stand desk', loading='eager')}</figure>
    </div>
    <div class="reveal prose">
      <p>{p['intro']}</p>
      <p><strong>"{p['quote']}"</strong></p>
      <p style="margin-top:2rem">
        <a class="btn" href="/contact#samples" data-event="sample_request">Request a sample</a>
        <a class="btn btn--ghost" href="/assets/brochures/{p['slug']}.pdf" style="margin-left:0.5rem" data-event="brochure_download">Download brochure</a>
      </p>
    </div>
  </div>
</section>

<section class="section section--ash">
  <div class="shell shell--wide">
    <div class="section__head reveal"><p class="eyebrow">The desktop</p>
      <h2 class="section__title">{p['material']}</h2>
      <p class="section__lede">{p['desktop']}</p></div>
    <div class="split">
      <div class="reveal">
        <figure class="figure">{img('decors-' + p['slug'].replace('the-', ''), p['name'] + ' standard decor range')}
          <figcaption>The {len(p['decors'])} standard decors. Bespoke finishes on request.</figcaption></figure>
      </div>
      <div class="reveal">
        <h3 style="font-size:var(--step-1)">Standard decors</h3>
        <ul class="decors" style="margin-top:1rem">{decors}</ul>
        <h3 style="font-size:var(--step-1);margin-top:2rem">Features and benefits</h3>
        <ul style="margin-top:1rem;padding-left:1.1rem;color:var(--ink-2);display:grid;gap:0.45rem">{features}</ul>
        <div style="margin-top:2rem">{desktop_spec}</div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="shell shell--wide">
    <div class="section__head reveal"><p class="eyebrow">In the room</p>
      <h2 class="section__title">{p['name']}, in use.</h2></div>
    <div class="cards cards--3 reveal-group">{gallery}</div>
  </div>
</section>

<section class="section section--ash">
  <div class="shell shell--wide">
    <div class="section__head reveal"><p class="eyebrow">Under the desktop</p>
      <h2 class="section__title">The frame, in full.</h2>
      <p class="section__lede">Lifting columns from one of the world's top three manufacturers.
        Dual motor, smooth and quiet, and warranted for ten years.</p></div>
    <div class="reveal">{spec_table(FRAME_SPEC, "Frame specification — shared across all four desks")}</div>
  </div>
</section>

<section class="section">
  <div class="shell shell--wide">
    <div class="section__head reveal"><p class="eyebrow">Next</p>
      <h2 class="section__title">{nxt['name']}</h2>
      <p class="section__lede">{nxt['tagline']}</p>
      <p style="margin-top:1.75rem"><a class="btn btn--ghost" href="/products/{nxt['slug']}">View {nxt['name']}</a></p>
    </div>
  </div>
</section>

{cta_band("Want to feel the finish before you specify it?", ("/contact#samples", "Request samples"), ("/products", "All four desks"))}
"""
    schema = f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Product","name":"{p['name']}","sku":"{p['sku']}",
"brand":{{"@type":"Brand","name":"Act_ive De_sk"}},"material":"{p['spec'][0][1]}",
"description":"{p['tagline']}"}}
</script>"""
    write(f"products/{p['slug']}.html",
          head(f"{p['name']} | {p['sku']} sit stand desk | Act_ive De_sk®",
               f"{p['name']} — {p['level'].lower()} electric sit stand desk with a {p['material']} "
               f"desktop and {len(p['decors'])} standard decors.",
               "/products", solid_nav=True) + body + schema + foot())


# ==========================================================================
# STORIES
# ==========================================================================
STORIES = [
    {"slug": "obi", "client": "OBI", "sector": "Retail",
     "summary": "A national retail name specifying Act_ive De_sk across its workplace.",
     "real": True},
]
PLACEHOLDER_STORIES = 5


def build_stories():
    cards = ""
    for s in STORIES:
        cards += f"""<a class="card" href="/stories/{s['slug']}">
  <div class="card__media">{img('gallery-02', s['client'] + ' workplace with Act_ive De_sk desks')}</div>
  <div class="card__body">
    <p class="card__meta">{s['sector']}</p>
    <h3 class="card__title">{s['client']}</h3>
    <p class="card__text">{s['summary']}</p>
    <span class="card__more">Read the story</span>
  </div>
</a>"""
    for i in range(PLACEHOLDER_STORIES):
        cards += """<div class="card card--placeholder">
  <div class="card__media">Client photography<br>to be supplied</div>
  <div class="card__body">
    <p class="card__meta">Client story</p>
    <h3 class="card__title">To be added</h3>
    <p class="card__text">A further client story, to be written up from the project record.</p>
  </div>
</div>"""

    body = f"""<section class="pagehead">
  <div class="shell shell--wide">
    <p class="eyebrow">Stories</p>
    <h1 class="pagehead__title">The workplaces that made the change.</h1>
    <p class="pagehead__lede">Every desk here went into a real building, for real people who had
      been sitting still for too long. These are the projects, and what happened next.</p>
  </div>
</section>

<section class="section section--tight">
  <div class="shell shell--wide"><div class="cards cards--3 reveal-group">{cards}</div></div>
</section>

<section class="section section--ash">
  <div class="shell shell--wide">
    <div class="section__head reveal"><p class="eyebrow">In their words</p>
      <h2 class="section__title">Straight from the people who signed it off.</h2></div>
    <div class="reveal">{testimonial_rail()}</div>
  </div>
</section>

{cta_band("Want your workplace to be the next story?")}
"""
    write("stories.html", head("Client Stories | Act_ive De_sk®",
                               "The workplaces that changed how they work, and what happened after the "
                               "Act_ive De_sk desks went in.", "/stories", solid_nav=True) + body + foot())

    for s in STORIES:
        build_story(s)


def build_story(s):
    body = f"""<section class="pagehead">
  <div class="shell shell--wide">
    <p class="eyebrow">{s['sector']} · Client story</p>
    <h1 class="pagehead__title">{s['client']}</h1>
    <p class="pagehead__lede">{s['summary']}</p>
  </div>
</section>

<section class="section section--tight">
  <div class="shell shell--wide reveal">
    <figure class="figure figure--ash">{img('gallery-02', s['client'] + ' workplace installation', loading='eager')}</figure>
  </div>
</section>

<section class="section">
  <div class="shell shell--narrow">
    <div class="prose reveal">
      <p style="padding:1.25rem;background:var(--ash);border-radius:var(--radius);color:var(--ink)">
        <strong>Story to be written.</strong> The brief, the specification, the installation and the
        outcome for {s['client']} will be written up here from the project record — with figures,
        photography and a quote signed off by the client.</p>
      <h2 style="font-size:var(--step-2);margin-top:2.5rem">The brief</h2>
      <p>To be supplied.</p>
      <h2 style="font-size:var(--step-2)">What we specified</h2>
      <p>To be supplied — desks, finishes, quantities and any screens or cable management.</p>
      <h2 style="font-size:var(--step-2)">The result</h2>
      <p>To be supplied.</p>
    </div>
  </div>
</section>

<section class="section section--ash">
  <div class="shell shell--wide">
    <div class="section__head reveal"><p class="eyebrow">More stories</p>
      <h2 class="section__title">Other workplaces we have changed.</h2>
      <p style="margin-top:1.75rem"><a class="btn btn--ghost" href="/stories">All client stories</a></p></div>
  </div>
</section>

{cta_band("Ready to talk about your own workplace?")}
"""
    write(f"stories/{s['slug']}.html",
          head(f"{s['client']} | Client story | Act_ive De_sk®",
               f"How {s['client']} specified Act_ive De_sk sit stand desks across its workplace.",
               "/stories", solid_nav=True) + body + foot())


# ==========================================================================
# SUSTAINABILITY
# ==========================================================================
def build_sustainability():
    pillars = [
        ("Reuse", "Reuse, reduce and sustain",
         "Existing furniture assessed before anything new is specified, and a recycling programme "
         "rather than a skip at the end of a fit-out."),
        ("Longevity", "Built to outlast the trend cycle",
         "Solid surface tops that cannot delaminate, colour running through the full thickness, and "
         "a ten-year warranty on every desk. The most sustainable desk is the one you do not replace."),
        ("Local", "Made close to home",
         "Our acoustic screens are locally made and carbon neutral, in 100% polyester with die-cast "
         "zinc clamps and a fire rating to BS EN 13501-1:2018."),
    ]
    cards = "".join(f"""<div class="card"><div class="card__body">
      <p class="card__meta">{tag}</p><h3 class="card__title">{title}</h3>
      <p class="card__text">{copy}</p></div></div>""" for tag, title, copy in pillars)

    body = f"""<section class="pagehead">
  <div class="shell shell--wide">
    <p class="eyebrow">Sustainability</p>
    <h1 class="pagehead__title">Saving our environment one desk at a time.</h1>
    <p class="pagehead__lede">A vision of a world where all workplace environments positively uplift
      human welfare, while conserving the earth's vitality.</p>
  </div>
</section>

<section class="section section--ink">
  <div class="shell">
    <div class="split">
      <div class="split__media reveal">
        <div class="globe" aria-hidden="true"><div class="globe__spin">
          <div class="globe__ring"></div>
          <div class="globe__lat" style="top:16%"></div>
          <div class="globe__lat" style="top:33%"></div>
          <div class="globe__lat" style="top:50%"></div>
          <div class="globe__lat" style="top:67%"></div>
          <div class="globe__lat" style="top:84%"></div>
          <div class="globe__lon" style="width:0;left:50%"></div>
          <div class="globe__lon" style="width:34%;left:33%;border-right:1px solid currentColor"></div>
          <div class="globe__lon" style="width:68%;left:16%;border-right:1px solid currentColor"></div>
        </div></div>
      </div>
      <div class="reveal">
        <p class="eyebrow">The vision</p>
        <h2 class="section__title">Conserving the earth's vitality.</h2>
        <p class="section__lede">We are not a furniture brand that moves boxes around. We are
          designers at heart, and that means asking what happens to a desk in year eleven — not
          just how it looks on day one.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="shell shell--wide">
    <div class="section__head reveal"><p class="eyebrow">How we do it</p>
      <h2 class="section__title">Three commitments, not three slogans.</h2></div>
    <div class="cards cards--3 reveal-group">{cards}</div>
  </div>
</section>

<section class="section section--ash">
  <div class="shell shell--wide">
    <div class="split">
      <div class="split__media reveal">
        <figure class="figure figure--ash">{img('perfectionist-lifestyle-02', 'The Perfectionist desk with solid surface top on birch plywood')}</figure>
      </div>
      <div class="reveal">
        <p class="eyebrow">Materials</p>
        <h2 class="section__title">A desktop that cannot wear away.</h2>
        <div class="prose" style="margin-top:1.5rem">
          <p>The Perfectionist's solid surface is a composition of acrylic, minerals and natural
            pigments bonded onto 18mm real Latvian birch plywood. Colour and texture run through the
            entire thickness of the material — they cannot wear away, and they cannot delaminate.</p>
          <p>Non-porous, stain and bacteria resistant, low maintenance and chemical resistant. It is
            warranted for ten years because it is built to last that long.</p>
        </div>
        <p style="margin-top:2rem"><a class="btn btn--ghost" href="/products/the-perfectionist">See The Perfectionist</a></p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="shell shell--wide">
    <div class="section__head reveal"><p class="eyebrow">Standards</p>
      <h2 class="section__title">Be a leader in holistic health design.</h2>
      <p class="section__lede">Our products help clients lead on holistic health, innovation and
        WELL Standards within their workplace projects — with free building appraisals, space
        planning and a design service to get the specification right first time.</p>
      <p style="margin-top:2rem"><a class="btn btn--ghost" href="/contact">Talk to us about a project</a></p>
    </div>
  </div>
</section>

{cta_band("Build a workplace that is better for people and the planet.")}
"""
    write("sustainability.html", head("Sustainability | Act_ive De_sk®",
                                       "Reuse, reduce and sustain: how Act_ive De_sk builds desks that last, "
                                       "made locally, with a recycling programme rather than a skip.",
                                       "/sustainability", solid_nav=True) + body + foot())


# ==========================================================================
# FOUNDER STORY
# ==========================================================================
def build_founder():
    body = f"""<section class="pagehead">
  <div class="shell shell--narrow">
    <p class="eyebrow">Founder story</p>
    <h1 class="pagehead__title">A Journey Ignited by Loss and Empathy</h1>
    <p class="pagehead__lede">By_ James C Scott · Founder / Creative Director · 13 January 2024</p>
  </div>
</section>

<section class="section section--tight">
  <div class="shell shell--narrow prose reveal">
    <p>In 2020, the world was struggling with the continuous challenges brought about by the COVID-19
      pandemic. Lives were lost, and the vulnerability of our health became a major issue. For me,
      reality hit home in the most profound way possible — not the loss of business I suffered in my
      workplace interior design studio, but the loss of my stepfather.</p>
  </div>
</section>

<section class="section section--ash">
  <div class="shell shell--narrow">
    <h2 class="section__title reveal">My stepfather.</h2>
    <div class="prose reveal" style="margin-top:1.75rem">
      <p>Ian had been a long-distance lorry driver all his life and loved it, and retired in 2017 at
        the ripe old age of 65. Plenty of time to enjoy his retirement, I thought — until a few years
        later in January 2019 he was diagnosed with stage 4 lung cancer. The news hit him and the
        whole family like a ton of bricks; we were lost for words. A couple of months later he had
        his first session of chemotherapy, and scans showed it seemed to be working and the cancer
        had not spread any further. Phew.</p>
      <p>2020 was a completely different story. My stepfather had for years always suffered from
        lower back and shoulder pain, and his lower back was giving him excruciating pain before his
        second bout of chemotherapy, which did not seem to work. He suddenly took a turn for the
        worse and died at home on September 24th, 2020. It was truly devastating for us all.</p>
      <p>A few weeks later my mum received the death certificate and read it out to me over the
        phone. I was dumbstruck — to hear the real reason my stepfather died. Not from his cancer as
        we all thought, but from "severe progressive discitis" in his lower back, caused by chronic
        lower back pain he had suffered with for years.</p>
      <p>The long-distance lorry driving on the roads of Britain had finally caught up on him,
        causing him chronic back and shoulder pain and costing him his life. It wasn't a fate he
        could easily escape; driving was not just a job for him, it was a passion. He could not do
        anything about his working conditions, but his working conditions of prolonged sitting
        finally caught up on him. I felt such great empathy for his loss, and something inside of me
        started burning up with such a force that I could not let this go.</p>
    </div>
    <figure class="figure reveal" style="margin-top:2.5rem">
      <div style="aspect-ratio:3/2;background:var(--ash-deep);border:1px solid var(--line);border-radius:var(--radius);display:grid;place-items:center;color:var(--ink-3);font-size:var(--step--1);text-align:center;padding:1rem">James's photograph — to be supplied</div>
      <figcaption>My stepfather's last company before retirement: Steelway in Wolverhampton</figcaption>
    </figure>
  </div>
</section>

<section class="section">
  <div class="shell shell--narrow prose reveal">
    <p>Early 2021, while still contemplating the loss of my stepfather, I was reading lots of
      articles about why so many people were getting seriously ill or dying from Covid. The number
      one reason that kept coming up was "due to a weak immune system", and or already "having some
      type of chronic pain".</p>
    <p>I started delving deeper into the impact prolonged sitting has on health, and it was
      frightening how big the epidemic is — especially in my field of work, workplace interiors. I
      have over two decades of designing award-winning workplaces, over 15,000 hours of space
      planning, specifying and designing over 15 million pounds worth of furniture, and undertaking
      countless workplace strategy projects for large .com companies.</p>
    <p>Our workplaces are full of people who sit at their static desks all day and it's becoming a
      silent killer. <strong>The BMJ (British Medical Journal) states:</strong> "Spending large
      amounts of time sitting or lounging around during the day is linked to around 70,000 deaths
      per year in the UK and the NHS spends more than £0.7bn per year treating the health
      consequences". <strong>And the costs to businesses according to Get A Move On is
      staggering:</strong> "An estimated 6.9 million working days are lost in the UK due to
      work-related musculoskeletal problems and the cost of poor mental health to UK business is
      estimated to be an astonishing £35bn annually".</p>
    <p>After three months of intense research, it was plain to see that prolonged sitting causes
      back, shoulder and neck pain — and it's the pain that increases cortisol levels, which play an
      important role in balancing our stress hormones. Stress hormones can suppress or break down
      the immune system's function. As a result, your body will be unable to fight against
      infections like viruses or bacteria, and you won't be able to achieve long-term healing,
      according to a study in the journal Trends in Neurosciences.</p>
    <p>Voila. Your immune system is your defence to your health and well-being. No wonder so many
      older people were dying from COVID-19 — your immune system deteriorates as you get older. The
      excruciating pain my stepfather suffered had compromised his immune system and left him unable
      to fight against his infection of the disc, which sadly took his life.</p>
    <p>Months later, while still contemplating how many people were still dying from COVID and my
      stepfather's death, an impulse shot through me and woke me up at 2am while sleeping. "I may
      not be able to help people who drive for long distances, but I can do something to help people
      in the office with their working conditions."</p>
    <p>The empathy for my stepfather's loss transformed into a burning force, and Act_ive De_sk was
      born. Beyond a business venture, it's a mission to combat the sedentary epidemic, especially
      within the realm of workplace design. My expertise in designing interiors for over a thousand
      commercial projects is fused with a passion for revolutionising the way we work.</p>
  </div>
</section>

<section class="section section--ash">
  <div class="shell shell--narrow">
    <figure class="figure reveal">
      <div style="aspect-ratio:3/2;background:var(--ash-deep);border:1px solid var(--line);border-radius:var(--radius);display:grid;place-items:center;color:var(--ink-3);font-size:var(--step--1);text-align:center;padding:1rem">James's photograph — to be supplied</div>
      <figcaption>Me out walking with my Jack Russell, Blade!</figcaption>
    </figure>
    <div class="prose reveal" style="margin-top:2.5rem">
      <p>Through Act_ive De_sk, I strive to break the chains of prolonged sitting — offering not just
        furniture but quality, affordable solutions and innovations that prioritise health and
        wellbeing. This journey is a tribute to my stepfather, a man whose passion became both a joy
        and, ultimately, a silent contributor to his demise.</p>
      <p>Join me in this mission. Let's reshape workspaces, defy the sedentary norm, and build a
        healthier, happier future for everyone.</p>
    </div>
  </div>
</section>

<section class="section section--ink">
  <div class="shell cta reveal">
    <p class="eyebrow eyebrow--centre">In memory</p>
    <h2 class="cta__title" style="margin-top:1.25rem">In honour of my stepfather, a beloved Blades fan. Ian Hawley.</h2>
    <p style="margin-top:1.5rem">James C Scott · Founder / Creative Director</p>
    <p style="margin-top:0.5rem">My stepfather's favourite artist, Rod Stewart — the song "Maggie May",
      dedicated to my mum, his beloved wife Maggie.</p>
    <div class="cta__actions"><a class="btn btn--invert" href="/contact">Join us to be part of the movement</a></div>
  </div>
</section>

{trust_bar()}
"""
    write("story.html", head("Our Story | Act_ive De_sk®",
                             "A journey ignited by loss and empathy — why Act_ive De_sk exists, in "
                             "founder James C Scott's own words.", "/story", solid_nav=True) + body + foot())


# ==========================================================================
# CONTACT + LEGAL
# ==========================================================================
def build_contact():
    body = f"""<section class="pagehead">
  <div class="shell shell--wide">
    <p class="eyebrow">Contact</p>
    <h1 class="pagehead__title">Let's talk about your workplace.</h1>
    <p class="pagehead__lede">Whether you are fitting out one floor or looking to stock Act_ive De_sk,
      start here. You will get a person, not an autoresponder.</p>
  </div>
</section>

<section class="section section--tight">
  <div class="shell shell--wide split">
    <form class="reveal" data-enquiry novalidate>
      <div class="form-grid form-grid--2">
        <p class="field"><label for="name">Name *</label>
          <input id="name" name="name" type="text" required autocomplete="name"></p>
        <p class="field"><label for="email">Email *</label>
          <input id="email" name="email" type="email" required autocomplete="email"></p>
        <p class="field"><label for="company">Company</label>
          <input id="company" name="company" type="text" autocomplete="organization"></p>
        <p class="field"><label for="phone">Phone</label>
          <input id="phone" name="phone" type="tel" autocomplete="tel"></p>
        <p class="field field--full"><label for="enquiry">What can we help with?</label>
          <select id="enquiry" name="enquiry">
            <option>Desks for our workplace</option>
            <option>Free trial desk (2 week loan)</option>
            <option>Finish samples</option>
            <option>Becoming a dealer</option>
            <option>Space planning or design service</option>
            <option>Something else</option>
          </select></p>
        <p class="field field--full"><label for="message">Message</label>
          <textarea id="message" name="message" rows="5"></textarea></p>
        <p class="field field--full" style="position:absolute;left:-9999px" aria-hidden="true">
          <label for="company-url">Leave empty</label>
          <input id="company-url" name="company-url" type="text" tabindex="-1" autocomplete="off"></p>
        <p class="field--full"><button class="btn" type="submit" data-event="enquiry_submit">Send enquiry</button></p>
        <p class="field--full form-status" data-form-status role="status" aria-live="polite"></p>
      </div>
    </form>
    <div class="prose reveal">
      <h2 style="font-size:var(--step-1)">Prefer to email?</h2>
      <p><a href="mailto:{EMAIL}" style="font-weight:600">{EMAIL}</a><br>
        <span style="font-size:var(--step--2);color:var(--ink-3)">Address to be confirmed before launch.</span></p>
      <h2 style="font-size:var(--step-1);margin-top:2rem" id="trial">Free trial desk</h2>
      <p>A two-week loan period with no obligation to purchase. Tell us how many people you would
        like to trial with and we will arrange it.</p>
      <h2 style="font-size:var(--step-1);margin-top:2rem" id="samples">Samples</h2>
      <p>Finish samples from any of the four desks, sent out so you can see and feel the decor before
        you specify it.</p>
      <h2 style="font-size:var(--step-1);margin-top:2rem">Registered office</h2>
      <p style="color:var(--ink-2)">ACTIVEDESK LIMITED<br>Penny Lane Business Centre<br>
        374 Smithdown Road<br>Liverpool L15 5AN<br>Company number {COMPANY_NO}</p>
    </div>
  </div>
</section>

<section class="section section--ink" id="dealer">
  <div class="shell">
    <div class="section__head reveal"><p class="eyebrow">Trade</p>
      <h2 class="section__title">Stock Act_ive De_sk.</h2>
      <p class="section__lede">We deliver through our dealer network and corporate clients, with
        unbeatable prices, unmatched customisation, short delivery and install lead times, and
        workplace consultancy alongside.</p>
      <p style="margin-top:2rem"><a class="btn btn--invert" href="mailto:{EMAIL}?subject=Dealer%20enquiry" data-event="dealer_enquiry">Enquire to become a dealer</a></p>
    </div>
  </div>
</section>

<section class="section section--ash">
  <div class="shell shell--narrow">
    <div class="section__head reveal"><p class="eyebrow">Newsletter</p>
      <h2 class="section__title" style="font-size:var(--step-2)">Keep in touch.</h2>
      <p class="section__lede">Occasional updates on new finishes, products and workplace health. By
        signing up you are agreeing to be contacted by Act_ive De_sk.</p></div>
    <form class="reveal" data-newsletter novalidate style="display:flex;flex-wrap:wrap;gap:0.75rem">
      <label class="vh" for="newsletter-email">Email address</label>
      <input id="newsletter-email" name="email" type="email" required placeholder="you@company.co.uk"
        style="flex:1 1 16rem;padding:0.85rem 1rem;border:1px solid var(--line-strong);border-radius:var(--radius);font:inherit">
      <button class="btn" type="submit">Sign up</button>
      <p class="form-status" data-form-status role="status" aria-live="polite" style="flex:1 1 100%"></p>
    </form>
  </div>
</section>
"""
    write("contact.html", head("Contact | Act_ive De_sk®",
                                "Talk to us about your workplace, request a free trial desk or samples, or "
                                "enquire about becoming an Act_ive De_sk dealer.",
                                "/contact", solid_nav=True) + body + foot())


LEGAL = {
    "privacy": ("Privacy Policy", """
      <h2 style="font-size:var(--step-1)">What we collect</h2>
      <p>When you send an enquiry, request a trial desk or samples, or sign up to the newsletter, we
        collect the details you give us — typically your name, email address, company and the content
        of your message.</p>
      <h2 style="font-size:var(--step-1)">Why we use it</h2>
      <p>To respond to your enquiry, to arrange trials, samples, quotations, delivery and
        installation, and — where you have asked us to — to send you occasional updates. We do not
        sell your data.</p>
      <h2 style="font-size:var(--step-1)">How long we keep it</h2>
      <p>Enquiry records are retained for as long as needed to serve you and to meet our legal and
        accounting obligations. Newsletter subscriptions are kept until you unsubscribe.</p>
      <h2 style="font-size:var(--step-1)">Your rights</h2>
      <p>Under UK GDPR you may request access to the personal data we hold about you, ask us to
        correct or erase it, object to or restrict how we use it, and request a copy in a portable
        format. You may also complain to the Information Commissioner's Office.</p>"""),
    "terms": ("Terms and Conditions", """
      <h2 style="font-size:var(--step-1)">Using this website</h2>
      <p>This website provides information about Act_ive De_sk products and services. Product
        specifications, finishes and availability may change, and nothing on this site constitutes a
        binding offer to sell.</p>
      <h2 style="font-size:var(--step-1)">Quotations and orders</h2>
      <p>Prices are provided on enquiry. Orders are governed by the quotation and the terms of sale
        supplied with it, which take precedence over anything stated here.</p>
      <h2 style="font-size:var(--step-1)">Delivery and installation</h2>
      <p>Our 21-day delivery and installation guarantee and any associated penalty terms apply as set
        out in your quotation.</p>
      <h2 style="font-size:var(--step-1)">Intellectual property</h2>
      <p>The Act_ive De_sk name, logo and the content of this website are owned by ACTIVEDESK LIMITED
        and may not be reproduced without permission.</p>"""),
    "cookies": ("Cookie Notice", """
      <h2 style="font-size:var(--step-1)">What this site uses</h2>
      <p>This website is built to work without tracking you across other sites. It does not set
        advertising cookies by default.</p>
      <h2 style="font-size:var(--step-1)">Analytics</h2>
      <p>We use privacy-friendly, cookieless analytics to understand how many people visit the site
        and which pages they find useful. This does not identify you individually.</p>
      <h2 style="font-size:var(--step-1)">Managing cookies</h2>
      <p>You can control and delete cookies through your browser settings at any time. Doing so will
        not prevent you from using this website.</p>"""),
}


def build_legal():
    for slug, (heading, content) in LEGAL.items():
        body = f"""<section class="pagehead">
  <div class="shell shell--narrow"><p class="eyebrow">Legal</p>
    <h1 class="pagehead__title">{heading}</h1></div>
</section>
<section class="section section--tight">
  <div class="shell shell--narrow prose reveal">
    <p style="padding:1.25rem;background:var(--ash);border-radius:var(--radius);color:var(--ink)">
      <strong>Awaiting approval.</strong> This page is laid out and ready. The wording must be
      reviewed and approved by Act_ive De_sk before the site goes live, and checked against the
      company's actual practices.</p>
    {content}
    <h2 style="font-size:var(--step-1)">Who we are</h2>
    <p>Act_ive De_sk® is a registered trademark of ACTIVEDESK LIMITED, a company registered in
      England and Wales under company number {COMPANY_NO}, with its registered office at {REG_OFFICE}.</p>
    <h2 style="font-size:var(--step-1)">Contact</h2>
    <p>Questions about this page can be sent to <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
  </div>
</section>"""
        write(f"{slug}.html", head(f"{heading} | Act_ive De_sk®",
                                    f"{heading} for Act_ive De_sk, a trading name of ACTIVEDESK LIMITED.",
                                    f"/{slug}", solid_nav=True) + body + foot())


def build_sitemap():
    urls = ["/", "/products", "/stories", "/sustainability", "/story", "/contact",
            "/privacy", "/terms", "/cookies"]
    urls += [f"/products/{p['slug']}" for p in PRODUCTS]
    urls += [f"/stories/{s['slug']}" for s in STORIES]
    entries = "".join(f"  <url><loc>https://activedesk.co.uk{u}</loc></url>\n" for u in urls)
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + entries + "</urlset>\n")


if __name__ == "__main__":
    print("Building Act_ive De_sk…")
    build_home()
    build_products()
    build_stories()
    build_sustainability()
    build_founder()
    build_contact()
    build_legal()
    build_sitemap()
    print("Done.")
