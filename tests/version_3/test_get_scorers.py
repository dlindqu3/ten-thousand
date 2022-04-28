import pytest
from ten_thousand.game_logic import GameLogic

pytestmark = [pytest.mark.version_3]


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (tuple(), tuple()),
        ((1,), (1,)),
        ((1, 2), (1,)),
        ((1, 2, 3), (1,)),
        ((1, 2, 3, 5), (1, 5)),
        ((5, 1, 2, 3), (1, 5)),
        ((2, 3, 4), tuple()),
    ],
)
def test_get_scorers(test_input, expected):
    actual = GameLogic.get_scorers(test_input)
    assert sorted(actual) == sorted(expected)

def test_edge_case_hot_dice_get_scorers():
    actual = GameLogic.get_scorers((1,2,3,4,5,6))
    expected = (1,2,3,4,5,6)
    assert actual == expected

def test_edge_case_pairs_get_scorers():
    actual = GameLogic.get_scorers((2,2,3,3,4,4))
    expected = (2,2,3,3,4,4)
    assert actual == expected

def test_edge_case_multi_dice_get_scorers():
    actual = GameLogic.get_scorers((1,1,2,3,4,6))
    expected = (1,1)
    assert actual == expected

def test_edge_case_multi_dice_2_get_scorers():
    actual = GameLogic.get_scorers((5,5,5,5,5,5))
    expected = (5,5,5,5,5,5)
    assert actual == expected