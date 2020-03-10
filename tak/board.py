from tak.square import Square

stoneCounts = {
    3: {"F": 10, "C": 0, "total": 10},
    4: {"F": 15, "C": 0, "total": 15},
    5: {"F": 21, "C": 1, "total": 22},
    6: {"F": 30, "C": 1, "total": 31},
    8: {"F": 50, "C": 2, "total": 52},
}


def get_stone_count(size: int):
    return stoneCounts.get(size)


class Board:
    def __init__(self, size: int, board=None):
        self.size = size
        self.board = list([[Square() for x in range(size)]
                           for y in range(size)])

    def get_position(self, position: str):
        (a, b) = position
        column = ord(a)-ord("a")
        row = int(b)
        return (row, column)

    def get_square(self, position: str):
        (row, column) = self.get_position(position)
        return self.board[row][column]

    def __iter__(self):
        return self.board.__iter__()
