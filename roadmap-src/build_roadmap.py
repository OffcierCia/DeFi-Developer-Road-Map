#!/usr/bin/env python3
"""Build the DeFi Developer Roadmap SVGs from roadmap.txt.

Usage: python3 build_roadmap.py [roadmap.txt]

Writes three self-contained SVGs next to this script:
  roadmap-github-dark.svg / roadmap-github-light.svg  (Option A: GitHub-native timeline)
  roadmap-teal.svg                                     (Option B: teal heritage, two-sided spine)

Standard library only. The SVGs use plain <text> and presentation attributes:
no CSS, no web fonts, no filters, no scripts, no images.
"""
import os
import sys
from xml.sax.saxutils import escape

HERE = os.path.dirname(os.path.abspath(__file__))
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, 'Helvetica Neue', Helvetica, Arial, 'Liberation Sans', sans-serif"
WIDTH = 880

# Per-character advance widths (units per 1000 em) for ASCII 32..126, taking the
# widest of SF Pro, Helvetica and Arial so labels never overflow their chips.
_REGULAR = [278, 278, 403, 605, 605, 889, 669, 254, 333, 333, 400, 605, 278, 429, 278, 279, 605, 556, 566, 592, 605, 585, 617, 556, 600, 617, 278, 278, 605, 605, 605, 556, 1015, 667, 667, 722, 722, 667, 611, 778, 722, 278, 500, 667, 556, 833, 722, 778, 667, 778, 722, 667, 611, 722, 667, 944, 667, 667, 617, 323, 279, 323, 605, 556, 500, 556, 556, 501, 556, 556, 304, 556, 556, 222, 222, 500, 222, 833, 556, 556, 556, 556, 333, 500, 302, 556, 500, 722, 500, 500, 500, 334, 260, 334, 605]
_BOLD = [278, 333, 474, 626, 631, 889, 722, 264, 360, 360, 431, 632, 278, 437, 278, 294, 638, 556, 589, 616, 632, 611, 639, 563, 631, 640, 333, 333, 631, 631, 631, 611, 975, 722, 722, 722, 722, 667, 611, 778, 722, 278, 556, 722, 611, 850, 722, 778, 667, 778, 722, 667, 611, 722, 667, 950, 667, 667, 626, 360, 294, 361, 631, 558, 500, 556, 611, 556, 611, 556, 337, 611, 611, 278, 278, 556, 278, 889, 611, 611, 611, 611, 389, 556, 335, 611, 556, 778, 556, 556, 500, 389, 280, 389, 631]


def text_width(s, size, bold=False):
    table = _BOLD if bold else _REGULAR
    units = sum(table[ord(c) - 32] if 32 <= ord(c) < 127 else 1000 for c in s)
    return units / 1000 * size * 1.08  # headroom for Segoe UI / Noto / DejaVu


# ---------------------------------------------------------------- source ----

class Node:
    def __init__(self, label, must=True):
        self.label, self.must, self.children = label, must, []

    @property
    def leaves(self):
        return [c for c in self.children if not c.children]

    @property
    def branches(self):
        return [c for c in self.children if c.children]


def parse(path):
    meta, steps, stack = {}, [], []
    for raw in open(path, encoding="utf-8"):
        line = raw.rstrip("\n")
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        indent = len(line) - len(line.lstrip(" "))
        text = line.strip()
        if indent == 0 and text.startswith("Step"):
            steps.append(Node(text))
            stack = [(0, steps[-1])]
        elif indent == 0:
            key, _, value = text.partition(":")
            meta[key.strip()] = value.strip()
        else:
            marker, label = text[0], text[2:].strip()
            if marker not in "+~":
                raise SystemExit(f"bad marker in line: {line!r}")
            while stack[-1][0] >= indent:
                stack.pop()
            node = Node(label, marker == "+")
            stack[-1][1].children.append(node)
            stack.append((indent, node))
    return meta, steps


