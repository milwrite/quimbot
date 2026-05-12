#!/usr/bin/env python3
"""Build CUNY Social Stories static site from _src/*.md.

Run: python3 build.py
"""

import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "_src"
MOTIF = "student-made scaffolding"
SITE_TITLE = "CUNY Social Stories"
SITE_SUBTITLE = "Yearly vignettes from the CUNY Reddit corpus, 2014–present"

PREFACE_HTML = """\
<p>The recurring motif is <strong>student-made scaffolding</strong>: CUNY Redditors repeatedly use subreddit space to build the missing supports around an institution they experience as affordable, valuable, and difficult to navigate. Across the years sampled, the register changes, but the pattern holds. Students ask strangers to translate bureaucratic portals, aid rules, degree audits, course sequencing, commuter routines, social norms, campus hazards, and job-market expectations into usable knowledge. Sometimes the scaffold is emotional, as when students admit loneliness, burnout, homelessness, or academic collapse and receive concrete next steps. Sometimes it is tactical, as when users share office-contact workarounds, refund guides, textbook sources, professor-rating tools, syllabi, or resume help. Sometimes it is political, as when students organize petitions or debate university-wide policy shifts.</p>
<p>Source databases queried (CUNY-only): <code>CUNY</code>, <code>Baruch</code>, <code>QueensCollege</code>, <code>HunterCollege</code>, <code>CCNY</code>, <code>BrooklynCollege</code>, <code>JohnJay</code>, <code>CUNYuncensored</code>. All anchor moments are paraphrased per the dissertation's disguise protocol; evidence IDs preserve traceability.</p>
"""

CODA_HTML = """\
<p>Across these years, CUNY Reddit shows students building the missing connective tissue around a public university system defined by affordability, commuting, bureaucracy, and uneven support. The motif does not stay fixed in one domain. It starts with belonging and persistence, moves into aid and transfer uncertainty, becomes workaround knowledge for offices and portals, expands into pandemic mutual aid, and later hardens into guides, petitions, alumni networks, and software tools. The arc also shows a changing threshold of expectation. Early posts ask how to survive the campus as it exists, while later posts increasingly assume that students must audit, repair, supplement, or publicly pressure the institution. The strongest throughline is not cynicism but practical solidarity, as strangers turn their own hard-won knowledge into a handrail for the next student trying not to fall through.</p>
<p>By the later years, the contrast is especially sharp around writing itself. In classes, AI detection pushes students toward defensive version control as drafts, timestamps, histories, screenshots, and explanations become a private audit trail. On CUNY Reddit, those same anxieties become collective composing. Students turn complaints and frustrations into warnings, procedural scripts, resource lists, software tools, and calls to act. The subreddit is therefore not just a record of student life around CUNY, but one of the local discursive arenas where students now practice everyday reading, writing, and institutional literacy together.</p>
"""

