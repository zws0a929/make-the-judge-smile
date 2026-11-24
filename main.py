#!/usr/bin/env python3
"""One line meant to make a judge smile.

The line works because it stacks small surprises: a peach that is still
warm from the sun, a gift passed through a fence rather than over it, and
a dull grey Tuesday that suddenly tastes like August. Nothing grand
happens — a neighbor simply shares what the tree overproduced — and that
quiet generosity is what makes the moment land.
"""

# The line in three movements: the scene, the gift, and the turn.
scene = "At lunch my neighbor slipped a still-warm peach through the fence, "
gift = "saying the tree made too many — "
turn = "and for a second the whole grey Tuesday tasted like August."


def build_line():
    """Stitch the three movements into the single entry line."""
    return scene + gift + turn


def main():
    print(build_line())


if __name__ == "__main__":
    main()
