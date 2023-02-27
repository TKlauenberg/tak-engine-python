from typing import Callable

from screenpy import Actor
from screenpy.pacing import beat
from screenpy.protocols import Performable


class Interaction(Performable):
    """dynamically created Interaction so that there is no class created every time"""

    @classmethod
    def where(cls, description, action):
        return Interaction(description, action)

    def __init__(self, description: str, action: Callable[[Actor], None]) -> None:
        self.description = description
        self.action = action

    def perform_as(self, the_actor: Actor) -> None:
        """perform the interaction"""
        # the screenpy decorator expects a self argument so a change of the Function is needed
        # the argument is not used but is simply there so that the decorator get's
        # the reference of the actor and passes it correctly to the action
        @beat(self.description)
        def action(_, actor: Actor):
            return self.action(actor)
        action(self, the_actor)
