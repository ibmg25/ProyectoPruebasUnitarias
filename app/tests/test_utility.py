from pokercalculator.card import Card
from pokercalculator.rank import Rank
from pokercalculator.suit import Suit
from pokercalculator.utility import Utility

def  test_replace_ace_for_one_if():
    assert Utility.replace_ace_for_one_if([3, 5, 7, 9]) == [3, 5, 7, 9]
    assert Utility.replace_ace_for_one_if([2, 3, 4, 14]) == [1, 2, 3, 4]
    assert Utility.replace_ace_for_one_if([2, 3, 4, 5]) == [2, 3, 4, 5]
    assert Utility.replace_ace_for_one_if([3, 4, 5, 14]) == [3, 4, 5, 14]
