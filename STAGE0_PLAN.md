# STAGE 0 — Revised plan (after the build kit landed)

Supersedes the first Stage 0, which was written from the short brief alone.
Source of truth is now `build-kit/` — the audit/copy bank (content) and the brand/motion
spec (design). **Awaiting Faisal's approval before build begins.**

---

## 1. What changed from my first Stage 0

| First pass | Corrected |
|---|---|
| Two testimonials exist | **Four** exist, all verbatim and usable |
| Tier materials partially known | Full canonical set: Active_01 25mm MFC colour · Active_02 25mm MFC wood · Active_03 19mm Perfect Sense matt · Active_04 6mm solid surface on 18mm ply |
| Founder story unknown, placeholder only | Full text recovered; a real bereavement, handled per SWAP_LIST §C |
| No health claims permitted at all | BMJ and Get A Move On figures permitted **with attributions named** |
| Recommended parametric Three.js | **Reversed — see §4** |
| 7-act homepage | **13 acts**, per the brand/motion spec |
| Signature = desk rises | Signature = desk rises **and the wordmark underscores rise in sync** |
| 4 pages | 13 routes + redirect map from the old WordPress URLs |

Two things I got right and am keeping: the underscore as a full design system rather than a
logo quirk, and the warm-ground palette direction.

---

## 2. Palette and type — provenance, stated honestly

The brand/motion spec is explicit: **do not invent a palette**, and at Stage 0 present what
was sampled versus what is proposed.

**Nothing was sampled. Everything below is proposed.** activedesk.co.uk is blocked by this
build environment's network policy (as are web.archive.org and SicoCreative's case study), so
no CSS access was possible. The audit's own crawl reached the same conclusion independently —
no hex codes or font names were extractable there either.

So the palette in `assets/css/site.css` is a considered proposal, not a derivation. It is one
`:root` block and re-tokening it costs minutes. The real route is SWAP_LIST §A1: James asks
SicoCreative for the brand guidelines.

| Token | Value | Rationale |
|---|---|---|
| `--paper` | `#F5F1EA` | Warm bone rather than cold white — flatters wood decors, reads premium |
| `--ink` | `#17150F` | Warm charcoal, softer against the warm ground than pure black |
| `--accent` | `#E8541D` | One confident accent doing all conversion work |
| `--wood` / `--steel` | `#B08954` / `#6F6E6A` | Material reference for the desk illustration |

Type: **Archivo** display / **Instrument Sans** body — both proposed, both placeholders for
whatever SicoCreative specified.

---

## 3. Scope recommendation — the one thing I want a decision on

The brand/motion spec asks for 13 routes. That is a full commercial build, and the status note
says this is spec work, that Arman's 5–6 September shoot has priority, and that James is an
October project.

**Recommendation: build the pitch, not the site.** Three things win the engagement:

1. **The homepage scroll narrative** — all 13 acts, complete. This is the demonstration.
2. **The interactive finish selector** — their most wasted asset. The Expressive's ten decors
   are known by name, so it can be built for real today with the other tiers as labelled slots.
3. **The legal footer plus /privacy, /terms, /cookies** — cheap to build, and it turns the most
   serious audit finding into something already solved rather than merely reported.

Defer the eleven inner pages until the engagement is signed. They are largely a content
exercise blocked on SWAP_LIST §A2–A4 anyway — building empty spec tables now is spec work that
cannot be finished.

Alternative if you want more surface area: add `/desks` only, since the four-tier comparison is
the second-strongest visual argument.

---

## 4. 3D versus CSS — I am reversing my recommendation

My first Stage 0 recommended a parametric Three.js desk. The brand/motion spec's decision rule
is the opposite: if a well-lit CSS version of the raise is convincing, ship that and treat 3D
as phase two.

**The spec is right, and I now have direct evidence.** The CSS desk currently on the preview
URL — telescoping legs, floor line, shadow that tightens as it stands — already reads as a
real desk raising. It cost a fraction of the effort, carries no library weight against the
600KB budget, has no capability-gate risk, and cannot fail on a low-end phone.

