# Southern Machinery - SMT Landing Pages

Single-file marketing landing pages by Southern Machinery (smthelp.com). Each page is one
self-contained `.html` with its CSS and JS inline: no build step, no dependencies. Open it in a
browser, or drop it on the web host as-is.

**26 product pages in 7 product lines, plus one catalogue hub that indexes them all.**

## The catalogue hub

`smt-tht-machine-catalog-hub-smart-ems-factory-southern-machinery.html` is the entry point: a
single self-contained page that classifies every product page in this repository, makes them
searchable without a server, and embeds the matching photographs, working videos and catalogue
documents.

- Client-side search across every title, description, keyword, model code and file path, with
  product-line filter chips, three sort orders and a `?q=` deep link
- Photographs from `ph.smthelp.com`, videos from the company YouTube board and documents from the
  catalogue board, interleaved so every product line has content under every filter
- Eight marketing articles written to the six-step brief, in all seven languages
- Same chrome as the product pages: dark/light toggle, 7-language switching with RTL Arabic,
  Chatwoot bottom right, `hreflang` alternates, Open Graph and JSON-LD
  (Organization, WebSite + SearchAction, ItemList, FAQPage, Blog, BreadcrumbList)

It is **generated**, not hand-edited. Change `tools/i18n_ui.py` (interface strings),
`tools/i18n_articles.py` (product lines and articles) or `tools/build_hub.py` (layout and
extraction), then rebuild:

```bash
python3 tools/build_hub.py          # rebuild the hub
python3 tools/build_hub.py --check  # exit 1 if it is out of date
python3 tools/preview.py 8080       # serve the repository, hub on /
```

`.github/workflows/refresh-hub.yml` runs the builder at **00:00 UTC every day** and on any push
that touches an `.html` file, so a new product page added to the repository joins the hub, its
product line count and its search index automatically. Pages added in the previous 45 days get a
"New" badge. Nothing is committed when the rebuild produces no change.

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
| SMT Feeder Calibration Jig for Smart EMS PCB Assembly | `materials-consumables/smt-feeder-calibration-jig-smart-ems-pcb-assembly.html` | 518 KB | 7 + x-default |
| AI Radial Splicing Tape 3/5/6-Hole & Splice Cutter | `materials-consumables/ai-radial-splicing-tape-3-5-6-hole-masking-kraft-paper-splice-cutter-southern-machinery.html` | 603 KB | 7 + x-default |
| THT Auto Insertion Radial Components Splicing Tape | `materials-consumables/tht-radial-components-splicing-tape-smart-ems-pcb-assembly.html` | 243 KB | 7 + x-default |

The AI radial splicing tape page covers the consumable that keeps a radial inserter fed through a
reel change: pre-cut 3-hole and 5-hole splices (6-hole, 2-hole and single-hole on request) in
masking or kraft paper, die-cut on both faces with locating dots, and the hand splice cutter for
12.7 mm and 15.0 mm radial tape. Four points where its sources disagree (pieces per roll, the
3-hole splice width, the hole counts offered and what the cutter size refers to) are printed side
by side. Its two tape photographs are embedded as small JPEGs because they are not yet on
ph.smthelp.com; every other image is hosted there or on smthelp.com's own image store.

The feeder calibration jig is a bench station rather than a placement machine: it mounts a feeder on
a fixture so a maintenance technician can watch feeder movement, check the pick-up position against a
monitor cross reference and confirm alignment before the feeder returns to the line. Published figures
name a 50X CCD camera, ring LED lighting and X/Y/H three-axis adjustment; the page prints them with
their source and adds an open-points section for the seven places the Southern Machinery documents do
not agree - two different monitor sizes (7 inch in the operation manual, 12 inch on a product image),
two voltage options, two orientations of the same machine dimensions, a machine weight of 45 kg
against an export packing list of net 13 kg / gross 40 kg, the feeder control zones, the model code,
and the fact that no calibration accuracy figure appears in any Southern Machinery document we hold.
The payback worksheet takes every money figure from the visitor, counts maintenance labour only, and
clamps released time at zero when the jig-assisted check would be slower than the manual one. Its
gallery draws on eleven photographs from `ph.smthelp.com` plus the annotated component view, which
is inlined because it has no equivalent on the public host. It links to the S-300B, the other page in
this band.

