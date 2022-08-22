from enum import Enum

from .board import Board
from .player import PlayerInfo
from .stone import Stone, StoneType
from .square import Square
from .direction import Direction
from .grammar import grammar


class MoveType(Enum):
    Place = "Place"
    Move = "Move"


def parse_direction(direction: str):
    if direction == '+':
        return Direction.Up
    if direction == '-':
        return Direction.Down
    if direction == '<':
        return Direction.Left
    if direction == '>':
        return Direction.Right
    raise Exception(f'cannot parse Direction "{direction}"')


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

    @staticmethod
    def parse(ptnMove: str):
        moveType = grammar['plyGrouped'].match(ptnMove)
        # MoveType = Move
        if moveType[2]:
            action = MoveType.Move
            parts = grammar['slideGrouped'].match(moveType[2])
            amount = 1 if parts[1] == '' else int(parts[1])
            position = parts[2]
            direction = parse_direction(parts[2])
            drops = [amount] if parts[4] == '' else[int(x) for x in parts[4]]
            move = Move(action=action, position=position,
                        direction=direction, drops=drops)
            return (True, move)
        # MoveType = Place
        if moveType[3]:
            action = MoveType.Place
            parts = grammar['placeGrouped'].match(moveType[3])
            stoneType = parts[1] if parts[1] else StoneType.FLAT
            position = parts[2]
            move = Move(action=action, position=position, stoneType=stoneType)
            return (True, move)
        return (False, f'move could not be parsed! move: {ptnMove}')
