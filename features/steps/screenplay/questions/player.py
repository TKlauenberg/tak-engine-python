from typing import Union

from screenpy import Actor
from screenpy.protocols import Answerable

import tak
from tak.stone import PlayerNumber

from features.steps.screenplay.abilities import PlayTheGame


class PlayerInfoFromNumber(Answerable):
    """Get the player with the specific number"""

    def __init__(self, player_number) -> None:
        self.number = player_number

    def describe(self):
        """Describe the Question."""
        return f"player number"

    def answered_by(self, the_actor: Actor) -> tak.PlayerInfo:
        """get the player info"""
        return the_actor.uses_ability_to(PlayTheGame).get_playerinfo(self.number)


class PlayerNumberOfStone(Answerable):
    """Get the player of the stone"""

    def __init__(self, stone: Union[Answerable, tak.Stone]) -> None:
        self.stone = stone

    def answered_by(self, the_actor: Actor) -> PlayerNumber:
        # check if type of stone is Answerable or tak.Stone
        # check is performed like in the screenpy lib
        if hasattr(self.stone, 'answered_by'):
            self.stone = self.stone.answered_by(the_actor)
        return self.stone.player
