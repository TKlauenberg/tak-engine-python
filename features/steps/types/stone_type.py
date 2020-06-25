import re

import parse
from behave import register_type

from tak.stone import StoneType, parse_stone_type


@parse.with_pattern(r"[FSC]")
def parse_stone_by_char(text):
    stoneType = parse_stone_type(text)
    return stoneType


register_type(StoneTypeByChar=parse_stone_by_char)


@parse.with_pattern(r"(flat stone)|(capstone)|(standing stone)")
def parse_stone_by_name(text):
    match = re.match(r"(flat stone)|(capstone)|(standing stone)", text)
    (flatStone, capStone, standingStone) = match.group(1, 2, 3)
    if flatStone is not None:
        return StoneType.FLAT
    if capStone is not None:
        return StoneType.CAP
    if standingStone is not None:
        return StoneType.STANDING


register_type(StoneTypeByName=parse_stone_by_name)
