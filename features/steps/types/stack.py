import parse
from behave import register_type

from features.steps.types import parse_player_color
from tak import PlayerNumber, Stone, StoneType


def get_stone(player: str):
    if player == '1':
        return Stone(type=StoneType.FLAT, player=PlayerNumber.One)
    else:
        return Stone(type=StoneType.FLAT, player=PlayerNumber.Two)

@parse.with_pattern(r"[12]+")
def parse_stack(text: str):
    return [get_stone(player) for player in list(text)]


register_type(Stack=parse_stack)
