from screenpy import Actor
from tak import Game

from features.steps.screenplay.abilities import PlayTheGame


class CreateAGame(object):
    @staticmethod
    def with_options(size, **options) -> "CreateAGameWithOptions":
        return CreateAGameWithOptions(size=size, options=options)
    @staticmethod
    def with_ptn(ptn: str):
        return CreateAGameWithPtn(ptn=ptn)


class CreateAGameWithOptions:
    def __init__(self, size, **options):
        super().__init__()
        self.options = options
        self.size = size
    def perform_as(self, the_actor: Actor) -> None:
        playTheGame: PlayTheGame = the_actor.ability_to(PlayTheGame)
        playTheGame.from_options(self.size, **self.options)


class CreateAGameWithPtn:
    def __init__(self, ptn: str):
        super().__init__()
        self.ptn = ptn

    def perform_as(self, the_actor: Actor) -> None:
        playTheGame: PlayTheGame = the_actor.ability_to(PlayTheGame)
        playTheGame.from_ptn(ptn=self.ptn)
