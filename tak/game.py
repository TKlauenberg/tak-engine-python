from .board import Board, get_stone_count
from .move import Move
from .player import PlayerInfo
from .stone import PlayerNumber
from .tps import TPS


class Game:
    def __init__(self, size, player1: str = None, player2: str = None, tps: str = None):
        if isinstance(size, str):
            size = int(size)
        stonebag = get_stone_count(size=size)
        if stonebag is None:
            raise Exception(f"Bord Size is not valid! Bord size is {size}")
        self.size = size
        self.player1 = PlayerInfo(
            player1 or "white", PlayerNumber.One, stonebag)
        self.player2 = PlayerInfo(
            player2 or "black", PlayerNumber.Two, stonebag)
        if not tps is None:
            (result, tps_or_error) = TPS.parse(boardSize=self.size, tps=tps, player1=self.player1, player2=self.player2)
            if result:
                self.board = Board(size=self.size, board=tps_or_error.board)
                self.moveCount = tps_or_error.move
                self.currentPlayer = tps_or_error.player
            else:
                raise Exception(tps_or_error)
        else:
            self.moveCount = 1
            self.board = Board(size)
            self.currentPlayer = self.player1

    def execute(self, move: Move):
        # first action is always a place of an enemy stone
        player = self.currentPlayer
        if self.moveCount == 1:
            player = self.player2 if self.currentPlayer == self.player1 else self.player1
        move.execute(self.board, player)
        if self.currentPlayer == self.player1:
            self.currentPlayer = self.player2
        else:
            self.currentPlayer = self.player1
            self.moveCount += 1
        return self