# --------------------------------------------------------------- themes -----

THEMES = {
    "github-dark": dict(
        bg="#0d1117", card="#161b22", card_stroke="#30363d", rule="#30363d",
        title="#f0f6fc", spine="#6e7681",
        must_fill="#1f6feb", must_text="#ffffff",
        ext_fill="#0d1117", ext_stroke="#8b949e", ext_text="#e6edf3",
        step_fill="#d29922", step_text="#0d1117",
        bubble_fill="#161b22", bubble_stroke="#8b949e", bubble_text="#f0f6fc",
    ),
    "github-light": dict(
        bg="#ffffff", card="#f6f8fa", card_stroke="#d0d7de", rule="#d0d7de",
        title="#1f2328", spine="#8c959f",
        must_fill="#0969da", must_text="#ffffff",
        ext_fill="#ffffff", ext_stroke="#6e7781", ext_text="#1f2328",
        step_fill="#fff8c5", step_text="#1f2328", step_stroke="#d4a72c",
        bubble_fill="#ffffff", bubble_stroke="#6e7781", bubble_text="#1f2328",
    ),
    "teal": dict(
        bg="#114B5F", card="#0D3D4E", card_stroke="#2C6E83", rule="#2C6E83",
        title="#FFFF88", spine="#C9E4EC",
        must_fill="#D7263D", must_text="#ffffff",
        ext_fill="#0D3D4E", ext_stroke="#A8D5B0", ext_text="#E4FDE1",
        step_fill="#FFFF88", step_text="#0B3A4A",
        bubble_fill="#0D3D4E", bubble_stroke="#E4FDE1", bubble_text="#ffffff",
    ),
}

CHIP_H, CHIP_PAD, GAP, FS = 26, 10, 6, 13


