# screenshot-swipe-privacy

Marketing + privacy-policy site for **Screenshot Swipe: Smart Notes**
(iOS app, App Store id 6757885971). The app's source lives in the sibling repo
`../screenshot-swipe`.

## Site layout

Plain static HTML — **no framework, no build step.**

| Path | Purpose |
|---|---|
| `index.html` | Landing page (download buttons, features, screenshots) |
| `privacy/index.html` | Privacy policy (App Store privacy URL should point here) |
| `blog/index.html` | Blog index — cards maintained manually between `BLOG_GRID` markers |
| `blog/[slug]/index.html` | Posts (self-contained pages; copy an existing post as scaffold) |
| `blog/[slug]/assets/` | Post images (WebP only) |
| `assets/` | Shared images: app icon, favicon, marketing screenshots (`shot-*.webp`) |
| `styles.css` | Single shared stylesheet (landing + blog + legal) |
| `scripts/make-cover.py` | Deterministic Pillow blog-cover compositor |
| `seo-tools/` | `product-context.md` (product facts) + `TODO_SEO.md` (keyword backlog) |
| `.agent/skills/` | Content skills (symlinked into `.claude/skills/`) |

## Deployment

GitHub Pages serves the **root of `main`** at
`https://mjrode.github.io/screenshot-swipe-privacy/`. Push to `main` = deploy
(live within ~2 minutes). `.nojekyll` keeps Pages from running Jekyll.

Because the site lives under a subpath, ALL internal links are root-absolute
with the prefix: `/screenshot-swipe-privacy/...`. Canonical/og URLs use the full
`https://mjrode.github.io/screenshot-swipe-privacy/...` form.

## Writing blog posts

Use the `blog-post-generator` skill (`.claude/skills/blog-post-generator/SKILL.md`).
It carries the full editorial voice rules (shared with GainFrame), the JSON-LD
entity contract, and the publish checklist (post + index card + sitemap entry in
one commit).

## Constraints

- Never remove or rename `privacy/` — the App Store listing depends on it.
- Post images are WebP only; captions follow the `post-caption` contract in the skill.
- Author entity is always Michael Rode with `url: https://gainframe.app/about`.
