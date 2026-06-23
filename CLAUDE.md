# 259201 — Introduction to Computers for Engineers

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
│   └── module03.qmd          # Example completed module
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
QUARTO_PYTHON=.venv/bin/python quarto render slides/module03.qmd

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

## Do NOT

- Modify `custom.scss` without asking — it affects all modules
- Skip any content from the source ipynb
- Use `monokai` highlight style (too dark for live editor)
- Put `{pyodide}` blocks inside `<details>` tags (breaks rendering)
