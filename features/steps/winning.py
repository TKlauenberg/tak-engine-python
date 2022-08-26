from behave import then
from tak import Game


@then(u'the game ends')
def the_game_ends(context):
    game: Game = context.game
    assert game.has_ended(), 'Game should have ended!'


@then(u'the result is "{result}"')
def the_result_is(context, result):
    game: Game = context.game
    assert game.result == result
