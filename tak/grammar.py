import re
requiredTagsRegExp = {
    'size': re.compile(r'^([3-9])$'),
}

otherTagsRegExp = {
    'player1': re.compile(r'^(.*)$'),
    'player2': re.compile(r'^(.*)$'),
    'date': re.compile(r'^(\d\d\d\d)\.(\d\d?)\.(\d\d?)$'),
    'result': re.compile(r'^(R-0|0-R|F-0|0-F|1-0|0-1|1\/2-1\/2|)$'),
    'event': re.compile(r'^.*$'),
    'site': re.compile(r'^.*$'),
    'round': re.compile(r'^\d+$'),
    'rating1': re.compile(r'^\d+$'),
    'rating2': re.compile(r'^\d+$'),
    'tps': re.compile(r'^[1-8xSC\',]+\s+[1,2]\s+\d+$'),
    'points': re.compile(r'^\d+$'),
    'time': re.compile(r'^\d\d(:\d\d){1,2}$'),
    'clock': re.compile(r'^\d+min(\+\d+sec)$|^((((\d\s+)?\d\d?:)?\d\d?:)?\d\d?\s*)?(\+(((\d\s+)?\d\d?:)?\d\d?:)?\d\d?)?$'),
}
requiredTags = requiredTagsRegExp.keys()
otherTags = otherTagsRegExp.keys()
tags = {**requiredTagsRegExp, **otherTagsRegExp}
space = r'(?:x[1-8]?)'
stack = r'(?:[12]+[SC]?)'
stackGrouped = r'([12]*)([12][SC]?)'
separator = r'[,\/]'
col = f'(?:{space}|{stack})'
cols = f'({col}?{separator}?)'
colGrouped = f'({space}?)({stack}?)({separator}?)'
tpsGrouped = f'((?:{col}|{separator})*)' + \
    r'(?:(\s+)([12]))?(?:(\s+)([1-8]\d*))?([\^]*)'
tag = r'(?:[^\[]*\[.*\]?)'
tagGrouped = r'([^\[]*\[\s*?)(\S+)(\s*)([\'"]?)([^\4]*)(\4)([\^]*\]?)'
stone = r'[FSC]?'
square = r'[a-i][1-8]'
count = r'[1-8]?'
direction = r'(?:[-+<>])'
drops = r'[1-8]*'
place = f'(?:{stone}{square})'
placeGrouped = f'({stone})({square})'
slide = f'(?:{count}{square}{direction}{drops}{stone})'
slideGrouped = f'({count})({square})({direction})({drops})({stone})'
comment = r'(?:\s*?\{[^}]*\}?)*'
commentText = r'\s*\{\\s*[^}]*[^}\s]?\s*\}?'
commentGrouped = r'(\s*\{\s*)([^}]*[^}\s])?(\s*\}?)'
result = r'(?:(?:\s|--)*(?:R-0|0-R|F-0|0-F|1-0|0-1|1\/2-1\/2))'
resultGrouped = r'((?:\s|--)*)(R-0|0-R|F-0|0-F|1-0|0-1|1\/2-1\/2)'
evaluation = r'[?!\'"]*'
nop = r'(?:\s*(?:load|--|\.\.\.))'
nopGrouped = r'(\\s*)(\\S+)'
ply = r'(?:\s*' + f'(?:{slide}|{place}){evaluation})'
plyGrouped = r'(\s*)'+f'(?:({slide})|({place}))({evaluation})'
linenum = r'(?:^|\s)+(?:\d+(?:-\d*)?\.+)+'
linenumGrouped = r'(^|\s+)((?:\d+(?:-\d*)?\.+)+)'
move = f'(?:{linenum}{comment}(?:{nop}|{ply})?{comment}{ply}?{comment}{result}?{comment}' + \
    r'[ \t]*[\^]*)'
moveGrouped = f'^({linenum})({comment})({nop}|{ply}?)({comment})({ply}?)({comment})({result}?)({comment})' + \
    r'(\s*)([\^]*)'
moveOnly = f'^{move}$'
ptnGrouped = f'^({tag}+)({comment})'+r'((?:.|\s)*?)((?:\s|--)*)$'
grammar = {
    'space': re.compile(space),
    'stack': re.compile(stack),
    'stackGrouped': re.compile(stackGrouped),
    'separator': re.compile(separator),
    'col': re.compile(col),
    'cols': re.compile(cols),
    'colGrouped': re.compile(colGrouped),
    'tpsGrouped': re.compile(tpsGrouped),
    'tag': re.compile(tag),
    'tagGrouped': re.compile(tagGrouped),
    'stone': re.compile(stone),
    'square': re.compile(square),
    'count': re.compile(count),
    'direction': re.compile(direction),
    'drops': re.compile(drops),
    'place': re.compile(place),
    'placeGrouped': re.compile(placeGrouped),
    'slide': re.compile(slide),
    'slideGrouped': re.compile(slideGrouped),
    'comment': re.compile(comment),
    'commentText': re.compile(commentText),
    'commentGrouped': re.compile(commentGrouped),
    'result': re.compile(result),
    'resultGrouped': re.compile(resultGrouped),
    'evaluation': re.compile(evaluation),
    'nop': re.compile(nop),
    'nopGrouped': re.compile(nopGrouped),
    'ply': re.compile(ply),
    'plyGrouped': re.compile(plyGrouped),
    'linenum': re.compile(linenum),
    'linenumGrouped': re.compile(linenumGrouped),
    'move': re.compile(move),
    'moveGrouped': re.compile(moveGrouped, re.MULTILINE),
    'moveOnly': re.compile(moveOnly),
    'ptnGrouped': re.compile(ptnGrouped),
}