STYLES = """\
:root{--bg:#0b0e14;--fg:rgba(255,255,255,.92);--muted:rgba(255,255,255,.6);--card:rgba(255,255,255,.04);--stroke:rgba(255,255,255,.12);--code:#0d1117;--accent:#9ecbff;--year:#c8c8c8;--active:#ffd479}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.7 ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,Arial,sans-serif;padding:24px}
article,main{max-width:820px;margin:0 auto}
h1{font-size:clamp(28px,4vw,42px);line-height:1.15;margin:0 0 8px;letter-spacing:-0.02em}
h2{font-size:clamp(18px,2.5vw,24px);margin:36px 0 12px;font-weight:600;letter-spacing:-0.01em}
.year-chip{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;letter-spacing:.18em;font-size:.9rem;color:var(--year);text-transform:uppercase;margin:0 0 4px}
.meta{color:var(--muted);font-size:14px;margin:8px 0 28px;display:flex;gap:14px;flex-wrap:wrap;align-items:baseline}
.meta .motif{font-style:italic}
.meta .subs{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:.8rem}
p{margin:0 0 16px}
a{color:var(--accent);text-decoration:none}
a:hover{text-decoration:underline}
code{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:.9em;background:var(--card);padding:2px 6px;border-radius:4px;border:1px solid var(--stroke)}
pre{background:var(--code);border:1px solid var(--stroke);border-radius:10px;padding:14px 18px;overflow:auto;margin:8px 0 18px;font-size:13px;line-height:1.5}
pre code{background:none;border:none;padding:0}
.evidence{border-top:1px solid var(--stroke);margin-top:24px;padding-top:16px;font-size:14px;color:var(--muted)}
.evidence strong{color:var(--fg);font-weight:600}
nav.crumbs{font-size:13px;color:var(--muted);margin-bottom:24px}
nav.pager{display:flex;justify-content:space-between;gap:16px;margin-top:48px;padding-top:24px;border-top:1px solid var(--stroke);font-size:14px}
nav.pager a{display:block;color:var(--muted);max-width:48%}
nav.pager a:hover{color:var(--fg)}
nav.pager .pager-label{display:block;font-size:11px;text-transform:uppercase;letter-spacing:.12em;color:var(--year);margin-bottom:4px}
nav.pager .pager-next{text-align:right}
ol.vlist{list-style:none;padding:0;margin:24px 0;border-top:1px solid var(--stroke)}
ol.vlist li{padding:14px 0;border-bottom:1px solid var(--stroke);display:flex;gap:16px;align-items:baseline;flex-wrap:wrap}
ol.vlist a{display:flex;gap:16px;align-items:baseline;color:inherit;flex:1 1 auto;min-width:0;text-decoration:none}
ol.vlist a:hover .title{text-decoration:underline}
ol.vlist .yr{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-weight:600;color:var(--year);min-width:5ch}
ol.vlist .title{font-size:1.05rem}
ol.vlist .subs{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:.75rem;color:var(--muted)}
footer{max-width:820px;margin:64px auto 0;padding-top:24px;border-top:1px solid var(--stroke);font-size:13px;color:var(--muted)}
footer a{color:var(--muted)}
footer a:hover{color:var(--fg)}

.read-all-link{display:inline-block;margin-top:16px;padding:10px 18px;border:1px solid var(--stroke);border-radius:8px;color:var(--muted);font-size:14px;text-decoration:none}
.read-all-link:hover{color:var(--fg);border-color:rgba(255,255,255,.3);text-decoration:none}

/* ===== Single-page (all.html) + timeline ===== */
body.allpage{padding:0}
.timeline{position:sticky;top:0;z-index:10;background:rgba(11,14,20,.96);backdrop-filter:saturate(120%) blur(8px);-webkit-backdrop-filter:saturate(120%) blur(8px);border-bottom:1px solid var(--stroke);padding:18px 16px 14px}
.timeline-inner{max-width:980px;margin:0 auto}
.timeline-head{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:14px;gap:16px;flex-wrap:wrap}
.timeline-head h1{font-size:clamp(16px,2vw,20px);margin:0;letter-spacing:-0.01em}
.timeline-head .crumbs{font-size:12px;color:var(--muted)}
.timeline-head .crumbs a{color:var(--muted)}
.timeline-head .crumbs a:hover{color:var(--fg)}
.timeline-bar{position:relative;height:28px}
.timeline-rail{position:absolute;left:0;right:0;top:11px;height:2px;background:var(--stroke);border-radius:1px}
.timeline-fill{position:absolute;left:0;top:11px;height:2px;background:linear-gradient(90deg,var(--accent),var(--active));border-radius:1px;width:0;transition:width .25s ease}
.timeline-track{position:relative;display:flex;justify-content:space-between;align-items:flex-start;list-style:none;margin:0;padding:0}
.timeline-track li{position:relative;flex:1 1 0;display:flex;justify-content:center}
.timeline-track a{display:flex;flex-direction:column;align-items:center;gap:6px;color:var(--muted);font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:11px;text-decoration:none;cursor:pointer;padding:2px 4px}
.timeline-track a:hover{color:var(--fg);text-decoration:none}
.timeline-track .dot{width:10px;height:10px;border-radius:50%;background:var(--bg);border:2px solid var(--stroke);box-shadow:0 0 0 3px var(--bg);transition:transform .2s ease,border-color .2s ease,background .2s ease}
.timeline-track a:hover .dot{border-color:var(--accent)}
.timeline-track a.active{color:var(--active)}
.timeline-track a.active .dot{transform:scale(1.4);border-color:var(--active);background:var(--active)}
.timeline-track a.visited .dot{border-color:var(--accent);background:var(--accent)}
.allpage main{max-width:820px;margin:0 auto;padding:24px}
.allpage .preface{max-width:820px;margin:8px auto 0;padding:8px 24px 0}
.allpage .preface h2{margin-top:24px}
.year-vignette{padding:48px 0 16px;border-top:1px solid var(--stroke)}
.year-vignette:first-of-type{border-top:none;padding-top:24px}
.year-vignette h2{margin:4px 0 0;font-size:clamp(24px,3vw,32px);font-weight:600;letter-spacing:-0.02em}
.year-vignette .meta{margin:10px 0 22px}
@media (max-width:680px){
  .timeline-track a .label{display:none}
  .timeline-track a.active .label{display:inline}
  .timeline{padding:14px 12px 10px}
}
"""


