# SWAP_LIST — Act_ive De_sk rebuild

Every placeholder, unverified figure and piece of content needed from the client.
Doubles as the client questionnaire.

---

## RESOLVED by the four product brochures (23 Aug)

The brochures closed most of the old spec gaps. Now published on the site as fact:

- **Full frame specification**, identical across all four desks: height 580–1230mm, width
  adjustment 1200–2000mm, arm length 585mm, dual motor electric, 38mm/s, &lt;50dB, 125kg load,
  anti-collision, 10,000 cycles at full rated load, steel powder-coated, white and black,
  AC 100–240V 50/60Hz 450VA in / 23V 13A out, BS EN 527-1, **10-year warranty**.
- **The width vs height conflict is settled**: 580–1230mm is height, 1200–2000mm is width.
- **Rated life** is 10,000 cycles and a 10-year warranty (the "7 years" in the earlier audit
  does not appear in any brochure).
- **SKU codes are A_1, A_2, A_3, A_4** — not Active_01–04 as the old page titles suggested.
  The site now uses the brochure codes. *Confirm which James wants used publicly.*
- **All four decor lists**, verbatim: Expressive 10, Naturalist 10, Smooth Operator 10,
  Perfectionist 8.
- **Desktop constructions** per tier, and the features/benefits lists.
- **Controller**: digital height display, stand-up reminder, 3 programmable presets,
  anti-collision. Lifting columns from one of the world's top three manufacturers.

Two brochure typos were corrected on the site: "FEILD GREY" → Field Grey, "GRANIT GREY" →
Granite Grey, "NABRASKA OAK" → Nebraska Oak. **Confirm these are typos and not the supplier's
actual decor names.**

## Imagery now in the build

28 images extracted from the brochures and the Naturalist gallery: lifestyle photography for
all four desks, frame renders (single white, back-to-back black), controller close-ups, the
decor grids, and six gallery shots. All optimised, 2.4MB total.

---

## STILL NEEDED — priority order

### 1. Client logos and stories — BLOCKING the trust sections
The homepage carries a "Specified and installed for" logo marquee and the Stories page carries
a client grid. Only **OBI** is real; everything else is a visible placeholder.
- Logo files (SVG or high-resolution PNG) plus permission to display each
- The client list — who else has bought or worked with Act_ive De_sk
- For each story: the brief, what was specified, quantities, the outcome, and a signed-off quote
- Installation photography

### 2. The OBI story
`/stories/obi` is built and laid out, with the narrative marked as to-be-written. It needs the
brief, the specification, the result and a client quote.

### 3. Testimonial attribution
All four testimonials are verbatim and live. Still missing: company names for Will Lewis, Phil
Thompson and Cameron Watson; company logos; headshots.

### 4. Brand assets from SicoCreative
The site is monochrome per the client's brand. Still worth requesting:
- The logo master (SVG) — the wordmark is currently set in type
- Confirmed typefaces (currently Archivo / Instrument Sans as stand-ins)
- The logo animation reference, to match the underscore timing exactly

### 5. Commercial and legal
- Public contact email — `hello@activedesk.co.uk` is assumed and must be confirmed
- Phone number
- VAT number
- Exact penalty-clause wording for the 21-day guarantee
- Returns policy
- Approval of the privacy, terms and cookie wording before launch
- Decision: publish indicative pricing?

### 6. Remaining content
- The seven body paragraphs from the old business page
- Sustainability: the recycling programme detail, and any certification that can be evidenced
- More product photography for The Expressive, Smooth Operator and Perfectionist galleries

---

## Decisions for Faisal

| # | Decision | Notes |
|---|---|---|
| D1 | Canonical host: www or non-www | Both indexed today — a real duplicate-host problem |
| D2 | Form backend | Formspree, Web3Forms or their Mailchimp. Currently mail-to with a marked provider insertion point |
| D3 | Fate of `offers.activedesk.co.uk` | Dead install, still indexed, times out |
| D4 | SKU convention: A_1 or Active_01 | Brochures say A_1; old page titles said Active_01 |

---

## Handle with care

- **The founder story records a real bereavement.** Ian Hawley, died 24 September 2020, severe
  progressive discitis. Mother Maggie. Dog Blade. Preserved faithfully at `/story`.
- **The "deaf certificate" typo** is corrected to "death certificate" on the rebuild. Raise it
  with James **privately, by call or in person — never in a written defect list.**
- **James's personal photographs** (Steelway, Wolverhampton; walking Blade) must never be
  replaced with generated imagery. Both slots are marked awaiting his originals.
- **Health statistics keep their attributions.** The BMJ and Get A Move On figures appear with
  their sources named. No new medical claims.

---

## Live-site defects fixed in the rebuild

| Defect | Fix |
|---|---|
| "deaf certificate" | → "death certificate" |
| "the danger's of prolonged sitting" | → "dangers" |
| Lowercase `act_ive De_sk` | → `Act_ive De_sk` throughout |
| Double-dot `..` ellipsis | → proper punctuation |
| Mixed US/UK spelling | → UK English throughout |
| Duplicate "Activedesk" titles on three pages | → unique title per page |
| No meta descriptions | → unique description per page |
| Spec tables as images/JS | → real HTML tables, readable by search engines and screen readers |
| No footer anywhere | → full legal footer, company number and registered office |
| Instagram never linked | → linked in the footer |
| No prices, no comparison | → comparison table with price on enquiry |

---

*Last updated: full rebuild, 23 Aug.*
