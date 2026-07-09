#!/usr/bin/env python3
"""Regenerate the Module 11 (Matplotlib) chart images as SVG.

Every figure here reproduces, verbatim, the code shown on the corresponding
slide — students must see exactly what running that snippet produces. Do not
restyle: stock matplotlib defaults are the point.

    python3 figures/make-figures.py          # all
    python3 figures/make-figures.py m11-bar  # one, by stem
"""
import math
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent.parent / "images"

# Text is emitted as paths so the slides render identically on any machine,
# with or without the font matplotlib picked here.
matplotlib.rcParams["svg.fonttype"] = "path"

_figures = {}


def figure(name):
    def wrap(fn):
        _figures[name] = fn
        return fn

    return wrap


def save(name):
    path = OUT / f"{name}.svg"
    plt.savefig(path, format="svg", bbox_inches="tight")
    plt.close("all")
    print(f"  wrote {path.name}")


# --- shared data, named as on the slides -----------------------------------
data8 = [6, 0, 2, 1, -5, 4, 3, 8]
x_pairs = [-2, -1, 2, 4, 8, 9, 12, 17]
y_pairs = [6, 0, 2, 1, -5, 4, 3, 8]
x1_5 = [17, -2, -1, 2, 4, 8, 9, 12]
y1_5 = [8, 6, 0, 2, 1, -5, 4, 3]
heart_x = [5, 3, 4, 5, 6, 7, 5, 5.35, 4.65, 5]
heart_y = [0, 2, 3, 2.5, 3, 2, 0, 0.9, 1.7, 2.5]

x1 = range(-1, 6)
y1 = [0.5 * i for i in x1]
x2 = range(-3, 4)
y2 = [i**2 for i in x2]
x3 = range(1, 7)
y3 = [1 / i for i in x3]

labels = ["Jan", "Feb", "Mar", "Apr", "May"]
values1 = [10, 20, 25, 12, 17]
values2 = [12, 5, 28, 4, 7]
barwidth = 0.4

hist_data = [12, 0, 21, 15, 41, 50, 55, 44, 100, 48, 51, 93,
             72, 5, 13, 16, 12, 27, 38, 49, 21, 65, 7, 72]

data2d = [
    [1, 2, 3, 4, 5, 6, 7],
    [2, 4, 6, 8, 10, 12, 10],
    [3, 6, 3, 6, 3, 6, 3],
    [6, 5, 4, 3, 2, 1, 2],
    [6, 6, 6, 9, 9, 9, 6],
    [10, 12, 10, 8, 5, 2, 5],
]


# --- Line plot --------------------------------------------------------------
@figure("m11-ex1")
def _():
    plt.plot(data8)


@figure("m11-ex4a")
def _():
    plt.plot(x_pairs, y_pairs)


@figure("m11-ex4b")
def _():
    plt.plot(y_pairs, x_pairs)


@figure("m11-ex5a")
def _():
    plt.plot(x1_5, y1_5)


@figure("m11-ex5b")
def _():
    plt.plot(heart_x, heart_y)


@figure("m11-ex6")
def _():
    u, a = 3, 10
    times = range(0, 10)
    distances = [u * t + 0.5 * a * t**2 for t in times]
    plt.plot(times, distances)


@figure("m11-ex7")
def _():
    u, a = 3, 10
    t = range(0, 10, 1)
    s = [u * ts + 0.5 * a * ts**2 for ts in t]
    plt.plot(t, s)
    plt.xlabel("Time(s)")
    plt.ylabel("Distance(m)")
    plt.title("Vehicle Movement Chart")


# --- Styling ----------------------------------------------------------------
@figure("m11-color")
def _():
    plt.plot(heart_x, heart_y, color=(0.5, 0, 1), marker="*")


@figure("m11-linewidth")
def _():
    plt.plot(heart_x, heart_y, color=(1, 0.5, 0), linewidth=4.0)


@figure("m11-linestyle")
def _():
    plt.plot(heart_x, heart_y, color=(1, 0.5, 0), linewidth=4.0, linestyle=":")


@figure("m11-marker")
def _():
    plt.plot(heart_x, heart_y, color=(1, 0.5, 0), linewidth=4.0,
             linestyle="--", marker="o")


@figure("m11-markersize")
def _():
    plt.plot(heart_x, heart_y, color=(1, 0, 0), linewidth=4.0,
             linestyle="", marker="+", markersize=12)


@figure("m11-multi")
def _():
    plt.plot(x1, y1)
    plt.plot(x2, y2)
    plt.plot(x3, y3)


