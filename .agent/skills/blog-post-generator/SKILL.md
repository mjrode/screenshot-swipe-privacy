---
name: Blog Post Generator (Screenshot Swipe)
description: Interactive workflow for generating, structuring, and publishing SEO-optimized marketing blog posts for Screenshot Swipe on the static GitHub Pages site.
triggers:
  - "write a blog post"
  - "new blog post"
  - "blog-post-generator"
---

# Blog Post Generator Skill — Screenshot Swipe

Ported from the GainFrame blog-post-generator and adapted for this repo's **static-HTML GitHub Pages site**. The editorial voice rules are identical to GainFrame's; the publishing mechanics are simpler (no Next.js, no MDX, no build step).

## Site Mechanics (read before writing anything)

| Fact | Value |
|---|---|
| Base URL | `https://mjrode.github.io/screenshot-swipe-privacy` |
| Hosting | GitHub Pages, `main` branch root, no build step — push = deploy |
| Post location | `blog/[slug]/index.html` (plain HTML, full page incl. header/footer) |
| Post images | `blog/[slug]/assets/*.webp` |
| Shared styles | `styles.css` at repo root (post classes: `post-callout`, `post-quick-answer`, `post-table`, `post-inline-screenshot`, `post-caption`, `post-steps`, `post-related`, `blog-post-cta`, `post-divider`) |
| Blog index | `blog/index.html` — add a card between `<!-- BLOG_GRID:START -->` and `<!-- BLOG_GRID:END -->`, newest first (manual; there is no generator script) |
| Sitemap | `sitemap.xml` — add the new URL manually |
| Internal links | Always root-absolute with the subpath prefix: `/screenshot-swipe-privacy/blog/[slug]/` |
| App Store link | `https://apps.apple.com/us/app/screenshot-swipe-smart-notes/id6757885971` |

**The easiest way to scaffold a new post:** copy `blog/how-to-organize-screenshots-iphone/index.html` and replace the content. It contains the canonical header, footer, breadcrumbs, JSON-LD blocks, CTA (with the App Store badge SVG), and Related Articles markup.

## The Workflow

### Phase 0: Duplicate Check
1. List directories in `blog/` — each one is a published post; the directory name is the slug.
2. If the requested topic overlaps an existing slug, warn the user and ask whether to update the existing post or take a new, distinct angle.

### Phase 1: Topic & Angle Interview
1. Ask for the target SEO keyword/topic. If they don't have one, check `seo-tools/TODO_SEO.md` and suggest the highest-ROI option.
2. Ask 1-2 pointed questions to capture their raw thoughts on the topic.
3. Ask how Screenshot Swipe specifically solves this better than alternatives. Ground claims in `seo-tools/product-context.md` — never invent features.

### Phase 2: Asset Gathering

**Screenshot library:** the canonical App Store marketing screenshots live in the app repo at `/Users/michael.rode/code/project/screenshot-swipe/[version]/apple/English (en-US)/` (check for the newest version directory — currently `2.52`). Web-ready WebP conversions of the best ones are already at `assets/shot-*.webp` in this repo:

| File | Shows |
|---|---|
| `assets/shot-01.webp` | "Review" — home screen, 287 photos ready, Smart Review CTA, daily reminder pill |
| `assets/shot-02.webp` | "Remind" — reminders settings, how-it-works card, daily reminder times |
| `assets/shot-04.webp` | "Analyze" — Smart Review analyzed screenshot with AI note + tags |
| `assets/shot-05.webp` | "Enrich" — details screen, AI note on sleep-data screenshot, tag chips |

Reuse these via `/screenshot-swipe-privacy/assets/shot-XX.webp` (no per-post copy needed). Only ask the user for net-new screenshots if the article needs a screen this set doesn't cover. Convert any new source with `cwebp -quiet -q 80` — never link `.png`/`.jpg` in a post.

**Cover images** are deterministic Pillow composites (no image model):
```bash
python3 scripts/make-cover.py "Title line one|Title line two" "path/to/marketing-shot.png" /tmp/cover.png
cwebp -quiet -q 82 /tmp/cover.png -o blog/[slug]/assets/cover.webp
```
Use one of the app-repo marketing PNGs as the shot — they share the cover's `#CFF7FF` background so they blend seamlessly. Reference the cover at 3 places: `og:image` (absolute URL), BlogPosting JSON-LD `image`, and the `post-hero-image` `<img>` (relative `assets/cover.webp`). Plus the blog-index card.

#### Roundup / listicle posts — first-class treatment for EVERY entry (mandatory)

Same rule as GainFrame: when a post ranks or lists third-party apps, every entry gets:
1. **A real screenshot**, WebP, in the post's `assets/` folder. Sources in preference order: iTunes API `screenshotUrls` (`curl "https://itunes.apple.com/lookup?id=[APP_ID]&country=us"`; upsize thumbs to `.../800x0w.png`); if the API returns none (increasingly common), scrape the app's `apps.apple.com` page HTML for `mzstatic.com` screenshot URLs; else the vendor's own site assets. **View every screenshot before using it** — reject text-only marketing slides and dated device frames (home-button iPhones, 2022 simulator shots).
2. **Two links minimum:** official website in the H2, App Store listing in the platform line.
3. **Verified ratings** from the iTunes API at write time (`averageUserRating` / `userRatingCount`). Never from memory. State the pull date in the post.
4. **Disclosure line** near the top: we make Screenshot Swipe. Be honest about where competitors beat us.