class Svg:
    def __init__(self, theme):
        self.t, self.out = theme, []

    def add(self, s):
        self.out.append(s)

    def text(self, x, y, s, size, fill, bold=False, anchor="middle"):
        weight = ' font-weight="700"' if bold else ""
        self.add(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}"{weight} fill="{fill}" text-anchor="{anchor}">{escape(s)}</text>')

    def line(self, x1, y1, x2, y2, color, width=1, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{width}"{d}/>')

    def path(self, d, color, width=1):
        self.add(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}"/>')

    def chip(self, x, y, label, must, bold=False):
        """Draw a pill; return its width. Must Know = solid fill, Extended = dashed outline."""
        t = self.t
        w = chip_width(label, bold)
        if must:
            self.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{CHIP_H}" rx="{CHIP_H / 2}" fill="{t["must_fill"]}"/>')
            color = t["must_text"]
        else:
            self.add(f'<rect x="{x + .75:.1f}" y="{y + .75:.1f}" width="{w - 1.5:.1f}" height="{CHIP_H - 1.5}" rx="{CHIP_H / 2 - .75}" '
                     f'fill="{t["ext_fill"]}" stroke="{t["ext_stroke"]}" stroke-width="1.5" stroke-dasharray="4 3"/>')
            color = t["ext_text"]
        self.text(x + w / 2, y + CHIP_H / 2 + FS * 0.35, label, FS, color, bold)
        return w

    def step(self, x, y, label, anchor="start"):
        t = self.t
        size, h = 16, 34
        w = text_width(label, size, True) + 32
        if anchor == "middle":
            x -= w / 2
        stroke = f' stroke="{t["step_stroke"]}" stroke-width="1"' if "step_stroke" in t else ""
        self.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h}" rx="{h / 2}" fill="{t["step_fill"]}"{stroke}/>')
        self.text(x + w / 2, y + h / 2 + size * 0.35, label, size, t["step_text"], True)
        return w, h

    def card(self, x, y, w, h):
        t = self.t
        self.add(f'<rect x="{x + .5:.1f}" y="{y + .5:.1f}" width="{w - 1:.1f}" height="{h - 1:.1f}" rx="10" fill="{t["card"]}" stroke="{t["card_stroke"]}" stroke-width="1"/>')

    def header(self, meta, y=0):
        t = self.t
        self.text(24, y + 46, meta["title"], 28, t["title"], True, "start")
        x = WIDTH - 24 - chip_width(meta["extended"]) - 8 - chip_width(meta["must"])
        x += self.chip(x, y + 26, meta["must"], True) + 8
        self.chip(x, y + 26, meta["extended"], False)
        self.line(24, y + 76, WIDTH - 24, y + 76, t["rule"])
        return y + 76

    def footer(self, cx, y, label):
        """Spine arrow into a speech bubble. Returns the bottom y."""
        t = self.t
        self.add(f'<path d="M{cx - 6:.1f} {y - 9:.1f} L{cx:.1f} {y:.1f} L{cx + 6:.1f} {y - 9:.1f}" fill="none" stroke="{t["spine"]}" stroke-width="2"/>')
        size, h = 15, 40
        w = text_width(label, size) + 40
        bx, by = cx - w / 2, y + 12
        self.add(f'<path d="M{bx + 10:.1f} {by:.1f} H{cx - 8:.1f} L{cx:.1f} {by - 8:.1f} L{cx + 8:.1f} {by:.1f} H{bx + w - 10:.1f} '
                 f'Q{bx + w:.1f} {by:.1f} {bx + w:.1f} {by + 10:.1f} V{by + h - 10:.1f} Q{bx + w:.1f} {by + h:.1f} {bx + w - 10:.1f} {by + h:.1f} '
                 f'H{bx + 10:.1f} Q{bx:.1f} {by + h:.1f} {bx:.1f} {by + h - 10:.1f} V{by + 10:.1f} Q{bx:.1f} {by:.1f} {bx + 10:.1f} {by:.1f} Z" '
                 f'fill="{t["bubble_fill"]}" stroke="{t["bubble_stroke"]}" stroke-width="1"/>')
        self.text(cx, by + h / 2 + size * 0.35, label, size, t["bubble_text"])
        return by + h

    def render(self, height, title):
        body = "\n".join(self.out)
        return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{height:.0f}" viewBox="0 0 {WIDTH} {height:.0f}" '
                f'role="img" font-family="{FONT}">\n<title>{escape(title)}</title>\n'
                f'<rect width="100%" height="100%" fill="{self.t["bg"]}"/>\n{body}\n</svg>\n')


def chip_width(label, bold=False):
    return text_width(label, FS, bold) + 2 * CHIP_PAD


def flow(labels_must, x0, x1):
    """Lay chips left-to-right, wrapping at x1. Returns [(x, dy, label, must)], height."""
    placed, x, dy = [], x0, 0
    for label, must in labels_must:
        w = chip_width(label)
        if x > x0 and x + w > x1:
            x, dy = x0, dy + CHIP_H + GAP
        placed.append((x, dy, label, must))
        x += w + GAP
    return placed, (dy + CHIP_H if placed else 0)


# ------------------------------------------- Option A: GitHub timeline -----

A_SPINE, A_CARD_X, A_HEAD_COL, A_INDENT = 34, 62, 210, 18


def a_rows(svg, node, depth, x_card, w_card, y, draw):
    """Head chip in the left column, its leaves flowing to the right; sub-branches below."""
    head_x = x_card + 14 + depth * A_INDENT
    leaves_x0, leaves_x1 = x_card + 14 + A_HEAD_COL, x_card + w_card - 14
    placed, h = flow([(c.label, c.must) for c in node.leaves], leaves_x0, leaves_x1)
    if draw:
        svg.chip(head_x, y, node.label, node.must, bold=True)
        for x, dy, label, must in placed:
            svg.chip(x, y + dy, label, must)
    assert head_x + chip_width(node.label, True) < leaves_x0 - 4, node.label
    y_end = y + max(h, CHIP_H)
    for sub in node.branches:
        y_sub = y_end + GAP + 4
        if draw:
            elbow_x = head_x + 12
            svg.path(f"M{elbow_x:.1f} {y + CHIP_H:.1f} V{y_sub + CHIP_H / 2 - 6:.1f} Q{elbow_x:.1f} {y_sub + CHIP_H / 2:.1f} "
                     f"{elbow_x + 6:.1f} {y_sub + CHIP_H / 2:.1f} H{head_x + A_INDENT:.1f}", svg.t["spine"])
        y_end = a_rows(svg, sub, depth + 1, x_card, w_card, y_sub, draw)
    return y_end


