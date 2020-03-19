import re

import parse
from behave import register_type

from tak import PlayerNumber


@parse.with_pattern(r"(black)|(white)")
def parse_player_color(text):
    if text == "white":
        return PlayerNumber.One
    else:
        return PlayerNumber.Two


register_type(PlayerColor=parse_player_color)