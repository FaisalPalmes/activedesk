# ACT_IVE DE_SK — BRAND SYSTEM, MOTION SPEC & PAGE ARCHITECTURE
*The design half of the rebuild brief. Pair with SITE_AUDIT_AND_COPY_BANK.md (the content half).*

---

# 1. THE BRAND SYSTEM

## The underscore is the whole identity — treat it as a system token, not a logo quirk

Brand name is styled **`Act_ive De_sk®`** (registered trademark, confirmed in the homepage title tag and on LinkedIn). The two underscores represent **desk legs**, and in the client's logo they **animate up and down, alternating — one rising while the other falls — smoothly and continuously looping**. *(Client-confirmed behaviour. The agency SicoCreative lists "Animations" among delivered items, consistent with this. The exact current CSS/JS implementation was not inspectable — rebuild it properly rather than copying.)*

**The device already extends beyond the logo — this is the key insight:**
- Product SKUs: **Active_01** (The Expressive), **Active_02** (The Naturalist), **Active_03** (The Smooth Operator), **Active_04** (The Perfectionist — inferred, verify)
- Bylines: "**By_** James C Scott"

**Mandate for the rebuild:** make the underscore a reusable design token used consistently across section numbers, product codes, list markers, form-field underlines, hover states, and loading indicators. It should feel like the brand has a grammar, not a logo.

**Casing rule to lock:** always `Act_ive De_sk` (the live site inconsistently renders `act_ive De_sk` in body copy on one page). Never "ActiveDesk" or "Active Desk" in brand-voice contexts, though plain "Active Desk" is acceptable in schema/meta where the styling would confuse parsers.

## Voice
Irreverent-but-mission-driven: pop-culture winks layered over a genuinely serious health argument. The tier names riff on music — **The Smooth Operator** (Sade) with copy about "cool cats and smooth criminals" (Michael Jackson), and "Get Up Stand Up, Stand up for your life!" (Bob Marley). **This is a deliberate, ownable system — preserve and extend it.** The tiers are personality archetypes, not spec labels; that's their single most distinctive verbal asset.

**Style rulings needed in the rebuild:**
- Replace the pervasive double-dot `..` ellipsis with proper punctuation (or a single considered `…`)
- Standardise on **UK English** throughout (site currently mixes "Revolutionizing"/"Customization" with "colour")
- Fix the copy defects listed in the audit file

## Colour & type — UNVERIFIED, must be sourced
No hex codes or font names were extractable (no CSS access). **Two routes, in order of preference:**
1. **Ask James for the brand guidelines** — SicoCreative (sicocreative.com/activedesk) built the identity and holds the master assets, animation files, palette and type specimens. Fastest and most accurate.
2. Failing that, sample the live site in-browser (DevTools → computed styles) and document what's found.
**Do not invent a palette.** At Stage 0 the build session should extract what it can from the live site and present a proposed token set for approval, clearly flagging what is derived vs guessed.

---

# 2. MOTION SPEC — the scroll experience

The brief is heavy scroll animation, reveals and desk movement. Below is what to build and, crucially, the discipline that keeps it premium rather than gimmicky.

## 2.1 THE SIGNATURE MECHANIC — logo underscores drive the desk

**This is the idea that makes the site.** The brand's underscores are desk legs. The site's hero desk rises as you scroll. **Tie them together:** as the user scrolls the hero, the desk rises from sitting to standing height *and the underscores in the wordmark rise in sync*. Scroll position drives both. The logo stops being decoration and becomes the interface.

Implementation: GSAP ScrollTrigger with `scrub`, pinning the hero. Eased, weighted motion — a desk has mass; it should not feel like a slider. On completion the underscores settle back into their idle alternating loop.

