from screenpy import Actor
from screenpy.protocols import Answerable

from features.steps.screenplay.abilities import PlayTheGame
from tak import PlayerNumber


class GameHasEnded(Answerable):
    """Get the information if the game has ended"""

    def describe(self):
        """Describe the Question."""
        return "if the game has ended"

    def answered_by(self, the_actor: Actor) -> bool:
        """get the current ended status"""
        return the_actor.uses_ability_to(PlayTheGame).game.has_ended()


class ResultOfTheGame(Answerable):
    """Get the result of the current game"""

    def describe(self):
        """Describe the Question."""
        return "result of the current game"

    def answered_by(self, the_actor: Actor) -> bool:
        """get the result of the current game"""
        return the_actor.uses_ability_to(PlayTheGame).game.result


class RoundOfTheGame(Answerable):
    """Get the current round of the game"""

    def describe(self):
        """Describe the Question."""
        return "current round of the game"

    def answered_by(self, the_actor: Actor) -> int:
        """get the current round"""
        return the_actor.uses_ability_to(PlayTheGame).current_round()


class NextPlayer(Answerable):
    """Get the next player in the game"""

    def describe(self):
        """Describe the Question."""
        return "the next player of the game"

    def answered_by(self, the_actor: Actor) -> PlayerNumber:
        return the_actor.uses_ability_to(PlayTheGame).next_player()
