from behave import given, step, then, when

from tak import parse


@when(u'{actor:w} parse the PTN file')
def i_parse_the_ptn_file(context, actor):
    (result, gamrOrError) = parse(context.text)
    context.parsingResult = result
    context.game = gamrOrError
    context.error = gamrOrError


@then(u'The parsing should be successful')
def the_parsing_should_be_successful(context):
    assert context.error


@then(u'The parsing should be unsuccessful')
def the_parsing_should_be_successful(context):
    assert context.parsingResult == False
