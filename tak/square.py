from enum import Enum

from tak.stone import StoneType


class Edge(Enum):
    Top = 1
    Bottom = 2
    Left = 4
    Right = 8


class Square:
    def __init__(self, position:str=None, *stones):
        self.position = position
        self.stones = stones

    def top(self):
        return self.stones[-1]

    def is_empty(self):
        return len(self.stones) == 0

    def has_stones(self):
        return len(self.stones) > 0

    def can_drop_stones(self, *stones):
        """
        Test if stones can be dropped on square


        stones -- stones which are tested
        """
        if self.is_empty():
            return (True, "")
        else:
            top = self.top()
            stoneType = top.type
            if stoneType == StoneType.FLAT:
                return (True, "")
            if stoneType == StoneType.STANDING:
                if len(stones) == 1:
                    if stones[0].type == StoneType.CAP:
                        return (True, "")
                    else:
                        return (False, "Can only flatten a wall with a capstone")
                else:
                    return (False, "Can only flatten a wall with one capstone")
            if stoneType == StoneType.CAP:
                return (False, "Cannot move a stone onto a capstone")
            return (False, "Top tile is not a stone")

    def drop(self, *stones):
        """
        Drop new stones on tile

        stones -- stones to be dropped
        return -- Stone[] new Tile stones
        """
        (canDrop, reason) = self.can_drop_stones(*stones)
        if canDrop:
            if not self.is_empty() and self.top().type == StoneType.STANDING:
                # flattening wall
                self.top().type = StoneType.FLAT
            self.stones = [*self.stones, *stones]
        else:
            raise Exception(reason)

    def take(self, count):
        """
        take stones from square

        count -- amount of stones to take
        """
        if count > len(self.stones):
            raise Exception(
                f"There {'are' if len(self.stones)>1 else 'is'} {len(self.stones)} stone{'s' if len(self.stones)>1 else ''} on this square. Cannot move {count} stones")
        else:
            takeStones = self.stones[-count:]
            self.stones = self.stones[: -count]
            return takeStones

    def __eq__(self, value):
        return (not value == None) and len(self.stones) == len(value.stones)and all([a == b for (a, b) in zip(self.stones, value.stones)])
