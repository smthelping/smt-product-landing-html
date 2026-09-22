# Southern Machinery - SMT Landing Pages

Single-file marketing landing pages by Southern Machinery (smthelp.com). Each page is one
self-contained `.html` with its CSS and JS inline: no build step, no dependencies. Open it in a
browser, or drop it on the web host as-is.

**9 pages in 2 product lines.**

## What every page carries

- Dark / light theme toggle, persisted in `localStorage`
- 7-language switching (en, es, pt, fr, ar with RTL, ru, zh), persisted, with a `?lang=<code>` override
- `hreflang` alternates plus `x-default`
- Chatwoot live chat, pinned bottom right
- YouTube product videos and catalogue download links
- Marketing articles written to the six-step brief (hook, diagnosis, framework, vehicle, loop, call to action)
- SEO / GEO meta, Open Graph and JSON-LD
- Evidence labels on every technical figure: `Verified material`, `Concept illustration` or `To be confirmed`
- A disclosure table wherever two of the source documents disagree, naming the source of each figure

## Pages

The nozzle family is still sitting at the repository root. The convention below says it belongs in
`nozzle-and-gripper/`; that move has not been made yet.

### Nozzle & Gripper (currently at root)

| Page | File | Size | Languages |
|---|---|---|---|
| Custom SMT Nozzle & Gripper Manufacturer | `custom-smt-nozzle-gripper-manufacturer-smart-ems-pcb-assembly.html` | 401 KB | 7 + x-default |
| JUKI SMT Pickup Nozzles | `juki-smt-pickup-nozzle-manufacturer-smart-ems-pcb-assembly.html` | 4.78 MB | 7 + x-default |
| FUJI SMT Nozzle Manufacturer | `smt-fuji-nozzle-manufacturer-smart-ems-pcb-assembly.html` | 2.60 MB | 7 + x-default |
| SMT Nozzle & Gripper Design Manufacturing for Smart EMS PCB Assembly | `smt-nozzle-gripper-design-manufacturing-smart-ems-pcb-assembly.html` | 74 KB | not yet |
| SMT Pickup Nozzle Series | `smt-nozzle-series-smart-ems-pcb-assembly.html` | 5.19 MB | 7 + x-default |
| PANASONIC SMT Nozzle Manufacturer | `smt-panasonic-nozzle-manufacturer-smart-ems-pcb-assembly.html` | 3.07 MB | 7 + x-default |
| SMT Siemens Nozzle Manufacturer for Smart EMS PCB Assembly | `smt-siemens-nozzle-manufacturer-smart-ems-pcb-assembly.html` | 2.65 MB | 7 + x-default |
| Yamaha SMT Nozzle Manufacturer | `smt-yamaha-nozzle-manufacturer-smart-ems-pcb-assembly.html` | 3.23 MB | 7 + x-default |

### Component Preparation - `materials-consumables/`

| Page | File | Size | Languages |
|---|---|---|---|
| S-300B Radial Lead Molding & Taping Machine for Smart EMS PCB Assembly | `materials-consumables/s-300b-radial-lead-molding-taping-machine-smart-ems-pcb-assembly.html` | 509 KB | 7 + x-default |

The S-300B page takes loose radial components out of a bulk bowl, forms the leads to the lead pitch
the downstream inserter is set for, checks polarity and electrical value, ejects the failures, and
delivers a sealed taped pack - boxed or reeled - at 180 +/- 20 components per minute. Its gallery
labels photographs of other machines in the radial and axial family as such rather than presenting
them as this model.

## Conventions for new pages

- File by product line in a directory (`nozzle-and-gripper/` for this family), not the root.
- Host content images on `ph.smthelp.com` rather than embedding them, so a page stays well under
  1 MB. An embedded `og:image` also cannot be read by social crawlers, which require a
  fetchable URL. (A tiny inline brand-mark fallback is fine.)
- Give each page its own `localStorage` keys for language and theme. Reusing another page's keys
  makes the two pages fight over the same stored preference.
- Where two of the documents we hold disagree, print both values side by side in a disclosure
  table. Never average them, never silently pick one, and say which source each figure came from.
- Check that the page count in this README matches the number of `.html` files before pushing.

---

Page list generated 2026-09-22 from the directory contents.
