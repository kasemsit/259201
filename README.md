# 259201 — Introduction to Computers for Engineers

Interactive lecture slides built with [Quarto](https://quarto.org/) Reveal.js and [quarto-live](https://github.com/r-wasm/quarto-live) (Pyodide) for in-browser Python execution.

## Modules

| Module | Topic |
|:------:|:------|
| 1 | Course Orientation / Introduction to Programming |
| 2 | Computational Thinking |
| 3 | Variables and Types, Operators, Input/Output |
| 4 | Collections: List, Tuple, Set and Dictionary |
| 5 | Conditions: Boolean, in, if-else, if-elif-else |
| 6 | Iterations (I): while-loop |
| 7 | Iterations (II): for-loop |
| 8 | Iterations and Collections |
| 9 | Functions |
| 10 | List Comprehension and 2D Arrays |
| 11 | Basic Data Visualization with Matplotlib |
| 12 | N-Dimensional Arrays with Numpy |

## Pyodide Limitations

Slides use [Pyodide](https://pyodide.org/) to run Python in the browser. Key limitations:

| Topic | Details |
|-------|---------|
| **Supported packages** | numpy, pandas, matplotlib, scipy, scikit-learn and other pre-compiled packages are available |
| **I/O** | No `input()`, no real filesystem access, no network (`requests`, `urllib`) |
| **Threading** | No multiprocessing / threading |
| **C extensions** | Only packages pre-compiled to WebAssembly; uncommon C/Rust extensions may be unavailable |
| **Performance** | ~3–5x slower than native Python |
| **Memory** | Limited by the browser (~2–4 GB) |
| **matplotlib** | Renders static images (PNG), not interactive plots |

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Build

```bash
# Render the entire site (homepage + all slides)
QUARTO_PYTHON=.venv/bin/python quarto render

# Render a single module
QUARTO_PYTHON=.venv/bin/python quarto render slides/module03.qmd

# Preview locally
QUARTO_PYTHON=.venv/bin/python quarto preview
```

Output is generated in `_output/`.

## Deploy to GitHub Pages

Automated via GitHub Actions — push to `main` triggers a build and deploy.

Ensure **Settings → Pages → Source** is set to **GitHub Actions**.
