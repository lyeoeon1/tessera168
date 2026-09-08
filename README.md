# Tessera 168 — website

Static pages served by GitHub Pages for the iPhone app **Tessera 168**
(`com.tonghung.app168`). No build step: what is in this repository is what is
served. Dark theme only, matching the app.

| Path | What it is |
|---|---|
| `index.html`, `vi/index.html` | landing and support page, English and Vietnamese |
| `privacy/`, `vi/privacy/` | the privacy policy |
| `terms/`, `vi/terms/` | the terms of use — the app's own EULA |
| `assets/` | one stylesheet, the icon, the mascot, four screenshots |

Live at <https://lyeoeon1.github.io/tessera168/>. The app and App Store Connect
point at:

- <https://lyeoeon1.github.io/tessera168/> — support URL
- <https://lyeoeon1.github.io/tessera168/privacy/> — privacy policy (`Legal.privacy`)
- <https://lyeoeon1.github.io/tessera168/terms/> — terms of use (`Legal.terms`)

Each of those has a Vietnamese twin under `/vi/`, and the app opens whichever
matches the language it is speaking.

**These files are generated from the app repository**, in `web/`, with the two
legal documents written in `docs/privacy-policy.md` and `docs/terms-of-use.md`.
Edit them there and copy the folder here, or the app and the site start telling
different stories.
