from screenpy import Actor

from features.steps.screenplay.abilities import PlayTheGame


class GameHasEnded:
    """Get the information if the game has ended"""

    def describe():
        """Describe the Question."""
        return "if the game has ended"

    def answered_by(self, the_actor: Actor) -> bool:
        """get the current ended status"""
        return the_actor.uses_ability_to(PlayTheGame).game.has_ended()


class ResultOfTheGame:
    """Get the result of the current game"""

    def describe(self):
        """Describe the Question."""
        return "result of the current game"

    def answered_by(self, the_actor: Actor) -> bool:
        """get the result of the current game"""
        return the_actor.uses_ability_to(PlayTheGame).game.result