## 2.2 Scroll effects inventory (build these)
- **Pinned scroll-scrub desk raise** — the hero moment above
- **Staggered reveals** — sections and their children fade/rise on entry, short travel (~30px), ~0.8–0.9s, small stagger. Never a bounce.
- **Scroll-progress indicator** — thin bar, accent colour, doubles as brand device
- **Condensing sticky nav** — shrinks and gains background on scroll, active-section highlighting
- **Parallax on full-bleed imagery** — subtle, 10–15% differential maximum
- **Horizontal pinned section for the finish swatches** (see 2.4) — scroll drives lateral movement through the finishes
- **Count-up animations** on the credential numbers (2 decades, 15,000 hours, £15m, 1,000+ projects) — these are strong and currently buried in prose
- **Text reveals** on major headlines — line-by-line mask reveal, not letter-by-letter (too slow, too 2019)
- **Sticky product cards** on the tier comparison — each tier card pins briefly as its detail scrolls past
- **Cursor-aware micro-interactions** on desktop only — magnetic buttons, subtle. Never a custom cursor that replaces the pointer.

## 2.3 Motion discipline (non-negotiable — this is what separates premium from tacky)
- **One signature moment per page maximum.** The desk raise is the homepage's. Other pages get a lesser hero moment.
- Everything respects `prefers-reduced-motion` — CSS and JS both. With motion off the site must be completely usable and still handsome.
- No animation may delay content legibility. Text is readable before, during and after any effect.
- No scroll-jacking. Never take control of scroll speed or force the user through a sequence they can't skip.
- Mobile: reduce aggressively. The pinned scrub raise is desktop/tablet; on phones use a lighter CSS/SVG version or a simple reveal. Test scroll-jank at 375px on a mid-range device before shipping.
- Every animation needs a reason. If it doesn't communicate something about the product or brand, cut it.

## 2.4 THE BIGGEST CONTENT OPPORTUNITY — the finish selector

The site claims **"Over 40 Standard Finishes, Design Without Boundaries!"** and shows **none of them interactively**. That's their most wasted asset. The Expressive alone has 10 named decors (Black, Toffee, Rose, Grey, Ice Blue, White, Cashmere, Dark Grey, Field Grey, Granite Grey).

**Build an interactive finish selector**: swatch grid, click/tap to live-swap the desktop on a hero product render, frame colour toggle (White/Black), finish name and tier displayed. Placed mid-scroll on the homepage AND on each product page. This single feature converts a text claim into the site's most engaging interaction — and it directly serves their "Unmatched Customization / Keep Your Colours Flying!" positioning.

