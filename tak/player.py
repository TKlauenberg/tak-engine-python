from enum import Enum

from .stone import PlayerNumber, Stone, StoneType


class StoneBag:
    def __init__(self, stones: dict = None, flatStones=None, capstones=None):
        if dict == None:
            self.flatStones = flatStones
            self.capstones = capstones
        else:
            self.flatStones = stones.get("F")
            self.capstones = stones.get("C")


class PlayerInfo:
    def __init__(self, name: str, player: PlayerNumber, gameStones):
        self.name = name
        self.player = player
        if isinstance(gameStones, StoneBag):
            self.stoneBag = gameStones
        else:
            self.stoneBag = StoneBag(gameStones)

    def get_total_stones(self) -> int:
        return self.stoneBag.flatStones + self.stoneBag.capstones

    def get_stone(self, type: StoneType):
        if type == StoneType.CAP:
            if self.stoneBag.capstones <= 0:
                return None
            else:
                self.stoneBag.capstones -= 1
                return Stone(type=StoneType.CAP, player=self.player)
        else:
            if self.stoneBag.flatStones <= 0:
                return None
            else:
                self.stoneBag.flatStones -= 1
                return Stone(type=type, player=self.player)
