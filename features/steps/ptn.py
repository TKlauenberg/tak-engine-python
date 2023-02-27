from behave import given, step, then, when
from screenpy import Actor, AnActor
from screenpy.actions import See
from screenpy.resolutions import IsEqualTo, IsNot

from features.steps.screenplay.abilities import PlayTheGame
from features.steps.screenplay.actions import CreateAGameWithPtn
from features.steps.screenplay.questions import GameError
from tak import parse


@when(u'{actor} parse the PTN file')
def i_parse_the_ptn_file(context, actor):
    the_actor = AnActor.named(actor).who_can(PlayTheGame())
    the_actor.was_able_to(CreateAGameWithPtn(context.text))
    context.actor = the_actor


@then(u'The parsing should be successful')
def the_parsing_should_be_successful(context):
    the_actor: Actor = context.actor
    the_actor.should(See.the(GameError(), IsEqualTo(None)))


@then(u'The parsing should be unsuccessful')
def the_parsing_should_be_unsuccessful(context):
    the_actor: Actor = context.actor
    the_actor.should(See.the(GameError(), IsNot(IsEqualTo(None))))
