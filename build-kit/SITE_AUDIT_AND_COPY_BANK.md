# ACT_IVE DE_SK — SITE AUDIT & VERBATIM COPY BANK
*Compiled 18 Aug 2026 from a three-agent crawl of activedesk.co.uk. This is the SOURCE OF TRUTH for the rebuild's content. Everything here was actually fetched from the live site or a cited public record. Items marked UNVERIFIED were not confirmed — never present them as fact.*

---

# PART 1 — WHAT THE CURRENT SITE IS

**Platform:** WordPress (confirmed via `/wp-content/uploads/` paths). Forms handled by **Intuit Mailchimp** — newsletter AND dealer registration.
**Company (Companies House, verified):** ACTIVEDESK LIMITED, company no. **13461733**, incorporated **17 June 2021**, status Active. Registered office: Penny Lane Business Centre, 374 Smithdown Road, Liverpool, L15 5AN. SIC 31010 (manufacture of office and shop furniture).
**Founder:** James C Scott (Founder/Creative Director).
**Brand agency:** SicoCreative (sicocreative.com/activedesk) — delivered Visual Identity, **Animations**, Signage, Business Cards, Sales Brochure, Pricing & Spec Brochures. They hold the master brand assets.
**Business model:** B2B / dealer-led lead generation. **No prices anywhere on the site. No cart, no checkout.** Conversion paths are dealer enquiry, sample requests, and a free trial desk.

## Confirmed page inventory
| URL | Status | Purpose |
|---|---|---|
| `/` | fetched | Homepage |
| `/about-us/` | fetched | Company philosophy, credentials, vision, 4 testimonials |
| `/founder-story/` | fetched | Long-form founder essay, 13 Jan 2024 |
| `/sit-stand-desk-for-business/` | fetched | B2B sales page, 7 benefit blocks, free trial offer |
| `/sit-stand-desk-architects-designers/` | fetched | Specifier/architect audience page |
| `/dealer-registration/` | fetched | Dealer signup (Mailchimp form) |
| `/the-perfectionist-sit-stand-desk/` | fetched | Premium tier product page (richest specs) |
| `/the-expressive-sit-stand-desk/` | indexed, unfetched | Active_01 entry tier |
| `/the-naturalist-sit-stand-desk/` | indexed, unfetched | Active_02 mid tier |
| `/the-smooth-operator-sit-stand-desk/` | indexed, unfetched | Active_03 high tier |
| `/contact-us/` | indexed, unfetched | Contact |
| `/wp-content/uploads/2024/08/Act_ive-De_sk-_The-Expressive-Brochure-V1.pdf` | fetched | Entry-tier spec brochure |
| `/wp-content/uploads/2024/08/active-desk-single-desk-installation-guide.pdf` | indexed, unfetched | Install guide |

**Untested (site outage prevented checking):** /faq, /delivery, /warranty, /returns, /privacy, /terms, /blog. Existence unknown.

## CRITICAL DEFECTS FOUND (the rebuild must fix all of these)

**1. ORIGIN INSTABILITY — the most serious commercial finding.**
Across ~25 minutes of testing, roughly **1 in 5 requests succeeded**. Failures were origin-level SERVER_ERROR and connection timeouts, not 404s. A site failing this often is losing real enquiries. Flag to the client immediately; it also means hosting must move (Vercel + static solves it entirely).

**2. NO FOOTER AT ALL — legal compliance gap.**
Verified across three separate pages: every page simply ends at the Mailchimp form. There is **no footer element whatsoever**. Consequences:
- No company registration number or registered office → **UK Companies Act 2006 (Trading Disclosures) requires these on a company website**
- No privacy policy, no terms, no cookie notice → **UK GDPR / PECR exposure**
- No VAT number, no phone, no address, no email, no social links, no copyright line
This is the single most urgent non-design fix.

**3. DANGLING SUBDOMAIN:** `offers.activedesk.co.uk` is a dead WordPress install, still indexed by Google, times out on connection. Security and SEO liability — restore or remove and de-index.

