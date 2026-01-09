#!/usr/bin/env python3
"""
Inline HTML for DocRaptor/Prince PDF with:
- CSS/JS inlining (JS stripped)
- Host rewrite (for anchors/non-asset cases)
- Tight margins
- Robust table fragmentation using native <table> (no clones)
- Merge inline code runs into single ```…``` blocks
- Normalize existing ```…``` blocks
- Embed NVIDIASans as data URI via @font-face (variable woff2)
- Print-only font override (configurable scope)
- Anchor fix: rewrite absolute /pdf/#... links to local #...
- TEST mode kept (DocRaptor watermark remains)

New:
- Playwright downloader to render JS and save fully-populated HTML
- Dynamic path overrides based on slug (HTML_FILE/ASSET_DIR/INLINED_HTML/OUTPUT_PDF)
- Fast asset download (requests.Session + parallel workers)
- UTF-8 enforced on all reads/writes to prevent mojibake
- Prince baseurl set to original source URL to avoid file:// links in PDFs
- Asset host rewrite DISABLED by default throughout discovery, download, and inlining
"""
import os
import re
import time
import mimetypes
import base64
import pathlib
import unicodedata
import urllib.parse as urlparse
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from bs4 import BeautifulSoup, Tag, NavigableString
import docraptor

# Playwright (JS-rendering)
try:
    from playwright.sync_api import sync_playwright
    PLAYWRIGHT_AVAILABLE = True
except Exception:
    PLAYWRIGHT_AVAILABLE = False

# =========================
# CONFIG (defaults; overridden when --url is used)
# =========================
HTML_FILE = "html-save/cumulus-linux-515-pdf.html"
ASSET_DIR = "html-save/cumulus-linux-515-pdf_files"
INLINED_HTML = "cumulus-linux-515-inlined.html"
OUTPUT_PDF = "cumulus-linux-515.pdf"

API_KEY_FALLBACK = "0uH2Qnz3ewlkBD1BmE3"  # prefer env
API_KEY = os.getenv("DOCRAPTOR_API_KEY", API_KEY_FALLBACK)

EMBED_CSS_IMAGES = True
EMBED_HTML_IMAGES = True
EMBED_FONTS = True  # ensure font embedding via @font-face happens

# Font override scope:
# "print" => PDF only (recommended)
# "all"   => both screen & print
FONT_SCOPE = "print"
FORCE_FONT_FAMILY = "'NVIDIASans'"
PRESERVE_MONOSPACE_FOR_CODE = True
EMBED_FAVICON = False

# Host rewrite map (used only when explicitly desired)
ENABLE_HOST_REWRITE = True
HOST_REWRITE_MAP = {
    "https://pdf-testing.d5j8yik1ci5ec.amplifyapp.com/networking-ethernet-software":
        "https://docs.nvidia.com/networking-ethernet-software",
}

# NEW: disable host rewrite for assets end-to-end
ENABLE_HOST_REWRITE_FOR_ASSETS = False  # set True only when production has matching hashed assets
ALLOWED_HOSTS = {"images.nvidia.com"}  # allowed external asset host for font embedding

REQUEST_HEADERS = {"User-Agent": "NVIDIA-Docs-Inliner/2.7 (+DocRaptor/Prince)"}
REQUEST_TIMEOUT = 25
POLL_INTERVAL = 5

# Prince/DocRaptor
PRINCE_MEDIA = "print"
PRINCE_COLOR_SPACE = "rgb"
ORIGINAL_URL = None  # set at runtime from --url

# Page margins
PAGE_MARGIN_TOP_MM = 9
PAGE_MARGIN_RIGHT_MM = 8
PAGE_MARGIN_BOTTOM_MM = 9  # +2 mm to keep content above TEST watermark band
PAGE_MARGIN_LEFT_MM = 8

FONT_MIME = {
    ".woff2": "font/woff2",
    ".woff": "font/woff",
    ".ttf": "font/ttf",
    ".otf": "font/otf",
    ".eot": "application/vnd.ms-fontobject",
    ".svg": "image/svg+xml",
}

# NVIDIASans variable font URL (official source)
NVIDIASANS_VAR_WGHT_URL = (
    "https://images.nvidia.com/etc/designs/nvidiaGDC/clientlibs_base/fonts/"
    "nvidia-sans/GLOBAL/var/NVIDIASansVF_W_Wght.woff2"
)

# Canonical docs host (used for anchor rewrite logic)
DOCS_HOST = "docs.nvidia.com"

# =========================
# Utilities
# =========================
resource_cache = {}

def is_http_url(href: str) -> bool:
    return href.startswith(("http://", "https://"))

def host_allowed(href: str) -> bool:
    if ALLOWED_HOSTS is None or not is_http_url(href):
        return True
    host = urlparse.urlparse(href).hostname or ""
    return host in ALLOWED_HOSTS

def infer_mime(u: str, default: str = "application/octet-stream") -> str:
    guessed, _ = mimetypes.guess_type(u)
    return guessed or default

def to_data_uri(raw: bytes, mime: str) -> str:
    return f"data:{mime};base64,{base64.b64encode(raw).decode('ascii')}"

def normalize_and_rewrite_url(u: str) -> str:
    """Host rewrite for non-asset cases (e.g., anchors) only."""
    if not u or u.startswith("#"):
        return u
    if not ENABLE_HOST_REWRITE:
        return u
    for old, new in HOST_REWRITE_MAP.items():
        if u.startswith(old):
            return new + u[len(old):]
    return u

def maybe_rewrite_for_asset(u: str) -> str:
    """Apply host rewrite to assets only if explicitly enabled."""
    if not ENABLE_HOST_REWRITE_FOR_ASSETS:
        return u
    return normalize_and_rewrite_url(u)

def read_local_bytes(base_dir: str, href: str) -> bytes:
    clean = urlparse.urlparse(href)
    rel = clean.path.lstrip("/")
    candidate = pathlib.Path(base_dir) / rel
    if candidate.is_file():
        return candidate.read_bytes()
    html_dir = pathlib.Path(HTML_FILE).parent
    alt = html_dir / rel
    if alt.is_file():
        return alt.read_bytes()
    for p in pathlib.Path(base_dir).rglob(pathlib.Path(rel).name):
        try:
            return p.read_bytes()
        except Exception:
            pass
    raise FileNotFoundError(f"Local asset not found: {href}")