The S-300B page takes loose radial components out of a bulk bowl, forms the leads to the lead pitch
the downstream inserter is set for, checks polarity and electrical value, ejects the failures, and
delivers a sealed taped pack - boxed or reeled - at 180 +/- 20 components per minute. Its gallery
labels photographs of other machines in the radial and axial family as such rather than presenting
them as this model.

### Feeder & Nozzle Service Equipment - `feeders-nozzles/`

| Page | File | Size | Languages |
|---|---|---|---|
| SMT Feeder Calibration Jig for FUJI NXT Feeders (S-FFCJ10) | `feeders-nozzles/smt-feeder-calibration-jig-fuji-nxt-southern-machinery.html` | 198 KB | 7 + x-default |
| SBF1001 Vibratory Bowl Feeder for Smart EMS PCB Assembly | `feeders-nozzles/sbf1001-vibratory-bowl-feeder-odd-form-auto-insertion-smart-ems.html` | 524 KB | 7 + x-default |
| Odd-Form Feeder & Nozzle Matcher - Customized Feeder Nozzle Catalog V03 | `feeders-nozzles/odd-form-insertion-customized-feeder-nozzle-catalog-v03-component-matcher-southern-machinery.html` | 802 KB | 7 + x-default |
| S-RF1001 Radial Taped Feeder for SMT Mounters: 90° bend and L-S capacitor versions | `feeders-nozzles/s-rf1001-radial-taped-feeder-smt-mounter-tht-radial-lead-insertion-90-bend-l-s-capacitor-smart-ems-factory.html` | 599 KB | 7 + x-default |

The jig is a bench station for FUJI NXT feeders, model S-FFCJ10: mount a feeder on the fixture,
watch its movement through a 50X CCD camera with ring LED lighting, adjust X/Y/H on the sub-base and
verify the pick-up position against a monitor cross reference before the feeder returns to the line.
The Taobao listing publishes an X-axis acceptance limit of +/-0.25 mm, a 350 x 500 x 550 mm body and
a 45 kg weight, and compatibility across ten feeder families - CP-4, CP-6, IP and QP BFC sub-bases
among them. Two values conflict across the sources: 45 kg against 35 kg, and the same machine
dimensions written two ways, 350 x 500 x 550 mm against L500 x W350 x H550. The page prints both
figures side by side with their sources named. Its product photographs are referenced from the
company's own CDN rather than ph.smthelp.com, because the matching images are not yet on the public
host; the logo is. **Sibling band due** - this page predates the bowl feeder below, so it carries no
interlink band of its own. Add one pointing at `sbf1001-...html` in the same shape as the S4000's
when the page is next touched.

The SBF1001 is the bulk-feeding half of an odd-form cell: a vibratory bowl indexes loose connectors,
LED lenses, terminals, hardware and plastic parts, a helical sort track brings them into one attitude,
polarity screening and lead cutting are options selected with the part in hand, and an optical fibre
sensor confirms a part is at the pick point before the head is released. The specification is taken
from the Southern Machinery Customized Feeder Nozzle Catalog V03 (page 5) and cross-checked line by
line against the internal SBF1001 parameter sheet, which agree on every published figure: 3 x 3 mm to
50 x 50 mm at 10 g to 300 g, 0.8 s per feed, +/-0.5 mm feeding precision, 220 V at 3 A average and
5 A peak, 0.4-0.6 MPa working air, and either a 760 x 460 x 910 mm single bowl at 150 kg or a
1120 x 460 x 910 mm front-and-rear two-bowl frame at 190 kg. Two supporting documents describe
neighbouring machines rather than this model - the BF200L four-track double-layer bowl and the MBF-L
bowl feeder manual - and the page labels every figure taken from them as belonging to that machine,
not to the SBF1001. Commissioning evidence is quoted as published: a 2-hour continuous feeding test
and a 48-hour ageing test. Every money figure in the payback calculator comes from the visitor; the
page states no price of its own. Its gallery draws on twelve photographs from ph.smthelp.com, and it
embeds nine working videos from the company YouTube board. It links to the FUJI NXT calibration jig
in the same band, and to the S7900, the S4000 and the S-300B - the machines its output feeds.

