from screenpy import Actor

from features.steps.screenplay.abilities import PlayTheGame


class GameError:
    """Get Current Error in Game"""

    def describe():
        """Describe the Question."""
        return "error of the game"

    def answered_by(the_actor: Actor):
        """get the game error"""
        return str(the_actor.uses_ability_to(PlayTheGame).error)
