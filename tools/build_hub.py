#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Southern Machinery single-file catalogue hub.

Scans every product landing page in the repository, extracts its metadata,
photographs, videos and catalogue documents, and renders one self-contained
HTML file. Run nightly by .github/workflows/refresh-hub.yml so that pages added
to the repository appear in the hub automatically.

    python3 tools/build_hub.py            # write the hub
    python3 tools/build_hub.py --check    # exit 1 if the hub is out of date
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import os
import re
import subprocess
import sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from i18n_ui import UI, LANGS, RTL, LANG_LABEL                      # noqa: E402
from i18n_articles import ARTICLES, CATEGORIES                      # noqa: E402

OUT_NAME = "smt-tht-machine-catalog-hub-smart-ems-factory-southern-machinery.html"
OUT_PATH = os.path.join(ROOT, OUT_NAME)

SITE = "https://file.autoinsertion.com/public/Product%20landing%20Page/"
CANONICAL = SITE + OUT_NAME
LOGO = "https://ph.smthelp.com/images/2024/06/26/Southern-Machinery-logo-300x83.png"
CATALOG_BOARD = "https://file.autoinsertion.com/public/Southern-Machinery-Product-Catalog-Board.html"
VIDEO_BOARD = "https://file.autoinsertion.com/public/Southern-Machinery-YouTube-Video-Board.html"
IMAGE_HOST = "https://ph.smthelp.com/"
WA = "https://wa.me/8613602562576"
MAIL = "info@smthelp.com"
SOCIAL = {
    "li_co": "https://www.linkedin.com/company/smtmachine",
    "li_me": "https://www.linkedin.com/in/smtsupplier",
    "tw": "https://twitter.com/smtspecialist",
    "fb": "https://www.facebook.com/autoinsertion",
    "yt": "https://www.youtube.com/c/Smthelping",
}

SKIP_FILES = {OUT_NAME, "index.html"}
SKIP_DIRS = {".git", ".github", "tools", "node_modules", "assets"}

# Images that are chrome rather than product photographs.
IMG_DENY = re.compile(r"(southern-machinery-logo|logo-300x83|favicon|/qr|wechat)", re.I)
DOC_EXT = (".pdf", ".pptx", ".xlsx", ".docx", ".doc", ".zip")

MODEL_RE = re.compile(
    r"\b(?:S-?\d{3,4}[A-Z]{0,2}|SIS\d{4}[A-Z]?|S[A-Z]{2}\d{3,4}[A-Z]?|S-[A-Z]{2,5}\d{2,4}[A-Z]?"
    r"|SLD\d{3}|BF\d{3}[A-Z]?|NXT|SP-\d{3,4})\b"
)
MODEL_DENY = {"S-300", "SMT", "THT", "NXT"}


# --------------------------------------------------------------------- helpers
def sh(*args: str) -> str:
    try:
        return subprocess.run(args, cwd=ROOT, capture_output=True, text=True,
                              timeout=60).stdout.strip()
    except Exception:
        return ""


def meta_of(txt: str, *, name: str = "", prop: str = "") -> str:
    attr, val = ("name", name) if name else ("property", prop)
    m = re.search(r'<meta\s+%s=["\']%s["\']\s+content=["\'](.*?)["\']' % (attr, re.escape(val)),
                  txt, re.I | re.S)
    return html.unescape(m.group(1)).strip() if m else ""


def clean_title(t: str) -> str:
    t = re.sub(r"\s*[|\u2014-]\s*Southern Machinery\s*$", "", t).strip()
    return re.sub(r"\s+", " ", t)


def discover() -> list[str]:
    out = []
    for dp, dns, fns in os.walk(ROOT):
        dns[:] = [d for d in dns if d not in SKIP_DIRS and not d.startswith(".")]
        for fn in fns:
            if fn.endswith(".html") and fn not in SKIP_FILES:
                out.append(os.path.relpath(os.path.join(dp, fn), ROOT).replace(os.sep, "/"))
    return sorted(out)


def category_of(relpath: str) -> str:
    d = os.path.dirname(relpath)
    for c in CATEGORIES:
        if c["dir"] and d == c["dir"]:
            return c["key"]
    return "nozzle-and-gripper"


def parse_page(rel: str) -> dict:
    full = os.path.join(ROOT, rel)
    with open(full, encoding="utf-8", errors="replace") as fh:
        body = fh.read()
    head = body[:30000]

    m = re.search(r"<title>(.*?)</title>", head, re.I | re.S)
    title = clean_title(html.unescape(m.group(1)).strip()) if m else rel

    desc = meta_of(head, name="description") or meta_of(head, prop="og:description")
    keys = meta_of(head, name="keywords")
    og = meta_of(head, prop="og:image")

    imgs = []
    for u in re.findall(r'https://ph\.smthelp\.com/[^"\'\s<)\\]+?\.(?:jpg|jpeg|png|webp|gif)',
                        body, re.I):
        if not IMG_DENY.search(u) and u not in imgs:
            imgs.append(u)
    # Prefer the medium (".md.") variants for gallery thumbnails where both exist.
    full_set = set(imgs)
    gallery = [u for u in imgs if ".md." in u or u.replace(".", ".md.", u.rfind(".")) not in full_set]

    hero = og if (og.startswith("https://ph.smthelp.com") and not IMG_DENY.search(og)) else ""
    if not hero:
        hero = imgs[0] if imgs else ""

    vids = list(OrderedDict.fromkeys(re.findall(
        r'(?:youtube(?:-nocookie)?\.com/(?:embed/|watch\?v=)|youtu\.be/)([A-Za-z0-9_-]{11})', body)))

    docs = []
    for u in re.findall(r'https://file\.autoinsertion\.com/public/[^"\'\s<)\\]+', body):
        u = u.rstrip(".,);'\"")
        if u.lower().endswith(DOC_EXT) and u not in docs:
            docs.append(u)

    hay = " ".join([title, desc, keys, rel])
    models = []
    for mm in MODEL_RE.findall(hay):
        mm = mm.upper()
        if mm not in MODEL_DENY and mm not in models:
            models.append(mm)

    added = sh("git", "log", "--diff-filter=A", "--format=%aI", "-1", "--", rel)[:10]
    touched = sh("git", "log", "--format=%aI", "-1", "--", rel)[:10]

    return {
        "p": rel, "t": title, "d": desc, "k": keys, "c": category_of(rel),
        "img": hero, "g": gallery[:14], "v": vids, "docs": docs,
        "m": models[:5], "kb": round(os.path.getsize(full) / 1024),
        "add": added, "up": touched or added,
    }


# Words that make an image relevant to a product line, used when a page carries
# no photograph of its own (several brand nozzle pages only embed the logo).
CAT_HINTS = {
    "nozzle-and-gripper": ("nozzle", "gripper"),
    "tht-auto-insertion": ("insertion", "insert", "radial", "axial", "oddform", "odd-form"),
    "feeders-nozzles": ("feeder", "feeding", "bowl", "calibration", "jig"),
    "materials-consumables": ("tape", "splice", "taping", "molding", "calibration"),
    "board-handling": ("loader", "destacker", "conveyor", "tray", "magazine", "pcb"),
    "smart-storage": ("reel", "storage", "rack", "shelf", "trolley", "sis"),
    "smt-lines": ("line", "led", "smt", "mounter"),
}
BRANDS = ("fuji", "yamaha", "panasonic", "juki", "siemens", "siplace", "samsung", "nxt", "npm")
STOP = {"the", "for", "and", "with", "smart", "ems", "pcb", "assembly", "southern",
        "machinery", "manufacturer", "smt", "tht", "html", "factory", "solution"}


def tokens(*parts: str) -> set[str]:
    t = set()
    for p in parts:
        for w in re.split(r"[^a-z0-9]+", p.lower()):
            if len(w) >= 3 and w not in STOP:
                t.add(w)
    return t