**4. SEO/title failures:**
- Homepage title is the only well-formed one: `Act_ive De_sk® | Best Quality Affordable Sit Stand Desk`
- `/about-us/`, `/sit-stand-desk-for-business/`, `/sit-stand-desk-architects-designers/` ALL share the generic duplicate title **"Activedesk"**
- Product pages show Google falling back to on-page body text — the signature of a **missing or empty `<title>`**
- **No meta descriptions found in any SERP snippet** — likely absent sitewide
- **www and non-www are BOTH indexed** — genuine duplicate-host problem; canonicalisation and redirects both broken

**5. Spec tables are not in the HTML text layer.** On the Perfectionist page, spec section headers (Height range, Load capacity, Motor, Speed, Noise level, Anti-collision, Duty cycle, Control box) returned **with no values attached** — the numbers are rendered as images or JS tabs. Invisible to Google and to screen readers. Spec figures must come from the client's brochures, not scraped.

**6. Copy defects on the live site — FIX, do not faithfully reproduce:**
- `"deaf certificate"` on the founder story — a typo for "death certificate", on the most emotionally important page on the site
- `"the danger's of prolonged sitting"` — stray apostrophe in the About Us H1
- Two homepage paragraphs **truncated mid-sentence**: "…hello to peak" and "…boosting overall"
- Brand name rendered lowercase `act_ive De_sk` on the business page, inconsistent with `Act_ive De_sk` elsewhere
- Heavy use of double-dots `..` as ellipsis throughout ("About Us..", "Finally..An Affordable", "We have your Back!..")
- Mixed US/UK spelling: "Revolutionizing", "Customization", "favorably" alongside "colour"

**7. Conflicting spec figures:** width adjustment stated as **1200–2000mm** on the Perfectionist page but **1100–1900mm** in the installation guide title. Likely two frame sizes. **Client must clarify.**

**8. Wasted assets:** claims "Over 40 Standard Finishes" but shows none interactively. Has an active Instagram that the website **does not link to anywhere**. Recruits dealers but lists **no stockists**.

---

# PART 2 — VERBATIM COPY BANK
*Use this to preserve their information and voice. Fix the defects noted above; keep everything else.*

## Master tagline
**Work Smarter. Be Healthier. Live Happier.**

## Homepage
**Hero:** "Complete Ergonomic Solutions For Maintaining Consistent Productivity And Efficiency While Ensuring Employee Health & Well-Being!"
**Primary CTA:** "Enquire To Become A Dealer"
**Founder teaser:** "My stepfather's chronic back pain which took his life, not cancer, was the catalyst for the seed to be born" → CTA "Read Founder Story"

**Sitting epidemic section — "Get Up Stand Up, Stand up for your life!"**
> "The impact of prolonged sitting from sedentary working conditions is having a detrimental impact on businesses and people's lives, and now becoming a silent killer. Conditions associated with prolonged sitting include cardiovascular disease, some forms of cancer, type 2 diabetes, and back, shoulder, and neck pain (MSK Conditions). Often these conditions don't catch up with people until middle to old age, and that's when it's too late, as they often turn into chronic conditions from years of unhealthy habits.
>
> Don't let this silent killer impact your business or your employees, stem the tide, and take charge of your health with Act_ive De_sk!
>
> We have your Back!"

**Static desks section — "Will Become A Thing Of The Past!"**
> "Sit Stand Desks are nothing new and there are some great furniture manufacturers with wonderful products out there. But for most businesses, they are just too expensive!
>
> Explore how the Act_ive De_sk business model was founded on creating affordable ergonomic solutions."

**Work Smarter — "Boost Employee Productivity!"**
> "Act_ive De_sk promotes movement and better posture, keeping your team energized and focused throughout the day. Say goodbye to mid-afternoon slumps and hello to peak" [TRUNCATED ON LIVE SITE — complete this sentence in the rebuild]

**Be Healthier — "Improved Employee Health!"**
> "Prolonged sitting has been linked to a host of health issues, including back pain, obesity, and cardiovascular disease. Act_ive De_sk encourages a healthier, more active lifestyle, reducing the risk of chronic conditions and boosting overall" [TRUNCATED ON LIVE SITE]
>
> "Change the bad habit of sitting all day, and say goodbye to sick days and work hours lost!"

