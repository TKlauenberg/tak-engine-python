import re

import parse
from behave import register_type


@parse.with_pattern(r"[a-h][1-8]")
def parse_position(text):
    return text


register_type(Position=parse_position)