def build_github(meta, steps, theme):
    svg = Svg(THEMES[theme])
    t = svg.t
    y = svg.header(meta) + 28
    spine_top = y + 17
    w_card = WIDTH - A_CARD_X - 20
    for step in steps:
        svg.step(A_SPINE - 17, y, step.label)
        y += 34 + 14
        groups = [step.leaves] if step.leaves else []
        groups += [[b] for b in step.branches]
        for group in groups:
            if len(group) == 1 and group[0].children:
                inner = a_rows(svg, group[0], 0, A_CARD_X, w_card, 0, False)
                svg.card(A_CARD_X, y, w_card, inner + 28)
                a_rows(svg, group[0], 0, A_CARD_X, w_card, y + 14, True)
            else:  # topics attached straight to the step: chips without a head
                placed, inner = flow([(c.label, c.must) for c in group], A_CARD_X + 14, A_CARD_X + w_card - 14)
                svg.card(A_CARD_X, y, w_card, inner + 28)
                for x, dy, label, must in placed:
                    svg.chip(x, y + 14 + dy, label, must)
            svg.line(A_SPINE, y + 14 + CHIP_H / 2, A_CARD_X, y + 14 + CHIP_H / 2, t["spine"])
            y += inner + 28 + 10
        y += 22
    # spine drawn under everything: insert at the front
    svg.out.insert(0, f'<line x1="{A_SPINE}" y1="{spine_top}" x2="{A_SPINE}" y2="{y + 6}" stroke="{t["spine"]}" stroke-width="2"/>')
    svg.add(f'<path d="M{A_SPINE - 6} {y - 3} L{A_SPINE} {y + 6} L{A_SPINE + 6} {y - 3}" fill="none" stroke="{t["spine"]}" stroke-width="2"/>')
    bottom = bubble_right(svg, A_SPINE, y + 6, meta["footer"])
    return svg.render(bottom + 24, meta["title"])


def bubble_right(svg, x_tip, y_tip, label):
    """Speech bubble to the right of the spine end, tail pointing back at the arrow."""
    t = svg.t
    size, h = 15, 40
    w = text_width(label, size) + 40
    bx, by = x_tip + 22, y_tip - h / 2
    cy = by + h / 2
    svg.add(f'<path d="M{bx + 10:.1f} {by:.1f} H{bx + w - 10:.1f} Q{bx + w:.1f} {by:.1f} {bx + w:.1f} {by + 10:.1f} V{by + h - 10:.1f} '
            f'Q{bx + w:.1f} {by + h:.1f} {bx + w - 10:.1f} {by + h:.1f} H{bx + 10:.1f} Q{bx:.1f} {by + h:.1f} {bx:.1f} {by + h - 10:.1f} '
            f'V{cy + 7:.1f} L{bx - 10:.1f} {cy:.1f} L{bx:.1f} {cy - 7:.1f} V{by + 10:.1f} Q{bx:.1f} {by:.1f} {bx + 10:.1f} {by:.1f} Z" '
            f'fill="{t["bubble_fill"]}" stroke="{t["bubble_stroke"]}" stroke-width="1"/>')
    svg.text(bx + w / 2, cy + size * 0.35, label, size, t["bubble_text"])
    return by + h


# ----------------------------------------- Option B: teal two-sided spine --

