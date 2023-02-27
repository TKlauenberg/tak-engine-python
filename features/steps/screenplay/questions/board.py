from screenpy import Actor
from tak import Board

from features.steps.screenplay.abilities import PlayTheGame


class BoardOfTheGame:
    """Get the board of the game"""

    def describe():
        """Describe the Question."""
        return "board of the game"

    def answered_by(self, the_actor:Actor) -> Board:
        """get the current board"""
        return the_actor.uses_ability_to(PlayTheGame).game.board

class BoardIsEmpty:
    """Question if the board is empty"""

    def describe():
        """Describe the Question."""
        return 'is the board empty'

    def answered_by(self, the_actor: Actor)->bool:
        board: Board = BoardOfTheGame().answered_by(the_actor)
        return all([square.is_empty() for row in board for square in row])

class SizeOfTheBoard:
    """Question of the size of the board"""

    def describe():
        """Describe the Question."""
        return 'the size of the board'

    def answered_by(self, the_actor: Actor)->int:
        return the_actor.uses_ability_to(PlayTheGame).get_size()