def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)", text, re.DOTALL)
    if not m:
        raise ValueError("missing frontmatter")
    raw_fm, body = m.group(1), m.group(2)
    fm = {}
    for line in raw_fm.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith("  - "):
            fm.setdefault("__list_key__", []).append(line[4:].strip())
            continue
        if ":" not in line:
            continue
        key, val = line.split(":", 1)
        key = key.strip()
        val = val.strip()
        if val == "":
            fm["__list_key__"] = []
            fm["__last_key__"] = key
            continue
        if val.startswith("[") and val.endswith("]"):
            fm[key] = [v.strip() for v in val[1:-1].split(",") if v.strip()]
        else:
            fm[key] = val.strip('"').strip("'")
    if "__last_key__" in fm:
        fm[fm["__last_key__"]] = fm.pop("__list_key__", [])
        fm.pop("__last_key__", None)
    fm.pop("__list_key__", None)
    return fm, body


def md_to_html(body):
    """Minimal markdown to HTML for paragraphs, **bold**, *italic*, `code`,
    and the special **Evidence**: ... line at the end."""
    lines = body.strip().splitlines()
    paragraphs, buf = [], []
    for line in lines + [""]:
        if line.strip() == "":
            if buf:
                paragraphs.append(" ".join(buf).strip())
                buf = []
        else:
            buf.append(line)

    html_parts = []
    for p in paragraphs:
        if p.startswith("**Evidence**:"):
            content = p[len("**Evidence**:"):].strip()
            html_parts.append(
                f'<p class="evidence"><strong>Evidence:</strong> '
                f"{inline_md(content)}</p>"
            )
        else:
            html_parts.append(f"<p>{inline_md(p)}</p>")
    return "\n".join(html_parts)


def inline_md(text):
    text = html.escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    return text


def page_chrome(title, body_html, crumbs_html="", body_class=""):
    body_attr = f' class="{body_class}"' if body_class else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<link rel="icon" type="image/png" href="../favicon.png">
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>{html.escape(title)}</title>
<style>
{STYLES}
</style>
</head>
<body{body_attr}>
{crumbs_html}
{body_html}
<footer>
  <p><a href="../index.html">← Quimbot</a> · <a href="index.html">Index</a> · <a href="all.html">Single-page</a> · CUNY Reddit corpus, paraphrased per disguise protocol</p>
</footer>
</body>
</html>
"""


def render_year_page(v, prev_v, next_v):
    title = f"{v['year']} — {v['title']} · {SITE_TITLE}"
    subs = " · ".join(f"r/{s}" for s in v.get("subreddits", []))

    crumbs = (
        '<nav class="crumbs"><a href="index.html">'
        f"{SITE_TITLE}</a> / {v['year']}</nav>"
    )

    pager_parts = []
    if prev_v:
        pager_parts.append(
            f'<a class="pager-prev" href="{prev_v["year"]}.html">'
            f'<span class="pager-label">← {prev_v["year"]}</span>'
            f'{html.escape(prev_v["title"])}</a>'
        )
    else:
        pager_parts.append(
            '<a class="pager-prev" href="index.html">'
            '<span class="pager-label">← All vignettes</span>Index</a>'
        )
    if next_v:
        pager_parts.append(
            f'<a class="pager-next" href="{next_v["year"]}.html">'
            f'<span class="pager-label">{next_v["year"]} →</span>'
            f'{html.escape(next_v["title"])}</a>'
        )
    else:
        pager_parts.append(
            '<a class="pager-next" href="index.html">'
            '<span class="pager-label">All vignettes →</span>Index</a>'
        )

    body = f"""<article>
  <p class="year-chip">{v['year']}</p>
  <h1>{html.escape(v['title'])}</h1>
  <div class="meta">
    <span class="motif">Motif: {MOTIF}</span>
    {f'<span class="subs">{subs}</span>' if subs else ''}
  </div>
  {md_to_html(v['body'])}
  <nav class="pager">{''.join(pager_parts)}</nav>