Precedent: `blog/best-iphone-screenshot-cleanup-apps/index.html` (Jul 2026).

### Phase 3: Drafting & Implementation

1. Create `blog/[slug]/assets/`, generate the cover, convert any new images.
2. Copy an existing post's `index.html` as the scaffold; replace title, meta description, canonical, og tags, JSON-LD, and body.
3. Draft content per the **Writing Voice & Style** rules below.
4. Add the card to `blog/index.html` (newest first) and the URL to `sitemap.xml`.
5. Deploy: stage only the new/changed files, commit, push to `main`. GitHub Pages serves it within a couple of minutes.

## Writing Voice & Style

These are GainFrame's editorial rules verbatim — they apply here unchanged.

### Tone: Authority First, Sell Later
- Write like an objective resource that earns trust before asking for anything.
- Mention Screenshot Swipe **at most twice** in the body — once naturally in a relevant section, once in the closing CTA.
- Be honest about limitations (e.g. "it's new — five ratings vs Swipewipe's 82,000"). Credibility > conversion.
- Hedge non-obvious claims ("a typical user…", "results are inconsistent…") rather than stating absolutes.

### Structure Rules
1. **Quick Answer block (mandatory, AEO-critical):** immediately after the H1/hero, a `post-callout post-quick-answer` div with a **40–60 word** direct answer to the article's primary question. No setup sentence — just the answer. Count the words.
2. **Opening hook (mandatory):** after the Quick Answer, open with a frustration the reader has personally experienced, with specific numbers. Never a thesis statement.
3. **H2s as full questions (mandatory for guides):** every H2 is a full grammatical question with a question mark — a query a real user would type. Roundup entry H2s instead use `N. [AppName](site) — best for …`.
4. **Numbered frameworks** render in `<div class="post-steps"><ol>…` and get `HowTo` JSON-LD when the post is procedural.
5. **FAQ section (mandatory for guides):** 4–8 H3 questions before the closing, answers 40–70 words, plain `<p>` tags, mirrored in `FAQPage` JSON-LD.
6. **Actionable closing (mandatory):** end with a concrete numbered framework, followed by the CTA block.

### Paragraph & Sentence Style
- Max 3–4 sentences per paragraph. Short punchy declarations. Second-person "you."
- **BANNED: "not X, but Y" antithesis constructions** (all variants). State the positive fact directly.
- **BANNED: meta/self-referential section headers** ("The Honest Part"). Name the content concretely.
- **BANNED: emoji.** Icons are inline SVG only.
- No filler. Every sentence advances the argument, gives data, or gives advice.

### Caption contract (recurring-bug guard)
The caption inside ANY image wrapper is `<p class="post-caption">`, styled ONLY by scoped rules in `styles.css` (`.post-inline-screenshot .post-caption`, `.post-hero-image .post-caption`). Never a bare `<p>` under an image, never a new caption class. If you introduce a NEW image wrapper class, add its scoped `.post-caption` rule to `styles.css` in the same commit.

### Comparison tables
- `post-table-wrapper` + `post-table`. When Screenshot Swipe is in the table, it is **column 2** with the `brand-first` modifier (`<table class="post-table brand-first">`) so it never scrolls out of view; order remaining columns most→least relevant.
- Third-party-only tables: plain `post-table` (no highlight modifier exists to misfire — column 2 tint only applies with `brand-first`).
- Yes/no cells: text ("Yes", "No") or inline SVG — never emoji. Bold our column's text cells.

### Author & Publisher Entity (E-E-A-T anchor — DO NOT DRIFT)

Every post's `BlogPosting` JSON-LD uses exactly:

```json
"author": {"@type": "Person", "name": "Michael Rode", "url": "https://gainframe.app/about"},
"publisher": {"@type": "Organization", "name": "Screenshot Swipe", "url": "https://mjrode.github.io/screenshot-swipe-privacy/", "logo": {"@type": "ImageObject", "url": "https://mjrode.github.io/screenshot-swipe-privacy/assets/icon.webp"}}
```

- `author.url` deliberately points at **gainframe.app/about** — the existing canonical Michael Rode Person entity page (same person, cross-site signal). Never change it without also updating gain-frame's /about contract.
- Never change `publisher.name`/`url`/`logo.url` without updating every published post in the same commit.
- Every post also emits a `BreadcrumbList` (Home → Blog → Post), plus `FAQPage` when there's a FAQ and `HowTo` when there's a step framework.

## Rules & Constraints
- Never write the post in one shot without the interview (unless the user explicitly says to go autonomous).
- Images must be WebP.
- Every post ends with a `blog-post-cta` block (App Store badge button) and a `post-related` block linking 2–5 existing posts.
- Update `blog/index.html` and `sitemap.xml` in the same commit as the post.
- If the post came from `seo-tools/TODO_SEO.md`, check it off with the publish date.

## Reference Files
- `seo-tools/product-context.md` — **READ FIRST.** Verifiable product facts, differentiators, honest limitations, voice.
- `seo-tools/TODO_SEO.md` — keyword backlog.
- `blog/best-iphone-screenshot-cleanup-apps/index.html` — roundup precedent.
- `blog/how-to-organize-screenshots-iphone/index.html` — guide precedent / scaffold source.
- `styles.css` — all post component classes.
