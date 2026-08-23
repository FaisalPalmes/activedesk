# Stage 0 — Brand reference & build decisions (Active Desk demo)

Status: awaiting Faisal's approval before any build work begins.

## 1. Verified facts (the ONLY facts the site may present as real)

Sourced from the kickoff brief (Faisal's own site review) and from search-engine-indexed
pages of activedesk.co.uk gathered on 2026-08-23. Direct fetching of activedesk.co.uk is
blocked by this build environment's network policy, so items marked ⚠ still need
confirmation or supplied content.

### Brand identity
- Trading name stylised **"Act_ive De_sk®"** (underscore styling confirmed in the site's
  own page titles and their LinkedIn company page). The underscores are a genuine brand
  asset — proposed as a recurring design motif (see Stage 0 presentation).
- Site title tagline: "Best Quality Affordable Sit Stand Desk".
- Health-led line: "Work Smarter. Be Healthier. Live Happier."
- About-page framing: helping reduce the dangers of prolonged sitting.
- Instagram: @activedesk.co.uk. Company: ACTIVEDESK LIMITED, Companies House no. 13461733.
- A founder-story page exists at activedesk.co.uk/founder-story/ (founder: James).
  ⚠ Narrative text not retrievable — placeholder slots only.

### Product tiers (naming convention "Active_0N" + character name)
| # | Name | Level | Verified material facts |
|---|------|-------|------------------------|
| Active_01 | The Expressive | Entry | Hardwearing laminate desktop; 11 standard colours; "for those creative people who love to… express their beautiful colourful self" |
| Active_02 | The Naturalist | Mid | Woodgrain reproduction laminates / decorative faced boards; woodgrains chosen for authentic character and colour grain; English-countryside framing |
| Active_03 | The Smooth Operator | High | Electric sit-stand; "for those cool cats and smooth criminals"; ultra-smooth touch desktops |
| Active_04 | The Perfectionist | Premium | 6mm solid surface bonded onto 18mm plywood; "for those who strive for perfection" |

- All desks are electric sit-stand. No prices published anywhere — enquiry-led.
- B2B: dealer registration page exists (activedesk.co.uk/dealer-registration/) plus a
  sit-stand-desk-for-business page.
- Newsletter email capture exists on the current site.
- Two short testimonials exist on the current site from **Phil Thompson** and **Will Lewis**.
  ⚠ Quote text not retrievable from here — must be pasted verbatim by Faisal, or the slots
  ship as labelled placeholders with the real names withheld until quotes are confirmed.

### Explicitly NOT facts (do not use)
- activedesk.co (dot-co, "ActiveDesk", treadmill-desk journey story) is a DIFFERENT,
  unrelated company. Nothing from it may appear in this build.
- No prices, motor specs, weight capacities, speeds, warranty terms, delivery times,
  health statistics, review counts or ratings exist in verified form. All such slots are
  styled placeholders tracked in SWAP_LIST.md.

## 2. Environment constraints noted during Stage 0
- Network egress in this build environment blocks activedesk.co.uk, web.archive.org,
  sicocreative.com (their brand agency's case study) and most other domains; web search
  works. Consequences:
  - Exact brand hex colours / logo file / fonts could not be sampled from their CSS.
    The demo palette below is proposed on its own merits per the brief's "modern-premium
    flavour" direction, and is trivially re-tokened later (single `:root` block).
  - CC0 model marketplaces (Poly Haven, Sketchfab) are not fetchable from here — one more
    reason the parametric 3D desk build is the right call.
- NEW_CLIENT_WEBSITE_PROMPT.md was not present in the repo at kickoff. The §4/§57 standards
  enumerated inside the kickoff brief are applied directly; drop the master prompt file in
  if any §5–§10 detail should differ.

## 3. Proposed design tokens (pending approval)
- Ground: warm near-neutral `--paper: #F5F1EA`, elevated cards `#FCFAF6`
- Ink: deep warm charcoal `--ink: #17150F`
- Accent (provisional until brand check): confident signal orange `--accent: #E8541D`,
  hover-deep `#C43F10`
- Support: muted stone `#8A8577` for secondary text (AA on paper at large sizes only;
  body secondary uses `#5D594E`)
- Wood tone for 3D material: `#B08954` range
- Fonts (Google Fonts, subset, two families): Display **Archivo** (SemiCondensed→Expanded
  variable axis, 600–800 tight-tracked) · Body **Instrument Sans** (400/500/600)

## 4. 3D approach decision
Parametric desk built from Three.js primitives (two telescoping three-stage leg columns,
crossbar frame, desktop slab with wood-tone PBR material), soft studio lighting
(key + fill + rim), sRGB-managed, neutral backdrop inheriting page palette. Chosen over a
downloaded GLB because: telescoping legs need separately rigged segments (downloaded desk
models are almost always single meshes), zero licence risk, tiny payload (~no model file
at all), and materials can be tokened to the palette. Recorded in SWAP_LIST.md that the
client's real desk can later be photographed/scanned to replace it.

## 5. Fallback ladder (summary)
1. Full experience: desktop, WebGL, motion allowed → 3D hero + pinned scrubbed Rise.
2. Mobile: hero 3D small-canvas only if butter-smooth at 375px, else CSS/SVG rise
   sequence; Rise section uses the SVG sequence on mobile by default.
3. No WebGL / low-end signals / prefers-reduced-motion → static poster frame images,
   scrub replaced by simple fades; page fully complete without the 3D layer.
