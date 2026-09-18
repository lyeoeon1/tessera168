# Ioniclabs — the studio site and the app sites

A static site, no build step. One stylesheet, one folder per page.

| Path | What it is |
|---|---|
| `index.html`, `vi/index.html` | the Ioniclabs studio page — every app in the lab, one card each |
| `apps/tessera168/`, `vi/apps/tessera168/` | Tessera 168's own site, the only shipped app |
| `tessera168/` | the short link `ioniclabs.app/tessera168` — forwards to the English app page |
| `CNAME` | the custom domain, `ioniclabs.app` |
| `share/`, `vi/share/` | the promotion: a free year of Pro for a post with 100 likes — the web half of `ShareForProView` in the app |
| `apps/coda/`, `apps/ferry/`, `apps/kiln/` (and their `vi/` twins) | the three apps that have not shipped; generated, see below |
| `privacy/`, `vi/privacy/` | the privacy policy — the HTML twins of `../docs/privacy-policy.md` |
| `terms/`, `vi/terms/` | the terms of use — the HTML twins of `../docs/terms-of-use.md` |
| `assets/site.css` | every rule for every page |
| `assets/shots/` | Tessera screenshots, dark mode, resized to 900 px tall |
| `assets/apps/*.svg`, `assets/ioniclabs.svg` | the icons the studio page needs |
| `tools/make_soon.py` | writes the six "coming soon" pages from one template |

The two legal pages are the app's own documents, not Apple's: `Legal.privacy`
and `Legal.terms` in `Lang.swift` point here, and the App Store description
links here. Edit a markdown source in `../docs/` and its two HTML pages in the
same commit, or the app and the site start telling different stories. Their
URLs — `/privacy/`, `/terms/` and the `/vi/` twins — are baked into a shipped
binary, so they must not move.

## The two layouts

The studio page follows sotalabs.io: wordmark in the middle of the header, one
huge uppercase sentence with yellow blocks struck through it, and app cards
that deliberately do not line up. The app pages follow capwords.app: a nav
that floats as a pill, one centred column, and a display serif (Fraunces) with
one italic phrase in the accent colour carrying each section.

Both are dark, because the screenshots are dark and a cream page around a black
phone reads as a mistake. Everything else — colours, Lexend for the body — is
the app's own theme, so the site and the phones on it are lit the same way.

## The apps that do not exist yet

Coda, Ferry and Kiln are placeholders: three plausible apps for this lab, each
marked **Coming soon**, so the studio page has a shelf instead of a single
card. Their pages are generated:

```bash
python3 tools/make_soon.py     # rewrites apps/{coda,ferry,kiln}/ and vi/apps/…
```

Edit the copy in `tools/make_soon.py` and re-run it. When one of them becomes
real, write it a hand-made page like Tessera's and delete it from `APPS`.

## Looking at it

```bash
python3 -m http.server 8899   # then open http://localhost:8899/
```

## Publishing

Every link is relative, so the site works from any sub-path. The contents of
this folder are published by the `lyeoeon1/tessera168` repo (GitHub Pages,
`main`, root) under the custom domain **`https://ioniclabs.app/`** — `CNAME`
here carries the name, and the domain's DNS lives in Cloudflare (four A records
to GitHub, grey cloud, never proxied, or the HTTPS certificate cannot renew).

The old address `https://lyeoeon1.github.io/tessera168/…` redirects to the same
path on `ioniclabs.app`. Build 10 has that old address baked in, so the redirect
must keep working: never delete the `tessera168` repo or rename it, and never
remove the custom domain without putting the old paths back.

`tessera168/` is the short link for bios and captions —
`ioniclabs.app/tessera168` — and forwards to the English app page. The site
opens in English from every entry point; Vietnamese is one tap away in the nav.

## The promotion pages

`share/` and `vi/share/` say exactly what the app's own offer screen says —
four steps, a caption to copy, and the small print as seven questions. The app
links here (`Social.promo`), so if the offer changes, both pages and
`Lang.swift` change in the same commit, the way the legal pages do.

The four handles on those pages — `@tessera168` on Instagram, TikTok, X and
Threads — are also written into the app. Instagram and Threads were registered
2026-09-19; TikTok and X follow. Keep the promotion off the live site and
`Social.offerLive` false until all four resolve. See
`../docs/marketing/social-kit.md`.

## Before 1.0 goes live

- The Tessera hero says "Coming to the App Store". Once the app is approved,
  swap that line for an App Store badge and link, in both languages, and swap
  the nav's "Get the app" mailto for the store link.
- The terms name us as "the individual named as the seller on the App's App
  Store product page", because that name is not written down anywhere in this
  repository. If you would rather state it outright, put your legal name (and,
  for EU consumer law, a postal address) in section 1 of `docs/terms-of-use.md`
  and both `terms/` pages.
- The terms assume Vietnamese governing law (section 16) and that Pro's free
  tier stays free (section 6). Both are promises — read them before publishing.
- These are the terms of a careful developer, not of a lawyer. For a paid app
  in many jurisdictions that is normal; if the app ever grows accounts, a
  server, or user-to-user content, have them reviewed.