**Live Happier — "Employee Satisfaction and Retention!"**
> "Investing in the well-being of your employees demonstrates your commitment to their success and happiness. With Act_ive De_sk, you'll create a positive work environment where your team feels valued, supported, and motivated to perform at their best with the help of their Sit Stand Desk."

**Closing CTA:** "Ready To Create a More Productive Workplace – A Healthier, Happier Team – Business Success & Growth?"

## The four tiers (VERBATIM, canonical order, with SKU codes)
- **Active_01 · The Expressive.** "Entry level desk 25mm desktop MFC colour decors" — *"A range of beautiful colour desk tops, for those people who love to express themselves."*
- **Active_02 · The Naturalist.** "Mid-level desk 25mm desktop MFC wood decors" — *"A range of beautiful wood desk tops, for those people who love natures beauty."*
- **Active_03 · The Smooth Operator.** "High-level desk 19mm desktop Perfect sense matt finish" — *"A range of ultra smooth touch desk tops, for those cool cats and smooth criminals out there."*
- **Active_04 · The Perfectionist.** "Premium-level desk 6mm solid surface bonded onto 18mm plywood" — *"A range of solid surface and real plywood desk tops, for those who strive for perfection."*
  *(Active_01/02/03 confirmed from indexed page titles; Active_04 inferred — verify with client)*

**Perfectionist page:** "The Perfectionist Desk." / "A sit stand desk for those people who strive to create perfection" / desktop described as *"a delicate composition of acrylic, minerals and natural pigments"*

## Other verbatim headlines (the brand voice — preserve this register)
- "No More Boring Desks, No More Back Breaking Static Desks."
- "Say goodbye to hefty price tags and boring desks"
- "Everyone is important and everyone deserves a desk!"
- "Finally..An Affordable Quality Sit Stand Desk With Unmatched Customization!"
- "Be A Leader In Holistic Health Design!"
- "Over 40 Standard Finishes, Design Without Boundaries!"
- "We have your Back!.."
- "Wipe Away Those Afternoon Slumps"
- "Keep Your Colours Flying!"
- "Saving Our Environment One Desk at a Time!"
- "Limited Budget, No Problem!"
- "Stay For A Lot, Lot Longer!"

## B2B page — /sit-stand-desk-for-business/
**Headline:** "Complete Ergonomic For Employee Comfort Health & Well-being!" / **Sub:** "Your Gateway to Business Success!"
**Section header:** "Why Act_ive De_sk" — opens "Are you tired of watching afternoon productivity levels plummet as your…"
**Bridge:** "Here is Why You Should Consider Purchasing Our Sit Stand Desks… ⇓"

Seven benefit blocks (heading / subhead):
1. "Enhanced Productivity." / "Wipe Away Those Afternoon Slumps."
2. "Healthier Employees." / "Health is Your Key to Success."
3. "Happier Employees." / "Stay For A Lot, Lot Longer!"
4. "Quality Meets Affordability." / "Limited Budget, No Problem!"
5. "Unmatched Customization." / "Keep Your Colours Flying!"
6. "Reuse, Reduce and Sustain." / "Saving Our Environment One Desk at a Time!"
7. "Delivery & Install." / "21 Days Delivery and Install Guaranteed!"

**Key offer:** "Claim Your FREE Trial Desk / No-Obligation To Purchase / (2 week loan period)"
**Guarantee:** "21 Days Delivery and Install Guaranteed!" — carries a **penalty clause** (free desks for every three-day delay; exact wording not recovered — get from client)
**Statistic used:** employee absence costs "an average of £237 per day"
*(The seven body paragraphs under these blocks were NOT recovered — client must supply or they need rewriting.)*

## About Us — /about-us/
**H1 (fix the apostrophe):** "We help reduce the danger's of prolonged sitting one desk at a time!"

> "We believe that every employee should have the choice to 'take charge of their health' while at work and every employer should be providing active furniture to enable this. Prolonged sitting at static desks is 'we believe' a silent killer and having detrimental effects on peoples long term health and lives. Act_ive De_sk was founded to bridge the gap between sitting and standing by providing businesses 'quality affordable' sit stand desks, that otherwise where unaffordable for 'everyone' within the office or very bland looking to say the least!"