def pick_fallback(pg: dict, pool: list[str], used: set[str]) -> str:
    """Choose the most relevant photograph on ph.smthelp.com for a page with none."""
    want = tokens(pg["t"], pg["p"])
    hints = CAT_HINTS.get(pg["c"], ())
    best, best_score = "", 0
    for url in pool:
        low = url.lower()
        # Never illustrate one manufacturer's page with another's hardware.
        if any(b in low and b not in want for b in BRANDS):
            continue
        score = 0
        if hints and any(h in low for h in hints):
            score += 4
        elif hints:
            continue  # keep the image on-topic for the product line
        for w in want:
            if w in low:
                score += 3 if w in BRANDS else 1
        if url in used:
            score -= 2
        if score > best_score:
            best, best_score = url, score
    return best


def interleave(groups: list[list], cap: int) -> list:
    """Round-robin across per-page groups so every product line is represented.

    Taking the first N items in page order would fill the whole gallery from one
    category; cycling one item per page at a time keeps the mix even.
    """
    out, i = [], 0
    while len(out) < cap:
        took = False
        for g in groups:
            if i < len(g):
                out.append(g[i])
                took = True
                if len(out) >= cap:
                    break
        if not took:
            break
        i += 1
    return out


def doc_label(url: str) -> str:
    name = url.rsplit("/", 1)[-1]
    from urllib.parse import unquote
    name = unquote(name)
    stem, _, ext = name.rpartition(".")
    stem = re.sub(r"[_]+", " ", stem)
    stem = re.sub(r"\s+", " ", stem).strip()
    return stem, ext.upper()


# ------------------------------------------------------------------- rendering
def esc(s: str) -> str:
    return html.escape(s, quote=True)


