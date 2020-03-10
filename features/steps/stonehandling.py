from behave import given, when, then, step
from tak import Move, MoveType, Game, Square
from hamcrest import assert_that, is_, equal_to


@when(u'the user places a {stonetype:StoneTypeByName} at {position:Position}')
def i_place_a_stone_at_position(context, stonetype, position):
    move = Move(action=MoveType.Place, position=position, stoneType=stonetype)
    game: Game = context.game
    game.execute(move)


@then(u'On {position:Position} is a {stone:Stone}')
def on_position_is_a_stone(context, position, stone):
    game: Game = context.game
    square: Square = game.board.get_square(position)
    assert_that(len(square.stones), is_(equal_to(1)))
    assert_that(square.top(), is_(equal_to(stone)))