> "Act_ive De_sk's philosophy is about providing value, but not just that providing quality and innovation too that's deeply rooted in our workplace design ethos. We are not your typical furniture or ecommerce brand who moves boxes around, we are designers at heart. We have many 'original' innovative new products coming out which we believe will revolutionize the way we work in our workplace environments."

> "We were founded in 2021, and maybe still early in our journey but our experience in our field of expertise runs deep, over 2 decades of designing award winning workplaces, over 15,000hrs space planning, specifying and designing over 15million pounds worth of furniture and under taking countless workplace strategy projects for large .com companies. We understand fully, 'how people work', and what they need to get the job done to thrive!"

**Vision:** "To see a world where all workplace environments positively uplift human welfare, while conserving the earths vitality"

> "Our clients are workplace consultants, designers, architects, furniture specifiers and business owners who are wanting innovative, cool ergonomic products at cost-effective prices. We don't just sell furniture, we also install it, design it and provide valuable information on how to best plan that furniture to maximize, businesses performance and employee health and well-being."

> "We offer free building appraisals 'how to best align your furniture layout with your building', free space planning 'maximize space efficiency and layout' and a free design service 'how best to pick your desk finishes to match your brand'."

> "We deliver our products through our dealer network and corporate clients giving them unbeatable prices, unmatched customization, short delivery and install lead times, along with workplace consultancy advise. Our products help our clients to be leaders in promoting holistic health, innovation and WELL Standards within their workplace projects. Our clients distribution helps more people to 'take charge of their health', work smarter, be healthier and live happier, longer life's."

> "We know our journey to change the UK human habit of prolonged sitting to a more vibrant, healthier, smarter and happier active standing culture is going to be long. But we will persist one desk at a time with education and a continuous love for human welfare!"

**Canonical credentials (consistent across pages — treat as fact):** founded 2021 · over 2 decades designing award-winning workplaces · over 15,000 hours space planning · over £15 million worth of furniture specified/designed · over a thousand commercial projects.

## Founder Story — /founder-story/ — THE BRAND'S GREATEST ASSET
**Title:** "A Journey Ignited by Loss and Empathy" · **Byline:** "By_ James C Scott" · **Published:** 13th Jan 2024
*(Note the `By_` underscore — the brand device extends into bylines.)*

> "In 2020, the world was struggling with the continuous challenges brought about by the COVID-19 pandemic. Lives were lost, and the vulnerability of our health became a major issue. For me, reality hit home in the most profound way possible, not the loss of business I suffered in my workplace interior design studio but the loss of my stepfather".

**"My Stepfather."**
> "Ian had been a long-distance lorry driver all his life and loved it and retired in 2017 at the ripe old age of 65! Plenty of time to enjoy his retirement I thought until a few years later in January 2019 he was diagnosed with stage 4 lung cancer. The news hit him and the whole family like a ton of bricks, we were lost for words. A couple of months after the news he had his first session of Chemotherapy and scans showed it seemed to be working and the cancer had not spread any further. Phew!"

> "2020 was a completely different story. My stepfather for years has always suffered from lower back and shoulder pain and his lower back was giving him excruciating pain before his second bout of Chemotherapy which did not seem to work! He suddenly took a turn for the worse and died at home on September 24th, 2020. It was truly devastating for us all…"

> "A few weeks later my mum received the deaf certificate and read it out to me over the phone, I was dumbstruck! To hear the real reason my stepfather died, not from his cancer as we all thought, but from 'severe progressive discitis' in his lower back caused by chronic lower back pain he had suffered with for years."
**[FIX: "deaf certificate" → "death certificate"]**

> "The long-distance lorry driving on the roads of Britain had finally caught up on him, causing him chronic back and shoulder pain and costing him his life! It wasn't a fate he could easily escape; driving was not just a job for him – it was a passion. He could not do anything about his working conditions, but his working conditions of prolonged sitting finally caught up on him. I felt such a great empathy for his loss and something inside of me started burning up with such a force that I could not let this go!"

**Image caption:** "My Stepfather's Last Company Before Retirement: Steelway in Wolverhampton"

