from tak import Game, Stone


def check_stone(expected: Stone, actual: Stone):
    assert expected.type == actual.type, f"stonetype not equal. expected {expected.type} but was {actual.player}"
    assert expected.player == actual.player, f"player not equal. expected {expected.player} but was {actual.player}"
    assert expected == actual, f"stone object not equal"


def check_stack(game: Game, position: str, *stack: list):
    square = game.board.get_square(position)
    assert len(square.stones) == len(stack), "stack has equal length"
    for i in range(len(stack)):
        check_stone(expected=stack[i], actual=square.stones[i])
    assert all([a == b for (a, b) in zip(square.stones, stack)])