*(Reference: Ergonofis' Sway configurator — ergonofis.com/pages/sway-desk — inline finish tiles feeding a customise CTA.)*

## 2.5 Optional 3D (scope carefully)
A Three.js desk (CDN, pinned version) makes the raise more impressive but adds weight and risk. **Decision rule:** if a well-lit CSS/image-sequence version of the raise looks convincing, ship that first and treat 3D as a phase-two enhancement. If 3D is used: lazy-init when near viewport, cap pixel ratio at 2, pause when off-screen or `document.hidden`, and capability-gate to a static poster on low-end devices / no WebGL / reduced-motion. **Total JS budget including libraries ≤ ~600KB compressed.**

---

# 3. COMPETITOR BENCHMARKS — specific things to steal

**1. Secretlab MAGNUS Pro — `https://secretlab.co/pages/magnus-pro`** ⭐ *the primary reference*
The strongest scroll-storytelling product page in this category: scroll-driven progressive disclosure revealing one feature at a time, animated transitions where the desktop physically raises between sit/stand states, exploded technical cross-sections, an accessory carousel, and a direct "vs. Typical Standing Desks" comparison block.
> **Steal:** the scroll-scrubbed desk raise (→ our signature mechanic, tied to the underscores) AND the "vs typical standing desks" comparison block — it makes the "quality without the hefty price tag" argument visually instead of in prose.

**2. Ergonofis Sway — `https://ergonofis.com/pages/sway-desk`** ⭐ *closest positioning match*
Premium solid-wood desks. Mid-page configurator with clickable finish tiles feeding a "Finish Customizing Your Desk" CTA; "Locally Handcrafted" / "Sustainably Made" callouts with a **B-Corp badge**; scroll progression hero → overview → feature deep-dives → testimonials → FAQ → comparison.
> **Steal:** the inline mid-scroll finish configurator (→ §2.4) and third-party sustainability badging to make "Saving Our Environment One Desk at a Time!" credible rather than merely asserted.

**3. Vari — `https://www.vari.com`** ⭐ *best B2B/dealer-model match*
Closest to Act_ive De_sk's actual business (dual B2B/consumer, space planning, design services). Runs a **Desk Finder Quiz**, a **Project Estimator** for business clients, a Desk Designer configurator, virtual showroom, 360° swatch carousels. Headline: "Work Elevated".
> **Steal:** the guided quiz + project estimator pairing. For a no-prices lead-gen model this is the highest-value conversion mechanic available — it qualifies dealer vs end-user traffic instead of dumping everyone into one Mailchimp form. Also mirror the split B2B/consumer navigation.

**4. Autonomous — `https://www.autonomous.ai/standing-desks`** *(counter-example)*
Seven models, transparent $249–$1,149 pricing, spec-led cards, no configurator or motion. Converts on clarity and price laddering alone. Headline pattern: "From dual to quad motors, steel frame, 50,000 lift cycles tested."
> **Steal:** the transparent good/better/best ladder with the differentiating spec in the headline. Act_ive De_sk has a perfect four-tier ladder and publishes **no prices and no comparison table**. Even indicative "from £" pricing plus a comparison grid would give "Quality Meets Affordability" something to stand on. *(Client decision — flag it, don't assume.)*

**5. FlexiSpot UK — `https://www.flexispot.co.uk`** *(social proof)*
"Shop the Look" styled-room feature, creator endorsements, an **embedded Instagram UGC feed**, Trustpilot link.
> **Steal:** the room-scene module and the live Instagram feed. Act_ive De_sk has an active Instagram the website doesn't link to *at all* — piping it in closes that loop for free and supplies real installed-environment photography.

**Note:** Fully.com is **dead** — it 302-redirects to store.hermanmiller.com/brands-fully. Don't benchmark against it.

---

# 4. PROPOSED PAGE ARCHITECTURE

Preserve all existing information; restructure for clarity and conversion. Split the audience properly — the current IA is flat and mixes B2B, specifier and end-user messaging.

```
/                                  Homepage — the scroll narrative (see §5)
/desks                             The range: four tiers, comparison table, finish selector
/desks/the-expressive              Active_01
/desks/the-naturalist              Active_02
/desks/the-smooth-operator         Active_03
/desks/the-perfectionist           Active_04
/finishes                          The 40+ finishes, interactive, filterable by tier
/for-business                      B2B: 7 benefits, free trial desk, 21-day guarantee
/for-specifiers                    Architects/designers: WELL, free space planning, samples
/dealers                           Become a dealer + registration form
/story                             Founder story (long-form, treated with real care)
/about                             Company, credentials, vision, testimonials
/contact                           Enquiry + samples + trial requests
/privacy  /terms  /cookies         NEW — legally required, currently absent
```

**Redirect map required** from the old WordPress URLs (`/sit-stand-desk-for-business/`, `/sit-stand-desk-architects-designers/`, `/the-perfectionist-sit-stand-desk/`, `/founder-story/`, `/about-us/`, `/dealer-registration/`, `/contact-us/`) to the new structure — these are indexed and carry what little SEO equity exists.

---

# 5. HOMEPAGE SCROLL NARRATIVE (act structure)

1. **Hero** — wordmark with animated underscores, master tagline "Work Smarter. Be Healthier. Live Happier.", the positioning line, dual CTA (business enquiry / explore the range). Desk at sitting height.
2. **THE RISE** — pinned scroll-scrub: desk rises to standing, underscores rise in sync. Copy stages through sit → transition → stand.
3. **The sitting epidemic** — the problem act. Their existing copy is strong; support it with restrained data visualisation. Keep the BMJ and Get A Move On statistics **with their attributions intact** — never present a health statistic without its source.
4. **Founder moment** — the stepfather teaser quote, understated and human, linking to /story. This is the brand's differentiator against every faceless competitor; give it room and dignity.
5. **Static desks will become a thing of the past** — the affordability argument. Consider a "vs typical standing desks" comparison block here (Secretlab pattern).
6. **Work Smarter / Be Healthier / Live Happier** — the three benefit pillars, one per scroll act, each with its own reveal. These map exactly onto the tagline and are the site's spine.
7. **The four characters** — tier lineup with SKU codes (Active_01–04), personality copy intact, sticky-card scroll behaviour, → /desks.
8. **The finish selector** — interactive swatches, the "40+ finishes" claim made real.
9. **Credentials** — animated count-ups: 2 decades · 15,000 hours · £15m specified · 1,000+ projects · founded 2021.
10. **Proof** — the four testimonials (request company names/logos from James).
11. **Commercial hooks** — free trial desk (2-week, no obligation), 21-day delivery-and-install guarantee with penalty clause, free space planning and design service. These are genuinely strong offers currently buried on an inner page.
12. **Close** — "Ready To Create a More Productive Workplace…" + dealer/business enquiry.
13. **Footer** — NEW and legally required: company number 13461733, registered office, privacy, terms, cookies, socials (Instagram + LinkedIn), contact details, copyright.

---

# 6. TECHNICAL REQUIREMENTS

- **Stack:** static HTML/CSS/vanilla JS. GSAP + ScrollTrigger via CDN (pinned version), deferred. No framework, no build step. *(Three.js only if 3D is approved at Stage 0.)*
- **Repo + deploy:** private GitHub repo, auto-deploy to Vercel on push to `main`. Preview URL only until the client signs off — never touch the live domain.
- **SEO (fixes their worst failures):** unique title + meta description on every page; OG/Twitter tags with a real 1200×630 image; canonical tags; **inline JSON-LD** — `Organization` (with the Companies House details) + `Product` per desk tier (no invented `aggregateRating`); sitemap.xml; robots.txt; **single canonical host** (pick www or non-www and 301 the other — the current duplicate indexing is a real problem).
- **Legal (currently absent — must ship):** privacy policy, terms, cookie notice, company number and registered office in the footer.
- **Analytics:** cookieless (Plausible) placeholder + one clearly-marked Meta Pixel insertion point. Conversion events: `dealer_enquiry`, `trial_request`, `sample_request`, `finish_selected`, `tier_view`, `call_tap`.
- **Accessibility:** WCAG 2.1 AA. Descriptive alt text on every image (the current site's coverage is unknown and likely poor). Keyboard navigable including the finish selector. Visible focus states. Reduced-motion honoured everywhere.
- **Performance:** Lighthouse mobile 90+ (85+ if 3D ships). Images WebP, sized, lazy-loaded below fold, hero preloaded. No image over ~500KB.
- **Forms:** wired to a real provider (Formspree/Web3Forms or their Mailchimp) with honeypot, visible success and failure states, and a phone fallback. **Never ship a dead form.**

---

# 7. RULES FOR THIS BUILD

1. **Never invent facts about their business.** No prices, no specs, no health statistics, no testimonials beyond the four verbatim ones. Missing data becomes a clearly-labelled placeholder tracked in SWAP_LIST.md.
2. **Health claims keep their attributions.** The BMJ and Get A Move On statistics may be used *with their sources named*. Do not add new medical claims.
3. **The founder story is handled with care.** It involves a real bereavement — Ian Hawley, died 24 September 2020. Fix the "deaf certificate" typo, preserve everything else, and never let design flourishes trivialise it. His personal photographs (Steelway; the dog, Blade) must never be swapped for AI imagery.
4. **Fix the copy defects** listed in the audit — don't faithfully reproduce typos.
5. **The word "AI" never appears** anywhere in client-facing text, code comments, or commit messages.
6. **Preserve every piece of information** the current site carries. This is a rebuild, not a reduction — the audit file is the inventory.