</article>"""
    return page_chrome(title, body, crumbs)


def render_index(vignettes):
    items = []
    for v in vignettes:
        subs = " · ".join(f"r/{s}" for s in v.get("subreddits", []))
        items.append(
            f'<li><a href="{v["year"]}.html">'
            f'<span class="yr">{v["year"]}</span>'
            f'<span class="title">{html.escape(v["title"])}</span></a>'
            + (f'<span class="subs">{subs}</span>' if subs else "")
            + "</li>"
        )
    body = f"""<main>
  <h1>{SITE_TITLE}</h1>
  <p class="meta"><span class="motif">Motif: {MOTIF}</span>
  <span>{len(vignettes)} vignettes · {vignettes[0]['year']}–{vignettes[-1]['year']}</span></p>

  <p><a class="read-all-link" href="all.html">Read all on one page →</a></p>

  <h2>Preface</h2>
  {PREFACE_HTML}

  <h2>Vignettes</h2>
  <ol class="vlist">
    {''.join(items)}
  </ol>

  <h2>Coda</h2>
  {CODA_HTML}
</main>"""
    return page_chrome(f"{SITE_TITLE}", body)


def render_single_page(vignettes):
    """Single-page version: all vignettes on one scrolling page, with a
    sticky horizontal timeline that highlights the current year."""

    timeline_items = []
    for v in vignettes:
        timeline_items.append(
            f'<li><a href="#y{v["year"]}" data-year="{v["year"]}">'
            f'<span class="dot"></span><span class="label">{v["year"]}</span>'
            f"</a></li>"
        )

    sections = []
    for v in vignettes:
        subs = " · ".join(f"r/{s}" for s in v.get("subreddits", []))
        sections.append(
            f'<section id="y{v["year"]}" class="year-vignette" data-year="{v["year"]}">\n'
            f'  <p class="year-chip">{v["year"]}</p>\n'
            f'  <h2>{html.escape(v["title"])}</h2>\n'
            f'  <div class="meta">\n'
            f'    <span class="motif">Motif: {MOTIF}</span>\n'
            + (f'    <span class="subs">{subs}</span>\n' if subs else "")
            + f'  </div>\n  {md_to_html(v["body"])}\n</section>'
        )

    script = """
