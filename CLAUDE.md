# 259201 — Computer Programming for Engineers

## Project Overview

University course lecture slides built with **Quarto Reveal.js** + **quarto-live** (Pyodide).
Original content lives in Jupyter notebooks (`ipynb/`), converted to interactive slide decks (`slides/`).

## Project Structure

```
259201/
├── CLAUDE.md
├── _quarto.yml              # Quarto project config
├── module_list.md            # Course module list (1–12)
├── requirements.txt          # Python dependencies (venv)
├── ipynb/                    # Source notebooks (Module 3–8)
├── slides/                   # Quarto slide decks (.qmd)
│   ├── custom.scss           # Shared theme/styling
│   ├── cross-references.md   # Slide-ID map for cross-module review links
│   ├── diagrams/             # Mermaid sources (*.mmd) → images/*.svg
│   ├── figures/              # make-figures.py → images/m11-*.svg
│   ├── poll/                 # Live audience voting (Firebase): vote.html, results.html, poll-config.js, make-qr.py
│   ├── mermaid-config.json   # Mermaid theme (fonts, colors, spacing)
│   ├── render-diagrams.sh    # diagrams/*.mmd → SVG + post-process
│   ├── images/               # Slide images (SVG diagrams, CC/xkcd comics)
│   ├── module03a.qmd         # Variables, Operators, Math
│   ├── module03b.qmd         # Input/Output, f-string
│   ├── module04a.qmd         # Collections: List
│   ├── module04b.qmd         # Collections: Tuple, Set, Dict
│   └── module05–08.qmd       # Conditions, while, for, iterations+collections
├── _output/                  # Rendered HTML output
│   └── slides/
├── _extensions/              # quarto-live extension
└── .claude/
    └── commands/
        └── convert-slides.md # /convert-slides slash command
```

## Commands

- `/convert-slides <filename.ipynb>` — Convert a notebook from `ipynb/` to a Quarto slide deck in `slides/`. See `.claude/commands/convert-slides.md` for full spec.

## Build & Render

```bash
# Render a single module
QUARTO_PYTHON=.venv/bin/python quarto render slides/module03a.qmd

# Output goes to _output/slides/moduleNN.html

# One-time: install the pinned mermaid-cli (node_modules/ is gitignored)
cd slides && PUPPETEER_SKIP_DOWNLOAD=1 npm install

# Regenerate Mermaid diagrams after editing diagrams/*.mmd (all, or named ones)
slides/render-diagrams.sh
slides/render-diagrams.sh diagrams/m5-if.mmd

# Regenerate the Module 11 matplotlib charts (all, or one by stem)
cd slides && ../.venv/bin/python figures/make-figures.py
cd slides && ../.venv/bin/python figures/make-figures.py m11-bar
```

## Images: three SVG pipelines

**Never add a raster diagram.** Photos and comics stay raster; everything we draw is SVG.

1. **Mermaid flowcharts** — `diagrams/*.mmd` → `images/*.svg` via `render-diagrams.sh`.
   Pre-rendered because Reveal.js measures hidden slides at zero width. The script also runs a
   Python post-processor that adds `rx="8"` to node rects and thickens edges — don't skip it.
   `mermaid-cli` is pinned in `slides/package.json`; the script falls back to a slow `npx` if
   `node_modules/` is missing.
   Shared `classDef` palette, keyed to `custom.scss`:

   | Role | fill | stroke | text |
   |---|---|---|---|
   | `term` (entry/exit) | `#ecf0f1` | `#7f8c8d` | `#2c3e50` |
   | `cond` (decision) | `#eaf2fb` | `#2980b9` | `#1a5276` |
   | `stmt` (true branch) | `#eafaf1` | `#27ae60` | `#145a32` |
   | `alt` (false branch) | `#fdedec` | `#c0392b` | `#922b21` |
   | `io` | `#fef5e7` | `#e67e22` | `#7e5109` |
   | `neut` | `#f4f6f7` | `#7f8c8d` | `#2c3e50` |

   When a flowchart sits beside a code skeleton, colour each branch to match its line of code
   (see `m5-if-elif-else`).

2. **Hand-drawn concept SVGs** — `images/mNN-<slug>.svg`, written directly in SVG. Conventions:
   - Root carries `font-family` = mono stack; each file has a `<style>` block
   - **`<text>` containing Thai gets `class="th"` (sans stack); code tokens stay mono.**
     Inside a `th` text, wrap code fragments in `<tspan class="c">`
   - Rounded boxes `rx="8"`, arrow markers `fill="#5d6d7e"`, `stroke-width` 1.5–2.5
   - Same palette as the Mermaid table above

3. **Matplotlib charts (Module 11)** — `figures/make-figures.py` → `images/m11-*.svg`.
   Each figure reproduces the code shown on its slide **verbatim** — students must see exactly what
   running that snippet produces. Stock matplotlib defaults; do not restyle.

Never inline `<svg>` into a `.qmd` — it makes the deck unreadable and the styling unshareable.

