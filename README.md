# SM-650 BGA Rework Station — Product Landing Page

A standalone, single-file HTML marketing page for the **SM-650 BGA Rework Station**.

- **Live page**: `sm-650-bga-rework-station-smart-ems-factory.html`
- **Brand**: Southern Machinery (SMThelp) — Shenzhen, China
- **Built**: 2026-09-18

## What's inside

| Feature | Detail |
|---|---|
| Languages | English, Spanish, Portuguese, French, Arabic (RTL), Russian, Chinese |
| Theme | Light / dark toggle with pre-paint anti-FOUC script |
| Videos | 6 embedded YouTube videos from the Southern Machinery channel |
| Articles | 8 process articles (Dan Koe six-step method) |
| Images | 13 product images inlined as base64 (no external dependencies) |
| Calculator | ROI payback calculator running on visitor-supplied numbers |
| SEO | JSON-LD (`@graph`: Organization, Product, FAQPage, TechArticle, BreadcrumbList), hreflang, Open Graph, Twitter Cards |
| GEO | All claims traceable to the SM-650 introduction document and BGA operation manual |
| Chat | Chatwoot widget (bottom-right) |

## Evidence discipline

Every specification, thermal figure and service commitment on the page is transcribed from:

1. `SM-650 BGA rework station introduction.pdf` — specification sheet, feature list, heating system and recorded temperature uniformity test.
2. `BGA Operation manual.pdf` — fixture setup, control interface, profile programming and the four operating modes.

Where the source does not state a value (current draw, placement tolerance in mm, throughput rate), the page says so rather than estimating.

## Build system

The `_build-sm650/` folder contains the source:

- `template.html` — markup with `data-i18n` placeholders
- `style.css` — design system (teal / deep-green + gold palette)
- `app.js` — behaviour layer (language switch, theme switch, calculator, video modal)
- `i18n/*.json` — 7 language dictionaries (English is the source of truth)
- `assets/img.json` — base64 inlined images
- `build.py` — assembles the single-file deliverable, pre-renders English for crawlers, injects JSON-LD and hreflang

Run:

```bash
cd _build-sm650
python3 build.py
```

Output: `../sm-650-bga-rework-station-smart-ems-factory.html`

## Deployment

The HTML file is self-contained (inline CSS/JS, base64 images). It can be:

- Opened directly in a browser (`file://`)
- Attached to an email
- Hosted on any static server or CDN
- Published to GitHub Pages

## Contact

- **Email**: info@smthelp.com
- **WhatsApp**: +86 136 0256 2576
- **Web**: https://www.smthelp.com
