# Convert ipynb to Quarto Reveal.js Slides

Convert a Jupyter notebook (.ipynb) from `ipynb/` into a Quarto reveal.js slide deck in `slides/`.

## Usage

```
/convert-slides <ipynb_filename>
```

Example: `/convert-slides 168_259201_Module04.ipynb`

## Input

The argument `$ARGUMENTS` is the ipynb filename (with or without `ipynb/` prefix).

## Instructions

1. **Read the ipynb file** from `ipynb/` directory. Parse all markdown and code cells.

2. **Extract the module number** from the filename (e.g., `Module04` → `module04`).

3. **Create `slides/moduleNN.qmd`** with the following YAML frontmatter (copy exactly):

```yaml
---
title: "Module N"
subtitle: "<subtitle from the notebook's first cell>"
format:
  live-revealjs:
    theme: [default, custom.scss]
    slide-number: c/t
    code-line-numbers: false
    code-overflow: wrap
    highlight-style: github
    transition: fade
    transition-speed: fast
    width: 1280
    height: 720
    margin: 0.08
    logo: ""
    footer: "259201 — Module N | ภาควิชาวิศวกรรมคอมพิวเตอร์ คณะวิศวกรรมศาสตร์ มหาวิทยาลัยเชียงใหม่"
    code-block-height: 480px
pyodide:
  packages: []
execute:
  echo: true
  eval: false
---
```

4. **Convert content** following these rules:

### Slide Structure
- Each major section (`## Section Title` in ipynb) becomes a **section title slide**:
  ```
  # Section Title {background-color="#2c3e50" .white-text}

  short description
  ```
- Each subsection or topic becomes a `## Slide Title` (level 2 heading = one slide).
- Keep content per slide concise. If a concept is too long, split into multiple slides.

### Exercise Slides (โจทย์)
Every exercise (โจทย์) in the ipynb MUST follow this pattern:

```markdown
## โจทย์ #N {.exercise}

<question text from ipynb — show the problem, NOT the code>
<use incremental reveals if the question has multiple steps — see below>

::: {.panel-tabset}

### Live Code

```{pyodide}
#| autorun: false
<starter code with ____ blanks — see rules below>
```

### Solution

```python
<full solution code>
```

```{.python .code-output}
<expected output>
```

<optional callout or note>

:::
```

For exercises marked "ชวนคิด" use `{.exercise-think}` instead of `{.exercise}`.

### Incremental Questions in Exercises
Many exercises in the ipynb have multi-step questions (e.g., "create variable → display value → check type → what type do you think it is?"). These MUST be presented incrementally using `. . .` so the instructor reveals one step at a time **before** the tabset:

```markdown
## โจทย์ #N {.exercise}

สร้างตัวแปร `s2` เก็บผลบวกของ `2500` กับ `1000`

. . .

แสดงค่าและตรวจสอบ type

. . .

**คิดก่อน:** `s2` จะเป็นชนิดใด?

::: {.panel-tabset}
...
:::
```

Rules:
- Read the ipynb's **algorithm/วิธีคิด** section to understand the steps.
- Each distinct instruction or thinking prompt = one `. . .` fragment.
- **คิดก่อน:** questions should always be the last fragment before the tabset, giving students time to think.
- Short single-step exercises (e.g., "แสดงผลข้อความ X") do NOT need incremental — go straight to the tabset.

### Starter Code Rules (Live Code tab)
- Give the **structure** of the solution with `____` as fill-in blanks for the key parts.
- Provide variable names, print statements, and setup code. Leave the **operator, function call, or expression** as `____`.
- Examples:
  - Variable assignment: `var1 = ____` (student fills the expression)
  - Operator exercise: `r = people ____ group` (student fills `%` or `//`)
  - Function call: `print(math.____(25))` (student fills `sqrt`)
  - Type conversion: `i = ____(42 + 3.5)` (student fills `int`)
- For `input()` exercises: since Pyodide doesn't support interactive input, hardcode a sample value:
  ```python
  # input() ไม่ทำงานใน Pyodide — จำลองด้วยค่าตรง
  x = '5'
  ```

### Concept/Explanation Slides
- Use `. . .` (incremental reveal) to show code examples step by step.
- Use `:::: {.columns}` for side-by-side layout.
- Use `::: {.incremental}` for bullet lists that appear one by one.
- Use `::: {.callout-note}`, `{.callout-tip}`, `{.callout-warning}`, `{.callout-important}` for highlighted boxes.
- Use `{.python .code-output}` for static output blocks.

### Slide IDs for Key Concepts
Add `{#mN-topic}` to every concept/explanation slide heading (NOT exercise slides). Use the pattern `mN-` where N is the module number:
```markdown
## Arithmetic Operators {#m4-list-ops}
```
This enables cross-module linking.

### Cross-Reference Links (Review Links)
Read `slides/cross-references.md` for the full dependency map. When a concept or exercise relies on knowledge from a previous module, add a review link callout:

```markdown
::: {.callout-note}
ทบทวน: [Comparison Operators (Module 3)](module03.html#m3-comparison)
:::
```

**When to add review links:**
- When a concept is used for the **first time since it was taught** (e.g., Module 5 using `%` for odd/even — link back to `m3-arithmetic`)
- When an exercise combines concepts from **multiple previous modules** (e.g., Module 8 using list + for-loop + if — link to all three)
- When the difficulty level is **high** and students are likely to forget the prerequisite
- Do NOT over-link — skip obvious things like basic variable assignment or `print()`

### Content Fidelity
- **Do NOT skip any content** from the ipynb. Every markdown cell and code cell must appear in the slides.
- Preserve the original Thai/English bilingual text.
- Preserve all mathematical notation using LaTeX (`$...$` or `$$...$$`).
- Preserve the exercise numbering from the ipynb.
- Include the **algorithm/วิธีคิด** hints from ipynb as part of the question text where appropriate.

### Summary Slide
End with a summary slide using two-column layout:
```markdown
# Summary {background-color="#2c3e50" .white-text}

## สรุป Module N

:::: {.columns}
::: {.column width="50%"}
...
:::
::: {.column width="50%"}
...
:::
::::
```

5. **Render the slides**:
```bash
QUARTO_PYTHON=/home/kasemsit/Projects/259201/.venv/bin/python quarto render slides/moduleNN.qmd
```

6. **Verify** the output file exists at `_output/slides/moduleNN.html` and report the slide count.

7. **Do NOT modify** `custom.scss`, `_quarto.yml`, or any other existing files.
