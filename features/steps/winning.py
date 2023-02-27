from behave import then
from screenpy import Actor
from screenpy.actions import See
from screenpy.resolutions import IsEqualTo

from screenplay.questions import GameHasEnded, ResultOfTheGame


@then(u'the game ends')
def the_game_ends(context):
    the_actor: Actor = context.actor
    the_actor.should(See.the(GameHasEnded, IsEqualTo(True)))


@then(u'the result is "{result}"')
def the_result_is(context, result):
    the_actor: Actor = context.actor
    the_actor.should(See.the(ResultOfTheGame, IsEqualTo(result)))