@figure("m11-multi-styled")
def _():
    plt.plot(x1, y1, color=(1, 0, 0), linestyle="-", marker="s")
    plt.plot(x2, y2, color=(0, 0, 1), linestyle=":", marker="^")
    plt.plot(x3, y3, color=(1, 0, 1), linestyle="", marker=".")


@figure("m11-format")
def _():
    plt.plot(x1, y1, "r-s")
    plt.plot(x2, y2, "b:^")
    plt.plot(x3, y3, "m .")


@figure("m11-legend")
def _():
    plt.plot(x1, y1, color=(1, 0, 0), linestyle="-", marker="s", label="Line1")
    plt.plot(x2, y2, "b:^", label="Line2")
    plt.plot(x3, y3, "m.", label="Line3")
    plt.legend()


@figure("m11-figsize")
def _():
    plt.figure(figsize=(5, 5))
    plt.plot(x1, y1, color=(1, 0, 0), linestyle="-", marker="s", label="Line1")
    plt.plot(x2, y2, "b:^", label="Line2")
    plt.plot(x3, y3, "m.", label="Line3")
    plt.legend()


# --- Bar plot ---------------------------------------------------------------
@figure("m11-bar")
def _():
    plt.bar(labels, values1)


@figure("m11-barh")
def _():
    plt.barh(labels, values1)


@figure("m11-barh-inv")
def _():
    plt.barh(labels, values1)
    plt.gca().invert_yaxis()


@figure("m11-bar-width")
def _():
    plt.bar(labels, values1, 0.5)


@figure("m11-bar-overlap")
def _():
    plt.bar(labels, values1, barwidth, label="values1")
    plt.bar(labels, values2, barwidth, label="values2")
    plt.legend()


@figure("m11-bar-ticks")
def _():
    bx1 = [i - barwidth / 2 for i in range(len(labels))]
    bx2 = [i + barwidth / 2 for i in range(len(labels))]
    plt.bar(bx1, values1, barwidth, label="values1")
    plt.bar(bx2, values2, barwidth, label="values2")
    plt.xticks(range(len(labels)), labels)
    plt.legend()


# --- Histogram --------------------------------------------------------------
@figure("m11-hist")
def _():
    plt.hist(hist_data)


@figure("m11-hist-bins")
def _():
    plt.hist(hist_data, 20)


@figure("m11-hist-xticks")
def _():
    plt.hist(hist_data)
    plt.xticks(range(0, 105, 5))


@figure("m11-hist-styled")
def _():
    plt.hist(hist_data, facecolor="blue", edgecolor="black")
    plt.xticks(range(0, 105, 10))


# --- Pie chart --------------------------------------------------------------
@figure("m11-pie")
def _():
    plt.pie(values1)


@figure("m11-pie-labels")
def _():
    plt.pie(values1, labels=labels)


@figure("m11-pie-pct")
def _():
    plt.pie(values1, labels=labels, autopct="%.2f%%")


@figure("m11-pie-explode")
def _():
    plt.pie(values1, labels=labels, explode=[0, 0, 0.1, 0, 0], autopct="%.2f%%")


# --- Heatmap ----------------------------------------------------------------
@figure("m11-heatmap")
def _():
    plt.imshow(data2d)


@figure("m11-heatmap-ticks")
def _():
    plt.imshow(data2d)
    plt.xticks(range(len(data2d[0])), range(1, len(data2d[0]) + 1))
    plt.yticks(range(len(data2d)), range(5, len(data2d) + 5))


@figure("m11-heatmap-hot")
def _():
    plt.imshow(data2d, cmap="hot")
    plt.colorbar()


# --- Subplots & figures -----------------------------------------------------
@figure("m11-subplot")
def _():
    xs = [i * 0.1 for i in range(201)]
    for j in range(6):
        plt.subplot(2, 3, j + 1)
        plt.plot(xs, [math.sin((j + 1) * i) for i in xs])


@figure("m11-subplot-loop")
def _():
    xs = [i * 0.01 for i in range(2001)]
    y = [[math.sin(i * (j + 1)) for i in xs] for j in range(8)]
    for j in range(8):
        plt.subplot(2, 4, j + 1)
        plt.plot(xs, y[j])


@figure("m11-figure")
def _():
    # The slide opens four figures; the image shows the first one.
    xs = [i * 0.1 for i in range(201)]
    plt.plot(xs, [math.sin(i) for i in xs])


def main():
    wanted = sys.argv[1:] or sorted(_figures)
    unknown = [w for w in wanted if w not in _figures]
    if unknown:
        sys.exit(f"unknown figure(s): {', '.join(unknown)}")
    for name in wanted:
        print(f"building {name}")
        _figures[name]()
        save(name)
    print(f"done: {len(wanted)} figures")


if __name__ == "__main__":
    main()
