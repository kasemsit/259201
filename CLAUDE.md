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
│   ├── images/               # Slide images (diagrams, CC/xkcd comics)
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
```

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
- **Colored syntax skeleton**: reuse the `.code-pattern` box (see `custom.scss`) with `<span>` colors for parts like `start:stop:step`
- **Images**: store in `slides/images/`, reference with `![](...){...}` (not `<img>`); credit CC/xkcd sources with license + link

## Splitting a long module (e.g. `moduleNN` → `moduleNNa` / `moduleNNb`)

- Each part is a standalone deck: own front-matter (title/subtitle/footer `Module NNa`), topics slide, and summary; cross-link the parts with a `callout-note`
- Keep slide IDs (`{#m...}`) unchanged so anchors stay stable; update every cross-module link (`moduleNN.html#...` → `moduleNNa/b.html#...`) across `slides/*.qmd`, `cross-references.md`, `convert-slides.md`, and `index.qmd`
- Verify with `grep -rn "moduleNN.html"` and re-render the dependent modules (stale `_output/*.html` keeps old links)

## Do NOT

- Modify `custom.scss` without asking — it affects all modules
- Skip any content from the source ipynb
- Use `monokai` highlight style (too dark for live editor)
- Put `{pyodide}` blocks inside `<details>` tags (breaks rendering)