<script>
(function(){
  var links = Array.from(document.querySelectorAll('.timeline-track a'));
  var sections = Array.from(document.querySelectorAll('.year-vignette[data-year]'));
  var fill = document.querySelector('.timeline-fill');
  var track = document.querySelector('.timeline-track');

  function setActive(year){
    var idx = -1;
    links.forEach(function(a, i){
      var match = a.dataset.year === String(year);
      a.classList.toggle('active', match);
      if (match) idx = i;
    });
    links.forEach(function(a, i){
      a.classList.toggle('visited', idx > -1 && i < idx);
    });
    if (fill && track && idx > -1 && links.length > 1){
      var first = links[0].getBoundingClientRect();
      var current = links[idx].getBoundingClientRect();
      var trackRect = track.getBoundingClientRect();
      var w = (current.left + current.width/2) - (first.left + first.width/2);
      var total = trackRect.width - first.width;
      var pct = total > 0 ? (w/total) * 100 : 0;
      fill.style.width = Math.max(0, Math.min(100, pct)) + '%';
    }
  }

  // IntersectionObserver: pick the section closest to the top of viewport
  var visible = new Map();
  var io = new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if (e.isIntersecting) visible.set(e.target, e.intersectionRatio);
      else visible.delete(e.target);
    });
    if (visible.size === 0) return;
    // Pick section whose top is closest to (but above) ~120px from viewport top.
    var best = null, bestTop = -Infinity;
    visible.forEach(function(_, el){
      var t = el.getBoundingClientRect().top;
      if (t <= 160 && t > bestTop){ bestTop = t; best = el; }
    });
    if (!best){
      // No section above the line — pick the topmost visible one.
      visible.forEach(function(_, el){
        var t = el.getBoundingClientRect().top;
        if (!best || t < best.getBoundingClientRect().top) best = el;
      });
    }
    if (best) setActive(best.dataset.year);
  }, { rootMargin: '-100px 0px -50% 0px', threshold: [0, 0.25, 0.5, 0.75, 1] });

  sections.forEach(function(s){ io.observe(s); });

  // Smooth-scroll on timeline click, accounting for sticky header height.
  links.forEach(function(a){
    a.addEventListener('click', function(ev){
      ev.preventDefault();
      var year = a.dataset.year;
      var target = document.getElementById('y' + year);
      if (!target) return;
      var headerH = document.querySelector('.timeline').offsetHeight + 8;
      var y = target.getBoundingClientRect().top + window.pageYOffset - headerH;
      window.scrollTo({ top: y, behavior: 'smooth' });
      history.replaceState(null, '', '#y' + year);
    });
  });

  // Initialize from hash if present, else first.
  var hash = window.location.hash.replace('#y', '');
  if (hash) setActive(hash); else if (sections.length) setActive(sections[0].dataset.year);
})();
</script>
"""

    body = f"""<header class="timeline" role="navigation" aria-label="Year timeline">
  <div class="timeline-inner">
    <div class="timeline-head">
      <h1>{SITE_TITLE} · {vignettes[0]['year']}–{vignettes[-1]['year']}</h1>
      <div class="crumbs"><a href="index.html">Index</a> · <a href="../index.html">Quimbot</a></div>
    </div>
    <div class="timeline-bar">
      <div class="timeline-rail"></div>
      <div class="timeline-fill"></div>
      <ol class="timeline-track">
        {''.join(timeline_items)}
      </ol>
    </div>
  </div>
</header>

<section class="preface">
  <p class="meta"><span class="motif">Motif: {MOTIF}</span>
  <span>{len(vignettes)} vignettes · paraphrased per disguise protocol</span></p>
  <h2>Preface</h2>
  {PREFACE_HTML}
</section>

<main>
{chr(10).join(sections)}

<section class="year-vignette" style="border-top:1px solid var(--stroke)">
  <h2>Coda</h2>
  {CODA_HTML}
</section>
</main>

{script}"""

    return page_chrome(
        f"{SITE_TITLE} · All vignettes",
        body,
        body_class="allpage",
    )


def main():
    files = sorted(SRC.glob("[0-9][0-9][0-9][0-9]*.md"))
    if not files:
        print("No source files in _src/", file=sys.stderr)
        sys.exit(1)

    vignettes = []
    for f in files:
        fm, body = parse_frontmatter(f.read_text(encoding="utf-8"))
        if str(fm.get("published", "")).lower() == "false":
            continue
        if "year" not in fm or "title" not in fm:
            print(f"  skip {f.name}: missing year/title", file=sys.stderr)
            continue
        fm["year"] = int(fm["year"])
        fm["body"] = body
        fm["source_file"] = f.name
        vignettes.append(fm)

    vignettes.sort(key=lambda v: v["year"])

    written = []
    for i, v in enumerate(vignettes):
        prev_v = vignettes[i - 1] if i > 0 else None
        next_v = vignettes[i + 1] if i + 1 < len(vignettes) else None
        out = ROOT / f"{v['year']}.html"
        out.write_text(render_year_page(v, prev_v, next_v), encoding="utf-8")
        written.append(out.name)

    index_out = ROOT / "index.html"
    index_out.write_text(render_index(vignettes), encoding="utf-8")
    written.append(index_out.name)

    all_out = ROOT / "all.html"
    all_out.write_text(render_single_page(vignettes), encoding="utf-8")
    written.append(all_out.name)

    print(f"Built {len(vignettes)} vignettes ({vignettes[0]['year']}–{vignettes[-1]['year']})")
    for name in written:
        print(f"  wrote {name}")


if __name__ == "__main__":
    main()