## Slide Conventions

- **Format**: `live-revealjs` with `custom.scss` theme
- **Highlight**: `github` (light background)
- **Section dividers**: `# Title {background-color="#2c3e50" .white-text}`
- **Exercise slides**: `## โจทย์ #N {.exercise}` — green left border
- **Think exercises**: `## โจทย์ #N: ชวนคิด {.exercise-think}` — orange left border
- **Every exercise** has a `panel-tabset` with **Live Code** (pyodide editor with starter code using `____` blanks) and **Solution** (static code + output)
- **`input()` exercises**: hardcode sample values since Pyodide doesn't support interactive input
- **Concept slides**: use `. . .` fragments, `{.incremental}`, columns, callouts
- **Bold** the word **คิดก่อน:** when used in exercise text
- **Inline code** styled red on light gray (`custom.scss`)
- **Emoji**: section dividers, topic slide, and summary slide carry a topical emoji
- **Reveal one column at a time**: add `.fragment` to each `::: {.column ...}`
- **Foldable answer** (no Live Code): use `<details><summary>…</summary> … </details>` (never wrap `{pyodide}` in it)
- **Bigger/smaller text on part of a slide**: use inline `[text]{style="font-size:1.5em"}` or a `::: {style="..."}` div — `.smaller` only works on a whole slide (`## Title {.smaller}`), not on a div
- **Colored syntax skeleton**: reuse the `.code-pattern` box (see `custom.scss`) with `<span>` colors for parts like `start:stop:step` — never render a syntax skeleton as an image
- **Images**: store in `slides/images/`, reference with `![](...){...}` (not `<img>`); credit CC/xkcd sources with license + link. See **Images: three SVG pipelines** above
- **Reusable `custom.scss` classes** (so you don't re-fight reveal defaults):
  - **Captioned image**: wrap in `:::: {.figbox}` (image) + `::: {.figcap}` (credit/caption) — centers the image and hugs the caption under it. Needed because reveal gives every `<img>` a border + `margin:15px 0`, so plain markdown captions drift away and don't center.
  - **Row of brand logos**: `::: {.logos}` around inline `![](logo-x.svg)` — strips the reveal img border/margin and lays them out centered.
  - **Syntax skeleton**: `.code-pattern` box with `<span>` colors (see below).
- **AI-generated images**: caption them honestly (e.g. `ภาพจำลอง (AI-generated)`); optimize to JPEG (~200–330 KB) before committing

## Splitting a long module (e.g. `moduleNN` → `moduleNNa` / `moduleNNb`)

- Each part is a standalone deck: own front-matter (title/subtitle/footer `Module NNa`), topics slide, and summary; cross-link the parts with a `callout-note`
- Keep slide IDs (`{#m...}`) unchanged so anchors stay stable; update every cross-module link (`moduleNN.html#...` → `moduleNNa/b.html#...`) across `slides/*.qmd`, `cross-references.md`, `convert-slides.md`, and `index.qmd`
- Verify with `grep -rn "moduleNN.html"` and re-render the dependent modules (stale `_output/*.html` keeps old links)

## Live audience polling (`slides/poll/`)

Realtime in-slide voting backed by **Firebase Realtime Database** (free Spark plan) — no paid service, self-owned.

- `poll-config.js` — Firebase config + a `POLLS` object (question/options per `pollId`). **The only file to edit to add a question.**
- `vote.html` — student page (opened via QR on phones) → pushes a vote.
- `results.html` — live bar chart, embedded in a slide as a raw-HTML `` ```{=html} `` `<iframe src="poll/results.html?poll=<id>">`.
- `make-qr.py` — regenerates `images/qr-poll-<id>.png` from the deployed vote URL (uses `qrcode`, in `requirements` after `pip install qrcode[pil]`).
- Pages are copied to `_output/slides/poll/` via the `resources:` key in `_quarto.yml` (iframes aren't auto-detected, so this is required).

**Sessions (so re-teaching doesn't mix results):** votes live at `polls/<pollId>/<session>/votes`; `session` defaults to **today's date**, so different class-days stay separate automatically. For two same-day sections, append `&session=secA` to **both** the iframe `src` and the QR URL.

Full setup (Firebase project, DB rules, deploy to Firebase Hosting / GitHub Pages) is in `slides/poll/README.md`. Example: the `#m1-poll` slide in `module01.qmd`.

## Do NOT

- Modify `custom.scss` without asking — it affects all modules
- Skip any content from the source ipynb
- Use `monokai` highlight style (too dark for live editor)
- Put `{pyodide}` blocks inside `<details>` tags (breaks rendering)
- Inline `<svg>` into a `.qmd`, or add a new raster diagram — draw SVG to `images/` instead
- Hand-edit a generated SVG. `images/x.svg` is generated if `diagrams/x.mmd` exists, or if the
  stem is `m11-*`. Change the `.mmd` / `make-figures.py` source and re-run instead
