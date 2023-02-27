from typing import TYPE_CHECKING
from behave import step, then

from features.steps.screenplay.questions.board import BoardIsEmpty
from screenpy import AnActor
from screenpy.actions import See
from screenpy.resolutions import IsEqualTo

from screenplay.abilities import PlayTheGame
from screenplay.actions import CreateAGame
from screenplay.questions import SizeOfTheBoard

if TYPE_CHECKING:
    from behave.model import Table
    from screenpy import Actor


def convert_options(value):
    try:
        return int(value)
    except ValueError as err:
        return value


@step(u'{actor:w} initializes a game with the parameters')
def the_user_initialize_a_game_with_the_parameters(context, actor):
    options = dict()
    table: Table = context.table
    for heading in table[0].headings:
        options[heading] = convert_options(table[0][heading])

    the_actor = AnActor.named(actor).who_can(PlayTheGame())
    the_actor.was_able_to(CreateAGame.with_options(**options))
    context.actor = the_actor


@then(u'The size of the board is {size:d}')
def the_size_of_the_board_is_number(context, size):
    the_actor: Actor = context.actor
    the_actor.should(
        See.the(SizeOfTheBoard(), IsEqualTo(size))
    )


@then(u'The board is empty')
def the_board_is_empty(context):
    the_actor: Actor = context.actor
    the_actor.should(See.the(BoardIsEmpty), IsEqualTo(True))
