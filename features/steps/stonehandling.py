from behave import given, step, then, when
from screenpy import Actor
from screenpy.actions import See
from screenpy.resolutions import IsEqualTo, IsNot

from features.steps.checks import check_stack, check_stone
from features.steps.screenplay.actions import Place
from features.steps.screenplay.questions import (GameError, NextPlayer,
                                                 PlayerOfTopStoneOn,
                                                 RoundOfTheGame,
                                                 TheStackOnPosition,
                                                 TypeOfTopStoneOn)
from tak import Direction, Game, Move, MoveType, Square
from tak.stone import StoneType


@step(u'{actor:w} places a {stonetype:StoneTypeByName} at {position:Position}')
def i_place_a_stone_at_position(context, actor: str, stone_type: StoneType, position: str):
    the_actor: Actor = context.actor
    the_actor.attempts_to(Place.a(stone_type).on(position))


@when(u'{actor:w} tries to place a {stonetype:StoneTypeByName} at {position:Position}')
def the_user_tries_to_place_a_stone_at_position(context, actor, stonetype, position):
    the_actor: Actor = context.actor
    the_actor.attempts_to(Place.a(stone_type).on(position))


@step(u'{actor:w} moves one stone from {position:Position} {direction:Direction}')
def the_user_moves_one_stone_from_c3_up(context, actor, position, direction):
    move = Move(action=MoveType.Move, amount=1,
                direction=direction, drops=[1], position=position)
    context.game.execute(move)


@when(u'{actor:w} tries to move one stone from {position:Position} {direction:Direction}')
def the_user_tries_to_move_one_stone_position_direction(context, actor,  position, direction):
    move = Move(action=MoveType.Move, amount=1,
                direction=direction, drops=[1], position=position)
    try:
        context.game.execute(move)
    except Exception as e:
        context.error = e


@when(u'{actor:w} moves {amount:d} stones from {position:Position} {direction:Direction}, dropping one stone at each square')
def the_user_moves_stones_from_position_direction(context, actor, amount: int, position: str, direction: Direction):
    drops = list([1 for i in range(amount)])
    move = Move(action=MoveType.Move, amount=amount,
                direction=direction, drops=drops, position=position)
    context.game.execute(move)


@when(u'{actor:w} tries to move {amount:d} stones from {position:Position} {direction:Direction}, dropping one stone at each square')
def the_user_tries_to_move_stones_from_position_direction(context, actor, amount: int, position: str, direction: Direction):
    drops = list([1 for i in range(amount)])
    move = Move(action=MoveType.Move, amount=amount,
                direction=direction, drops=drops, position=position)
    try:
        context.game.execute(move)
    except Exception as e:
        context.error = e


@when(u'{actor:w} tries to move {amount:d} stones from {position:Position} {direction:Direction} with all stones')
def the_user_tries_to_move_stones_from_position_direction_with_all_stones(context, actor, amount, position, direction):
    move = Move(action=MoveType.Move, amount=amount,
                direction=direction, drops=[amount], position=position)
    try:
        context.game.execute(move)
    except Exception as e:
        context.error = e


@then(u'On {position:Position} is a {stone:Stone}')
def on_position_is_a_stone(context, position, stone):
    the_actor: Actor = context.actor
    the_actor.should(
        See.the(TheStackOnPosition(pos=position), IsEqualTo([stone])))


@then(u'On {position:Position} should be a stack with a {stone:Stone} and a {stone2:Stone}')
def on_positioon_should_be_a_stack_with_stones(context, position, stone, stone2):
    check_stack(context.game, position, stone, stone2)


@then(u'{actor:w} should get an error')
def the_user_should_get_an_error(context, actor):
    the_actor: Actor = context.actor
    the_actor.should(See.the(GameError(), IsNot(IsEqualTo(None))))


@then(u'The error message should be "{text}"')
def the_error_message_should_be_message(context, text):
    the_actor: Actor = context.actor
    the_actor.should(See.the(GameError(), IsEqualTo(text)))


@then(u'On {position:Position} should be a stack with stones "{stack:Stack}"')
def on_pos_should_be_a_stack_with_stones(context, position, stack):
    the_actor: Actor = context.actor
    the_actor.should(
        See.the(TheStackOnPosition(pos=position), IsEqualTo(stack)))


@then(u'the top stone on {position:Position} should be {player:PlayerColor}')
def the_top_stone_on_pos_should_be_color(context, position, player):
    the_actor: Actor = context.actor
    the_actor.should(See.the(PlayerOfTopStoneOn(position), IsEqualTo(player)))


@then(u'the top stone on {position:Position} should be of type {stoneType:StoneTypeByChar}')
def the_top_stone_on_pos_should_be_of_type_stonetype(context, position, stoneType):
    the_actor: Actor = context.actor
    the_actor.should(See.the(TypeOfTopStoneOn(position), IsEqualTo(stoneType)))


@then(u'the current Round should be {count:d}')
def the_current_round_should_be_10(context, count):
    the_actor: Actor = context.actor
    the_actor.should(See.the(RoundOfTheGame(), IsEqualTo(count)))


@then(u'the next Player should be {player:Player}')
def the_next_player_should_be_player_2(context, player):
    the_actor: Actor = context.actor
    the_actor.should(See.the(NextPlayer(), IsEqualTo(player)))
