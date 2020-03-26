from .board import Board, get_stone_count
from .move import Move
from .player import PlayerInfo
from .stone import PlayerNumber


class Game:
    def __init__(self, size, player1: str = None, player2: str = None, tps: str = None):
        if isinstance(size, str):
            size = int(size)
        stonebag = get_stone_count(size=size)
        if stonebag is None:
            raise Exception(f"Bord Size is not valid! Bord size is {size}")
        self.size = size
        pplayer1layer1Name = player1 or "white"
        self.player1 = PlayerInfo(
            pplayer1layer1Name, PlayerNumber.One, stonebag)
        pplayer2layer2Name = player2 or "black"
        self.player2 = PlayerInfo(player2, PlayerNumber.Two, stonebag)
        self.moveCount = 1
        self.hasEnded = False
        self.board = Board(size)
        self.currentPlayer = self.player1

    def execute(self, move: Move):
        # first action is always a place of an enemy stone
        player = self.currentPlayer
        if (self.moveCount == 1):
            player = self.player2 if self.currentPlayer == self.player1 else self.player1
        move.execute(self.board, player)
        if (not self.hasEnded):
            if (self.currentPlayer == self.player1):
                self.currentPlayer = self.player2
            else:
                self.currentPlayer = self.player1
                self.moveCount += 1
        return self
