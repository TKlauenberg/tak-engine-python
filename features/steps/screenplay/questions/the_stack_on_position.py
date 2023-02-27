from screenpy import Actor
from screenpy.protocols import Answerable

import tak
from features.steps.screenplay.abilities import PlayTheGame


class TheStackOnPosition(Answerable):
    """Get the player with the specific number"""

    def __init__(self, pos: str) -> None:
        self.pos = pos

    def describe(self):
        """Describe the Question."""
        return f"stack on specific position"

    def answered_by(self, the_actor: Actor) -> tak.PlayerInfo:
        """get the stack"""
        return the_actor.uses_ability_to(PlayTheGame).get_stack_on_position(self.pos)
