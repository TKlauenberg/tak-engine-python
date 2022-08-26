from tabnanny import check
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
        self.result = None
        if not tps is None:
            (result, tps_or_error) = TPS.parse(boardSize=self.size,
                                               tps=tps, player1=self.player1, player2=self.player2)
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

    def has_ended(self):
        if self.result is None:
            roads = self.board.get_roads()
            if len(roads) > 0:
                if len(roads) == 1:
                    winningPlayer = roads[0][0].top().player
                else:
                    couldPlayerOneWin = any(
                        [road[0].top().player == PlayerNumber.One for road in roads])
                    couldPlayerTwoWin = any(
                        [road[0].top().player == PlayerNumber.Two for road in roads])
                    if couldPlayerOneWin and couldPlayerTwoWin:
                        winningPlayer = self.currentPlayer
                    elif couldPlayerOneWin:
                        winningPlayer = PlayerNumber.One
                    else:
                        winningPlayer = PlayerNumber.Two
                self.result = 'R-0' if winningPlayer == PlayerNumber.One else '0-R'
                return True
            if self.board.is_full() or self.player1.get_total_stones()==0 or self.player2.get_total_stones()==0:
                (scorePlayer1, scorePlayer2) = self.board.get_score()
                if scorePlayer1==scorePlayer2:
                    self.result = '1/2-1/2'
                elif scorePlayer1>scorePlayer2:
                    self.result = 'F-0'
                else:
                    self.result = '0-F'
                return True
            return False
        else:
            return True