def build() -> str:
    pages = [parse_page(p) for p in discover()]
    today = dt.datetime.now(dt.timezone.utc)
    stamp = today.strftime("%Y-%m-%d")

    # recency badge: added within 45 days
    for pg in pages:
        try:
            pg["new"] = (today.date() - dt.date.fromisoformat(pg["add"])).days <= 45
        except Exception:
            pg["new"] = False

    cat_order = [c["key"] for c in CATEGORIES]
    pages.sort(key=lambda x: (cat_order.index(x["c"]), x["t"].lower()))

    # Pages that embed no photograph of their own borrow the closest match from
    # the shared ph.smthelp.com pool, so no card falls back to a bare icon.
    pool, used = [], {p["img"] for p in pages if p["img"]}
    for pg in pages:
        for u in pg["g"]:
            if u not in pool:
                pool.append(u)
    for pg in pages:
        if not pg["img"]:
            pg["img"] = pick_fallback(pg, pool, used)
            if pg["img"]:
                used.add(pg["img"])

    # ---- aggregate videos, documents and photographs, tagged by category.
    # Each asset is kept in a per-page group and then interleaved, so selecting
    # any product line chip still shows photographs, videos and documents.
    seen_v, vid_groups = set(), []
    for pg in pages:
        g = []
        for v in pg["v"]:
            if v not in seen_v:
                seen_v.add(v)
                g.append({"id": v, "c": pg["c"], "t": pg["t"]})
        vid_groups.append(g)
    videos = interleave(vid_groups, 36)

    seen_d, doc_groups = set(), []
    for pg in pages:
        g = []
        for u in pg["docs"]:
            if u not in seen_d:
                seen_d.add(u)
                label, ext = doc_label(u)
                g.append({"u": u, "c": pg["c"], "t": label, "x": ext})
        doc_groups.append(g)
    docs = interleave(doc_groups, 72)

    seen_img, img_groups = set(), []
    for pg in pages:
        g = []
        for u in pg["g"]:
            if u not in seen_img:
                seen_img.add(u)
                g.append({"u": u, "c": pg["c"], "t": pg["t"]})
        img_groups.append(g)
    photos = interleave(img_groups, 56)

    counts = {c["key"]: sum(1 for p in pages if p["c"] == c["key"]) for c in CATEGORIES}
    # Headline stats count everything the repository holds, not just what is shown.
    nums = {"pages": len(pages), "cats": len([c for c in CATEGORIES if counts[c["key"]]]),
            "videos": len(seen_v), "docs": len(seen_d), "images": len(seen_img)}

    # ---- i18n dictionary -----------------------------------------------------
    I18N = {}
    for lg in LANGS:
        d = dict(UI[lg])
        for k, v in list(d.items()):
            if isinstance(v, str) and "{" in v:
                try:
                    d[k] = v.format(**nums, n="{n}", total="{total}")
                except (KeyError, IndexError):
                    pass
        d["stat1v"] = str(nums["pages"])
        d["stat2v"] = str(nums["cats"])
        d["stat3v"] = str(nums["videos"])
        d["stat4v"] = str(nums["docs"])
        for c in CATEGORIES:
            d["cat_%s" % c["key"]] = c["n"][lg]
            d["catd_%s" % c["key"]] = c["d"][lg]
        for i, a in enumerate(ARTICLES, 1):
            d["a%d_t" % i] = a[lg]["t"]
            d["a%d_s" % i] = a[lg]["s"]
            for b in range(1, 7):
                d["a%d_b%d" % (i, b)] = a[lg]["b%d" % b]
        I18N[lg] = d

    # ---- JSON-LD -------------------------------------------------------------
    en = I18N["en"]
    ld = [
        {"@context": "https://schema.org", "@type": "Organization",
         "name": "Shenzhen Southern Machinery Sales and Service Co., Ltd",
         "alternateName": "Southern Machinery", "url": "https://www.smthelp.com/",
         "logo": LOGO, "email": MAIL,
         "description": "Design and manufacture of SMT and THT equipment for smart EMS factories.",
         "address": {"@type": "PostalAddress", "addressLocality": "Shenzhen",
                     "addressRegion": "Guangdong", "addressCountry": "CN"},
         "sameAs": [SOCIAL["li_co"], SOCIAL["li_me"], SOCIAL["tw"], SOCIAL["fb"], SOCIAL["yt"]]},
        {"@context": "https://schema.org", "@type": "WebSite", "url": CANONICAL,
         "name": en["seo_title"], "description": en["seo_desc"],
         "inLanguage": LANGS,
         "potentialAction": {"@type": "SearchAction",
                             "target": {"@type": "EntryPoint",
                                        "urlTemplate": CANONICAL + "?q={search_term_string}"},
                             "query-input": "required name=search_term_string"}},
        {"@context": "https://schema.org", "@type": "ItemList",
         "name": "Southern Machinery SMT and THT equipment pages",
         "numberOfItems": len(pages),
         "itemListElement": [
             {"@type": "ListItem", "position": i + 1, "url": SITE + os.path.basename(p["p"]),
              "name": p["t"]} for i, p in enumerate(pages)]},
        {"@context": "https://schema.org", "@type": "FAQPage",
         "mainEntity": [{"@type": "Question", "name": en["q%d" % i],
                         "acceptedAnswer": {"@type": "Answer", "text": en["a%d" % i]}}
                        for i in range(1, 7)]},
        {"@context": "https://schema.org", "@type": "Blog", "url": CANONICAL + "#insights",
         "name": en["ins_h2"],
         "blogPost": [{"@type": "BlogPost", "headline": en["a%d_t" % i],
                       "description": en["a%d_s" % i], "inLanguage": "en",
                       "datePublished": stamp,
                       "author": {"@type": "Organization", "name": "Southern Machinery"},
                       "publisher": {"@type": "Organization", "name": "Southern Machinery",
                                     "logo": {"@type": "ImageObject", "url": LOGO}}}
                      for i in range(1, len(ARTICLES) + 1)]},
        {"@context": "https://schema.org", "@type": "BreadcrumbList",
         "itemListElement": [
             {"@type": "ListItem", "position": 1, "name": "Southern Machinery",
              "item": "https://www.smthelp.com/"},
             {"@type": "ListItem", "position": 2, "name": "SMT & THT equipment catalog",
              "item": CANONICAL}]},
    ]

    hreflang = "\n".join(
        '<link rel="alternate" hreflang="%s" href="%s">' % (lg, CANONICAL + ("" if lg == "en" else "?lang=" + lg))
        for lg in LANGS) + '\n<link rel="alternate" hreflang="x-default" href="%s">' % CANONICAL

    # ---- category chips, cards, sections ------------------------------------
    chips = ['<button class="chip is-on" data-cat="all" type="button">'
             '<span data-i18n="filter_all">%s</span> <b>%d</b></button>' % (esc(en["filter_all"]), len(pages))]
    for c in CATEGORIES:
        if not counts[c["key"]]:
            continue
        chips.append(
            '<button class="chip" data-cat="%s" type="button"><i aria-hidden="true">%s</i> '
            '<span data-i18n="cat_%s">%s</span> <b>%d</b></button>'
            % (c["key"], c["icon"], c["key"], esc(c["n"]["en"]), counts[c["key"]]))

    cards = []
    for pg in pages:
        cat = next(c for c in CATEGORIES if c["key"] == pg["c"])
        badge = ('<span class="badge-new" data-i18n="card_new">%s</span>' % esc(en["card_new"])) if pg["new"] else ""
        models = "".join('<span class="mdl">%s</span>' % esc(m) for m in pg["m"])
        thumb = ('<img loading="lazy" decoding="async" src="%s" alt="%s">' % (esc(pg["img"]), esc(pg["t"]))
                 if pg["img"] else '<span class="ph-ico">%s</span>' % cat["icon"])
        cards.append(
            '<article class="card" data-cat="%s" data-new="%d">'
            '<a class="card-media" href="%s">%s%s</a>'
            '<div class="card-body">'
            '<span class="card-cat" data-i18n="cat_%s">%s</span>'
            '<h3 class="card-t"><a href="%s">%s</a></h3>'
            '<p class="card-d">%s</p>'
            '<div class="mdls">%s</div>'
            '<div class="card-meta"><span>%d <span data-i18n="card_videos">%s</span></span>'
            '<span>%d <span data-i18n="card_docs">%s</span></span>'
            '<span>%d <span data-i18n="card_photos">%s</span></span></div>'
            '<a class="card-go" href="%s"><span data-i18n="card_open">%s</span> →</a>'
            '</div></article>'
            % (pg["c"], 1 if pg["new"] else 0, esc(pg["p"]), thumb, badge,
               pg["c"], esc(cat["n"]["en"]), esc(pg["p"]), esc(pg["t"]),
               esc(pg["d"][:190]), models,
               len(pg["v"]), esc(en["card_videos"]), len(pg["docs"]), esc(en["card_docs"]),
               len(pg["g"]), esc(en["card_photos"]), esc(pg["p"]), esc(en["card_open"])))

    gal = "".join(
        '<a class="shot" data-cat="%s" href="%s" target="_blank" rel="noopener">'
        '<img loading="lazy" decoding="async" src="%s" alt="%s"><span>%s</span></a>'
        % (p["c"], esc(p["u"]), esc(p["u"]), esc(p["t"]), esc(p["t"]))
        for p in photos)

    vid = "".join(
        '<div class="vid" data-cat="%s" data-yt="%s">'
        '<button class="vid-btn" type="button" aria-label="%s">'
        '<img loading="lazy" decoding="async" src="https://i.ytimg.com/vi/%s/hqdefault.jpg" alt="%s">'
        '<span class="play" aria-hidden="true"></span></button>'
        '<p class="vid-t">%s</p></div>'
        % (v["c"], v["id"], esc(en["vid_play"]), v["id"], esc(v["t"]), esc(v["t"]))
        for v in videos)

    doc = "".join(
        '<a class="doc" data-cat="%s" href="%s" target="_blank" rel="noopener">'
        '<span class="doc-x">%s</span><span class="doc-t">%s</span>'
        '<span class="doc-go" data-i18n="doc_open">%s</span></a>'
        % (d["c"], esc(d["u"]), esc(d["x"]), esc(d["t"]), esc(en["doc_open"]))
        for d in docs)

    posts = []
    for i, a in enumerate(ARTICLES, 1):
        cat = next(c for c in CATEGORIES if c["key"] == a["cat"])
        steps = "".join(
            '<h4 data-i18n="step%d">%s</h4><p data-i18n="a%d_b%d">%s</p>'
            % (s, esc(en["step%d" % s]), i, s, esc(en["a%d_b%d" % (i, s)]))
            for s in range(1, 7))
        posts.append(
            '<article class="post" id="insight-%s">'
            '<header><span class="post-cat" data-i18n="cat_%s">%s</span>'
            '<h3 data-i18n="a%d_t">%s</h3>'
            '<p class="post-s" data-i18n="a%d_s">%s</p></header>'
            '<div class="post-body">%s</div>'
            '<p class="post-more"><button type="button" data-i18n="ui_more">%s</button></p>'
            '</article>'
            % (a["id"], a["cat"], esc(cat["n"]["en"]), i, esc(en["a%d_t" % i]),
               i, esc(en["a%d_s" % i]), steps, esc(en["ui_more"])))

    faq = "".join(
        '<details class="faq"><summary data-i18n="q%d">%s</summary>'
        '<p data-i18n="a%d">%s</p></details>'
        % (i, esc(en["q%d" % i]), i, esc(en["a%d" % i])) for i in range(1, 7))

    langopts = "".join('<option value="%s">%s</option>' % (lg, LANG_LABEL[lg]) for lg in LANGS)

    search_rows = [{"i": n, "c": p["c"],
                    "s": " ".join([p["t"], p["d"], p["k"], " ".join(p["m"]), p["p"]]).lower(),
                    "u": p["up"]} for n, p in enumerate(pages)]

    return TEMPLATE.format(
        lang="en", canonical=CANONICAL, hreflang=hreflang, logo=LOGO,
        title=esc(en["seo_title"]), desc=esc(en["seo_desc"]), keys=esc(en["seo_keys"]),
        ogimg=esc(pages[0]["img"] if pages else LOGO),
        jsonld=json.dumps(ld, ensure_ascii=False, separators=(",", ":")),
        i18n=json.dumps(I18N, ensure_ascii=False, separators=(",", ":")),
        rows=json.dumps(search_rows, ensure_ascii=False, separators=(",", ":")),
        langs=json.dumps(LANGS), rtl=json.dumps(RTL),
        langopts=langopts, chips="".join(chips), cards="".join(cards),
        gallery=gal, videos=vid, docsec=doc, posts="".join(posts), faq=faq,
        t=en, stamp=stamp, total=len(pages),
        wa=WA, mail=MAIL, catboard=CATALOG_BOARD, vidboard=VIDEO_BOARD, imghost=IMAGE_HOST,
        li_co=SOCIAL["li_co"], li_me=SOCIAL["li_me"], tw=SOCIAL["tw"],
        fb=SOCIAL["fb"], yt=SOCIAL["yt"], year=today.year,
    )


