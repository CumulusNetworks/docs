
#!/usr/bin/env python3
"""
Inline HTML for DocRaptor/Prince PDF with:
- CSS/JS inlining (JS stripped)
- Host rewrite (staging -> production)
- Tight margins
- Robust table fragmentation using native <table> (no clones)
- Merge inline code runs into single <pre><code>...</code></pre>
- Normalize existing <pre> blocks (remove nested chips)
- Embed NVIDIASans as data URI via @font-face (variable woff2)
- Print-only font override (configurable scope)
- Anchor fix: rewrite absolute /pdf/#... links to local #... and ensure heading IDs
- TEST mode kept (DocRaptor watermark remains)
"""
import os
import re
import time
import mimetypes
import base64
import pathlib
import unicodedata
import urllib.parse as urlparse
import requests
from bs4 import BeautifulSoup, Tag, NavigableString
import docraptor

# =========================
# CONFIG
# =========================
HTML_FILE = "html-save/cumulus-linux-515-pdf.html"
ASSET_DIR = "html-save/cumulus-linux-515-pdf_files"
INLINED_HTML = "cumulus-linux-515-inlined.html"
OUTPUT_PDF = "cumulus-linux-515.pdf"

API_KEY_FALLBACK = "0uH2Qnz3ewlkBD1BmE3"  # prefer env
API_KEY = os.getenv("DOCRAPTOR_API_KEY", API_KEY_FALLBACK)

EMBED_CSS_IMAGES = True
EMBED_HTML_IMAGES = True
EMBED_FONTS = True  # — ensure font embedding via @font-face happens

# Font override scope:
#   "print" => PDF only (recommended, keeps browser/inlined HTML untouched)
#   "all"   => both screen & print (forces NVIDIASans everywhere)
FONT_SCOPE = "print"

FORCE_FONT_FAMILY = "'NVIDIASans'"  # logical name used in @font-face
PRESERVE_MONOSPACE_FOR_CODE = True
EMBED_FAVICON = False

ENABLE_HOST_REWRITE = True
HOST_REWRITE_MAP = {
    "https://pdf-testing.d5j8yik1ci5ec.amplifyapp.com/networking-ethernet-software":
    "https://docs.nvidia.com/networking-ethernet-software",
}
ALLOWED_HOSTS = {"images.nvidia.com"}

REQUEST_HEADERS = {"User-Agent": "NVIDIA-Docs-Inliner/2.5 (+DocRaptor/Prince)"}
REQUEST_TIMEOUT = 25
POLL_INTERVAL = 5

# Use print media so @media print rules apply
PRINCE_MEDIA = "print"
PRINCE_COLOR_SPACE = "rgb"

# Tight page margins
PAGE_MARGIN_TOP_MM = 11
PAGE_MARGIN_RIGHT_MM = 6
PAGE_MARGIN_BOTTOM_MM = 11  # +2 mm to keep content above TEST watermark band
PAGE_MARGIN_LEFT_MM = 6

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
    ext = pathlib.Path(urlparse.urlparse(u).path).suffix.lower()
    guessed, _ = mimetypes.guess_type(u)
    return guessed or default

def to_data_uri(raw: bytes, mime: str) -> str:
    return f"data:{mime};base64,{base64.b64encode(raw).decode('ascii')}"

