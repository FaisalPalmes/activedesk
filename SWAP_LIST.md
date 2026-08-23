# SWAP_LIST — Act_ive De_sk rebuild

Every placeholder, unverified figure and piece of content needed from the client.
Doubles as the client questionnaire. Maintained throughout the build.

Status key: **BLOCKING** (build cannot proceed without it) · **PLACEHOLDER** (styled slot
ships, swap later) · **DECISION** (a choice, not a missing fact).

---

## A. To request from James — priority order

### A1. Brand assets — BLOCKING for final visual sign-off
| Item | Why it matters | Source |
|---|---|---|
| Palette hex values | The build currently uses a proposed palette. Nothing in the identity was sampled — no CSS access. | SicoCreative |
| Font files / names + licences | Same. Display and body faces are currently proposed. | SicoCreative |
| Logo animation files | The underscores animate alternately in the real logo. Rebuilding it properly needs the timing/easing reference. | SicoCreative |
| Logo master (SVG preferred) | Wordmark is currently set in type, not their real mark. | SicoCreative |
| Photography library | Product shots, installed environments, finish close-ups. | James |

*Route: SicoCreative (sicocreative.com/activedesk) built the identity and holds the masters.
Asking James to request them is faster and more accurate than sampling.*

### A2. Specification figures — PLACEHOLDER until supplied
Recovered specs are Expressive-only (from the brochure PDF) plus shared frame data.
Everything below is an empty spec cell in the comparison table.

| Missing | Tiers affected |
|---|---|
| Motor count and type | all four |
| Lift speed (mm/s) | Naturalist, Smooth Operator, Perfectionist |
| Noise level (dB) | Naturalist, Smooth Operator, Perfectionist |
| Duty cycle | all four |
| Load capacity | Naturalist, Smooth Operator, Perfectionist |
| Desktop size options | all four |
| Edge detail | all four |
| Full decor/colour names | Naturalist, Smooth Operator, Perfectionist |
| Frame warranty term (desktop is 10yr) | all four |
| Returns policy | site-wide |

**Conflict to resolve — BLOCKING for the spec table:**
Width adjustment is stated as **1200–2000mm** on the Perfectionist page but **1100–1900mm**
in the installation guide title. Height appears to be **580–1230mm**. Almost certainly two
frame sizes, but this must be confirmed rather than guessed.

**Confirm:** is the Perfectionist SKU code **Active_04**? Active_01/02/03 are confirmed from
indexed page titles; 04 is inferred.

### A3. Missing copy — PLACEHOLDER
- The **seven body paragraphs** under the benefit blocks on the business page. Not recovered
  from the live site; either James supplies them or they need writing from scratch.
- Two homepage paragraphs are **truncated mid-sentence on the live site** ("…hello to peak"
  and "…boosting overall"). The endings do not exist anywhere — James must complete them.
- Exact **penalty-clause wording** for the 21-day delivery-and-install guarantee. The offer
  is verified; the mechanism (free desks per three-day delay) is second-hand.

### A4. Trust and proof — PLACEHOLDER
All four testimonials are verbatim and usable now, but attribution is thin — only Derek
Knowles has a role, none have a company, none have a photo.
- Company names for Will Lewis, Phil Thompson, Cameron Watson
- Company logos (permission to display)
- Headshots
- Any named installations that can be referenced publicly
- Stockist list — they recruit dealers but list none

### A5. Legal and company details — required for the footer
The current site has **no footer at all**, so none of this is published anywhere.
Confirmed from Companies House and safe to publish: company no. **13461733**, registered
office **Penny Lane Business Centre, 374 Smithdown Road, Liverpool, L15 5AN**.
Still needed from James:
- VAT number (if registered)
- Public contact email and phone
- Whether the registered office is also the correspondence address
- Approval of the privacy policy, terms and cookie notice before they go live

---

## B. Decisions needed

| # | Decision | Owner | Notes |
|---|---|---|---|
| B1 | Publish indicative pricing ("from £…")? | James | They publish none anywhere. Even a from-price would give "Quality Meets Affordability" something to stand on. Flag, never assume. |
| B2 | Canonical host: www or non-www | James/Faisal | Both are currently indexed — a genuine duplicate-host problem. Pick one, 301 the other. |
| B3 | Form backend: Formspree, Web3Forms, or their existing Mailchimp | Faisal | Mailchimp already handles newsletter and dealer registration. |
| B4 | Fate of `offers.activedesk.co.uk` | James | Dead WordPress install, still indexed, times out. Restore or remove and de-index. |
| B5 | Build scope for the pitch (see STAGE0_PLAN.md §3) | Faisal | Full 13-page IA is a large amount of spec work for an October project. |
| B6 | 3D desk — phase two or not at all | Faisal | Current recommendation: ship the CSS raise, treat 3D as an enhancement. |

---

## C. Handle with care

- **The founder story involves a real bereavement.** Ian Hawley, stepfather, died 24 September
  2020 of severe progressive discitis. Mother Maggie. Dog Blade. The story is the brand's
  greatest asset and must never be trivialised by a design flourish.
- **The "deaf certificate" typo** sits on that page and should read "death certificate".
  Per Faisal's instruction: raise this with James **privately, by call or in person — never
  in a written defect list or a bulk email.**
- **James's personal photographs** (Steelway in Wolverhampton; walking Blade) must never be
  replaced with generated imagery. They are the emotional proof of the story.
- **Health statistics keep their attributions.** The BMJ figure (~70,000 deaths per year,
  £0.7bn NHS cost) and the Get A Move On figures (6.9m working days lost, £35bn mental health
  cost) may be used **with their sources named**. No new medical claims, ever.

---

## D. Live-site defects being fixed in the rebuild
*(Recorded so nothing is faithfully reproduced by accident.)*

| Defect | Fix |
|---|---|
| "deaf certificate" (founder story) | → "death certificate" — raise with James privately first |
| "the danger's of prolonged sitting" (About H1) | → "dangers" |
| Two truncated homepage paragraphs | Needs James — see A3 |
| Lowercase `act_ive De_sk` on business page | → `Act_ive De_sk` everywhere |
| Double-dot `..` ellipsis throughout | → proper punctuation or a single `…` |
| Mixed US/UK spelling ("Revolutionizing", "Customization", "favorably") | → UK English throughout |
| Three pages share the duplicate title "Activedesk" | → unique title per page |
| Product pages with empty/missing titles | → unique title per page |
| No meta descriptions sitewide | → unique description per page |
| Spec tables rendered as images/JS | → real HTML tables, readable by search engines and screen readers |
| No footer anywhere | → full legal footer |
| Instagram never linked | → linked in footer |

---

## E. Placeholders currently in the build

| Placeholder | Where | Replace with |
|---|---|---|
| Proposed palette tokens | `assets/css/site.css` `:root` | SicoCreative palette (A1) |
| Archivo / Instrument Sans | `:root` font tokens | SicoCreative typefaces (A1) |
| Type-set wordmark | header | Real logo master (A1) |
| CSS desk illustration | rise section | Product photography or 3D (B6) |
| Price cells | comparison table (not yet built) | B1 decision |
| Spec cells | comparison table (not yet built) | A2 figures |

---

*Last updated: Stage 0 revision, after the build kit landed.*
