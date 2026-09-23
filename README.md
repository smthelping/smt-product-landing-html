# Southern Machinery - SMT Landing Pages

Single-file marketing landing pages by Southern Machinery (smthelp.com). Each page is one
self-contained `.html` with its CSS and JS inline: no build step, no dependencies. Open it in a
browser, or drop it on the web host as-is.

**13 pages in 4 product lines.**

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

### THT Auto Insertion - `tht-auto-insertion/`

| Page | File | Size | Languages |
|---|---|---|---|
| S3000 Radial Insertion Machine for Smart EMS THT PCB Assembly | `tht-auto-insertion/s3000-radial-insertion-machine-smart-ems-tht-pcb-assembly.html` | 426 KB | 7 + x-default |
| S4000 Axial Insertion Machine for Smart EMS THT PCB Assembly | `tht-auto-insertion/s4000-axial-insertion-machine-smart-ems-tht-pcb-assembly.html` | 523 KB | 7 + x-default |
| S7900 OddForm Insertion Machine Solution for Smart EMS THT PCB Assembly | `tht-auto-insertion/s7900-odd-form-insertion-machine-smart-ems-tht-pcb-assembly.html` | 627 KB | 7 + x-default |

The S3000 inserts taped radial components into through-hole boards and cuts and clinches the leads
in the same pass. Ten feeder stations as standard, fourteen optional; insertion at any angle from
0 to 360 degrees in one-degree steps; machine-vision hole correction; boards from 50 x 50 mm to
400 x 300 mm, 0.79 to 2.36 mm thick. The page prints both of the speed figures its own documents
disagree on rather than choosing one, and it carries a wear-parts section built from the published
spare parts list for the 2.5, 5.0, 7.5 and 10.0 mm standard frame. It links to the S-300B, which
prepares the components this machine inserts, and to the S4000 and the S7900, the other two
machines on the same through-hole line.

The S4000 is the axial counterpart: it inserts taped axial components - diodes, resistors and
jumper wire - at any angle on a servo rotary table, cuts and forms the leads and clinches them in
one continuous cycle. The feeder bank is modular from 5 to 60 stations, dual jumper-wire feeders
run two wire gauges without a changeover, and the software writes production data into an
MES-compatible folder. The 2024 brochure prints both a 20,000 CPH top speed and a 10,000 CPH
actual speed; the page keeps both and explains which one to plan a shift around. Seven figures
differ between the brochure and the series manual, and all seven are printed side by side in a
disclosure table with their sources named. It links to the S3000, which handles the radial half of
the same through-hole line, and to the S7900 and the S-300B alongside it.

The S7900 is the odd-form machine: connectors, relays, transformers, trimmers, bulk electrolytics,
DIP ICs and spade terminals - the parts that arrive in bowls, tubes and trays and still get placed
by hand. Two, four or six servo heads on one platform, 0.6 to 2 s per component depending on head
count and clinching, insertion at any angle from 0 to 360 degrees, and bowl, tape, tube and tray
feeders on the same base. What makes this page different from the S3000 and S4000 pages is its
starting point: a real customer through-hole BOM of 36 lines, split line by line into the 26 that
go on the odd-form head, the 9 ammo-pack axial lines that belong on an S4000 instead, and the one
crimped ground harness that stays manual. Part numbers, reference designators beyond the generic
class letters and the customer's identity are withheld, and the page says so. Three documents
describe the platform - the 2025 catalog, a precision automation presentation and a customer
solution document - and their 15 disagreements are printed side by side in a disclosure table
rather than averaged. Its gallery labels each photograph with what it actually shows, including
where a picture is of a different model in the family or of a line the S7900 runs in. The payback
worksheet takes every money figure from the visitor and states no price of its own. It links to the
S3000, the S4000 and the S-300B, the three machines that run alongside it on a through-hole line.

### PCB Handling - `board-handling/`

| Page | File | Size | Languages |
|---|---|---|---|
| ESD Tray with Grids for Smart EMS PCB Assembly | `board-handling/esd-tray-with-grids-for-smart-ems-tht-pcb-assembly.html` | 458 KB | 7 + x-default |

The tray holds panels and loose parts in 20 cells on a fluted divider grid - 457 x 289 x 45 mm
inside, cells at about 91 x 72 mm - with an anti-static EVA base pad and a cover that lets loaded
trays stack. The dividers lift out, so one tray is re-pitched for a different part by moving a
divider rather than by buying new tooling. Nine models are listed, standard range 290 x 260 to
457 x 312 mm. Six points the documents do not settle - which tray is actually being quoted,
surface resistivity against surface resistance, body construction, temperature grade, grid
construction and cell count, and which standards were tested - are printed in a disclosure table
with the source of each figure named, and the pages that state `To be confirmed` say so in their
structured data as well. The gallery labels each photograph with what it shows, including the
frames that are of other trays, racks and trolleys in the anti-static family rather than of this
part number. No price appears anywhere on the page; the payback worksheet takes every money figure
from the visitor.

**No sibling band yet.** The other pages of the anti-static handling family - the PCB basket
trolleys, the magazine racks, the separators - are not in this repository, so this page is the
first and only one in `board-handling/`. Linking to files that do not exist here would put dead
links on a page that is otherwise self-contained, so the band is left out until the family
arrives. Add it then, in the same shape as the S4000's.

## Conventions for new pages

- File by product line in a directory (`nozzle-and-gripper/` for this family), not the root.
- Host content images on `ph.smthelp.com` rather than embedding them, so a page stays well under
  1 MB. An embedded `og:image` also cannot be read by social crawlers, which require a
  fetchable URL. (A tiny inline brand-mark fallback is fine.)
- Give each page its own `localStorage` keys for language and theme. Reusing another page's keys
  makes the two pages fight over the same stored preference.
- Where two of the documents we hold disagree, print both values side by side in a disclosure
  table. Never average them, never silently pick one, and say which source each figure came from.
- Close the page with a same-family interlink band: `<section id="family">` holding one
  `class="btn btn-o"` pill per sibling machine, each carrying a `data-i18n` key. The band's row
  needs a bare `.acts{display:flex;gap:12px}` rule - the hero and CTA variants are scoped, so
  without it the pills sit flush against each other.
- Store translated strings in the dictionaries as text, not as HTML. The runtime writes them with
  `textContent`, so an `&amp;` in a value shows up on screen as the five characters `&amp;`.
- Check that the page count in this README matches the number of `.html` files before pushing.

---

Page list generated 2026-09-23 from the directory contents.