TEMPLATE = r"""<!DOCTYPE html>
<html lang="{lang}" data-theme="light" dir="ltr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{keys}">
<meta name="author" content="Southern Machinery">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta name="theme-color" content="#0c665c">
<link rel="canonical" href="{canonical}">
{hreflang}
<meta property="og:type" content="website">
<meta property="og:site_name" content="Southern Machinery">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{ogimg}">
<meta property="og:url" content="{canonical}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@smtspecialist">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{ogimg}">
<link rel="icon" href="{logo}">
<link rel="preconnect" href="https://ph.smthelp.com">
<link rel="preconnect" href="https://i.ytimg.com">
<script type="application/ld+json">{jsonld}</script>
<style>
*,*::before,*::after{{box-sizing:border-box}}
:root{{
--bg:#f6f8f8;--bg2:#fff;--bg3:#eef3f2;--ink:#0f1c1b;--ink2:#4a5f5d;--line:#d9e4e2;
--brand:#0c665c;--brand2:#0a8c7a;--accent:#e8a33d;--card:#fff;--shadow:0 1px 2px rgba(10,40,38,.06),0 8px 24px rgba(10,40,38,.06);
--radius:14px;--max:1200px
}}
[data-theme=dark]{{
--bg:#0b1514;--bg2:#101e1d;--bg3:#152625;--ink:#e8f1ef;--ink2:#9db3b0;--line:#213836;
--brand:#2fbda6;--brand2:#49d8bf;--accent:#f0b659;--card:#101e1d;--shadow:0 1px 2px rgba(0,0,0,.4),0 8px 24px rgba(0,0,0,.35)
}}
html{{scroll-behavior:smooth;-webkit-text-size-adjust:100%}}
body{{margin:0;background:var(--bg);color:var(--ink);
font:16px/1.65 "Inter",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue","Noto Sans","Noto Sans Arabic","Noto Sans SC",Arial,sans-serif;
transition:background .25s,color .25s}}
img{{max-width:100%;display:block}}
a{{color:var(--brand);text-decoration:none}}
a:hover{{text-decoration:underline}}
h1,h2,h3,h4{{line-height:1.22;margin:0 0 .5em;font-weight:760;letter-spacing:-.018em}}
.wrap{{max-width:var(--max);margin:0 auto;padding:0 22px}}
.sr{{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}}
.skip{{position:absolute;left:-9999px;top:0;background:var(--brand);color:#fff;padding:10px 16px;z-index:99}}
.skip:focus{{left:8px;top:8px}}

.topbar{{background:var(--brand);color:#fff;font-size:12.5px;letter-spacing:.01em}}
.topbar .wrap{{padding-block:7px;display:flex;gap:14px;justify-content:space-between;align-items:center;flex-wrap:wrap}}
.topbar a{{color:#fff;opacity:.92}}

header.site{{position:sticky;top:0;z-index:40;background:color-mix(in srgb,var(--bg2) 88%, transparent);
backdrop-filter:saturate(1.6) blur(10px);border-bottom:1px solid var(--line)}}
.nav{{display:flex;align-items:center;gap:18px;padding:11px 0}}
.brand{{display:flex;align-items:center;gap:11px;flex-shrink:0}}
.brand img{{height:40px;width:auto}}
.brand span{{font-size:11.5px;color:var(--ink2);max-width:160px;line-height:1.3;display:block}}
.menu{{display:flex;gap:4px;margin-inline-start:auto;flex-wrap:wrap}}
.menu a{{color:var(--ink2);font-size:14px;font-weight:600;padding:7px 11px;border-radius:9px}}
.menu a:hover{{background:var(--bg3);color:var(--brand);text-decoration:none}}
.tools{{display:flex;gap:8px;align-items:center;flex-shrink:0}}
.btn-i{{width:38px;height:38px;border-radius:10px;border:1px solid var(--line);background:var(--bg2);
color:var(--ink);font-size:16px;cursor:pointer;display:grid;place-items:center;transition:.18s}}
.btn-i:hover{{border-color:var(--brand);color:var(--brand)}}
select.lang{{height:38px;border-radius:10px;border:1px solid var(--line);background:var(--bg2);color:var(--ink);
padding:0 9px;font:inherit;font-size:13.5px;cursor:pointer;max-width:132px}}

.hero{{padding:62px 0 42px;background:
radial-gradient(1100px 420px at 78% -12%,color-mix(in srgb,var(--brand) 16%,transparent),transparent 62%),
radial-gradient(760px 340px at 4% 0%,color-mix(in srgb,var(--accent) 11%,transparent),transparent 58%)}}
.kick{{display:inline-block;font-size:12px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;
color:var(--brand2);background:color-mix(in srgb,var(--brand) 12%,transparent);
padding:6px 13px;border-radius:999px;margin-bottom:18px}}
.hero h1{{font-size:clamp(31px,5.1vw,56px);margin-bottom:16px;max-width:17ch}}
.hero h1 em{{font-style:normal;color:var(--brand);display:block}}
.hero p.lead{{font-size:clamp(16px,1.7vw,19.5px);color:var(--ink2);max-width:62ch;margin:0 0 26px}}
.cta-row{{display:flex;gap:12px;flex-wrap:wrap}}
.btn{{display:inline-flex;align-items:center;gap:9px;padding:13px 22px;border-radius:11px;font-weight:700;
font-size:15px;border:1px solid transparent;cursor:pointer;transition:.18s;text-decoration:none}}
.btn-p{{background:var(--brand);color:#fff;box-shadow:var(--shadow)}}
.btn-p:hover{{background:var(--brand2);text-decoration:none;transform:translateY(-1px)}}
.btn-s{{background:var(--bg2);color:var(--ink);border-color:var(--line)}}
.btn-s:hover{{border-color:var(--brand);color:var(--brand);text-decoration:none}}
.stats{{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:40px}}
.stat{{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:18px}}
.stat b{{display:block;font-size:clamp(23px,3vw,33px);color:var(--brand);line-height:1.1}}
.stat span{{font-size:12.5px;color:var(--ink2)}}

section{{padding:56px 0;border-top:1px solid var(--line)}}
section>.wrap>.kick{{margin-bottom:12px}}
h2.sec{{font-size:clamp(23px,3.1vw,35px);max-width:21ch}}
p.lead2{{color:var(--ink2);max-width:72ch;margin:0 0 26px;font-size:16.5px}}

.searchbar{{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin-bottom:16px}}
.sinput{{position:relative;flex:1 1 330px}}
.sinput input{{width:100%;height:50px;border-radius:12px;border:1.5px solid var(--line);background:var(--bg2);
color:var(--ink);padding:0 44px 0 16px;font:inherit;font-size:15.5px;transition:.18s}}
.sinput input:focus{{outline:none;border-color:var(--brand);box-shadow:0 0 0 4px color-mix(in srgb,var(--brand) 14%,transparent)}}
.sinput::after{{content:"⌕";position:absolute;inset-inline-end:15px;top:11px;font-size:21px;color:var(--ink2);pointer-events:none}}
select.sort{{height:50px;border-radius:12px;border:1.5px solid var(--line);background:var(--bg2);color:var(--ink);
padding:0 12px;font:inherit;font-size:14.5px;cursor:pointer}}
.chips{{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:14px}}
.chip{{border:1px solid var(--line);background:var(--bg2);color:var(--ink2);border-radius:999px;
padding:7px 14px;font:inherit;font-size:13.5px;font-weight:620;cursor:pointer;transition:.16s;display:inline-flex;gap:7px;align-items:center}}
.chip i{{font-style:normal;opacity:.75}}
.chip b{{font-size:11.5px;opacity:.6;font-weight:700}}
.chip:hover{{border-color:var(--brand);color:var(--brand)}}
.chip.is-on{{background:var(--brand);border-color:var(--brand);color:#fff}}
.chip.is-on b{{opacity:.85}}
.rescount{{font-size:13.5px;color:var(--ink2);margin:0 0 18px}}
.empty{{display:none;padding:34px;text-align:center;color:var(--ink2);background:var(--bg3);border-radius:var(--radius)}}
.empty.on{{display:block}}

.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(285px,1fr));gap:18px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;
display:flex;flex-direction:column;transition:.2s;box-shadow:var(--shadow)}}
.card:hover{{transform:translateY(-3px);border-color:var(--brand)}}
.card-media{{position:relative;display:block;aspect-ratio:16/10;background:var(--bg3);overflow:hidden}}
.card-media img{{width:100%;height:100%;object-fit:cover;transition:.4s}}
.card:hover .card-media img{{transform:scale(1.045)}}
.ph-ico{{display:grid;place-items:center;height:100%;font-size:44px;color:var(--ink2);opacity:.4}}
.badge-new{{position:absolute;top:10px;inset-inline-start:10px;background:var(--accent);color:#1b1205;
font-size:11px;font-weight:800;padding:3px 9px;border-radius:999px;letter-spacing:.03em}}
.card-body{{padding:15px 16px 16px;display:flex;flex-direction:column;gap:8px;flex:1}}
.card-cat{{font-size:11px;font-weight:800;letter-spacing:.07em;text-transform:uppercase;color:var(--brand2)}}
.card-t{{font-size:16.5px;margin:0;line-height:1.3}}
.card-t a{{color:var(--ink)}}
.card-t a:hover{{color:var(--brand)}}
.card-d{{font-size:13.5px;color:var(--ink2);margin:0;line-height:1.55}}
.mdls{{display:flex;gap:5px;flex-wrap:wrap}}
.mdl{{font-size:11px;font-weight:700;background:var(--bg3);color:var(--ink2);padding:2px 8px;border-radius:6px}}
.card-meta{{display:flex;gap:12px;font-size:11.5px;color:var(--ink2);margin-top:auto;padding-top:8px;flex-wrap:wrap}}
.card-go{{font-size:13.5px;font-weight:700;margin-top:4px}}

.shots{{display:grid;grid-template-columns:repeat(auto-fill,minmax(176px,1fr));gap:12px}}
.shot{{position:relative;border-radius:11px;overflow:hidden;aspect-ratio:4/3;background:var(--bg3);border:1px solid var(--line)}}
.shot img{{width:100%;height:100%;object-fit:cover;transition:.35s}}
.shot:hover img{{transform:scale(1.07)}}
.shot span{{position:absolute;inset-inline:0;bottom:0;background:linear-gradient(transparent,rgba(0,0,0,.82));
color:#fff;font-size:11.5px;padding:18px 9px 8px;opacity:0;transition:.25s;line-height:1.35}}
.shot:hover span{{opacity:1}}

.vids{{display:grid;grid-template-columns:repeat(auto-fill,minmax(276px,1fr));gap:18px}}
.vid-btn{{position:relative;display:block;width:100%;padding:0;border:1px solid var(--line);background:var(--bg3);
border-radius:12px;overflow:hidden;cursor:pointer;aspect-ratio:16/9}}
.vid-btn img{{width:100%;height:100%;object-fit:cover}}
.play{{position:absolute;inset:0;margin:auto;width:58px;height:40px;border-radius:10px;background:rgba(0,0,0,.68);
transition:.2s}}
.play::after{{content:"";position:absolute;top:50%;left:50%;transform:translate(-42%,-50%);
border-style:solid;border-width:9px 0 9px 15px;border-color:transparent transparent transparent #fff}}
.vid-btn:hover .play{{background:#cc0000}}
.vid iframe{{width:100%;aspect-ratio:16/9;border:0;border-radius:12px;display:block}}
.vid-t{{font-size:13px;color:var(--ink2);margin:9px 0 0;line-height:1.45}}

.docs{{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:11px}}
.doc{{display:flex;align-items:center;gap:12px;background:var(--card);border:1px solid var(--line);
border-radius:11px;padding:12px 14px;transition:.18s}}
.doc:hover{{border-color:var(--brand);text-decoration:none;transform:translateY(-2px)}}
.doc-x{{font-size:10px;font-weight:800;background:var(--brand);color:#fff;padding:4px 7px;border-radius:5px;flex-shrink:0}}
.doc-t{{font-size:13.5px;color:var(--ink);flex:1;line-height:1.4;word-break:break-word}}
.doc-go{{font-size:12px;font-weight:700;color:var(--brand);flex-shrink:0}}

.posts{{display:grid;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));gap:18px}}
.post{{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:22px;
display:flex;flex-direction:column;box-shadow:var(--shadow)}}
.post-cat{{font-size:11px;font-weight:800;letter-spacing:.07em;text-transform:uppercase;color:var(--brand2)}}
.post h3{{font-size:19.5px;margin:7px 0 9px}}
.post-s{{color:var(--ink2);font-size:14.5px;margin:0;font-style:italic}}
.post-body{{display:none;margin-top:14px;border-top:1px solid var(--line);padding-top:14px}}
.post.open .post-body{{display:block}}
.post-body h4{{font-size:12px;font-weight:800;letter-spacing:.07em;text-transform:uppercase;
color:var(--brand);margin:16px 0 6px}}
.post-body h4:first-child{{margin-top:0}}
.post-body p{{font-size:14.5px;color:var(--ink2);margin:0;line-height:1.68}}
.post-more{{margin:14px 0 0}}
.post-more button{{background:none;border:0;color:var(--brand);font:inherit;font-size:14px;font-weight:700;
cursor:pointer;padding:0}}
.post-more button:hover{{text-decoration:underline}}

.faq{{background:var(--card);border:1px solid var(--line);border-radius:11px;margin-bottom:10px;overflow:hidden}}
.faq summary{{padding:15px 18px;cursor:pointer;font-weight:680;font-size:15.5px;list-style:none;
display:flex;justify-content:space-between;gap:14px;align-items:center}}
.faq summary::-webkit-details-marker{{display:none}}
.faq summary::after{{content:"+";font-size:21px;color:var(--brand);flex-shrink:0}}
.faq[open] summary::after{{content:"–"}}
.faq p{{padding:0 18px 17px;margin:0;color:var(--ink2);font-size:14.5px}}

.cta{{background:linear-gradient(135deg,var(--brand),color-mix(in srgb,var(--brand) 62%,#042e29));color:#fff;border:0}}
.cta h2,.cta .kick{{color:#fff}}
.cta .kick{{background:rgba(255,255,255,.17)}}
.cta p.lead2{{color:rgba(255,255,255,.9)}}
.cta .btn-p{{background:#fff;color:var(--brand)}}
.cta .btn-p:hover{{background:var(--accent);color:#1b1205}}
.cta .btn-s{{background:rgba(255,255,255,.1);color:#fff;border-color:rgba(255,255,255,.35)}}
.cta .btn-s:hover{{background:rgba(255,255,255,.2);color:#fff;border-color:#fff}}

footer.site{{background:var(--bg2);border-top:1px solid var(--line);padding:46px 0 24px;font-size:14px}}
.fgrid{{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:30px}}
footer h4{{font-size:12px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--ink2);margin-bottom:13px}}
footer ul{{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:9px}}
footer ul a{{color:var(--ink);display:inline-flex;gap:9px;align-items:center}}
footer ul a:hover{{color:var(--brand)}}
footer .fbrand img{{height:44px;margin-bottom:12px}}
footer .fbrand p{{color:var(--ink2);margin:0 0 6px;font-size:13.5px;max-width:34ch}}
.fbot{{border-top:1px solid var(--line);margin-top:32px;padding-top:18px;display:flex;justify-content:space-between;
gap:16px;flex-wrap:wrap;color:var(--ink2);font-size:12.5px}}
.ico{{width:19px;height:19px;flex-shrink:0;fill:currentColor;opacity:.78}}

#top{{position:fixed;inset-inline-end:22px;bottom:92px;width:42px;height:42px;border-radius:11px;
border:1px solid var(--line);background:var(--bg2);color:var(--ink);cursor:pointer;display:none;
place-items:center;font-size:17px;z-index:30;box-shadow:var(--shadow)}}
#top.on{{display:grid}}

[dir=rtl] .card-go,[dir=rtl] .cta-row{{direction:rtl}}
[dir=rtl] .play::after{{transform:translate(-58%,-50%) scaleX(-1)}}

@media(max-width:900px){{
.stats{{grid-template-columns:repeat(2,1fr)}}
.fgrid{{grid-template-columns:1fr 1fr}}
.menu{{display:none}}
}}
@media(max-width:560px){{
.hero{{padding:40px 0 30px}}
.brand span{{display:none}}
.fgrid{{grid-template-columns:1fr}}
section{{padding:42px 0}}
}}
@media(prefers-reduced-motion:reduce){{*{{animation:none!important;transition:none!important}}html{{scroll-behavior:auto}}}}
</style>
</head>
<body>
<a class="skip" href="#catalog">Skip to the equipment catalog</a>

<div class="topbar"><div class="wrap">
<span data-i18n="topbar">{t[topbar]}</span>
<a href="mailto:{mail}">{mail}</a>
</div></div>

<header class="site"><div class="wrap nav">
  <a class="brand" href="#top-anchor" id="top-anchor">
    <img src="{logo}" alt="Southern Machinery" width="300" height="83">
    <span data-i18n="brand_sub">{t[brand_sub]}</span>
  </a>
  <nav class="menu" aria-label="Main">
    <a href="#catalog" data-i18n="nav_catalog">{t[nav_catalog]}</a>
    <a href="#photos" data-i18n="nav_gallery">{t[nav_gallery]}</a>
    <a href="#videos" data-i18n="nav_videos">{t[nav_videos]}</a>
    <a href="#documents" data-i18n="nav_docs">{t[nav_docs]}</a>
    <a href="#insights" data-i18n="nav_insights">{t[nav_insights]}</a>
    <a href="#faq" data-i18n="nav_faq">{t[nav_faq]}</a>
    <a href="#contact" data-i18n="nav_contact">{t[nav_contact]}</a>
  </nav>
  <div class="tools">
    <button class="btn-i" id="themeBtn" type="button" title="{t[ui_theme_label]}"
      data-i18n-title="ui_theme_label" aria-label="{t[ui_theme_label]}">☀</button>
    <select class="lang" id="langSel" title="{t[ui_lang_label]}" data-i18n-title="ui_lang_label"
      aria-label="{t[ui_lang_label]}">{langopts}</select>
  </div>
</div></header>

<main>
<div class="hero"><div class="wrap">
  <span class="kick" data-i18n="hero_badge">{t[hero_badge]}</span>
  <h1><span data-i18n="hero_h1a">{t[hero_h1a]}</span> <em data-i18n="hero_h1b">{t[hero_h1b]}</em></h1>
  <p class="lead" data-i18n="hero_sub">{t[hero_sub]}</p>
  <div class="cta-row">
    <a class="btn btn-p" href="#catalog" data-i18n="hero_cta1">{t[hero_cta1]}</a>
    <a class="btn btn-s" href="#contact" data-i18n="hero_cta2">{t[hero_cta2]}</a>
  </div>
  <div class="stats">
    <div class="stat"><b data-i18n="stat1v">{total}</b><span data-i18n="stat1l">{t[stat1l]}</span></div>
    <div class="stat"><b data-i18n="stat2v">7</b><span data-i18n="stat2l">{t[stat2l]}</span></div>
    <div class="stat"><b data-i18n="stat3v">0</b><span data-i18n="stat3l">{t[stat3l]}</span></div>
    <div class="stat"><b data-i18n="stat4v">0</b><span data-i18n="stat4l">{t[stat4l]}</span></div>
  </div>
</div></div>

<section id="catalog"><div class="wrap">
  <span class="kick" data-i18n="search_kick">{t[search_kick]}</span>
  <h2 class="sec" data-i18n="search_h2">{t[search_h2]}</h2>
  <p class="lead2" data-i18n="search_lead">{t[search_lead]}</p>
  <div class="searchbar">
    <div class="sinput">
      <label class="sr" for="q" data-i18n="search_label">{t[search_label]}</label>
      <input id="q" type="search" autocomplete="off" placeholder="{t[search_ph]}" data-i18n-ph="search_ph">
    </div>
    <select class="sort" id="sortSel" aria-label="{t[sort_label]}" data-i18n-title="sort_label">
      <option value="cat" data-i18n="sort_cat">{t[sort_cat]}</option>
      <option value="az" data-i18n="sort_az">{t[sort_az]}</option>
      <option value="new" data-i18n="sort_new">{t[sort_new]}</option>
    </select>
    <button class="btn btn-s" id="resetBtn" type="button" data-i18n="filter_reset">{t[filter_reset]}</button>
  </div>
  <div class="chips" id="chips">{chips}</div>
  <p class="rescount" id="rescount"></p>
  <div class="grid" id="grid">{cards}</div>
  <div class="empty" id="empty" data-i18n="filter_none">{t[filter_none]}</div>
</div></section>

<section id="photos"><div class="wrap">
  <span class="kick" data-i18n="gal_kick">{t[gal_kick]}</span>
  <h2 class="sec" data-i18n="gal_h2">{t[gal_h2]}</h2>
  <p class="lead2" data-i18n="gal_lead">{t[gal_lead]}</p>
  <div class="shots" id="shots">{gallery}</div>
  <p class="rescount" style="margin-top:16px"><a href="{imghost}" target="_blank" rel="noopener"
     data-i18n="gal_note">{t[gal_note]}</a></p>
</div></section>

<section id="videos"><div class="wrap">
  <span class="kick" data-i18n="vid_kick">{t[vid_kick]}</span>
  <h2 class="sec" data-i18n="vid_h2">{t[vid_h2]}</h2>
  <p class="lead2" data-i18n="vid_lead">{t[vid_lead]}</p>
  <div class="vids" id="vids">{videos}</div>
  <p class="rescount" style="margin-top:18px"><a class="btn btn-s" href="{vidboard}" target="_blank"
     rel="noopener" data-i18n="vid_board">{t[vid_board]}</a></p>
</div></section>

<section id="documents"><div class="wrap">
  <span class="kick" data-i18n="doc_kick">{t[doc_kick]}</span>
  <h2 class="sec" data-i18n="doc_h2">{t[doc_h2]}</h2>
  <p class="lead2" data-i18n="doc_lead">{t[doc_lead]}</p>
  <div class="docs" id="docs">{docsec}</div>
  <p class="rescount" style="margin-top:18px"><a class="btn btn-s" href="{catboard}" target="_blank"
     rel="noopener" data-i18n="doc_board">{t[doc_board]}</a></p>
</div></section>

<section id="insights"><div class="wrap">
  <span class="kick" data-i18n="ins_kick">{t[ins_kick]}</span>
  <h2 class="sec" data-i18n="ins_h2">{t[ins_h2]}</h2>
  <p class="lead2" data-i18n="ins_lead">{t[ins_lead]}</p>
  <div class="posts">{posts}</div>
</div></section>

<section id="faq"><div class="wrap">
  <span class="kick" data-i18n="faq_kick">{t[faq_kick]}</span>
  <h2 class="sec" data-i18n="faq_h2">{t[faq_h2]}</h2>
  <div style="margin-top:22px">{faq}</div>
</div></section>

<section id="contact" class="cta"><div class="wrap">
  <span class="kick" data-i18n="cta_kick">{t[cta_kick]}</span>
  <h2 class="sec" data-i18n="cta_h2">{t[cta_h2]}</h2>
  <p class="lead2" data-i18n="cta_lead">{t[cta_lead]}</p>
  <div class="cta-row">
    <a class="btn btn-p" href="mailto:{mail}?subject=Southern%20Machinery%20equipment%20enquiry"
       data-i18n="cta_mail">{t[cta_mail]}</a>
    <a class="btn btn-s" href="{wa}" target="_blank" rel="noopener" data-i18n="cta_wa">{t[cta_wa]}</a>
    <a class="btn btn-s" href="{catboard}" target="_blank" rel="noopener" data-i18n="cta_catalog">{t[cta_catalog]}</a>
    <a class="btn btn-s" href="{imghost}" target="_blank" rel="noopener" data-i18n="cta_images">{t[cta_images]}</a>
  </div>
</div></section>
</main>

<footer class="site"><div class="wrap">
  <div class="fgrid">
    <div class="fbrand">
      <img src="{logo}" alt="Southern Machinery" width="300" height="83">
      <p data-i18n="foot_rights">{t[foot_rights]}</p>
      <p data-i18n="foot_addr">{t[foot_addr]}</p>
    </div>
    <div>
      <h4 data-i18n="foot_follow">{t[foot_follow]}</h4>
      <ul>
        <li><a href="{li_co}" target="_blank" rel="noopener me"><svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M4.98 3.5A2.5 2.5 0 112.5 6 2.5 2.5 0 014.98 3.5zM3 8.98h4V21H3zM9.5 8.98h3.83v1.64h.05a4.2 4.2 0 013.78-2.08C21.1 8.54 22 11 22 14.24V21h-4v-6c0-1.43-.03-3.27-2-3.27s-2.3 1.56-2.3 3.17V21h-4z"/></svg><span data-i18n="foot_li_co">{t[foot_li_co]}</span></a></li>
        <li><a href="{li_me}" target="_blank" rel="noopener"><svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M4.98 3.5A2.5 2.5 0 112.5 6 2.5 2.5 0 014.98 3.5zM3 8.98h4V21H3zM9.5 8.98h3.83v1.64h.05a4.2 4.2 0 013.78-2.08C21.1 8.54 22 11 22 14.24V21h-4v-6c0-1.43-.03-3.27-2-3.27s-2.3 1.56-2.3 3.17V21h-4z"/></svg><span data-i18n="foot_li_me">{t[foot_li_me]}</span></a></li>
        <li><a href="{tw}" target="_blank" rel="noopener"><svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M18.9 2H22l-7.1 8.1L23.2 22h-6.6l-5.2-6.8L5.5 22H2.4l7.6-8.7L1.2 2h6.8l4.7 6.2zm-1.1 18h1.8L7.3 3.8H5.4z"/></svg><span data-i18n="foot_tw">{t[foot_tw]}</span></a></li>
        <li><a href="{fb}" target="_blank" rel="noopener"><svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M22 12a10 10 0 10-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.3c-1.2 0-1.6.8-1.6 1.6V12h2.8l-.4 2.9h-2.4v7A10 10 0 0022 12z"/></svg><span data-i18n="foot_fb">{t[foot_fb]}</span></a></li>
        <li><a href="{yt}" target="_blank" rel="noopener"><svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M23 12s0-3.2-.4-4.7a2.5 2.5 0 00-1.8-1.8C19.3 5 12 5 12 5s-7.3 0-8.8.5A2.5 2.5 0 001.4 7.3C1 8.8 1 12 1 12s0 3.2.4 4.7a2.5 2.5 0 001.8 1.8C4.7 19 12 19 12 19s7.3 0 8.8-.5a2.5 2.5 0 001.8-1.8C23 15.2 23 12 23 12zM9.8 15.3V8.7l6 3.3z"/></svg><span data-i18n="foot_yt">{t[foot_yt]}</span></a></li>
      </ul>
    </div>
    <div>
      <h4 data-i18n="foot_browse">{t[foot_browse]}</h4>
      <ul>
        <li><a href="{catboard}" target="_blank" rel="noopener" data-i18n="foot_cat_board">{t[foot_cat_board]}</a></li>
        <li><a href="{imghost}" target="_blank" rel="noopener" data-i18n="foot_img_board">{t[foot_img_board]}</a></li>
        <li><a href="{vidboard}" target="_blank" rel="noopener" data-i18n="vid_board">{t[vid_board]}</a></li>
        <li><a href="#catalog" data-i18n="nav_catalog">{t[nav_catalog]}</a></li>
      </ul>
    </div>
    <div>
      <h4 data-i18n="foot_contact">{t[foot_contact]}</h4>
      <ul>
        <li><a href="mailto:{mail}"><svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 4H4a2 2 0 00-2 2v12a2 2 0 002 2h16a2 2 0 002-2V6a2 2 0 00-2-2zm0 4.2l-8 5-8-5V6l8 5 8-5z"/></svg><span data-i18n="foot_email">{t[foot_email]}</span></a></li>
        <li><a href="{wa}" target="_blank" rel="noopener"><svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 00-8.6 15l-1.3 4.7 4.8-1.3A10 10 0 1012 2zm5.8 14.2c-.2.7-1.4 1.3-2 1.4-.5.1-1.2.1-1.9-.1-2.7-.9-4.5-3.6-4.6-3.8-.1-.2-1.1-1.5-1.1-2.8s.7-2 .9-2.2c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 2c.1.2.1.4 0 .5l-.3.5-.3.3c-.1.1-.3.3-.1.6.1.3.6 1.1 1.4 1.7 1 .8 1.7 1 2 1.2.2.1.4.1.5-.1l.7-.9c.2-.2.4-.2.6-.1l1.9.9c.2.1.4.2.4.3.1.1.1.6-.1 1.2z"/></svg><span data-i18n="foot_wa">{t[foot_wa]}</span></a></li>
        <li><a href="#contact" data-i18n="cta_kick">{t[cta_kick]}</a></li>
      </ul>
    </div>
  </div>
  <div class="fbot">
    <span>© {year} Shenzhen Southern Machinery Sales and Service Co., Ltd</span>
    <span><span data-i18n="foot_sync">{t[foot_sync]}</span> <time datetime="{stamp}">{stamp}</time></span>
  </div>
</div></footer>

<button id="top" type="button" title="{t[ui_back_top]}" data-i18n-title="ui_back_top"
  aria-label="{t[ui_back_top]}">↑</button>

<script>
/* ---------------------------------------------------------------- data */
var I18N={i18n};
var ROWS={rows};
var LANGS={langs};
var RTL={rtl};
var LANG_KEY="sm_hub_lang", THEME_KEY="sm_hub_theme";
var $=function(s,r){{return (r||document).querySelector(s)}};
var $$=function(s,r){{return Array.prototype.slice.call((r||document).querySelectorAll(s))}};
function t(k,lg){{var d=I18N[lg]||I18N.en;return (d&&d[k]!=null)?d[k]:(I18N.en[k]!=null?I18N.en[k]:k)}}

/* ------------------------------------------------------------- language */
function applyLang(lang,persist){{
  if(LANGS.indexOf(lang)<0) lang="en";
  var h=document.documentElement;
  h.setAttribute("lang",lang);
  h.setAttribute("dir",RTL.indexOf(lang)>=0?"rtl":"ltr");
  $$("[data-i18n]").forEach(function(el){{
    var v=t(el.getAttribute("data-i18n"),lang);
    if(el.hasAttribute("data-i18n-html")) el.innerHTML=v; else el.textContent=v;
  }});
  $$("[data-i18n-title]").forEach(function(el){{
    el.setAttribute("title",t(el.getAttribute("data-i18n-title"),lang));
    if(el.hasAttribute("aria-label")) el.setAttribute("aria-label",t(el.getAttribute("data-i18n-title"),lang));
  }});
  $$("[data-i18n-ph]").forEach(function(el){{
    el.setAttribute("placeholder",t(el.getAttribute("data-i18n-ph"),lang));
  }});
  $$(".post.open .post-more button").forEach(function(b){{b.textContent=t("ui_less",lang)}});
  document.title=t("seo_title",lang);
  var m;
  if((m=$('meta[name="description"]'))) m.setAttribute("content",t("seo_desc",lang));
  if((m=$('meta[name="keywords"]'))) m.setAttribute("content",t("seo_keys",lang));
  if((m=$('meta[property="og:title"]'))) m.setAttribute("content",t("seo_title",lang));
  if((m=$('meta[property="og:description"]'))) m.setAttribute("content",t("seo_desc",lang));
  if((m=$('meta[name="twitter:title"]'))) m.setAttribute("content",t("seo_title",lang));
  if((m=$('meta[name="twitter:description"]'))) m.setAttribute("content",t("seo_desc",lang));
  $("#langSel").value=lang;
  if(persist!==false){{try{{localStorage.setItem(LANG_KEY,lang)}}catch(e){{}}}}
  render();
}}

/* ---------------------------------------------------------------- theme */
function applyTheme(mode,persist){{
  if(mode!=="dark") mode="light";
  document.documentElement.setAttribute("data-theme",mode);
  var b=$("#themeBtn"); if(b) b.textContent=mode==="dark"?"☾":"☀";
  var m=$('meta[name="theme-color"]');
  if(m) m.setAttribute("content",mode==="dark"?"#0b1514":"#0c665c");
  if(persist!==false){{try{{localStorage.setItem(THEME_KEY,mode)}}catch(e){{}}}}
}}

/* --------------------------------------------------------- catalog search */
var CARDS=[], state={{q:"",cat:"all",sort:"cat"}};
function render(){{
  var lang=document.documentElement.getAttribute("lang")||"en";
  var q=state.q.trim().toLowerCase();
  var terms=q?q.split(/\s+/):[];
  var shown=0;
  CARDS.forEach(function(c,i){{
    var row=ROWS[i];
    var okCat=state.cat==="all"||row.c===state.cat;
    var okQ=true;
    for(var k=0;k<terms.length;k++){{ if(row.s.indexOf(terms[k])<0){{okQ=false;break}} }}
    var on=okCat&&okQ;
    c.style.display=on?"":"none";
    if(on) shown++;
  }});
  var rc=$("#rescount");
  if(rc) rc.textContent=t("filter_results",lang).replace("{{n}}",shown).replace("{{total}}",ROWS.length);
  $("#empty").classList.toggle("on",shown===0);

  /* gallery, videos and documents follow the active product line */
  ["#shots .shot","#vids .vid","#docs .doc"].forEach(function(sel){{
    $$(sel).forEach(function(el){{
      el.style.display=(state.cat==="all"||el.getAttribute("data-cat")===state.cat)?"":"none";
    }});
  }});
}}
function sortGrid(){{
  var g=$("#grid"), idx=CARDS.map(function(c,i){{return i}});
  var order={{cat:function(a,b){{return a-b}},
    az:function(a,b){{return CARDS[a].querySelector(".card-t").textContent.trim()
      .localeCompare(CARDS[b].querySelector(".card-t").textContent.trim())}},
    new:function(a,b){{return (ROWS[b].u||"").localeCompare(ROWS[a].u||"")}}}};
  idx.sort(order[state.sort]||order.cat);
  idx.forEach(function(i){{g.appendChild(CARDS[i])}});
}}

/* ------------------------------------------------------------------ init */
(function init(){{
  var th=null; try{{th=localStorage.getItem(THEME_KEY)}}catch(e){{}}
  if(!th&&window.matchMedia&&window.matchMedia("(prefers-color-scheme: dark)").matches) th="dark";
  applyTheme(th||"light",false);

  CARDS=$$("#grid .card");

  var lg=null;
  try{{lg=new URLSearchParams(location.search).get("lang")}}catch(e){{}}
  if(!lg){{try{{lg=localStorage.getItem(LANG_KEY)}}catch(e){{}}}}
  if(!lg){{
    var nv=(navigator.language||"en").slice(0,2).toLowerCase();
    if(LANGS.indexOf(nv)>=0) lg=nv;
  }}
  applyLang(lg||"en",false);

  try{{
    var pq=new URLSearchParams(location.search).get("q");
    if(pq){{state.q=pq;$("#q").value=pq;render()}}
  }}catch(e){{}}

  $("#themeBtn").addEventListener("click",function(){{
    applyTheme(document.documentElement.getAttribute("data-theme")==="dark"?"light":"dark");
  }});
  $("#langSel").addEventListener("change",function(){{applyLang(this.value)}});

  var tm;
  $("#q").addEventListener("input",function(){{
    var v=this.value; clearTimeout(tm);
    tm=setTimeout(function(){{state.q=v;render()}},110);
  }});
  $("#sortSel").addEventListener("change",function(){{state.sort=this.value;sortGrid()}});
  $("#resetBtn").addEventListener("click",function(){{
    state.q="";state.cat="all";state.sort="cat";
    $("#q").value="";$("#sortSel").value="cat";
    $$("#chips .chip").forEach(function(c){{c.classList.toggle("is-on",c.getAttribute("data-cat")==="all")}});
    sortGrid();render();
  }});
  $$("#chips .chip").forEach(function(c){{
    c.addEventListener("click",function(){{
      state.cat=c.getAttribute("data-cat");
      $$("#chips .chip").forEach(function(x){{x.classList.remove("is-on")}});
      c.classList.add("is-on");
      render();
    }});
  }});

  /* YouTube facade: nothing is requested from YouTube until a thumbnail is clicked */
  $$(".vid-btn").forEach(function(b){{
    b.addEventListener("click",function(){{
      var w=b.parentNode, id=w.getAttribute("data-yt");
      var f=document.createElement("iframe");
      f.src="https://www.youtube-nocookie.com/embed/"+id+"?autoplay=1&rel=0";
      f.title=w.querySelector(".vid-t").textContent;
      f.loading="lazy"; f.allow="accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture";
      f.allowFullscreen=true;
      w.replaceChild(f,b);
    }});
  }});

  $$(".post-more button").forEach(function(b){{
    b.addEventListener("click",function(){{
      var p=b.closest(".post"), open=p.classList.toggle("open");
      var lang=document.documentElement.getAttribute("lang")||"en";
      b.textContent=t(open?"ui_less":"ui_more",lang);
    }});
  }});

  var tb=$("#top");
  window.addEventListener("scroll",function(){{tb.classList.toggle("on",window.scrollY>700)}},{{passive:true}});
  tb.addEventListener("click",function(){{window.scrollTo({{top:0,behavior:"smooth"}})}});
}})();
</script>

<!-- Chatwoot live chat, pinned bottom right on every page -->
<script>
window.chatwootSettings = {{"position":"right","type":"standard","launcherTitle":"Southern Machinery Global Support"}};
(function(d,t){{
  var BASE_URL="https://chat.smthelp.com";
  var g=d.createElement(t),s=d.getElementsByTagName(t)[0];
  g.src=BASE_URL+"/packs/js/sdk.js";
  g.async=true;
  s.parentNode.insertBefore(g,s);
  g.onload=function(){{
    window.chatwootSDK.run({{websiteToken:'saMcpgSupcmd1VQwytgPLfbK',baseUrl:BASE_URL}});
  }};
}})(document,"script");
</script>
</body>
</html>
"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="exit 1 when the hub is stale")
    args = ap.parse_args()

    out = build()
    old = ""
    if os.path.exists(OUT_PATH):
        with open(OUT_PATH, encoding="utf-8") as fh:
            old = fh.read()

    def strip_stamp(s: str) -> str:
        return re.sub(r'<time datetime="\d{4}-\d{2}-\d{2}">\d{4}-\d{2}-\d{2}</time>', "", s)

    if args.check:
        if strip_stamp(old) != strip_stamp(out):
            print("hub is out of date; run: python3 tools/build_hub.py")
            return 1
        print("hub is current")
        return 0

    if strip_stamp(old) == strip_stamp(out):
        print("no content change: %s" % OUT_NAME)
        return 0

    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(out)
    print("wrote %s (%.0f KB)" % (OUT_NAME, len(out.encode()) / 1024))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