The odd-form feeder matcher answers the NPI engineer's first question - which feeder and which nozzle for
this part - with an interactive quick-match table: 76 component lines, each mapped to a Southern
Machinery feeder model and nozzle type, filterable by category, packaging, lead pitch, body L/W/H,
lead count and lead diameter, with free-text search, a result count, reset, and a card view on phones.
A row opens the feeder description and a WhatsApp or email feasibility request pre-filled with the
component's dimensions; a check-your-part box compares the visitor's own numbers with each model's
published envelope. The lines come from four anonymised odd-form evaluations and BOM lists plus the
bulk-feeder qualification template - customer names, part numbers, supplier names and prices are
withheld - and the ten feeder models (SAF1001, SRF1001, STF1003, SBF1001, SBF2002, SLF1001, SJF1001,
STP1001, SSPC101, SRT7001) with their size, weight, lead-diameter and accuracy figures are taken from
the Customized Feeder Nozzle Catalog V03. The S-MVF01 reciprocating belt feeder is a separate model
from the catalog's SBF2002 and is listed as its own entry: the four connector lines from its
qualification template name it, and its own landing page is linked. Parts on 32 mm carrier tape are a
confirmed mapping - the host machine's own 32 mm tape feeder with a Southern Machinery nozzle - and the
table gives such rows a "Confirmed mapping" status; lead time is not a catalog figure and is shown as to
be confirmed. A five-step NPI stepper (packaging, measure, match, free sample test,
trial and payback) carries a checklist and feeds the HowTo JSON-LD. The table, its filters and every
label switch with the language selector. Five source conflicts are printed side by side, among them
three radial lines whose lead-width column holds the body width. Eight articles of 370 to 490 words
each cover packaging, measurement, nozzles, oversized parts, bulk feeding, the feasibility check and the
trial. It embeds 23 videos and 12 catalog PDFs, and its sibling band links to the S7900, the SBF1001
bowl feeder, the S-MVF01 belt feeder, the S3000, the S4000 and the FUJI NXT calibration jig.

The S-RF1001 page covers the radial lead taped feeder that lets an SMT mounter pick and insert
radial THT parts. Its figures come from the S-RF1001 brochure (550 x 110 x 130 mm, air-driven, DC 24 V
input signal, the eleven-row tape table and the YAMAHA, JUKI and UNIVERSAL solutions); the 90° bend
and L-S capacitor versions come from the two eDrawings 3D files, rendered to stills because the files
hold no extractable GLB. The 3D stage is procedural (tape index, lead cut, 90° bend, gripper pick and
insert) and a tape checker compares the visitor's P0, F, d, H, H1 and t with the brochure limits. The
disclosure table lists seven open points, among them "RF 200 adjustable" in the tape table, 25 mm lead
spacing against the 27.5 mm large-span video, eleven brand logos against three documented host
solutions, and no published feeding speed. Built with the `product-3d-doc-html-landing` skill v1.0.1.
**Sibling band due** - link the SBF1001 bowl feeder and S3000 radial insertion pages when next touched.

### THT Auto Insertion - `tht-auto-insertion/`

| Page | File | Size | Languages |
|---|---|---|---|
| S3000 Radial Insertion Machine for Smart EMS THT PCB Assembly | `tht-auto-insertion/s3000-radial-insertion-machine-smart-ems-tht-pcb-assembly.html` | 426 KB | 7 + x-default |
| S4000 Axial Insertion Machine for Smart EMS THT PCB Assembly | `tht-auto-insertion/s4000-axial-insertion-machine-smart-ems-tht-pcb-assembly.html` | 523 KB | 7 + x-default |
| S7900 OddForm Insertion Machine Solution for Smart EMS THT PCB Assembly | `tht-auto-insertion/s7900-odd-form-insertion-machine-smart-ems-tht-pcb-assembly.html` | 627 KB | 7 + x-default |
| Mobile Charger THT Auto Insertion & Wave Soldering Line for Smart EMS PCB Assembly | `tht-auto-insertion/mobile-charger-tht-auto-insertion-wave-soldering-line-smart-ems-pcb-assembly.html` | 950 KB | 7 + x-default |
| S3300 Bulk LED Radial Insertion Machine, 15,000 CPH for LED Display PCB Assembly | `tht-auto-insertion/s3300-bulk-led-radial-insertion-machine-15000-cph-led-display-pcb-assembly.html` | 570 KB | 7 + x-default |

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

