import re

import parse
from behave import register_type

from features.steps.types import parse_player_color
from tak import Stone, StoneType


@parse.with_pattern(r"(?:(?:(?:flat)|(?:standing)) (?:(?:black)|(?:white)) stone)|(?:(?:(?:black)|(?:white)) capstone)")
def parse_stone(text):
    match = re.match(
        r"(((?:flat)|(?:standing)) ((?:black)|(?:white)) stone)|(((?:black)|(?:white)) capstone)", text)
    (isNoCapstone, standingOrFlat, flatOrStandingColor,
     capstoneColor) = match.group(1, 2, 3, 5)
    if isNoCapstone is not None:
        player = parse_player_color(flatOrStandingColor)
        if standingOrFlat == "standing":
            stoneType = StoneType.STANDING
        else:
            stoneType = StoneType.FLAT
    else:
        player = parse_player_color(capstoneColor)
        stoneType = StoneType.CAP
    return Stone(type=stoneType, player=player)


register_type(Stone=parse_stone)