> "Early 2021 while still contemplating the loss of my stepfather I was reading lots of articles about why so many people were getting seriously ill or dying from Covid. And the Number one reason that kept coming up was 'due to a weak immune system' and or already 'having some type of chronic pain'."

> "I started delving deeper and looking into the impact prolonged sitting has on health, and it was frightening how big the epidemic is, especially in my field of work, workplace interiors. I have over 2 decades of designing award-winning workplaces, over 15,000 hours of space planning, specifying, and designing over 15 million pounds worth of furniture, and undertaking countless workplace strategy projects for large .com companies."

> "Our workplaces are full of people who sit at their static desks all day and it's becoming a silent killer! The BMJ (British Medical Journal) states: 'Spending large amounts of time sitting or lounging around during the day is linked to around 70,000 deaths per year in the UK and the NHS spends more than £0.7bn per year treating the health consequences'. And the costs to businesses according to Get A Move On is staggering: 'An estimated 6.9 million working days are lost in the UK due to work-related musculoskeletal problems and the cost of poor mental health to UK business is estimated to be an astonishing £35bn annually'."

> "After 3 months of intense research, it was plain to see that prolonged sitting causes back, shoulder, and neck pain and it's the pain that increases cortisol levels which play an important role in balancing our stress hormones. Stress hormones can suppress or break down the immune system's function! As a result, your body will be unable to fight against infections, like viruses or bacteria, and you won't be able to achieve long-term healing. According to a study in the journal Trends in Neurosciences."

> "Voila!! Your immune system is your defense to your health and well-being!! No wonder so many older people were dying from COVID-19, your immune system deteriorates as you get older. The excruciating pain my stepfather suffered had compromised his immune system and left him unable to fight against his infection of the disc, which sadly took his life!"

> "Months later while still contemplating how many people were still dying from COVID and my stepfather's death, an impulse shot through me and woke me up at 2 am while sleeping. 'I may not be able to help people who drive for long distances but I can do something to help people in the office with their working conditions'."

> "The empathy for my stepfather's loss transformed into a burning force, and Act_ive De_sk was born. Beyond a business venture, it's a mission to combat the sedentary epidemic, especially within the realm of workplace design. My expertise in designing interiors for over a thousand commercial projects is fused with a passion for revolutionizing the way we work."

**Photo caption:** "Me out walking with my Jack Russell, Blade!"

> "Through Act_ive De_sk, I strive to break the chains of prolonged sitting, offering not just furniture but quality, affordable solutions and innovations that prioritize health and wellbeing. This journey is a tribute to my stepfather, a man whose passion became both a joy and, ultimately, a silent contributor to his demise."

> "Join me in this mission. Let's reshape workspaces, defy the sedentary norm, and build a healthier, happier future for everyone…."

**Sign-off:** "Join us to be part of the movement" · "In honor of my stepfather, a beloved Blades Fan!" · "Ian Hawley :)" · "James C Scott / Founder/Creative Director" · "MY Stepfather's favorite artist 'Rod Stewart: Song entitled 'Maggie May', dedicated to my mum, his beloved wife 'Maggie'!"

