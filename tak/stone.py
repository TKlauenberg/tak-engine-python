from enum import Enum

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
