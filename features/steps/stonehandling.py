from behave import given, step, then, when

from features.steps.checks import check_stack, check_stone
from tak import Direction, Game, Move, MoveType, Square


@step(u'the user places a {stonetype:StoneTypeByName} at {position:Position}')
def i_place_a_stone_at_position(context, stonetype, position):
    move = Move(action=MoveType.Place, position=position, stoneType=stonetype)
    game: Game = context.game
    game.execute(move)


@when(u'the user tries to place a {stonetype:StoneTypeByName} at {position:Position}')
def the_user_tries_to_place_a_stone_at_position(context, stonetype, position):
    move = Move(action=MoveType.Place, position=position, stoneType=stonetype)
    try:
        context.game.execute(move)
    except Exception as e:
        context.error = e


@step(u'the user moves one stone from {position:Position} {direction:Direction}')
def the_user_moves_one_stone_from_c3_up(context, position, direction):
    move = Move(action=MoveType.Move, amount=1,
                direction=direction, drops=[1], position=position)
    context.game.execute(move)


@when(u'the user tries to move one stone from {position:Position} {direction:Direction}')
def the_user_tries_to_move_one_stone_position_direction(context, position, direction):
    move = Move(action=MoveType.Move, amount=1,
                direction=direction, drops=[1], position=position)
    try:
        context.game.execute(move)
    except Exception as e:
        context.error = e


@when(u'the user moves {amount:d} stones from {position:Position} {direction:Direction}, dropping one stone at each square')
def the_user_moves_stones_from_position_direction(context, amount: int, position: str, direction: Direction):
    drops = list([1 for i in range(amount)])
    move = Move(action=MoveType.Move, amount=amount,
                direction=direction, drops=drops, position=position)
    context.game.execute(move)


@when(u'the user tries to move {amount:d} stones from {position:Position} {direction:Direction}, dropping one stone at each square')
def the_user_tries_to_move_stones_from_position_direction(context, amount: int, position: str, direction: Direction):
    drops = list([1 for i in range(amount)])
    move = Move(action=MoveType.Move, amount=amount,
                direction=direction, drops=drops, position=position)
    try:
        context.game.execute(move)
    except Exception as e:
        context.error = e


@when(u'the user tries to move {amount:d} stones from {position:Position} {direction:Direction} with all stones')
def the_user_tries_to_move_stones_from_position_direction_with_all_stones(context, amount, position, direction):
    move = Move(action=MoveType.Move, amount=amount,
                direction=direction, drops=[amount], position=position)
    try:
        context.game.execute(move)
    except Exception as e:
        context.error = e


@then(u'On {position:Position} is a {stone:Stone}')
def on_position_is_a_stone(context, position, stone):
    game: Game = context.game
    square: Square = game.board.get_square(position)
    assert len(square.stones) == 1, "square should only have one stone"
    check_stone(expected=stone, actual=square.top())


@then(u'On {position:Position} should be a stack with a {stone:Stone} and a {stone2:Stone}')
def on_positioon_should_be_a_stack_with_stones(context, position, stone, stone2):
    check_stack(context.game, position, stone, stone2)


@then(u'the user should get an error')
def the_user_should_get_an_error(context):
    assert context.error != None, 'user should get an error'


@then(u'The error message should be "{text}"')
def the_error_message_should_be_message(context, text):
    assert str(context.error) == text
