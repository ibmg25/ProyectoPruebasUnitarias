from pokercalculator.calculator import Calculator
from pokercalculator.card import Card
from pokercalculator.hand import Hand
from pokercalculator.rank import Rank
from pokercalculator.suit import Suit

calculator = Calculator("./txts/winner1.txt")

hand1 = Hand([Card(Rank.ACE, Suit.SPADES),
          Card(Rank.ACE, Suit.HEARTS),
          Card(Rank.FIVE, Suit.DIAMONDS),
          Card(Rank.NINE, Suit.DIAMONDS),
          Card(Rank.THREE, Suit.DIAMONDS)])

hand2 = Hand([Card(Rank.KING, Suit.SPADES),
          Card(Rank.KING, Suit.HEARTS),
          Card(Rank.FIVE, Suit.DIAMONDS),
          Card(Rank.NINE, Suit.DIAMONDS),
          Card(Rank.THREE, Suit.DIAMONDS)])

def test_check_winners_helper():
    assert calculator._Calculator__check_winners_helper(2, 1) == 0
    assert calculator._Calculator__check_winners_helper(1, 2) == 1
    assert calculator._Calculator__check_winners_helper(1, 1) == 2

def test_check_winners():
    assert calculator._Calculator__check_winners(hand1, hand2) < 2
    assert calculator._Calculator__check_winners(hand1, hand1) >= 2