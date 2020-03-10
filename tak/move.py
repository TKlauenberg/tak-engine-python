from enum import Enum

from .board import Board
from .player import PlayerInfo
from .stone import Stone, StoneType


class MoveType(Enum):
    Place = "Place"
    Move = "Move"


class Direction(Enum):
    Up = "+"
    Down = "-"
    Left = "<"
    Right = ">"


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
                if (len(square.stones)>0):
                    raise "Cannot place a stone on a non empty board"
                else:
                    square.drop(stone)
            else:
                raise "Player has not enough stones"
        # else:
        #     square = board.get_square(self.position)
        #     square.take(self.amount)
        #     for index,drop in enumerate(self.drops):
        #         dropSquare = board.get_neighbour_square(board, self.position, self.direction, index + 1)
        #         if dropSquare==None:
        #             raise "Cannot move out of the board"
