from behave.formatter.steps import StepsUsageFormatter
from behave.model_core import Status
from behave.runner_util import make_undefined_step_snippets
from six import string_types
from behave import parser

STEP_MODULE_TEMPLATE = '''\
# -*- coding: {encoding} -*-
"""
Missing step implementations (proof-of-concept).
"""

from behave import given, when, then, step

{step_snippets}
'''


def make_undefined_step_snippet(step, language=None):
    """Helper function to create an undefined-step snippet for a step.

    :param step: Step to use (as Step object or string).
    :param language: i18n language, optionally needed for step text parsing.
    :return: Undefined-step snippet (as string).
    """
    if isinstance(step, string_types):
        step_text = step
        steps = parser.parse_steps(step_text, language=language)
        step = steps[0]
        assert step, "ParseError: %s" % step_text

    prefix = u"u"
    single_quote = "'"
    if single_quote in step.name:
        step.name = step.name.replace(single_quote, r"\'")

    schema = u"@%s(%s'%s')\ndef %s(context):\n"
    schema += u"    raise NotImplementedError(%s'STEP: %s %s')\n\n"
    snippet = schema % (step.step_type, prefix, step.name, step.name.replace(" ", "_").lower(),
                        prefix, step.step_type.title(), step.name)
    return snippet


class SnippetsFormatter(StepsUsageFormatter):
    """Formatter that writes missing steps snippets into a step module file.

    Reuses StepsUsageFormatter class because it already contains the logic
    for discovering missing/undefined steps.

    .. code-block:: ini

        # -- FILE: behave.ini
        # NOTE: Long text value needs indentation on following lines.
        [behave.userdata]
        behave.formatter.missing_steps.template = # -*- coding: {encoding} -*-
            # Missing step implementations.
            from behave import given, when, then, step

            {step_snippets}
    """
    name = "missing-steps"
    description = "Writes implementation for missing step definitions."
    template = STEP_MODULE_TEMPLATE

    def __init__(self, stream_opener, config):
        super(SnippetsFormatter, self).__init__(stream_opener, config)

    def close(self):
        """Called at end of test run.
        NOTE: Overwritten to avoid to truncate/overwrite output-file.
        """
        if self.step_registry and self.undefined_steps:
            # -- ENSURE: Output stream is open.
            self.stream = self.open()
            self.report()

        # -- FINALLY:
        self.close_stream()

    # -- REPORT SPECIFIC-API:
    def report(self):
        """Writes missing step implementations by using step snippets."""
        step_snippets = make_undefined_step_snippets(self.undefined_steps, make_undefined_step_snippet)
        encoding = self.stream.encoding or "UTF-8"
        function_separator = u"\n\n\n"
        step_snippets_text = function_separator.join(step_snippets)
        module_text = self.template.format(encoding=encoding,
                                           step_snippets=step_snippets_text)
        self.stream.write(module_text)
        self.stream.write("\n")
