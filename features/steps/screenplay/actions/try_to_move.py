from types import SimpleNamespace
from typing import Callable, Iterable, Protocol

from screenpy import Actor
from tak import Direction, Move, MoveType

from features.steps.screenplay.abilities import PlayTheGame
from .move import From, Moving


class TryMoveStones:
    """Interaction for placing stones"""

    def __init__(self, amount: int, position: str, direction: Direction, drops: Iterable[int]) -> None:

        self.move = Move(action=MoveType.Move, position=position,
                         amount=amount, direction=direction, drops=drops)

    def perform_as(self, the_actor: Actor) -> None:
        """perform action"""
        play_the_game: PlayTheGame = the_actor.ability_to(PlayTheGame)
        play_the_game.try_execute(self.move)


def tries_to_move(amount: int) -> From:
    def _from(position: str) -> Moving:
        def moving(direction: Direction):
            def dropping_one_stone_on_each_square():
                drops = [1 for x in range(0, amount)]
                return TryMoveStones(amount=amount, position=position, direction=direction, drops=drops)

            def moving_the_complete_stack():
                return TryMoveStones(amount=amount, position=position, direction=direction, drops=[amount])
            return SimpleNamespace({
                "dropping_one_stone_on_each_square": dropping_one_stone_on_each_square,
                "moving_the_complete_stack": moving_the_complete_stack
            })
        return SimpleNamespace({"moving": moving})
    return SimpleNamespace({"from": _from})
