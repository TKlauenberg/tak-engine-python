from behave import given, when, then  # pylint: disable=no-name-in-module
from hamcrest import *
from tak.square import Square
from tak.stone import StoneType
from tak.player import Player


@given(u'an empty square')
def step_impl(context):
    context.square = Square()


@when(u'the developer drops a white stone')
def step_impl(context):
    stone = {'type': StoneType.FLAT, 'player': Player.One}
    context.square.drop(stone)
    stone2 = {'type': StoneType.FLAT, 'player': Player.One}
    context.square.drop(stone2)


@then(u'the square should have a white stone')
def step_impl(context):
    stones = context.square.stones
    stone = {'type': StoneType.FLAT, 'player': Player.One}
    assert_that(stones, only_contains(stone))
