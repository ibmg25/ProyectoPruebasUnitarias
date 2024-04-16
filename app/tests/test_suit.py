from pokercalculator.suit import Suit

def test_get_suit_by_suit_value():
    assert Suit.get_suit_by_suit_value('S') == Suit.SPADES