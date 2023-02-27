from screenpy import Actor
from screenpy.protocols import Answerable

import tak
from features.steps.screenplay.abilities import PlayTheGame


class PlayerInfoFromNumber(Answerable):
    """Get the next player"""

    def __init__(self, player_number) -> None:
        self.number = player_number

    def describe():
        """Describe the Question."""
        return "next player"

    def answered_by(self, the_actor: Actor) -> tak.PlayerInfo:
        """get the next player"""
        return the_actor.uses_ability_to(PlayTheGame).next_player()
