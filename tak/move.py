from enum import Enum

from .board import Board
from .player import PlayerInfo
from .stone import Stone, StoneType
from .square import Square
from .direction import Direction


class MoveType(Enum):
    Place = "Place"
    Move = "Move"


class Move:
    def __init__(self, action: MoveType, position: str, stoneType: StoneType = None, amount: int = None, direction: Direction = None, drops: list = None):
        self.action = action
        self.position = position
        self.stoneType = stoneType
        self.amount = amount
        self.direction = direction
        self.drops = drops

    def execute(self, board: Board, player: PlayerInfo):
        if (self.action == MoveType.Place):
            stone = player.get_stone(self.stoneType)
            if (isinstance(stone, Stone)):
                square = board.get_square(self.position)
                if (len(square.stones) > 0):
                    raise Exception(
                        "Cannot place a stone on a non empty board")
                else:
                    square.drop(stone)
            else:
                raise Exception("Player has not enough stones")
        else:
            square: Square = board.get_square(self.position)
            stones = square.take(self.amount)
            for index, drop in enumerate(self.drops):
                dropSquare: Square = board.get_neighbour_square(
                    position=self.position, direction=self.direction, length=index + 1)
                if dropSquare == None:
                    raise Exception("Cannot move out of the board")
                # no check needed for undefined because otherwithe the square.take method throws an error
                dropStones = stones[:drop]
                stones = stones[drop:]
                if (dropSquare.can_drop_stones(*dropStones)):
                    dropSquare.drop(*dropStones)
                else:
                    raise Exception(f"Cannot drop stones on {self.position}")
