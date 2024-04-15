from pokercalculator.card import Card
from pokercalculator.rank import Rank
from pokercalculator.suit import Suit

def test_from_string():
    jack_of_clubs = Card.from_string("JC")
    assert Rank.JACK == jack_of_clubs.rank and Suit.CLUBS == jack_of_clubs.suit

def test_to_string_name():
    assert "THREE OF HEARTS" == Card(Rank.THREE, Suit.HEARTS).to_string_name()

def test_str():
    assert "5D" == str(Card(Rank.FIVE, Suit.DIAMONDS))