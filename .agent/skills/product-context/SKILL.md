---
name: Product Context (Screenshot Swipe)
description: Refresh the SEO/content-focused product context snapshot at seo-tools/product-context.md. Single source of truth for what Screenshot Swipe IS, who it's for, differentiators, and honest limitations. All content skills (blog-post-generator, future comparison/keyword skills) reference that file.
triggers:
  - "product context"
  - "update product context"
  - "refresh product context"
  - "/product-context"
---

# Product Context Skill — Screenshot Swipe

Adapted from the GainFrame product-context skill. Maintains `seo-tools/product-context.md`
as the **stable** product snapshot content skills load on every run.

**Goes in the file:** tagline, elevator pitch, category/platform, verifiable features,
pricing tiers, differentiators, honest limitations, competitor set, brand voice rules.

**Does NOT go in the file:** ratings/review counts to quote in posts (always re-pull from
the iTunes API at write time), revenue/MRR, week-by-week plans.

## Sources, in priority order

| Priority | Source | Used for |
|---|---|---|
| 1 | `../screenshot-swipe/METADATA_v3.0.md` (or newer `METADATA_v*.md`) | Live App Store copy: title, subtitle, keywords, description |
| 2 | iTunes API: `curl "https://itunes.apple.com/lookup?id=6757885971&country=us"` | Version, price, rating snapshot, live description |
| 3 | `../screenshot-swipe/AGENT_CONTEXT.md` + `PRIVACY_POLICY.md` | Architecture facts, privacy claims |
| 4 | `privacy/index.html` in this repo | Published privacy commitments (load-bearing for content claims) |

## Workflow

1. Read the sources above; diff against the current `seo-tools/product-context.md`.
2. Update changed facts. Convert relative claims to verifiable ones. Never invent features.
3. Stamp the "Last refreshed" date at the top of the file.
4. Flag to the user anything that changed in a way that invalidates published posts
   (pricing changes, removed features, new privacy behavior).

## Refresh triggers

- A new app version ships with feature or pricing changes.
- Before writing any comparison post (competitor facts drift).
- Any time a content skill catches the file contradicting the live listing.
