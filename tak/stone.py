from enum import Enum


class PlayerNumber(Enum):
    One = 1
    Two = 2


class StoneType(Enum):
    FLAT = "F"
    STANDING = "S"
    CAP = "C"


def parse_stone_type(stoneType):
    switcher = {
        "F": StoneType.FLAT,
        "S": StoneType.STANDING,
        "C": StoneType.CAP,
    }
    return switcher.get(stoneType, f"Cannot parse Stone {stoneType}. Possible StoneTypes are \"F, S and C\"")


class Stone:
    def __init__(self, type: StoneType, player: PlayerNumber):
        self.type = type
        self.player = player

    def __eq__(self, value):
        return (not value == None) and self.type == value.type and self.player == value.player
