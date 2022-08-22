import re

import parse
from behave import register_type

from tak import Direction


@parse.with_pattern(r"((?:up)|(?:\+)|(?:↑))|((?:down)|(?:-)|(?:↓))|((?:right)|(?:>)|(?:→))|((?:left)|(?:<)|(?:←))")
def parse_direction(text):
    match = re.match(
        r"((?:up)|(?:\+)|(?:↑))|((?:down)|(?:-)|(?:↓))|((?:right)|(?:>)|(?:→))|((?:left)|(?:<)|(?:←))", text)
    (up, down, right, left) = match.group(1, 2, 3, 4)
    if up:
        return Direction.Up
    if down:
        return Direction.Down
    if right:
        return Direction.Right
    if left:
        return Direction.Left


register_type(Direction=parse_direction)
