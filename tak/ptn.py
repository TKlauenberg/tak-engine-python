from tak.grammar import grammar, requiredTags
from tak.tag import Tag
from tak.game import Game
from tak.move import Move


def parse(text: str):
    file = grammar['ptnGrouped'].match(text)
    if not file:
        return (False, 'not a valid PTN file')
    headerText = file[1]
    body = file[3]

    headerLines = grammar['tag'].findall(headerText)
    parsedTags = [Tag.parse(x) for x in headerLines]
    if not all([x for (x, y) in parsedTags]):
        parseErrors = [error for (result, error) in parsedTags if not result]
        return (False, parseErrors[0])
    tags = [tag for (result, tag) in parsedTags]
    missingTags = [tagName for tagName in requiredTags if all([tagName != tag.get_key() for tag in tags])]
    if len(missingTags) > 0:
        return (False, f"Some Tags are missing: {missingTags}")
    if len(set([tag.get_key() for tag in tags])) != len(tags):
        return (False, "duplicate tag entries")
    tagMap = dict([(tag.get_key(), tag) for tag in tags])
    gameOptionTags = ['size', 'player1', 'player2', 'tps']
    gameOptions = dict([(tag, tagMap.get(tag).value) for tag in gameOptionTags if tagMap.get(tag) != None])
    try:
        game = Game(**gameOptions)
    except Exception as ex:
        return (False, ex)
    if body:
        moveLines = grammar['moveGrouped'].match(body)
        line = game.moveCount
        moves = []
        # if we have a tps string, it could be that we have only one move in the first line
        if moveLines[1] != '' and moveLines[5] == '':
            currentLine = int(moveLines[1].strip())
            if currentLine != line:
                return (False, f'Expected Line {line} but found {currentLine}')
            (moveParseSuccess, moveOrError) = Move.parse(moveLines[3].strip())
            if not moveParseSuccess:
                return (False, moveOrError)
            moves.append(moveOrError)
            moveLines = grammar['moveGrouped'].match(moveLines[10]) if moveLines[10] else None
        while moveLines!= None:
            currentLine = int(moveLines[1].strip())
            if currentLine != line:
                return (False, f'Expected Line {line} but found {currentLine}')
            (firstMoveParseSuccess, firstMove) = Move.parse(moveLines[3].strip())
            if not firstMoveParseSuccess:
                return (False, firstMove)
            moves.append(firstMove)
            (seccondMoveParseSuccess, seccondMove) = Move.parse(moveLines[5].strip())
            if not seccondMoveParseSuccess:
                return (False, seccondMove)
            moves.append(seccondMove)
            moveLines = grammar['moveGrouped'].match(
                moveLines[10]) if moveLines[10] else None
            line += 1
            for move in moves:
                game.execute(move)
    return (True, game)


if __name__ == "__main__":
    text = parse("""[Player1 ""]
[Player2 ""]
[Size "5"]
[Date "2020.03.19"]
[Time "15:08:50"]

1. c3 c4
2. b3""")
    print(text)
