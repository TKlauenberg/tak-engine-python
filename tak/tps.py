from tak.board import Board, get_stone_count
from tak.grammar import grammar
from tak.player import PlayerInfo, PlayerNumber
from tak.square import Square
from tak.stone import parse_stone_type, StoneType

startColumnCharCode = ord('a')


class TPS:
    def __init__(self, board: Board, player: PlayerInfo, move: int):
        self.board = board
        self.player = player
        self.move: move

    @staticmethod
    def parse(tps: str, boardSize: int, player1: PlayerInfo, player2: PlayerInfo):
        parts = grammar['tpsGrouped'].match(tps)
        (boardStr, nextPlayer, moveStr) = parts.group(1, 3, 5)
        if boardStr == '':
            return (False, 'TPS didn\'t match grammar')
        if nextPlayer == '':
            return (False, 'Missing next Player from TPS')
        if moveStr == '':
            return (False, 'Missing next Movecount from TPS')
        (boardResult, board) = TPS.parseBoard(tps, boardSize, player1, player2)

    @staticmethod
    def parseBoard(tpsPart: str, boardSize: int, player1: PlayerInfo, player2: PlayerInfo):
        rest = tpsPart
        currentRowPos = boardSize
        currentRow = []
        currentColumnPos = startColumnCharCode
        board = []
        while rest != '':
            part = grammar['colGrouped'].match(rest)
            if part[0] == '':
                return (False, 'could not parse tps')
            (emptySquares, stackOnSquare, endTpsLine) = part.group(1, 2, 3)
            if emptySquares != '':
                # parse second char to int for the amount of empty squares
                # format is 'x2' as an example
                countSquares = int(emptySquares[1])
                for _ in [x for x in range(countSquares)]:
                    square = Square(f'{chr(currentColumnPos)}{currentRowPos}')
                    currentRow.append(square)
                    currentRowPos += 1
            if stackOnSquare != '':
                position = f'{chr(currentColumnPos)}{currentRowPos}'
                topStoneType = StoneType.FLAT
                if not stackOnSquare[-1].isdigit():
                    (isResultPositive, stoneTypeOrError) = parse_stone_type(stackOnSquare[-1])
                    if isResultPositive:
                        topStoneType = stoneTypeOrError
                    else:
                        return (False, stoneTypeOrError)
                    stackOnSquare = stackOnSquare[:-1]
                playerNumbers = [int(x) for x in stackOnSquare]
                convertToPlayers = [player1 if x == 1 else player2 for x in playerNumbers]
                stones = [player.get_stone(StoneType.FLAT) for player in convertToPlayers]
                if any([stone == None for stone in stones]):
                    return (False, 'Not enough stones for this board. Could not use TPS')
                currentRow.append(Square(position=position))






if __name__ == "__main__":
    stonebag = get_stone_count(size=3)
    player1 = PlayerInfo(
        name='test', player=PlayerNumber.One, gameStones=stonebag)
    player2 = PlayerInfo(
        name='test2', player=PlayerNumber.Two, gameStones=stonebag)
    test = TPS.parse('1,x2/x3/x3 2 1', 3,player1, player2)