**Key names:** Stepfather **Ian Hawley** (Sheffield United "Blades" fan). Mother **Maggie**. Dog **Blade** (Jack Russell).
**Emotional architecture to preserve:** loss → investigation → mechanism → epiphany → mission → tribute. The *mechanism* step (pain → cortisol → suppressed immunity → couldn't fight the disc infection) is what makes it land rather than being mere sentiment.

## Testimonials (VERBATIM — all four, from /about-us/)
> "Excellent value, great design, speed of installation and immediate positive impact!" — **Will Lewis**
> *(homepage runs a longer variant with the hook: "We Had People Suffering With Bad Backs!")*

> "Looks And Value For Money! The end result was amazing and my entire team have commented favorably on their look, quiet movement and modern look and feel our office now has. I myself was on the fence, but I wouldn't hesitate now!" — **Derek Knowles, Operations Director**

> "We were surprised by the increased energy levels and productivity! Increased collaboration by people being on their feet more, and the cost and quality was amazing!" — **Phil Thompson**

> "Thank You For Revolutionizing Our Workplace!.. Active Desk has truly transformed our office environment! Their electric stand-up desks are not only of exceptional quality but also offered at a competitive price!" — **Cameron Watson**

**Credibility gap:** no company names, roles (except Derek Knowles) or photos on any attribution. Ask James for company names + logos + headshots — it would materially strengthen the rebuild.

## Newsletter
"Sign up" / "By clicking Sign up you are agreeing to be contacted by Act_ive De_sk." / "* indicates required" / "Intuit Mailchimp"

---

# PART 3 — SPEC INVENTORY (everything factual recovered)

## Frame (from Perfectionist page — likely shared across range)
- Configurations: "Single or Back To Back" / "Dual Or On Each Leg"
- Width Adjustment Range: **1200mm to 2000mm** *(conflicts with 1100-1900mm in install guide — CLARIFY)*
- Frame Colour: **White & Black** · Frame Finish: **Steel (powder coated)**
- Control: **Digital Display (3 preset settings + reminder)**
- Voltage Input: **AC 100-240V 50/60Hz 450VA** · Voltage Output: **23V 13A**
- CE Compliance: **BS EN 527-1**
- Life (cycles at full rated load): **7 Years**
- Height range: **1200–2000mm** (Perfectionist page) vs **580–1230mm** (install guide) — the latter is almost certainly the height, the former the width. **CLARIFY WITH CLIENT.**

## The Expressive (from brochure PDF — most complete spec set)
- 25mm MFC laminate top, white laminate balancer underside
- Steel powder-coated frame
- Height: **580–1230mm** · Width adjust: **1200–2000mm**
- Load: **125kg** · Speed: **38mm/s** · Noise: **<50dB**
- Digital display, **3 presets**, **anti-collision**
- **10-year warranty**
- Decors (10): Black, Toffee, Rose, Grey, Ice Blue, White, Cashmere, Dark Grey, Field Grey, Granite Grey
- Frame: White & Black

## The Perfectionist desktop
6mm solid surface (acrylic, minerals, natural pigments) bonded to 18mm Latvian birch plywood, clear lacquer. Durable, scratch/chip resistant, non-porous, stain and bacteria resistant, low maintenance, chemical resistant. **10-year warranty.**

## Accessories (Perfectionist page)
- **Screen system:** noise reduction/privacy, nine standard designs, customisable, 100% polyester (PET), die-cast zinc clamps, **12mm** thickness, clamp fixing, fire rating **BS EN 13501-1:2018**, pinnable surface, carbon neutral, locally made
- **Cable management:** **1050mm** cable basket (tilt feature), **1250mm** cable slinky (magnetic leg option), power bar with UK fused sockets + USB charging + data/AV
- **Desktop power modules:** UK sockets, data, HDMI, TUF-R HP, 25W USB, phone charging

## Commercial propositions (verified)
21-day delivery-and-install guarantee with penalty clause (free desks per 3-day delay) · free 2-week no-obligation trial desk · **40+ standard finishes** · WELL Building Standard alignment · free building appraisal, space planning and design consultation · sustainability/recycling programme

## NOT RECOVERED — must come from client
Motor count/type · speed and noise for tiers other than Expressive · duty cycle · desktop size options · edge detail · full colour/decor names for Naturalist, Smooth Operator, Perfectionist · returns policy · frame warranty term · the 7 body paragraphs on the B2B page · exact penalty-clause wording · **all pricing** (none published anywhere)

---

# PART 4 — IMAGERY: IMPORTANT CORRECTION

**The crawl could NOT verify any imagery.** WebFetch strips `<img>` tags — no filenames, alt text, counts or AI-generation signals were recoverable for any page. Two things follow:

1. **Do not assume the existing photos are AI-generated.** That is unverified. Two founder-story images are demonstrably personal photography: the Steelway, Wolverhampton photo (his stepfather's last employer) and "Me out walking with my Jack Russell, Blade!". **These must never be replaced with AI imagery** — they are the emotional proof of the story.
2. **Alt-text coverage is unknown** and likely a gap on a small WordPress build. The rebuild fixes this by default.

Faisal to do a manual browser pass (View Source) to inventory images, alts, nav/footer hrefs and the logo animation implementation before the build starts.