def normalize_and_rewrite_url(u: str) -> str:
    # Leave pure fragments alone
    if not u or u.startswith("#"):
        return u
    if not ENABLE_HOST_REWRITE:
        return u
    for old, new in HOST_REWRITE_MAP.items():
        if u.startswith(old):
            return new + u[len(old):]
    return u

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
    url = normalize_and_rewrite_url(url)
    resp = requests.get(url, headers=REQUEST_HEADERS, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()
    return resp.content

def get_resource_bytes(href: str, base_dir: str) -> bytes:
    href = normalize_and_rewrite_url(href)
    key = f"BYTES::{href}"
    if key in resource_cache:
        return resource_cache[key][0]
    if not host_allowed(href):
        raise PermissionError(f"Host not allowed for embedding: {href}")
    raw = fetch_http_bytes(href) if is_http_url(href) else read_local_bytes(base_dir, href)
    resource_cache[key] = (raw, infer_mime(href))
    return raw

def get_resource_text(href: str, base_dir: str) -> str:
    href = normalize_and_rewrite_url(href)
    key = f"TEXT::{href}"
    if key in resource_cache:
        return resource_cache[key][0].decode("utf-8", errors="replace")
    raw = get_resource_bytes(href, base_dir)
    resource_cache[key] = (raw, infer_mime(href))
    return raw.decode("utf-8", errors="replace")

def to_data_uri_from(href: str, base_dir: str) -> str:
    href = normalize_and_rewrite_url(href)
    raw = get_resource_bytes(href, base_dir)
    mime = infer_mime(href)
    return to_data_uri(raw, mime)

# =========================
# CSS rewriting
# =========================
IMPORT_RE = re.compile(r'@import\s+(?:url\()?["\']?([^"\'\)]+)["\']?\)?\s*;', re.I)
URL_RE    = re.compile(r'url\(\s*["\']?([^"\'\)]+)["\']?\s*\)', re.I)

def inline_css_imports(css_text: str, base_dir: str) -> str:
    out = css_text
    while True:
        m = IMPORT_RE.search(out)
        if not m:
            break
        import_url = normalize_and_rewrite_url(m.group(1).strip())
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
        u = normalize_and_rewrite_url(m.group(1).strip())
        if u.startswith("data:") or u.startswith("#"):
            return m.group(0)
        try:
            data_uri = to_data_uri_from(u, base_dir)
            return f"url({data_uri})"
        except Exception:
            return f"url({u})"
    return URL_RE.sub(repl, css_text)

def inline_stylesheet_href(href: str, base_dir: str) -> str:
    href = normalize_and_rewrite_url(href)
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

    for m in re.finditer(r":root\s*\{([^\}]*)\}", big, re.I | re.S):
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
a, a:visited {{ color: var(--color-link); text-decoration: underline; }}

/* Tight page box */
@page {{
  size: Letter;
  margin: {PAGE_MARGIN_TOP_MM}mm {PAGE_MARGIN_RIGHT_MM}mm {PAGE_MARGIN_BOTTOM_MM}mm {PAGE_MARGIN_LEFT_MM}mm;
}}
"""
    style_tag = soup.new_tag("style")
    style_tag.string = css
    head.insert(0, style_tag)

def inline_link_styles(soup: BeautifulSoup, base_dir: str):
    for link in list(soup.find_all("link")):
        rel = [r.lower() for r in (link.get("rel") or [])]
        href = link.get("href")
        if href:
            href = normalize_and_rewrite_url(href)
            link["href"] = href
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
    if not soup.find("meta", attrs={"charset": True}):
        meta = soup.new_tag("meta", charset="utf-8")
        head.insert(0, meta)

def embed_inline_style_attrs(soup: BeautifulSoup, base_dir: str):
    for tag in soup.find_all(style=True):
        style_text = tag.get("style") or ""
        if ENABLE_HOST_REWRITE:
            for old, new in HOST_REWRITE_MAP.items():
                style_text = style_text.replace(old, new)
        try:
            tag["style"] = rewrite_css_urls(style_text, base_dir)
        except Exception:
            tag["style"] = style_text

def _embed_srcset(srcset: str, base_dir: str) -> str:
    parts = [p.strip() for p in srcset.split(",") if p.strip()]
    out = []
    for part in parts:
        tokens = part.split()
        url = normalize_and_rewrite_url(tokens[0])
        desc = " ".join(tokens[1:]) if len(tokens) > 1 else ""
        if url.startswith("data:"):
            out.append(part); continue
        try:
            data_uri = to_data_uri_from(url, base_dir)
            out.append((data_uri + (" " + desc if desc else "")))
        except Exception:
            out.append(part)
    return ", ".join(out)

def embed_html_images(soup: BeautifulSoup, base_dir: str):
    if not EMBED_HTML_IMAGES:
        return
    for img in soup.find_all("img", src=True):
        src = normalize_and_rewrite_url(img["src"])
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
            src = normalize_and_rewrite_url(src)
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
    """
    Fetch the NVIDIASans variable WOFF2 from images.nvidia.com, convert to data URI,
    and embed as @font-face. Scope can be "print" or "all".
    """
    if not EMBED_FONTS:
        return

    head = soup.head or soup.new_tag("head")
    if not soup.head:
        soup.insert(0, head)

    # Fetch & embed as data URI
    try:
        font_data_uri = to_data_uri_from(NVIDIASANS_VAR_WGHT_URL, base_dir)
    except Exception as e:
        # If fetch fails, do nothing—Prince will fall back to system fonts
        warn = soup.new_tag("!--")
        warn.string = f" Failed to fetch NVIDIASans WOFF2: {e} "
        head.append(warn)
        return

    face_css = f"""
@font-face {{
  font-family: {FORCE_FONT_FAMILY};
  src: url('{font_data_uri}') format('woff2');
  font-weight: 100 1000;   /* variable weight range */
  font-stretch: 25% 151%;  /* variable stretch range */
  font-style: normal;
}}
"""

    override_prefix = "" if scope == "all" else "@media print {\n"
    override_suffix = "" if scope == "all" else "\n}"

    mono = "'Oxygen Mono','Fira Mono','SFMono-Regular',Menlo,Consolas,'Liberation Mono',monospace"
    use_css = f"""
{override_prefix}
/* Use embedded NVIDIASans (scope: {scope}) */
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
# Merge contiguous inline code lines to a single pre block
# =========================
def merge_inline_code_runs_into_pre(soup: BeautifulSoup):
    """
    Merge contiguous runs of <p><code>...</code></p> or <div><code>...</code></div>
    into a single <pre><code>...</code></pre> to restore a consecutive block.
    """
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
            if len(run) >= 2:  # merge 2+ lines
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
# Normalize existing <pre> blocks (remove nested chips, ensure single <code>)
# =========================
def normalize_pre_code_blocks(soup: BeautifulSoup):
    for pre in soup.find_all("pre"):
        txt = pre.get_text("\n")
        for c in list(pre.children): c.extract()
        code = soup.new_tag("code")
        code.string = txt
        pre.append(code)

# =========================
# Unhide tab content: remove hidden flags & attributes that suppress tables
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
        if st: el["style"] = st
        else: el.attrs.pop("style", None)

# =========================
# Inline style stripping (avoid clamps)
# =========================
_BLOCKING_INLINE_PROPS = [
    r"overflow\s*:\s*[^;]+;?",
    r"max-height\s*:\s*[^;]+;?",
    r"height\s*:\s*[^;]+;?",
    r"visibility\s*:\s*hidden\s*;?",
    r"opacity\s*:\s*0\s*;?",
    r"display\s*:\s*none\s*;?",          # NEW: strip inline display:none
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
    if new_style: tag["style"] = new_style
    else: tag.attrs.pop("style", None)

def strip_blocking_inline_styles(soup: BeautifulSoup) -> None:
    for tag in soup.find_all(["table", "thead", "tbody", "tr", "td", "th", "pre", "code"]):
        _strip_blocking_inline_styles(tag)

# =========================
# Anchor utilities & fix
# =========================
def _slugify(text: str) -> str:
    """
    Make a URL-friendly slug from heading text.
    Lowercase, hyphens, ASCII-only, compact multiple hyphens.
    """
    if not text:
        return ""
    t = unicodedata.normalize("NFKD", text)
    t = "".join(ch for ch in t if not unicodedata.combining(ch))
    t = re.sub(r"[^A-Za-z0-9\-\_\s]", "", t)
    t = re.sub(r"\s+", "-", t.strip().lower())
    t = re.sub(r"-{2,}", "-", t)
    return t

def fix_internal_heading_anchors(soup: BeautifulSoup) -> None:
    """
    Ensure all headings have ids, and rewrite absolute same-document PDF anchors
    to local fragments so Prince/DocRaptor creates proper internal destinations.
    """
    # 1) Ensure headings are linkable: add missing ids via slugified text
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

        # Already a fragment: normalize
        if href.startswith("#"):
            a.attrs.pop("target", None)
            continue

        parsed = urlparse.urlparse(href)
        host = parsed.hostname or ""
        frag = parsed.fragment or ""
        path = parsed.path or ""

        # Rewrite /pdf/#frag to local #frag
        if host == DOCS_HOST and "/pdf" in path and frag:
            a["href"] = f"#{frag}"
            a.attrs.pop("target", None)
            continue

        # If same host and fragment exists locally, rewrite to local fragment
        if host == DOCS_HOST and frag and soup.find(id=frag):
            a["href"] = f"#{frag}"
            a.attrs.pop("target", None)
            continue

    # 3) Legacy anchors: <a name="..."> also get ids
    for a in soup.find_all("a", attrs={"name": True}):
        name = a.get("name")
        if name and not a.get("id"):
            a["id"] = name

# =========================
# FINAL CSS (print enforcement + fragmentation + table/background fixes)
# =========================
def inject_pdf_enforcement_css(soup: BeautifulSoup, hints):
    head = soup.head or soup.new_tag("head")
    if not soup.head: soup.insert(0, head)
    css = f"""
/* --- PDF enforcement (last, !important) --- */
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

/* Base text: keep theme weight, enforce color/size only */
body, p, li, td, th {{
  color: {hints['color_fg']} !important;
  font-size: {hints['base_px']}px !important;
}}
h1, h2, h3, h4, h5, h6 {{
  color: {hints['color_heading']} !important;
}}

/* Unhide all tab panes/wrappers in print */
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

/* Native tables: allow splitting, keep header/footer repeat */
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

/* Table box rules */
table {{
  page-break-inside: auto !important;
  width: 100%;
  border-collapse: separate !important;   /* avoid outer frame fighting breaks */
  border-spacing: 0 !important;
  border: none !important;
  break-inside: auto !important;
  page-break-before: auto !important;
  page-break-after: auto !important;
}}
td, th {{
  page-break-inside: auto !important;     /* allow cell content fragmentation */
  white-space: normal !important;
  word-break: break-word !important;
  overflow-wrap: anywhere !important;
  border: 0.6pt solid #C0C7CF !important; /* thin grid */
  background: transparent !important;
  background-color: transparent !important;
  box-shadow: none !important;
  outline: none !important;
}}

/* --- Table background resets (neutralize common zebra patterns) --- */
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

/* Inline code chips (fragment-safe) — used outside block code */
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

/* Keep chip look inside table cells without painting the whole cell */
td code, th code {{
  background: #eef2f6 !important;
  display: inline !important;
  -webkit-box-decoration-break: clone !important;
  box-decoration-break: clone !important;
  white-space: normal !important;
  font-size: 0.95rem !important;
}}

/* Fix: inside block code, remove per-line chips completely */
pre code, .highlight code, .code-block code,
pre code *, .highlight code *, .code-block code * {{
  background: transparent !important;
  border: none !important;
  padding: 0 !important;
  box-shadow: none !important;
  -webkit-box-decoration-break: slice !important;
  box-decoration-break: slice !important;
}}

/* Block code (fragment-safe single frame) */
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

/* Print dominance backstop (if a theme leaks screen-only styles) */
@media print {{
  .book-tabs, .book-tabs-content, .markdown-inner,
  .tab-content, .tab-pane {{
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
  }}
}}
"""

    # Print sizing & table layout fixes
    css += """
@media print {
  /* Slightly smaller base type for PDF to reduce overflows */
  html, body, .content, article, section, p, li, td, th {
    font-size: 14px !important;
  }

  /* Predictable column widths and better wrapping */
  table {
    table-layout: fixed !important;
    width: 100% !important;
  }

  /* More breathing room and robust wrapping in cells */
  td, th {
    padding: 6px 8px !important;
    word-break: break-word !important;
    overflow-wrap: anywhere !important;
  }

  /* Long inline code in table cells should wrap and not overflow */
  td code, th code {
    white-space: pre-wrap !important;
    word-break: break-word !important;
    overflow-wrap: anywhere !important;
    font-size: 0.95rem !important;
  }
}
"""

    # Universal multi-column widths (first column wider; 2nd/3rd/4th sized if present)
    css += """
@media print {
  /* Make the first column wider for code, up to 55% if possible */
  td:first-child, th:first-child {
    width: 55% !important;
    max-width: 0 !important;
    word-break: break-all !important;
    overflow-wrap: anywhere !important;
  }
  /* For 2-column tables, second column gets 45% */
  td:nth-child(2), th:nth-child(2) {
    width: 45% !important;
    max-width: 0 !important;
    word-break: break-word !important;
    overflow-wrap: anywhere !important;
  }
  /* For 3-column tables, third column gets 30% */
  td:nth-child(3), th:nth-child(3) {
    width: 30% !important;
    max-width: 0 !important;
    word-break: break-word !important;
    overflow-wrap: anywhere !important;
  }
  /* For 4-column tables, fourth column gets 25% */
  td:nth-child(4), th:nth-child(4) {
    width: 25% !important;
    max-width: 0 !important;
    word-break: break-word !important;
    overflow-wrap: anywhere !important;
  }
}
"""

    style_tag = soup.new_tag("style"); style_tag.string = css; head.append(style_tag)

# =========================
# Pipeline
# =========================
def process_html(html_path: str, asset_dir: str) -> str:
    html = pathlib.Path(html_path).read_text(encoding="utf-8", errors="replace")
    if ENABLE_HOST_REWRITE:
        for old, new in HOST_REWRITE_MAP.items():
            html = html.replace(old, new)
    soup = BeautifulSoup(html, "html.parser")

    hints = extract_site_style_hints(soup)
    inject_nonfont_brand_css(soup, hints)
    inline_link_styles(soup, asset_dir)

    for style in soup.find_all("style"):
        if style.string:
            if ENABLE_HOST_REWRITE:
                for old, new in HOST_REWRITE_MAP.items():
                    style.string = style.string.replace(old, new)
            style.string = rewrite_css_urls(style.string, base_dir=asset_dir)

    strip_scripts_and_handlers(soup)
    expand_hidden_content(soup)
    embed_inline_style_attrs(soup, asset_dir)
    embed_html_images(soup, asset_dir)

    # 1) Merge many <p><code>...</code></p> into one <pre><code>...</code></pre>
    merge_inline_code_runs_into_pre(soup)
    # 2) Normalize all existing <pre> blocks to a single inner <code> (plain text)
    normalize_pre_code_blocks(soup)
    # 3) Ensure tab panes/wrappers are not hidden
    unhide_tab_content(soup)
    # 4) Strip inline style clamps from key content
    strip_blocking_inline_styles(soup)

    # 5) NEW: Fix heading IDs and rewrite absolute PDF anchors to local fragments
    fix_internal_heading_anchors(soup)

    # --- Embed NVIDIASans and force usage (print-only by default) ---
    inject_nvidia_sans_fontface(soup, asset_dir, scope=FONT_SCOPE)

    # Enforcement CSS (fragmentation, backgrounds, etc.)
    inject_pdf_enforcement_css(soup, hints)

    return str(soup)

# =========================
# DocRaptor async (TEST MODE kept)
# =========================
def submit_to_docraptor(inlined_html: str, output_pdf: str):
    configuration = docraptor.Configuration()
    configuration.username = API_KEY
    doc_api = docraptor.DocApi(docraptor.ApiClient(configuration))

    print(f"Submitting async job to DocRaptor (TEST mode, media={PRINCE_MEDIA}, color_space={PRINCE_COLOR_SPACE})...")
    async_doc = doc_api.create_async_doc({
        "test": True,  # keep watermark overlays for now
        "name": output_pdf,
        "document_type": "pdf",
        "document_content": inlined_html,
        "javascript": False,
        "prince_options": {
            "media": PRINCE_MEDIA,
            "color_space": PRINCE_COLOR_SPACE
        }
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
                print(f"✅ PDF saved as {OUTPUT_PDF} ({final_mb:.2f} MB)")
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
# Main
# =========================
def main():
    if not API_KEY or API_KEY.strip() == "":
        raise SystemExit("Missing DOCRAPTOR_API_KEY. Set it in your env or edit API_KEY_FALLBACK.")
    inlined = process_html(HTML_FILE, ASSET_DIR)
    pathlib.Path(INLINED_HTML).write_text(inlined, encoding="utf-8")
    total_mb = len(inlined.encode("utf-8")) / (1024 * 1024)
    print(f"✅ Wrote inlined HTML -> {INLINED_HTML} ({total_mb:.2f} MB)")
    print(f"Embedded resources cached: {len(resource_cache)} entries")
    submit_to_docraptor(inlined, OUTPUT_PDF)

if __name__ == "__main__":
    main()

