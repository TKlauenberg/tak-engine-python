from behave import given, step, then, when
from behave.model import Table
from hamcrest import *

from tak.game import Game


def convert_options(value):
    try:
        return int(value)
    except ValueError as err:
        return value


@step(u'the user initializes a game with the parameters')
def the_user_initialize_a_game_with_the_parameters(context):
    options = dict()
    table: Table = context.table
    for heading in table[0].headings:
        options[heading] = convert_options(table[0][heading])
    context.game = Game(**options)


@then(u'The size of the board is {size:d}')
def the_size_of_the_board_is_number(context, size):
    assert_that(context.game.board.size, equal_to(size))
    assert_that(context.game.size, equal_to(size))


@then(u'The board is empty')
def the_board_is_empty(context):
    squares = [square.is_empty() for rows in context.game.board for square in rows]
    assert_that(all(squares), is_(True))