The mobile charger line page is the first line-level page in this band: a seven-station reference
layout (magazine loader, S3010A radial, S7020T terminal, S7020A odd-form, an S7040 four-head odd-form
cell with bowl and S-MVF01 bulk feeders, S-WS350 wave soldering, outfeed) with an interactive Three.js
model of the line, a charger BOM split by package and feeding method, per-machine specifications
labelled with their source, and a ten-row disclosure table for the figures our documents disagree on
(S3010A speed, span and feeder count; S7020T speed and footprint; odd-form speed; S-MVF01 cycle;
S-WS350 preheat length and pot limit; model names on the drawings). Three line drawings that are not
yet on ph.smthelp.com are inlined as small WebP files; every other image is hosted there. It links to
the S3000, S4000 and S7900 pages.

### PCB Handling - `board-handling/`

| Page | File | Size | Languages |
|---|---|---|---|
| ESD Tray with Grids for Smart EMS PCB Assembly | `board-handling/esd-tray-with-grids-for-smart-ems-tht-pcb-assembly.html` | 458 KB | 7 + x-default |
| SMT PCB Loader Solution: magazine, mini, L-type, destacker, vacuum, combo, 1.2 m LED, semiconductor and flexible-PCB loaders | `board-handling/smt-pcb-loader-solution-magazine-mini-l-type-destacker-vacuum-combo-led-loader-smart-ems-factory.html` | 737 KB | 7 + x-default |

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

**SMT PCB loader solution.** One page for the whole loader family, built from the loader catalogue,
the product sheets and presentations of the S-MLD250, SL600A, SBU460, SFBL250, SLF330 and SLD350L.
A Three.js scene shows nine loader mechanisms (magazine pusher, mini, L-type, bottom destacker,
vacuum pick, combo, 1.2 m LED, three-magazine semiconductor, robot into pallet); a loader finder
picks the model from board size, thickness and supply form. A model table lists 18 rows, and seven
points where the documents disagree (two S-MLD250 spec sets, SLD250L used for three machines,
SBU/SLC destacker names, SLF250/330 figures, SVL size order, air pressure, SL600A magazine height)
are printed in a disclosure table. No price appears; the payback worksheet fields start empty.
Presentation clips are on a public Google Drive folder.

**Sibling band:** still none - the ESD tray and the loader page are different families.

### Smart Storage - `smart-storage/`

| Page | File | Size | Languages |
|---|---|---|---|
| SIS7200A SMT Intelligent Reel Storage Rack with Pick-to-Light for Smart EMS Factories | `smart-storage/sis7200a-smt-intelligent-reel-storage-rack-pick-to-light-smart-ems-factory.html` | 530 KB | 7 + x-default |
| SIS5210A 5-Layer Mobile SMT Smart Reel Rack for Mixed 7 and 13 Inch Reels | `smart-storage/sis5210a-5-layer-mobile-smt-smart-reel-rack-mixed-7-13-inch-reels-pick-to-light.html` | 446 KB | 7 + x-default |

