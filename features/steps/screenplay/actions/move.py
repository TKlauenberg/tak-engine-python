from types import SimpleNamespace
from typing import Callable, Iterable, Protocol

from screenpy import Actor
from tak import Direction, Move, MoveType

from features.steps.screenplay.abilities import PlayTheGame


class MoveStones:
    """Interaction for placing stones"""

    def __init__(self, amount: int, position: str, direction: Direction, drops: Iterable[int]) -> None:

        self.move = Move(action=MoveType.Move, position=position,
                         amount=amount, direction=direction, drops=drops)

    def perform_as(self, the_actor: Actor) -> None:
        """perform action"""
        play_the_game: PlayTheGame = the_actor.ability_to(PlayTheGame)
        play_the_game.execute(self.move)

class MovingResult(Protocol):
    def dropping_one_stone_on_each_square(self) -> MoveStones:
        pass
    def moving_the_complete_stack(self) -> MoveStones:
        pass


class Moving(Protocol):
    def moving(self, direction: Direction)->MovingResult:
        pass


class From(Protocol):
    def from_(self, position: str) -> Moving:
        pass

def move(amount: int) -> From:
    def _from(position: str) -> Moving:
        def moving(direction: Direction)->MovingResult:
            def dropping_one_stone_on_each_square():
                drops = [1 for x in range(0, amount)]
                return MoveStones(amount=amount, position=position, direction=direction, drops=drops)

            def moving_the_complete_stack():
                return MoveStones(amount=amount, position=position, direction=direction, drops=[amount])
            return SimpleNamespace({
                "dropping_one_stone_on_each_square": dropping_one_stone_on_each_square,
                "moving_the_complete_stack": moving_the_complete_stack
            })
        return SimpleNamespace({"moving": moving})
    return SimpleNamespace({"from_": _from})
