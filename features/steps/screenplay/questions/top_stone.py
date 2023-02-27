from screenpy import Actor
from screenpy.protocols import Answerable

import tak
from features.steps.screenplay.abilities import PlayTheGame


def get_top_stone(the_actor: Actor, pos: str) -> tak.Stone:
    return the_actor.uses_ability_to(PlayTheGame).get_square_on_position(pos).top()


class PlayerOfTopStoneOn(Answerable):
    """Get the player with the specific number"""

    def __init__(self, pos: str) -> None:
        self.pos = pos

    def describe(self):
        """Describe the Question."""
        return "get player of the top stone"

    def answered_by(self, the_actor: Actor) -> tak.PlayerInfo:
        """get player of the top stone"""
        return get_top_stone(the_actor, self.pos).player


class TypeOfTopStoneOn(Answerable):
    """Get the player with the specific number"""

    def __init__(self, pos: str) -> None:
        self.pos = pos

    def describe(self):
        """Describe the Question."""
        return "get type of the top stone"

    def answered_by(self, the_actor: Actor) -> tak.PlayerInfo:
        """get type of the top stone"""
        return get_top_stone(the_actor, self.pos).type