def fetch_http_bytes(url: str) -> bytes:
    url = maybe_rewrite_for_asset(url)
    resp = requests.get(url, headers=REQUEST_HEADERS, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()
    return resp.content

def get_resource_bytes(href: str, base_dir: str) -> bytes:
    href = maybe_rewrite_for_asset(href)
    key = f"BYTES::{href}"
    if key in resource_cache:
        return resource_cache[key][0]
    if not host_allowed(href):
        raise PermissionError(f"Host not allowed for embedding: {href}")
    raw = fetch_http_bytes(href) if is_http_url(href) else read_local_bytes(base_dir, href)
    resource_cache[key] = (raw, infer_mime(href))
    return raw

def get_resource_text(href: str, base_dir: str) -> str:
    href = maybe_rewrite_for_asset(href)
    key = f"TEXT::{href}"
    if key in resource_cache:
        return resource_cache[key][0].decode("utf-8", errors="replace")
    raw = get_resource_bytes(href, base_dir)
    resource_cache[key] = (raw, infer_mime(href))
    return raw.decode("utf-8", errors="replace")

def to_data_uri_from(href: str, base_dir: str) -> str:
    href = maybe_rewrite_for_asset(href)
    raw = get_resource_bytes(href, base_dir)
    mime = infer_mime(href)
    return to_data_uri(raw, mime)

# =========================
# CSS rewriting
# =========================
IMPORT_RE = re.compile(r'@import\s+\(?:url\(\)?[\"\']?([^\\"\'\)]+)[\"\']?\)?\s*;', re.I)
URL_RE    = re.compile(r'url\(\s*[\"\']?([^\\"\'\)]+)[\"\']?\s*\)', re.I)

def inline_css_imports(css_text: str, base_dir: str) -> str:
    out = css_text
    while True:
        m = IMPORT_RE.search(out)
        if not m: break
        import_url = m.group(1).strip()
        import_url = maybe_rewrite_for_asset(import_url)
        try:
            imported = get_resource_text(import_url, base_dir)
            imported = inline_css_imports(imported, base_dir)
            imported = rewrite_css_urls(imported, base_dir)
            out = out[:m.start()] + imported + out[m.end():]
        except Exception:
            out = out[:m.start()] + out[m.end():]
    return out

def rewrite_css_urls(css_text: str, base_dir: str) -> str:
    def repl(m: re.Match) -> str:
        u = m.group(1).strip()
        u = maybe_rewrite_for_asset(u)
        if u.startswith("data:") or u.startswith("#"):
            return m.group(0)
        try:
            data_uri = to_data_uri_from(u, base_dir)
            return f"url({data_uri})"
        except Exception:
            return f"url({u})"
    return URL_RE.sub(repl, css_text)

def inline_stylesheet_href(href: str, base_dir: str) -> str:
    href = maybe_rewrite_for_asset(href)
    css = get_resource_text(href, base_dir)
    css = inline_css_imports(css, base_dir)
    css = rewrite_css_urls(css, base_dir)
    return css

# =========================
# HTML processing
# =========================
def extract_site_style_hints(soup: BeautifulSoup):
    hints = {
        "color_fg": "#111111",
        "color_bg": "#ffffff",
        "color_link": "#76B900",
        "color_heading": "#0f0f0f",
        "base_px": 16.0,
    }

    style_texts = []
    for style in soup.find_all("style"):
        if style.string:
            style_texts.append(style.string)
    big = "\n".join(style_texts)

    for m in re.finditer(r":root\s*\{([^\}*]*)\}", big, re.I | re.S):
        block = m.group(1)
        for var, key in [
            ("--color-fg", "color_fg"),
            ("--color-bg", "color_bg"),
            ("--color-link", "color_link"),
            ("--color-heading", "color_heading"),
            ("--font-size-base", "base_px"),
        ]:
            vm = re.search(rf"{re.escape(var)}\s*:\s*([^;]+);", block, re.I)
            if vm:
                val = vm.group(1).strip()
                if key == "base_px":
                    pxm = re.search(r"([\d.]+)\s*px", val, re.I)
                    if pxm:
                        hints["base_px"] = float(pxm.group(1))
                else:
                    hints[key] = val

    html_block = re.search(r"html\s*\{[^\}]*font-size\s*:\s*([^\};]+)", big, re.I | re.S)
    if html_block:
        pxm = re.search(r"([\d.]+)\s*px", html_block.group(0), re.I)
        if pxm:
            hints["base_px"] = float(pxm.group(1))

    a_color = re.search(r"\ba\s*[,:{][^\{]*\{[^\}]*color\s*:\s*([^;]+);", big, re.I | re.S)
    if a_color:
        hints["color_link"] = a_color.group(1).strip()

    return hints

def inject_nonfont_brand_css(soup: BeautifulSoup, hints):
    head = soup.head or soup.new_tag("head")
    if not soup.head:
        soup.insert(0, head)

    css = f"""
:root {{
  --color-fg: {hints['color_fg']};
  --color-bg: {hints['color_bg']};
  --color-link: {hints['color_link']};
  --color-link-visited: {hints['color_link']};
  --color-heading: {hints['color_heading']};
  --font-size-base: {hints['base_px']}px;
}}
html, body {{
  font-size: var(--font-size-base);
  line-height: 1.6;
  margin: 0;
  color: var(--color-fg);
  background: var(--color-bg);
}}
a, a:visited {{
  color: var(--color-link);
  text-decoration: underline;
}}
@page {{
  size: Letter;
  margin: {PAGE_MARGIN_TOP_MM}mm {PAGE_MARGIN_RIGHT_MM}mm {PAGE_MARGIN_BOTTOM_MM}mm {PAGE_MARGIN_LEFT_MM}mm;
}}

/* Neutralize scroll containers for print/screen */
.scroll {{
  overflow: visible !important;
  height: auto !important;
  max-height: none !important;
  position: static !important;
  clear: both !important;
}}
"""
    style_tag = soup.new_tag("style")
    style_tag.string = css
    head.insert(0, style_tag)

def inline_link_styles(soup: BeautifulSoup, base_dir: str):
    for link in list(soup.find_all("link")):
        rel = [r.lower() for r in (link.get("rel") or [])]
        href = link.get("href")

        # DO NOT host-rewrite href here; we embed styles directly
        if href and ("stylesheet" in rel):
            try:
                css = inline_stylesheet_href(href, base_dir)
                style_tag = soup.new_tag("style")
                style_tag.string = css
                link.replace_with(style_tag)
            except Exception:
                link.decompose()
            continue

        if any(r in {"preload", "prefetch", "preconnect"} for r in rel):
            link.decompose()
            continue

        if any(r in {"icon", "shortcut icon"} for r in rel):
            if not EMBED_FAVICON:
                link.decompose()
                continue
            if href:
                try:
                    link["href"] = to_data_uri_from(href, base_dir)
                except Exception:
                    link.decompose()
                    continue

def strip_scripts_and_handlers(soup: BeautifulSoup):
    for script in soup.find_all("script"):
        script.decompose()
    for tag in soup.find_all(True):
        for attr in list(tag.attrs):
            if attr.lower().startswith("on"):
                del tag.attrs[attr]

def expand_hidden_content(soup: BeautifulSoup):
    for d in soup.find_all("details"):
        d["open"] = "open"

    head = soup.head or soup.new_tag("head")
    if not soup.head:
        soup.insert(0, head)
    reveal = soup.new_tag("style")
    reveal.string = "details > summary { display: list-item; }"
    head.append(reveal)

    # Ensure UTF-8 meta is present
    if not soup.find("meta", attrs={"charset": True}):
        meta = soup.new_tag("meta", charset="utf-8")
        head.insert(0, meta)

def embed_inline_style_attrs(soup: BeautifulSoup, base_dir: str):
    for tag in soup.find_all(style=True):
        style_text = tag.get("style") or ""
        try:
            tag["style"] = rewrite_css_urls(style_text, base_dir)
        except Exception:
            tag["style"] = style_text

def _embed_srcset(srcset: str, base_dir: str) -> str:
    parts = [p.strip() for p in srcset.split(",") if p.strip()]
    out = []
    for part in parts:
        tokens = part.split()
        url = tokens[0]
        url = maybe_rewrite_for_asset(url)
        desc = " ".join(tokens[1:]) if len(tokens) > 1 else ""
        if url.startswith("data:"):
            out.append(part); continue
        try:
            data_uri = to_data_uri_from(url, base_dir)
            out.append(data_uri + (" " + desc if desc else ""))
        except Exception:
            out.append(part)
    return ", ".join(out)

def embed_html_images(soup: BeautifulSoup, base_dir: str):
    if not EMBED_HTML_IMAGES:
        return
    for img in soup.find_all("img", src=True):
        src = img["src"]
        src = maybe_rewrite_for_asset(src)
        img["src"] = src
        if not src.startswith("data:"):
            try:
                img["src"] = to_data_uri_from(src, base_dir)
            except Exception:
                pass

        srcset = img.get("srcset")
        if srcset:
            try:
                img["srcset"] = _embed_srcset(srcset, base_dir)
            except Exception:
                pass

    for source in soup.find_all("source"):
        srcset = source.get("srcset")
        if srcset:
            try:
                source["srcset"] = _embed_srcset(srcset, base_dir)
            except Exception:
                pass

        src = source.get("src")
        if src:
            src = maybe_rewrite_for_asset(src)
            source["src"] = src
            if not src.startswith("data:"):
                try:
                    source["src"] = to_data_uri_from(src, base_dir)
                except Exception:
                    pass

# =========================
# Embed NVIDIASans via @font-face (data URI)
# =========================
def inject_nvidia_sans_fontface(soup: BeautifulSoup, base_dir: str, scope: str = "print"):
    if not EMBED_FONTS:
        return

    head = soup.head or soup.new_tag("head")
    if not soup.head:
        soup.insert(0, head)

    try:
        font_data_uri = to_data_uri_from(NVIDIASANS_VAR_WGHT_URL, base_dir)
    except Exception as e:
        warn = soup.new_tag("!--")
        warn.string = f" Failed to fetch NVIDIASans WOFF2: {e} "
        head.append(warn)
        return

    face_css = f"""
@font-face {{
  font-family: {FORCE_FONT_FAMILY};
  src: url('{font_data_uri}') format('woff2');
  font-weight: 100 1000;
  font-stretch: 25% 151%;
  font-style: normal;
}}
"""
    override_prefix = "" if scope == "all" else "@media print {\n"
    override_suffix = "" if scope == "all" else "\n}"

    mono = "'Oxygen Mono','Fira Mono','SFMono-Regular',Menlo,Consolas,'Liberation Mono',monospace"
    use_css = f"""
{override_prefix}
html, body, .content, article, section, p, li, td, th {{
  font-family: {FORCE_FONT_FAMILY}, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif !important;
  font-synthesis: none !important;
}}
code, pre, kbd, samp {{
  font-family: {mono} !important;
}}
{override_suffix}
"""
    style_tag = soup.new_tag("style")
    style_tag.string = face_css + "\n" + use_css
    head.append(style_tag)

# =========================
# Merge contiguous inline code lines to a single <pre>
# =========================
def merge_inline_code_runs_into_pre(soup: BeautifulSoup):
    def is_code_para(tag: Tag) -> bool:
        if not isinstance(tag, Tag): return False
        if tag.name not in ("p", "div"): return False
        codes = [c for c in tag.children if isinstance(c, Tag) and c.name == "code"]
        non_ws_text = [t for t in tag.children if isinstance(t, NavigableString) and t.strip()]
        return len(codes) == 1 and len(non_ws_text) == 0

    for container in soup.select(".book-tabs-content, .markdown-inner, section, article, .content"):
        kids = list(container.children)
        i = 0
        while i < len(kids):
            run = []
            while i < len(kids) and isinstance(kids[i], Tag) and is_code_para(kids[i]):
                run.append(kids[i]); i += 1
            if len(run) >= 2:
                lines = [r.find("code", recursive=False).get_text() for r in run]
                pre = soup.new_tag("pre")
                code = soup.new_tag("code")
                code.string = "\n".join(lines)
                pre.append(code)
                run[0].insert_before(pre)
                for r in run: r.decompose()
                kids = list(container.children)
            else:
                i += 1

# =========================
# Normalize blocks
# =========================
def normalize_pre_code_blocks(soup: BeautifulSoup):
    for pre in soup.find_all("pre"):
        txt = pre.get_text("\n")
        for c in list(pre.children):
            c.extract()
        code = soup.new_tag("code")
        code.string = txt
        pre.append(code)

# =========================
# Unhide tab content
# =========================
def unhide_tab_content(soup: BeautifulSoup):
    for el in soup.select(".book-tabs, .book-tabs-content, .markdown-inner, .tab-content, .tab-pane"):
        for attr in ("aria-hidden", "hidden"):
            if el.has_attr(attr):
                del el[attr]
        st = el.get("style") or ""
        st = re.sub(r"(display\s*:\s*none\s*;?)", "", st, flags=re.I)
        st = re.sub(r"(visibility\s*:\s*hidden\s*;?)", "", st, flags=re.I)
        st = re.sub(r"(opacity\s*:\s*0\s*;?)", "", st, flags=re.I)
        st = re.sub(r"\s{2,}", " ", st).strip().strip(";")
        if st:
            el["style"] = st
        else:
            el.attrs.pop("style", None)

# =========================
# Inline style stripping (avoid clamps)
# =========================
_BLOCKING_INLINE_PROPS = [
    r"overflow\s*:\s*[^;]+;?",
    r"max-height\s*:\s*[^;]+;?",
    r"height\s*:\s*[^;]+;?",
    r"visibility\s*:\s*hidden\s*;?",
    r"opacity\s*:\s*0\s*;?",
    r"display\s*:\s*none\s*;?",
    r"transform\s*:\s*[^;]+;?",
    r"clip-path\s*:\s*[^;]+;?",
    r"filter\s*:\s*[^;]+;?",
    r"contain\s*:\s*[^;]+;?",
    r"position\s*:\s*(sticky|fixed)\s*;?",
    r"float\s*:\s*[^;]+;?",
    r"display\s*:\s*(inline-block|table|flex|grid)\s*;?",
    r"page-break-inside\s*:\s*avoid\s*;?",
    r"border\s*:[^;]+;?",
    r"box-shadow\s*:[^;]+;?",
    r"background\s*:[^;]+;?",
    r"outline\s*:[^;]+;?",
]

def _strip_blocking_inline_styles(tag) -> None:
    style = tag.get("style")
    if not style: return
    new_style = style
    for pat in _BLOCKING_INLINE_PROPS:
        new_style = re.sub(pat, "", new_style, flags=re.I)
    new_style = re.sub(r"\s{2,}", " ", new_style).strip().strip(";")
    if new_style:
        tag["style"] = new_style
    else:
        tag.attrs.pop("style", None)

def strip_blocking_inline_styles(soup: BeautifulSoup) -> None:
    for tag in soup.find_all(["table", "thead", "tbody", "tr", "td", "th", "pre", "code"]):
        _strip_blocking_inline_styles(tag)

# =========================
# Dynamic <colgroup> widths per table (anchors-safe)
# =========================
def inject_dynamic_colgroups(soup: BeautifulSoup) -> None:
    """Insert a <colgroup> with width percentages per table to stabilize layout
    under Prince/DocRaptor without touching anchors. Applies only to tables
    whose first row has no colspan/rowspan."""
    def has_span(cell):
        return cell.has_attr('colspan') or cell.has_attr('rowspan')

    def first_row_cells(table):
        thead = table.find('thead')
        if thead:
            tr = thead.find('tr')
            if tr:
                return tr.find_all(['th', 'td'], recursive=False)
        tbody = table.find('tbody') or table
        tr = tbody.find('tr')
        return tr.find_all(['th', 'td'], recursive=False) if tr else []

    def norm_text(el):
        return re.sub(r"\s+", " ", (el.get_text(' ', strip=True) or '')).strip().lower()

    def compute_widths(headers, n):
        # Known 4-col files pattern
        known_4 = ['file name and location','description','cumulus linux documentation','debian documentation']
        if n == 4 and all((not known_4[i]) or known_4[i] in headers[i] for i in range(4)):
            # Favor last column for long URLs
            return [22.0, 28.0, 20.0, 30.0]
        # Generic: start equal
        base = [1.0]*n
        for i in range(n):
            h = headers[i]
            if 'description' in h: base[i] += 0.8
            if 'documentation' in h or 'doc' in h: base[i] += 0.4
            if 'file' in h or 'location' in h: base[i] += 0.5
        total = sum(base) or 1.0
        perc = [(w/total)*100.0 for w in base]
        # Round and ensure sum ~ 100
        s = sum(perc)
        perc = [round(p*100.0/s, 2) for p in perc]
        return perc

    for table in soup.find_all('table'):
        if table.find('colgroup'):
            continue
        cells = first_row_cells(table)
        if not cells:
            continue
        if any(has_span(c) for c in cells):
            continue
        n = len(cells)
        headers = [norm_text(c) for c in cells]
        widths = compute_widths(headers, n)
        colgroup = soup.new_tag('colgroup')
        for p in widths:
            col = soup.new_tag('col')
            col['style'] = f'width: {p:.2f}%;'
            colgroup.append(col)
        first_child = table.contents[0] if table.contents else None
        if first_child:
            first_child.insert_before(colgroup)
        else:
            table.append(colgroup)


# =========================
# Extract images from <pre><code> blocks
# =========================
def extract_images_from_pre_code(soup: BeautifulSoup) -> None:
    """Move <img> tags out of <pre><code>…</code></pre> so Prince/DocRaptor renders them.
    If a code block contains only images (no text), replace the <pre> with those images
    to avoid an empty grey code box.
    """
    for pre in soup.find_all('pre'):
        code = pre.find('code')
        if not code:
            continue
        imgs = list(code.find_all('img'))
        if not imgs:
            continue
        # Determine if there is meaningful text aside from images
        has_text = False
        for child in list(code.children):
            if isinstance(child, Tag) and child.name == 'img':
                continue
            if isinstance(child, NavigableString) and child.strip():
                has_text = True
                break
            if isinstance(child, Tag) and child.name != 'img':
                has_text = True
                break
        if not has_text:
            # Replace the <pre> with images only
            for img in imgs:
                pre.insert_before(img.extract())
            pre.decompose()
        else:
            # Move images after the <pre> block
            for img in imgs:
                pre.insert_after(img.extract())

# =========================
# Anchor utilities & fix
# =========================
def _slugify(text: str) -> str:
    if not text:
        return ""
    t = unicodedata.normalize("NFKD", text)
    t = "".join(ch for ch in t if not unicodedata.combining(ch))
    t = re.sub(r"[^A-Za-z0-9\\-\\_\\s]", "", t)
    t = re.sub(r"\\s+", "-", t.strip().lower())
    t = re.sub(r"\\-+", "-", t)
    return t

def fix_internal_heading_anchors(soup: BeautifulSoup) -> None:
    # 1) Ensure headings have ids
    for h in soup.find_all(re.compile(r"^h[1-6]$")):
        if not h.get("id"):
            inner_id = None
            a = h.find("a", attrs={"id": True}) or h.find("a", attrs={"name": True})
            if a:
                inner_id = a.get("id") or a.get("name")
            h_id = inner_id or _slugify(h.get_text(separator=" ").strip())
            if h_id:
                h["id"] = h_id

    # 2) Rewrite absolute anchors pointing to /pdf/#... into local '#...'
    for a in soup.find_all("a", href=True):
        href = (a["href"] or "").strip()
        if not href:
            continue
        if href.startswith("#"):
            a.attrs.pop("target", None)
            continue

        parsed = urlparse.urlparse(href)
        host = parsed.hostname or ""
        frag = parsed.fragment or ""
        path = parsed.path or ""

        if host == DOCS_HOST and "/pdf" in path and frag:
            a["href"] = f"#{frag}"
            a.attrs.pop("target", None)
            continue

        if host == DOCS_HOST and frag and soup.find(id=frag):
            a["href"] = f"#{frag}"
            a.attrs.pop("target", None)
            continue
        
        # --- NEW: handle links that end in '/#' with NO fragment, using final path segment ---
        # Accept both absolute and relative links; treat staging host as well.
        ends_with_empty_hash = href.endswith('/#') or (not frag and path and href.strip().endswith('#'))
        if ends_with_empty_hash:
            trimmed = path.rstrip('/')
            candidate = trimmed.split('/')[-1] if trimmed else ''
            if candidate:
                # 1. Exact id match
                target_el = soup.find(id=candidate)
                # 2. Heading id set membership
                if not target_el:
                    heading_ids = {h.get('id') for h in soup.find_all(re.compile(r'^h[1-6]$')) if h.get('id')}
                    if candidate in heading_ids:
                        target_el = True
                # 3. Prefix match (case-sensitive)
                if not target_el:
                    for h in soup.find_all(re.compile(r'^h[1-6]$')):
                        hid = h.get('id')
                        if hid and hid.startswith(candidate):
                            target_el = h
                            candidate = hid
                            break
                # 4. Case-insensitive match
                if not target_el:
                    for h in soup.find_all(re.compile(r'^h[1-6]$')):
                        hid = h.get('id')
                        if hid and hid.lower() == candidate.lower():
                            target_el = h
                            candidate = hid
                            break
                # 5. Slugified match
                if not target_el:
                    slug_candidate = _slugify(candidate)
                    for h in soup.find_all(re.compile(r'^h[1-6]$')):
                        hid = h.get('id')
                        if hid and _slugify(hid) == slug_candidate:
                            target_el = h
                            candidate = hid
                            break
                if target_el:
                    a['href'] = f'#{candidate}'
                    a.attrs.pop('target', None)
                    continue
        # --- END NEW BLOCK ---

    # 3) Legacy anchors: also get ids
    for a in soup.find_all("a", attrs={"name": True}):
        name = a.get("name")
        if name and not a.get("id"):
            a["id"] = name

    # 4) NEW: Rewrite general anchor links from staging to docs.nvidia.com
    for a in soup.find_all("a", href=True):
        href = (a["href"] or "").strip()
        if not href or href.startswith("#"):
            continue
        # Only rewrite if the link starts with the staging host
        for old, new in HOST_REWRITE_MAP.items():
            if href.startswith(old):
                # Replace only the host part, preserve path/query/fragment
                new_href = new + href[len(old):]
                a["href"] = new_href
                break

# =========================
# FINAL CSS (print enforcement)
# =========================
def inject_pdf_enforcement_css(soup: BeautifulSoup, hints):
    head = soup.head or soup.new_tag("head")
    if not soup.head:
        soup.insert(0, head)

    css = f"""
html, body, * {{
  print-color-adjust: exact;
  -webkit-print-color-adjust: exact;
  forced-color-adjust: none;
}}
a, a:link, a:visited {{
  color: {hints['color_link']} !important;
  text-decoration: underline !important;
  border-bottom: none !important;
}}
a[href^="#"] {{ color: {hints['color_link']} !important; }}
body, p, li, td, th {{
  color: {hints['color_fg']} !important;
  font-size: {hints['base_px']}px !important;
}}
h1, h2, h3, h4, h5, h6 {{
  color: {hints['color_heading']} !important;
}}
.book-tabs, .book-tabs-content, .markdown-inner,
.tab-content, .tab-pane {{
  display: block !important;
  visibility: visible !important;
  opacity: 1 !important;
  position: static !important;
  height: auto !important;
  max-height: none !important;
  overflow: visible !important;
}}
table, thead, tbody, tr, td, th {{
  position: static !important;
  float: none !important;
  overflow: visible !important;
  height: auto !important;
  max-height: none !important;
  visibility: visible !important;
  opacity: 1 !important;
}}
.book-tabs-content table, .markdown-inner table {{
  display: table !important;
}}
thead {{ display: table-header-group !important; }}
tfoot {{ display: table-footer-group !important; }}
tbody {{ display: table-row-group !important; }}
tr    {{ display: table-row !important; page-break-inside: auto !important; }}
td, th{{ display: table-cell !important; }}
table {{
  page-break-inside: auto !important;
  width: 100%;
  border-collapse: separate !important;
  border-spacing: 0 !important;
  border: none !important;
  break-inside: auto !important;
  page-break-before: auto !important;
  page-break-after: auto !important;
}}
td, th {{
  page-break-inside: auto !important;
  white-space: normal !important;
  word-break: break-word !important;
  overflow-wrap: anywhere !important;
  border: 0.6pt solid #C0C7CF !important;
  background: transparent !important;
  background-color: transparent !important;
  box-shadow: none !important;
  outline: none !important;
}}
tbody tr:nth-child(odd),
tbody tr:nth-child(even),
tbody td:nth-child(odd),
tbody td:nth-child(even),
tbody th:nth-child(odd),
tbody th:nth-child(even),
table tr:nth-child(odd) td,
table tr:nth-child(even) td,
table tr:nth-child(odd) th,
table tr:nth-child(even) th {{
  background: transparent !important;
  background-color: transparent !important;
}}
code {{
  background: #eef2f6 !important;
  color: inherit !important;
  padding: 0 2px !important;
  border-radius: 3px !important;
  border: 1px solid #d9dee5 !important;
  box-shadow: none !important;
  -webkit-box-decoration-break: clone !important;
  box-decoration-break: clone !important;
}}
td code, th code {{
  background: #eef2f6 !important;
  display: inline !important;
  -webkit-box-decoration-break: clone !important;
  box-decoration-break: clone !important;
  white-space: normal !important;
  font-size: 0.95rem !important;
}}
pre code, .highlight code, .code-block code,
pre code *, .highlight code *, .code-block code * {{
  background: transparent !important;
  border: none !important;
  padding: 0 !important;
  box-shadow: none !important;
  -webkit-box-decoration-break: slice !important;
  box-decoration-break: slice !important;
}}
pre, .highlight, .code-block {{
  display: block !important;
  page-break-before: auto !important;
  page-break-after: auto !important;
  page-break-inside: auto !important;
  white-space: pre-wrap !important;
  word-break: break-word !important;
  overflow-wrap: anywhere !important;
  overflow: visible !important;
  font-size: 0.95rem !important;
  background: #eef2f6 !important;
  border: 1px solid #d9dee5 !important;
  border-radius: 4px !important;
}}
img, svg, video, figure {{
  max-width: 100% !important;
  page-break-inside: auto !important;
}}
:root {{ orphans: 2; widows: 2; }}
@media print {{
  .book-tabs, .book-tabs-content, .markdown-inner,
  .tab-content, .tab-pane {{
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
  }}
}}
"""
    css += """
@media print {
  html, body, .content, article, section, p, li, td, th {
    font-size: 14px !important;
  }
  table {
    table-layout: fixed !important;
    width: 100% !important;
    border-collapse: collapse !important;
  }
  thead, tbody, tfoot, tr, td, th {
    box-sizing: border-box !important;
    vertical-align: top !important;
  }
  td, th {
    padding: 6px 8px !important;
    word-break: break-word !important;
    overflow-wrap: anywhere !important;
    hyphens: auto !important;
  }
  /* URLs should be allowed to break within cells */
  td a, th a {
    word-break: break-all !important;
  }
  /* Code in cells should wrap and not overflow */
  td code, th code {
    white-space: pre-wrap !important;
    word-break: break-word !important;
    overflow-wrap: anywhere !important;
    font-size: 0.95rem !important;
  }
  /* Stabilize list items and code blocks in print to avoid overlap */
  ol, ul, li {
    position: static !important;
  }
  li {
    page-break-inside: avoid !important;
    break-inside: avoid !important;
  }
  li > pre,
  li > .scroll,
  li > .book-tabs,
  li > .book-tabs-content,
  li > .markdown-inner {
    page-break-inside: avoid !important;
    break-inside: avoid !important;
  }
  /* Add breathing room between sequential code blocks inside lists */
  li > pre,
  li > .scroll pre,
  li > .book-tabs-content pre {
    margin-top: 6px !important;
    margin-bottom: 10px !important;
  }
  /* Ensure scroll containers don't clamp in print */
  .scroll {
    overflow: visible !important;
    height: auto !important;
    max-height: none !important;
    position: static !important;
    clear: both !important;
  }
}
"""
    style_tag = soup.new_tag("style")
    style_tag.string = css
    head.append(style_tag)

# =========================
# Pipeline
# =========================
def process_html(html_path: str, asset_dir: str) -> str:
    html = pathlib.Path(html_path).read_text(encoding="utf-8", errors="replace")

    soup = BeautifulSoup(html, "html.parser")

    hints = extract_site_style_hints(soup)
    inject_nonfont_brand_css(soup, hints)
    inline_link_styles(soup, asset_dir)

    for style in soup.find_all("style"):
        if style.string:
            style.string = rewrite_css_urls(style.string, base_dir=asset_dir)

    strip_scripts_and_handlers(soup)
    expand_hidden_content(soup)
    embed_inline_style_attrs(soup, asset_dir)
    extract_images_from_pre_code(soup)
    embed_html_images(soup, asset_dir)
    merge_inline_code_runs_into_pre(soup)
    normalize_pre_code_blocks(soup)
    unhide_tab_content(soup)
    strip_blocking_inline_styles(soup)

    # NEW: dynamic colgroups before anchor fixes
    inject_dynamic_colgroups(soup)

    fix_internal_heading_anchors(soup)
    inject_nvidia_sans_fontface(soup, asset_dir, scope=FONT_SCOPE)
    inject_pdf_enforcement_css(soup, hints)

    return str(soup)

# =========================
# DocRaptor async (TEST MODE kept)
# =========================
def submit_to_docraptor(inlined_html: str, output_pdf: str):
    configuration = docraptor.Configuration()
    configuration.username = API_KEY
    doc_api = docraptor.DocApi(docraptor.ApiClient(configuration))

    opts = {
        "media": PRINCE_MEDIA,
        "color_space": PRINCE_COLOR_SPACE,
    }
    # Critical: set baseurl so relative links don't become file:// in the PDF
    if ORIGINAL_URL:
        opts["baseurl"] = ORIGINAL_URL

    print(f"Submitting async job to DocRaptor (TEST mode, media={PRINCE_MEDIA}, color_space={PRINCE_COLOR_SPACE}, baseurl={opts.get('baseurl', 'None')})...")
    async_doc = doc_api.create_async_doc({
        "test": False,  # keep watermark overlays
        "name": output_pdf,
        "document_type": "pdf",
        "document_content": inlined_html,
        "javascript": False,
        "prince_options": opts
    })
    print(f"Async job created: status_id={async_doc.status_id}")

    start_time = time.time()
    while True:
        try:
            status = doc_api.get_async_doc_status(async_doc.status_id)
            elapsed = time.time() - start_time
            if status.status == "completed":
                print(f"✅ Completed in {elapsed:.1f}s. Downloading PDF...")
                pdf_data = doc_api.get_async_doc(async_doc.status_id)
                pathlib.Path(output_pdf).write_bytes(pdf_data)
                final_mb = pathlib.Path(output_pdf).stat().st_size / (1024 * 1024)
                print(f"✅ PDF saved as {output_pdf} ({final_mb:.2f} MB)")
                break
            elif status.status == "failed":
                print(f"❌ Failed after {elapsed:.1f}s: {status}")
                break
            else:
                print(f"[{elapsed:.1f}s] Status: {status.status}")
        except docraptor.exceptions.ApiException:
            print(f"[{time.time() - start_time:.1f}s] Still processing... (waiting)")
        time.sleep(POLL_INTERVAL)

# =========================
# Downloader helpers (URL -> slug -> dynamic paths)
# =========================
def slug_from_url(u: str) -> str:
    parsed = urlparse.urlparse(u)
    path = (parsed.path or "").rstrip("/")
    parts = [p for p in path.split("/") if p]
    if "pdf" not in parts:
        raise ValueError("URL must include a trailing '//pdf/' segment")
    i = parts.index("pdf")
    if i < 1:
        raise ValueError("Cannot find slug immediately before '/pdf/'")
    return parts[i - 1]

def derive_paths_from_slug(slug: str):
    base = pathlib.Path("html-save")
    html_file  = str(base / f"{slug}-pdf.html")
    asset_dir  = str(base / f"{slug}-pdf_files")
    inlined_html = f"{slug}-inlined.html"
    output_pdf   = f"{slug}.pdf"
    return html_file, asset_dir, inlined_html, output_pdf

def _ensure_dirs(html_file: str, asset_dir: str):
    pathlib.Path(html_file).parent.mkdir(parents=True, exist_ok=True)
    pathlib.Path(asset_dir).mkdir(parents=True, exist_ok=True)

def _collect_asset_urls(main_html: str, base_url: str):
    soup = BeautifulSoup(main_html, "html.parser")
    urls = set()

    def add(u: str):
        if not u: return
        # Build absolute URL relative to the source page; DO NOT host-rewrite assets here
        u_abs = urlparse.urljoin(base_url, u)
        if u_abs.startswith("#") or u_abs.startswith("data:"):
            return
        urls.add(u_abs)

    for link in soup.find_all("link", href=True):
        rel = [r.lower() for r in (link.get("rel") or [])]
        if any(r in {"stylesheet", "icon", "shortcut icon"} for r in rel):
            add(link["href"])

    for img in soup.find_all("img", src=True):
        add(img["src"])
        srcset = img.get("srcset")
        if srcset:
            for part in [p.strip() for p in srcset.split(",") if p.strip()]:
                add(part.split()[0])

    for source in soup.find_all("source"):
        if source.get("src"):
            add(source["src"])
        srcset = source.get("srcset")
        if srcset:
            for part in [p.strip() for p in srcset.split(",") if p.strip()]:
                add(part.split()[0])

    for tag in soup.find_all(style=True):
        style_text = tag.get("style") or ""
        for m in URL_RE.finditer(style_text):
            add(m.group(1).strip())

    return soup, urls

def _save_asset_to_dir_with_session(u: str, asset_dir: str, session: requests.Session):
    # DO NOT host-rewrite assets here; keep original host (staging)
    path = urlparse.urlparse(u).path.lstrip("/")
    if not path: return
    local_path = pathlib.Path(asset_dir) / path
    local_path.parent.mkdir(parents=True, exist_ok=True)
    resp = session.get(u, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()
    local_path.write_bytes(resp.content)

def _rewrite_html_links_to_local(soup: BeautifulSoup, base_url: str):
    """
    Rewrite href/src attributes for assets to local path-only references so
    inlining prefers local assets via ASSET_DIR.
    NOTE: We intentionally do NOT rewrite anchors here.
    """
    def path_only(u: str) -> str:
        # Resolve only against the source page; NO host-rewrite for assets
        u_abs = urlparse.urljoin(base_url, u)
        parsed = urlparse.urlparse(u_abs)
        base_host = urlparse.urlparse(base_url).hostname
        if parsed.hostname and parsed.hostname != base_host:
            # External assets: leave absolute URL untouched
            return u_abs
        p = parsed.path
        return p if p.startswith("/") else f"/{p}"

    for link in soup.find_all("link", href=True):
        rel = [r.lower() for r in (link.get("rel") or [])]
        if any(r in {"stylesheet", "icon", "shortcut icon"} for r in rel):
            link["href"] = path_only(link["href"])

    for img in soup.find_all("img", src=True):
        img["src"] = path_only(img["src"])
        if img.get("srcset"):
            parts = []
            for part in [p.strip() for p in img["srcset"].split(",") if p.strip()]:
                tks = part.split()
                url = path_only(tks[0])
                desc = " ".join(tks[1:]) if len(tks) > 1 else ""
                parts.append(url + (f" {desc}" if desc else ""))
            img["srcset"] = ", ".join(parts)

    for source in soup.find_all("source"):
        if source.get("src"):
            source["src"] = path_only(source["src"])
        if source.get("srcset"):
            parts = []
            for part in [p.strip() for p in source["srcset"].split(",") if p.strip()]:
                tks = part.split()
                url = path_only(tks[0])
                desc = " ".join(tks[1:]) if len(tks) > 1 else ""
                parts.append(url + (f" {desc}" if desc else ""))
            source["srcset"] = ", ".join(parts)

    return soup

# =========================
# Playwright downloader (JS-rendered HTML)
# =========================
def render_html_with_playwright(url: str) -> str:
    if not PLAYWRIGHT_AVAILABLE:
        raise RuntimeError("Playwright is not available. Install with 'pip install playwright' and 'playwright install chromium'.")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # IMPORTANT: navigate to the exact source URL, do not rewrite here
        target = url
        page.set_default_timeout(30000)  # 30s
        page.goto(target, wait_until="networkidle")
        page.wait_for_load_state("domcontentloaded")

        # Wait for JS to populate canonical/external anchors (if the app hydrates late)
        try:
            page.wait_for_function(
                """
                () => {
                  const anchors = Array.from(document.querySelectorAll('a[rel="canonical"]'));
                  return anchors.length === 0 ||
                         anchors.every(a => a.href && /^https?:/.test(a.href));
                }
                """,
                timeout=5000
            )
        except Exception:
            pass

        # Promote computed absolute href back into attribute,
        # but do NOT write the page URL or javascript: links.
        page.evaluate("""
        () => {
          const pageUrl = location.href.split('#')[0];
          document.querySelectorAll('a').forEach(a => {
            try {
              const attr = (a.getAttribute('href') || '').trim();
              const abs  = (a.href || '').trim();
              if (!abs || abs.startsWith('javascript:')) return;
              if (attr && attr.startsWith('#')) return;
              const absNoFrag = abs.split('#')[0];
              if (absNoFrag === pageUrl) return; // don't write the page URL back
              const isAttrAbsoluteHttp = /^https?:/i.test(attr);
              const isAbsAbsoluteHttp  = /^https?:/i.test(abs);
              if ((!attr || !isAttrAbsoluteHttp) && isAbsAbsoluteHttp) {
                a.setAttribute('href', abs);
              }
            } catch (e) {}
          });
        }
        """)

        html = page.content()
        browser.close()
        return html

def download_site_playwright(url: str, html_file: str, asset_dir: str):
    _ensure_dirs(html_file, asset_dir)
    html_text = render_html_with_playwright(url)
    soup, asset_urls = _collect_asset_urls(html_text, base_url=url)

    # Inject <base> so relative links resolve correctly when opened locally
    head = soup.head or soup.new_tag("head")
    if not soup.head:
        soup.insert(0, head)
    if not soup.find("base", attrs={"href": True}):
        base_tag = soup.new_tag("base", href=url)
        meta_charset = head.find("meta", attrs={"charset": True})
        if meta_charset:
            meta_charset.insert_after(base_tag)
        else:
            head.insert(0, base_tag)

    session = requests.Session()
    session.headers.update(REQUEST_HEADERS)
    max_workers = min(16, max(4, len(asset_urls)))
    if asset_urls:
        print(f"Downloading {len(asset_urls)} assets (parallel={max_workers})...")
        with ThreadPoolExecutor(max_workers=max_workers) as ex:
            futs = {ex.submit(_save_asset_to_dir_with_session, u, asset_dir, session): u for u in asset_urls}
            for fut in as_completed(futs):
                u = futs[fut]
                try:
                    fut.result()
                except Exception as e:
                    print(f"⚠️ Asset fetch failed: {u} ({e})")

    soup = _rewrite_html_links_to_local(soup, base_url=url)
    pathlib.Path(html_file).write_text(str(soup), encoding="utf-8")

# =========================
# Python static downloader (fallback, no JS)
# =========================
def download_site_python(url: str, html_file: str, asset_dir: str):
    _ensure_dirs(html_file, asset_dir)
    session = requests.Session()
    session.headers.update(REQUEST_HEADERS)
    resp = session.get(url, timeout=REQUEST_TIMEOUT)  # no host rewrite for page fetch
    resp.encoding = resp.apparent_encoding or "utf-8"
    html_text = resp.text

    soup, asset_urls = _collect_asset_urls(html_text, base_url=url)

    head = soup.head or soup.new_tag("head")
    if not soup.head:
        soup.insert(0, head)
    if not soup.find("base", attrs={"href": True}):
        base_tag = soup.new_tag("base", href=url)
        meta_charset = head.find("meta", attrs={"charset": True})
        if meta_charset:
            meta_charset.insert_after(base_tag)
        else:
            head.insert(0, base_tag)

    max_workers = min(16, max(4, len(asset_urls)))
    if asset_urls:
        print(f"Downloading {len(asset_urls)} assets (parallel={max_workers})...")
        with ThreadPoolExecutor(max_workers=max_workers) as ex:
            futs = {ex.submit(_save_asset_to_dir_with_session, u, asset_dir, session): u for u in asset_urls}
            for fut in as_completed(futs):
                u = futs[fut]
                try:
                    fut.result()
                except Exception as e:
                    print(f"⚠️ Asset fetch failed: {u} ({e})")

    soup = _rewrite_html_links_to_local(soup, base_url=url)
    pathlib.Path(html_file).write_text(str(soup), encoding="utf-8")

# =========================
# Main
# =========================
def main():
    if not API_KEY or API_KEY.strip() == "":
        raise SystemExit("Missing DOCRAPTOR_API_KEY. Set it in your env or edit API_KEY_FALLBACK.")

    parser = argparse.ArgumentParser(description="Inline HTML and render PDF via DocRaptor/Prince.")
    parser.add_argument("--url", help="Source URL ending with '//pdf/' to download before processing.")
    parser.add_argument("--download", choices=["playwright", "python"], default="playwright",
                        help="Downloader to use when --url is provided (default: playwright).")
    parser.add_argument("--output", help="Override output PDF filename (defaults to '<slug>.pdf' when --url is used).")
    args = parser.parse_args()

    if args.url:
        slug = slug_from_url(args.url)
        global HTML_FILE, ASSET_DIR, INLINED_HTML, OUTPUT_PDF, ORIGINAL_URL
        HTML_FILE, ASSET_DIR, INLINED_HTML, OUTPUT_PDF = derive_paths_from_slug(slug)
        # Base URL for Prince must be the original source URL you passed in
        ORIGINAL_URL = args.url
        if args.output:
            OUTPUT_PDF = args.output

        print(f"▶ Using slug '{slug}'")
        print(f"   HTML_FILE    = {HTML_FILE}")
        print(f"   ASSET_DIR    = {ASSET_DIR}")
        print(f"   INLINED_HTML = {INLINED_HTML}")
        print(f"   OUTPUT_PDF   = {OUTPUT_PDF}")

        if args.download == "playwright":
            if not PLAYWRIGHT_AVAILABLE:
                print("⚠️ Playwright is not installed; falling back to Python static downloader.")
                download_site_python(args.url, HTML_FILE, ASSET_DIR)
            else:
                download_site_playwright(args.url, HTML_FILE, ASSET_DIR)
        else:
            download_site_python(args.url, HTML_FILE, ASSET_DIR)

    inlined = process_html(HTML_FILE, ASSET_DIR)
    pathlib.Path(INLINED_HTML).write_text(inlined, encoding="utf-8")
    total_mb = len(inlined.encode("utf-8")) / (1024 * 1024)
    print(f"✅ Wrote inlined HTML -> {INLINED_HTML} ({total_mb:.2f} MB)")
    print(f"Embedded resources cached: {len(resource_cache)} entries")

    submit_to_docraptor(inlined, OUTPUT_PDF)

if __name__ == "__main__":
    main()
