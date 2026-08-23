# KICKOFF PROMPT — Act_ive De_sk website rebuild
*Paste everything below the line as your first message in a fresh Claude Code session. Folder setup at the bottom.*

---

## 0. WHO YOU'RE WORKING FOR

I'm **Faisal Palmes** — I run **studioPalmes**, a one-person freelance studio in Manchester: bespoke websites (built with Claude Code, deployed on Vercel), professional photography and videography, social content, Meta ads and email marketing for independent owner-run businesses. I build around a full-time job, so my sessions are early mornings and evenings: work in clear reviewable stages, never leave the repo broken between them, and flag anything that would burn hours for marginal gain so I can decide.

**This project:** rebuilding the website for **Act_ive De_sk** (activedesk.co.uk), a UK sit-stand desk brand founded by **James C Scott**. James was referred to me personally by an existing client. He wants marketing and sales help; the website is where I start. The rebuild must preserve every piece of information the current site carries while making it dramatically more engaging, credible and conversion-focused.

**My standards:** premium and bespoke, never template-looking · everything must work when the client pokes at it — test before declaring done · **never fabricate facts about a client's business** · the word "AI" appears nowhere in client-facing text, code comments or commits · private GitHub repo, auto-deploy to Vercel, preview URL only until sign-off.

## 1. READ THESE FIRST

Two files in this repo are the brief. Read both fully before writing any code:

1. **`SITE_AUDIT_AND_COPY_BANK.md`** — a full three-agent crawl of the existing site: page inventory, critical defects (including legal compliance gaps), the complete verbatim copy bank, the full spec inventory, and what could not be recovered. This is the **content source of truth**.
2. **`BRAND_MOTION_AND_UX_SPEC.md`** — the brand system (the underscore device), the motion spec including the signature scroll mechanic, competitor benchmarks with specific ideas to steal, proposed page architecture, the homepage act structure, and technical requirements. This is the **design source of truth**.

If `NEW_CLIENT_WEBSITE_PROMPT.md` is also present, it's my house build system — its standards apply wherever these two files don't override them.

## 2. THE HEADLINE BRIEF

Build a **premium, scroll-driven website** for Act_ive De_sk: heavy scroll animation and reveals, a signature mechanic where **the desk rises from sitting to standing height as the user scrolls, with the animated underscores in the `Act_ive De_sk` wordmark rising in sync** (the underscores represent desk legs — this is the brand's own device and tying it to scroll is the idea that makes the site). Fully responsive, engaging, educational, genuinely premium.

Non-negotiable outcomes:
- Every piece of information from the current site is preserved (see the copy bank)
- The critical defects are fixed: **no footer exists on the current site at all** — no company number, no privacy policy, no terms, no cookie notice (UK Companies Act and UK GDPR/PECR gaps), plus duplicate/missing title tags, no meta descriptions, spec tables invisible to search engines, and several live copy typos
- An **interactive finish selector** — they claim "Over 40 Standard Finishes" and currently show none; this is their most wasted asset
- Clear audience routing: business buyers, specifiers/architects, and dealers are currently all funnelled into one flat structure

## 3. HOW TO WORK

**Stage 0 — plan, then stop for my approval.** Fetch the live site for brand reference (bare domain `https://activedesk.co.uk` — the `www.` subdomain fails robots checks, and the origin is genuinely unstable so retry patiently and sequentially). Then present: proposed colour tokens and font pairing with reasoning (flagging clearly what you sampled vs what you're proposing, since the real palette needs to come from the client), the page list, the homepage act map, the motion inventory, whether you recommend 3D or a lighter approach for the desk raise, and the schema plan. **Wait for my go.**

**Then build in stages**, verifying as you go — console clean, no horizontal overflow at 375px, sections legible. One extra mandatory checkpoint: **once the scroll-scrub desk raise works end to end, stop and show me before building anything else.** It's the make-or-break moment of the site and I want to approve the feel.

**Maintain `SWAP_LIST.md`** throughout: every placeholder, every unverified spec, every piece of content I need to get from James. That file becomes my client questionnaire.

**Finish with:** full QA (accessibility, performance, reduced-motion, forms, schema validation, redirect map from the old WordPress URLs), `node --check` on the script, and the Vercel deploy steps.

## 4. HARD RULES

- **Never invent facts** — no prices (they publish none anywhere), no specs beyond those in the copy bank, no new health claims, no testimonials beyond the four verbatim ones. Gaps become labelled placeholders in SWAP_LIST.md.
- **Health statistics keep their attributions.** The BMJ and "Get A Move On" figures may be used *with sources named*. Add nothing medical.
- **The founder story involves a real bereavement.** James's stepfather, Ian Hawley, died on 24 September 2020. Fix the "deaf certificate" typo (it should read "death certificate"), preserve the rest faithfully, and never let design flourishes trivialise it. His personal photographs must never be replaced with generated imagery.
- **Fix the live site's copy defects** rather than reproducing them — full list in the audit file.
- **Motion discipline:** one signature moment per page, everything respects `prefers-reduced-motion`, no scroll-jacking, the site must be complete and handsome with animation disabled, mobile motion reduced aggressively.
- UK English throughout. Brand always styled `Act_ive De_sk`.

Begin with Stage 0.

---

## SETUP (before opening Claude Code)

```
mkdir activedesk-site && cd activedesk-site
# copy in: SITE_AUDIT_AND_COPY_BANK.md, BRAND_MOTION_AND_UX_SPEC.md, KICKOFF_PROMPT.md
# and NEW_CLIENT_WEBSITE_PROMPT.md if you're using the house system
git init
printf "node_modules/\n.DS_Store\n.claude/settings.local.json\n" > .gitignore
git add . && git commit -m "Project brief"
# create a PRIVATE GitHub repo, push, connect to Vercel for auto-deploy on main
```

Then paste everything above the SETUP line as your first message.
