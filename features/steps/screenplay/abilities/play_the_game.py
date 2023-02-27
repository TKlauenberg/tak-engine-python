from tak import Game, Move, PlayerNumber, parse


class PlayTheGame:
    """screenplay ability to create a Tak Game"""

    def __init__(self) -> None:
        self.game: Game = None
        self.result = None
        self.error = None

    def from_options(self, size, **gameOptions):
        self.game = Game(size, **gameOptions)
        return self

    def from_ptn(self, ptn: str):
        (self.result, game_or_error) = parse(ptn)
        if self.result:
            self.game = game_or_error
        else:
            self.error = game_or_error

    def get_result(self):
        return self.result

    # def get_tps(self):
    #     if self.game is None:
    #         raise AssertionError("Game is not initialized")
    #     self.game.
    def execute(self, move: Move):
        if self.game is None:
            raise AssertionError("Game is not initialized")
        self.game.execute(move=move)
        return self

    def try_execute(self, move: Move):
        if self.game is None:
            raise AssertionError("Game is not initialized")
        try:
            self.game.execute(move=move)
        except BaseException as err:
            self.error = err
        return self

    def get_square_on_position(self, pos: str):
        if self.game is None:
            raise AssertionError("Game is not initialized")
        return self.game.board.get_square(position=pos)

    def get_stack_on_position(self, pos: str):
        square = self.get_square_on_position(pos)
        return square.stones

    def next_player(self):
        if self.game is None:
            raise AssertionError("Game is not initialized")
        return self.game.currentPlayer.player

    def current_round(self):
        if self.game is None:
            raise AssertionError("Game is not initialized")
        return self.game.moveCount

    def get_size(self):
        if self.game is None:
            raise AssertionError("Game is not initialized")
        return self.game.size

    def get_board(self):
        if self.game is None:
            raise AssertionError("Game is not initialized")
        return self.game.board

    def get_playerinfo(self, player: PlayerNumber):
        if self.game is None:
            raise AssertionError("Game is not initialized")
        if player is PlayerNumber.One:
            return self.game.player1
        else:
            return self.game.player2

    def has_ended(self):
        if self.game is None:
            raise AssertionError("Game is not initialized")
        return self.game.has_ended()
