#!/usr/bin/env bash
# Pre-render Mermaid diagrams to static SVG. Reveal.js measures hidden slides at
# zero width, so diagrams must be baked to SVG rather than rendered in-browser.
# Re-run after editing any diagrams/*.mmd.
set -e
cd "$(dirname "$0")"
export PUPPETEER_SKIP_DOWNLOAD=1

targets=("$@")
if [ ${#targets[@]} -eq 0 ]; then
  targets=(diagrams/*.mmd)
fi

# Prefer the version pinned in package.json; `npm install` here to get it.
if [ -x node_modules/.bin/mmdc ]; then
  mmdc() { node_modules/.bin/mmdc "$@"; }
else
  echo "note: node_modules missing — falling back to npx (slow). Run: npm install"
  mmdc() { npx -y @mermaid-js/mermaid-cli "$@"; }
fi

for f in "${targets[@]}"; do
  name=$(basename "$f" .mmd)
  echo "rendering $name"
  mmdc -i "$f" -o "images/$name.svg" -c mermaid-config.json -b transparent
done

# Post-process: round node corners (mermaid's cornerRadius is ignored for
# label-container rects) and thicken the edges so they read from the back row.
python3 - "${targets[@]}" << 'PYEOF'
import re, sys, os

EXTRA_CSS = (
    ".flowchart-link{stroke:#5d6d7e!important;stroke-width:1.8px!important;}"
    ".arrowheadPath{fill:#5d6d7e!important;}"
    ".marker{fill:#5d6d7e!important;stroke:#5d6d7e!important;}"
    ".cluster rect{rx:10px;border-radius:10px;}"
)

paths = [os.path.join("images", os.path.basename(a)[:-4] + ".svg") for a in sys.argv[1:]]
for path in paths:
    with open(path) as f:
        svg = f.read()
    svg = re.sub(
        r'(<rect class="basic label-container"(?![^>]*\brx=)[^>]*?)(/?>)',
        r'\1 rx="8"\2', svg)
    if EXTRA_CSS not in svg:
        svg = svg.replace('</style>', EXTRA_CSS + '</style>', 1)
    with open(path, 'w') as f:
        f.write(svg)
print(f"styled {len(paths)} SVGs")
PYEOF

echo "done"