**Recommendation: ship the CSS raise. Revisit 3D only once real product photography exists**,
at which point an image sequence from actual desk photographs would beat both options — and
that is a photography sale for you rather than modelling work.

---

## 5. Signature mechanic — the spec

The homepage's one signature moment.

- GSAP ScrollTrigger, hero pinned, `scrub` bound to scroll position
- Desk travels seated → standing; **the two wordmark underscores rise in sync**, driven by the
  same progress value, so the logo becomes the interface
- Eased and weighted — a desk has mass; never a slider feel
- Copy stages through sit → transition → stand alongside
- On completion the underscores settle back into their idle alternating loop
- Mobile: no pin, no scrub — a lighter reveal, per motion discipline
- `prefers-reduced-motion`: desk shown standing, copy shown in full, no scrub

Idle loop note: the real logo animates the underscores alternately and continuously — one
rising as the other falls. That is implemented on the preview URL now, so the device is live
even before the scroll mechanic is built.

---

## 6. Motion inventory

Pinned scroll-scrub raise (the signature) · staggered reveals (~30px, ~0.85s, small stagger,
no bounce) · scroll-progress bar in the accent · condensing sticky nav with active-section
highlighting · subtle parallax on full-bleed imagery (10–15% max) · horizontal pinned finish
swatches · count-ups on the credentials · line-by-line mask reveals on major headlines ·
sticky tier cards · magnetic buttons on desktop only.

Discipline: one signature moment per page, everything reduced-motion aware, no scroll-jacking,
mobile reduced aggressively, and the site complete and handsome with motion disabled.

---

## 7. Page architecture and redirects

Per the brand/motion spec. Redirect map from the indexed WordPress URLs:

| Old | New |
|---|---|
| `/sit-stand-desk-for-business/` | `/for-business` |
| `/sit-stand-desk-architects-designers/` | `/for-specifiers` |
| `/the-expressive-sit-stand-desk/` | `/desks/the-expressive` |
| `/the-naturalist-sit-stand-desk/` | `/desks/the-naturalist` |
| `/the-smooth-operator-sit-stand-desk/` | `/desks/the-smooth-operator` |
| `/the-perfectionist-sit-stand-desk/` | `/desks/the-perfectionist` |
| `/founder-story/` | `/story` |
| `/about-us/` | `/about` |
| `/dealer-registration/` | `/dealers` |
| `/contact-us/` | `/contact` |

Implemented as 301s in `vercel.json`.

---

## 8. Schema plan

- `Organization` — legal name ACTIVEDESK LIMITED, company number 13461733, registered office,
  founder James C Scott, `sameAs` Instagram and LinkedIn, founding date 17 June 2021
- `Product` per tier — name, SKU (Active_01–04), material, brand, `hasMerchantReturnPolicy`
  omitted until the returns policy exists
- **No `aggregateRating`, no `offers` with prices** — none are published and none will be invented
- `BreadcrumbList` on inner pages · `Article` on the founder story with the real publication
  date (13 January 2024) and `By_ James C Scott` as author

Brand renders as `Act_ive De_sk` in all brand-voice contexts; plain "Active Desk" only in
schema and meta where the styling would confuse parsers.

---

## 9. Forms and analytics

Forms wired to a real provider before ship — never a dead form. Honeypot, visible success and
failure states, phone fallback. Provider is decision B3.

Cookieless Plausible placeholder plus one clearly-marked Meta Pixel insertion point. Events:
`dealer_enquiry`, `trial_request`, `sample_request`, `finish_selected`, `tier_view`, `call_tap`.

---

## 10. What I need to proceed

1. **Approve or redirect the scope recommendation in §3** — this is the decision that shapes
   everything else.
2. **Approve the reversal in §4** (CSS raise, 3D deferred).
3. **Approve the proposed palette as a working placeholder**, understanding it is proposed and
   not sampled, while the SicoCreative request goes out.

Everything else in SWAP_LIST can arrive during the build without blocking it.