B_COL_W, B_PAD, B_STEP_IN = 398, 12, 20


def b_tree(svg, node, x, x1, y, draw, headless=False):
    """Outline tree inside a card: head, then leaves and sub-branches hanging off a guide line."""
    if not headless:
        if draw:
            svg.chip(x, y, node.label, node.must, bold=True)
        y_head_bottom = y + CHIP_H
        y += CHIP_H + GAP
        cx = x + B_STEP_IN
    else:
        cx = x
    ticks = []
    placed, h = flow([(c.label, c.must) for c in node.leaves], cx, x1)
    if placed:
        if draw:
            for px, dy, label, must in placed:
                svg.chip(px, y + dy, label, must)
        ticks.append(y + CHIP_H / 2)
        y += h + GAP
    for sub in node.branches:
        ticks.append(y + CHIP_H / 2)
        y = b_tree(svg, sub, cx, x1, y, draw) + GAP
    if draw and not headless:
        gx = x + 9
        svg.line(gx, y_head_bottom, gx, ticks[-1] - 6, svg.t["spine"])
        for ty in ticks:
            svg.path(f"M{gx:.1f} {ty - 6:.1f} Q{gx:.1f} {ty:.1f} {gx + 6:.1f} {ty:.1f} H{cx - 2:.1f}", svg.t["spine"])
    return y - GAP


def build_teal(meta, steps):
    svg = Svg(THEMES["teal"])
    t = svg.t
    mid = WIDTH / 2
    y = svg.header(meta) + 26
    spine_top = y
    left_x, right_x = 20, WIDTH - 20 - B_COL_W
    for step in steps:
        svg.step(mid, y, step.label, anchor="middle")
        y += 34 + 16
        cols = [y, y]
        groups = ([(step, True)] if step.leaves else []) + [(b, False) for b in step.branches]
        for node, headless in groups:
            side = 0 if cols[0] <= cols[1] else 1
            cx = left_x if side == 0 else right_x
            inner = b_tree(svg, node, cx + B_PAD, cx + B_COL_W - B_PAD, 0, False, headless) if not headless else \
                flow([(c.label, c.must) for c in node.leaves], cx + B_PAD, cx + B_COL_W - B_PAD)[1]
            cy = cols[side]
            svg.card(cx, cy, B_COL_W, inner + 2 * B_PAD)
            if headless:
                placed, _ = flow([(c.label, c.must) for c in node.leaves], cx + B_PAD, cx + B_COL_W - B_PAD)
                for px, dy, label, must in placed:
                    svg.chip(px, cy + B_PAD + dy, label, must)
            else:
                b_tree(svg, node, cx + B_PAD, cx + B_COL_W - B_PAD, cy + B_PAD, True)
            ty = cy + B_PAD + CHIP_H / 2
            edge = cx + B_COL_W if side == 0 else cx
            svg.line(edge, ty, mid, ty, t["spine"])
            svg.add(f'<circle cx="{mid}" cy="{ty:.1f}" r="3.5" fill="{t["spine"]}"/>')
            cols[side] = cy + inner + 2 * B_PAD + 12
        y = max(cols) + 18
    svg.out.insert(0, f'<line x1="{mid}" y1="{spine_top}" x2="{mid}" y2="{y + 10}" stroke="{t["spine"]}" stroke-width="2"/>')
    bottom = svg.footer(mid, y + 10, meta["footer"])
    return svg.render(bottom + 28, meta["title"])


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "roadmap.txt")
    meta, steps = parse(src)
    outputs = {
        "roadmap-github-dark.svg": build_github(meta, steps, "github-dark"),
        "roadmap-github-light.svg": build_github(meta, steps, "github-light"),
        "roadmap-teal.svg": build_teal(meta, steps),
    }
    for name, data in outputs.items():
        with open(os.path.join(HERE, name), "w", encoding="utf-8") as f:
            f.write(data)
        print("wrote", name)


if __name__ == "__main__":
    main()
