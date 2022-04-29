import pytest
from ten_thousand.game_logic import GameLogic

pytestmark = [pytest.mark.version_3]

@pytest.mark.parametrize(
    "test_input,expected",
    [
        ((1,), (1,)),
        ((1, 2), (1,)),
        ((1, 2, 3), (1,)),
        ((1, 2, 3, 4), (1,)),
        ((1,2,3,4,5), (1, 5)),
        ((1,2,3,4,5,6), (1,2,3,4,5,6)),
        ((1,1,2,3,4,5), (1,1,5)),
        ((1,2,2,2,4,5), (1,2,2,2,5)),
        ((1,3,3,3,4,5), (1,3,3,3,5)),
        ((1,4,4,4,5,6), (1,4,4,4,5)),
        ((1,3,5,5,5,5), (1,5,5,5,5)),
        ((5,5,5,5,5,5), (5,5,5,5,5,5)),
    ],
)

@pytest.mark.skip("Custom Bug Fixing Test")
def test_get_scorers(test_input, expected):
    actual = GameLogic.get_scorers(test_input)
    assert sorted(actual) == sorted(expected)

@pytest.mark.skip("Custom Bug Fixing Test")
def test_edge_case_multi_dice_2_get_scorers():
    actual = GameLogic.get_scorers((5,5,5,5,5,5))
    expected = (5,5,5,5,5,5)
    assert actual == expected

@pytest.mark.skip("Custom Bug Fixing Test")
def test_edge_case_three_of_a_kind_get_scorers():
    actual = GameLogic.get_scorers((2,2,2,3,3,3))
    expected = (2,2,2,3,3,3)
    assert actual == expected

@pytest.mark.skip("Custom Bug Fixing Test")
def test_edge_case_hot_dice_get_scorers():
    actual = GameLogic.get_scorers((1,2,3,4,5,6))
    expected = (1,2,3,4,5,6)
    assert actual == expected
