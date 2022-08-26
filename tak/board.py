from enum import Flag
from functools import reduce


from tak.stone import PlayerNumber, StoneType

from .direction import Direction
from .square import Square

stoneCounts = {
    3: {"F": 10, "C": 0, "total": 10},
    4: {"F": 15, "C": 0, "total": 15},
    5: {"F": 21, "C": 1, "total": 22},
    6: {"F": 30, "C": 1, "total": 31},
    8: {"F": 50, "C": 2, "total": 52},
}


class Edge(Flag):
    NoEdge = 0
    Top = 1
    Bottom = 2
    Left = 4
    Right = 8


topToBottom = Edge.Top | Edge.Bottom
leftToRight = Edge.Left | Edge.Right


def get_stone_count(size: int):
    return stoneCounts.get(size)


class Board:
    def __init__(self, size: int, board=None):
        self.size = size
        if board != None:
            self.board = board
        else:
            self.board = list([[Square(position=self.position_to_string(y, x)) for x in range(size)]
                               for y in range(size)])

    def get_position(self, position: str):
        (a, b) = position
        column = ord(a) - ord("a")
        row = int(b) - 1
        return (row, column)

    def position_to_string(self, row: int, column: int):
        return f"{chr(ord('a')+column)}{row+1}"

    def get_square(self, position: str):
        (row, column) = self.get_position(position)
        return self.board[row][column]

    def get_score(self):
        squares = reduce(lambda x, y: x+y, self.board)
        filtered = [square for square in squares if not square.is_empty(
        ) and square.top().type == StoneType.FLAT]
        player1Score = reduce(
            lambda x, y: x+y, [1 for square in filtered if square.top().player == PlayerNumber.One], 0)
        player2Score = reduce(
            lambda x, y: x+y, [1 for square in filtered if square.top().player == PlayerNumber.Two], 0)
        return (player1Score, player2Score)

    def get_neighbour_square(self, position: str, direction: Direction, length=1):
        (row, column) = self.get_position(position)
        if direction is Direction.Down:
            row -= length
        elif direction is Direction.Up:
            row += length
        elif direction is Direction.Left:
            column -= length
        elif direction is Direction.Right:
            column += length
        if self.size < row or row < 0 or self.size < column or column < 0:
            return None
        return self.board[row][column]

    def get_all_neighbour_squares(self, position: str):
        (row, column) = self.get_position(position=position)
        up = None if row >= self.size-1 else self.board[row+1][column]
        down = None if row <= 0 else self.board[row-1][column]
        left = None if column <= 0 else self.board[row][column-1]
        right = None if column >= self.size-1 else self.board[row][column+1]
        return [square for square in [up, down, left, right] if not square is None]

    def get_roads(self):
        bottom_squares = self.board[0]
        left_squares = [self.board[x][0] for x in range(1, (self.size))]
        valid_border_squares = [square for square in bottom_squares +
                                left_squares if not square.top() is None and square.top().type != StoneType.STANDING]
        roadsList = [self.find_roads_from_tile(
            square=square) for square in valid_border_squares]
        roads = reduce(lambda x, y: x+y, roadsList, [])
        return roads

    def find_roads_from_tile(self, square: Square, road: list[Square] = []):
        edges = self.get_edges(square.position)
        square.edges = edges
        newRoad = [square, *road]
        roadEdges = reduce(lambda x, y: x | y, [i.edges for i in newRoad], Edge.NoEdge)
        isTopToBottom = roadEdges & topToBottom == topToBottom
        isLeftToRight = roadEdges & leftToRight == leftToRight
        if isTopToBottom or isLeftToRight:
            return [road]
        else:
            neighbours = self.get_all_neighbour_squares(square.position)
            positions = [x.position for x in road]
            roadsList = [self.find_roads_from_tile(neighbour, newRoad) for neighbour in neighbours if not neighbour.top() is None and (neighbour.top(
            ).type == StoneType.FLAT or neighbour.top().type == StoneType.CAP) and neighbour.top().player == square.top().player and neighbour.position not in positions]
            roads = reduce(lambda x, y: x+y, roadsList, [])
            return roads

    def get_edges(self, position: str):
        (x, y) = self.get_position(position=position)
        edge = Edge.NoEdge
        if x == 0:
            edge |= Edge.Left
        elif x == (self.size-1):
            edge |= Edge.Right
        if y == 0:
            edge |= Edge.Bottom
        elif y == (self.size-1):
            edge |= Edge.Top
        return edge

    def is_full(self):
        return all([all([square.has_stones() for square in row]) for row in self.board])

    def __iter__(self):
        return self.board.__iter__()
