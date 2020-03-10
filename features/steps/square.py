from behave import given, then, when  # pylint: disable=no-name-in-module
from hamcrest import *

from tak.square import Square
from tak.stone import Stone, StoneType, PlayerNumber


@given(u'an empty square')
def step_impl(context):
    context.square = Square()


@when(u'the developer drops a white stone')
def step_impl(context):
    stone = Stone(type=StoneType.FLAT, player=PlayerNumber.One)
    context.square.drop(stone)


@then(u'the square should have a white stone')
def step_impl(context):
    stones = context.square.stones
    stone = Stone(type=StoneType.FLAT, player=PlayerNumber.One)
    assert_that(stones, only_contains(stone))