The SIS7200A is a pick-to-light reel rack: 1,400 seven-inch reels thinner than 17 mm on seven
layers used from both faces, 2130 x 400 x 2000 mm, every slot with its own LED. Reels go into any
free slot the rack lights, and work orders light their reels in separate colours, oldest date code
first. The interactive 3D rack runs six warehouse tasks - put-away, a three-order kit, FIFO by date
code, stocktake, a shortage call from the line and a wrong-slot alarm - and reports the slot address
of any reel tapped. Specification cards cover the SIS7200A, the SIS5210A five-layer rack (7 and 13 inch reels mixed freely), the SIR7000B,
SIR5000B and SIR5000C, and the software and HTTP + JSON interface (API V3.1), each figure naming its
source document. Seven places where the documents disagree are printed side by side: rack sizes and
capacities across SIS7200A / SIS7000A / SIR7000B, the two SIS4000A designs, power, communication,
the two efficiency case studies, the LED palette, and figures from an earlier landing page (720+ reels, 3-5 s retrieval, 99.9%, 3-12 month
payback) that no datasheet supports and that are marked `To be confirmed`. The gallery uses eleven
photographs and renderings from ph.smthelp.com plus one controller-box photo embedded as a small WebP
because it is not on the public host. SIS5210A (printed SIS5120A on its product sheet) and SIR5000C are separate models (confirmed by
Southern Machinery, 2026-11-02), not two versions of one trolley. Twelve YouTube videos come from the company board, and eight
factory-floor clips play from a public Google Drive folder.

The SIS5210A page covers the five-layer rack on casters: 1320 x 400 x 1630 mm, 60 kg, 600 seven-inch
or 300 thirteen-inch reels with the two sizes mixed freely, DC 5 V battery inside and a Wi-Fi
controller on top. Its 3D model is a mix planner: tap any half-layer to switch it between 7-inch and
13-inch slots and the capacity updates live (five presets, from all 7-inch to half and half), then
watch put-away by size, a three-order kit that rolls to a feeder bank and back, FIFO, a shortage call
and a wrong-size alarm. Six open points are printed side by side: the model name (the product sheet
says SIS5120A, confirmed as SIS5210A), 13-inch capacity against the drawn layer heights, stainless
frame against the aluminium-profile rendering, battery runtime not stated, the sheet's 90% labour and
6-month ROI claims (`To be confirmed`, no customer case held), and a 2019 smart cart whose figures
belong to a different product. No dedicated SIS5210A video exists yet, so the video section says so
and shows the sister racks.

**No sibling band yet.** The other storage pages - the reel storage silo, the stencil storage
cabinet, the X-ray counter - are not in this repository, so the band is left out until they arrive.

### SMT Lines - `smt-lines/`

| Page | File | Size | Languages |
|---|---|---|---|
| LED T8 Tube 1.2 m Strip SMT Assembly Line with 16-Strip Carriers and ROI Calculator | `smt-lines/led-t8-tube-1-2m-strip-smt-assembly-line-16-strip-carrier-roi-smart-ems-factory.html` | 702 KB | 7 + x-default |

A turnkey SMT line for 1170 mm LED T8 tube strips (8 or 10 mm wide, SMD2835, FR-4 or aluminium
MCPCB, 96 or 120 LEDs): SVL-460L vacuum loader, SCL-1200 stencil printer, three S-350E conveyors,
SM-MS20 20-head 82,000 CPH LED placement, SRF-1000L 10+10 zone long-board reflow, SM-CVB1200 buffer,
SM-VL-800 inline AOI and SM-UL1200 unloader, with forty 1195 x 240 mm carriers that hold sixteen
strips each. Design basis 481 good strips per hour, 3,848 per 8-hour shift, four operators, 24 x 5 m.
The interactive 3D line follows the 24 x 5 m layout; carriers pick up LEDs at placement and turn green
after AOI, and a 96 / 120 LED switch shows the bottleneck (76 / 86 s) and calculated output (557 / 492
per hour). Facts come from the line's technical schedules (capacity, carrier concept, station matrix,
FAT/SAT, utilities, packing). **Unit prices and the customer name are left out on purpose.** The ROI
calculator fixes the investment at USD 392,750, the equipment total plus 25% for freight, duties,
installation, utilities and contingency; all other inputs are editable placeholders, and a 1/2/3-shift
table updates live. Seven open points are printed side by side, including the 1.71 s placement margin
at 120 LEDs (`To be confirmed` in the sample run) and the earlier 1.2 million tubes a month concept page,
whose basis differs. Machine photos are embedded once as small WebP (they are not on the public host)
and reused through a single image map; twelve related YouTube videos come from the company board.

**No sibling band yet.** Other complete-line pages are not in this repository yet.

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

Page list generated 2026-11-02 from the directory contents.
