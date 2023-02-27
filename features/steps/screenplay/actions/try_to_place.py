from types import SimpleNamespace

from screenpy import Actor
from tak import Move, MoveType, StoneType

from features.steps.screenplay.abilities import PlayTheGame
from .place import On


class TriesToPlace:
    """Interaction for placing stones"""

    @classmethod
    def a(cls, stone_type: StoneType)->On:
        def on(position: str):
            return TriesToPlace(stone_type=stone_type, position=position)
        return SimpleNamespace({"on": on})

    def __init__(self, stone_type: StoneType, position: str):
        super().__init__()
        self.stone_type = stone_type
        self.position = position

    def perform_as(self, the_actor: Actor) -> None:
        """perform action"""
        play_the_game: PlayTheGame = the_actor.ability_to(PlayTheGame)
        move = Move(action=MoveType.Place, position=self.position,
                    stoneType=self.stone_type)
        play_the_game.try_execute(move)
