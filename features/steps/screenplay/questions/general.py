from screenpy import Actor

from features.steps.screenplay.abilities import PlayTheGame


class GameError:
    """Get Current Error in Game"""

    def describe(self):
        """Describe the Question."""
        return "error of the game"

    def answered_by(self, the_actor: Actor):
        """get the game error"""
        return str(the_actor.uses_ability_to(PlayTheGame).error)
