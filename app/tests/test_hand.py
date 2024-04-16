from pokercalculator.hand import Hand
from pokercalculator.card import Card

def test_from_string():
    input = "7D 2S 3C JD 2H"
    hand = Hand(Hand.from_string(input))
    assert isinstance(hand, Hand)

def test_to_string_name():
    cards = [
            Card.from_string("7D"),
            Card.from_string("2S"),
            Card.from_string("3C"),
            Card.from_string("JD"),
            Card.from_string("2H")
        ]
    assert ("SEVEN OF DIAMONDS\n" +
            "TWO OF SPADES\n" +
            "THREE OF CLUBS\n" +
            "JACK OF DIAMONDS\n" +
            "TWO OF HEARTS" == Hand(cards).to_string_name())
    
def test_str():
    cards = [
            Card.from_string("7D"),
            Card.from_string("2S"),
            Card.from_string("3C"),
            Card.from_string("JD"),
            Card.from_string("2H")
        ]
    assert "7D 2S 3C JD 2H" == str(Hand(cards))