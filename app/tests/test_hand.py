from pokercalculator.hand import Hand
from pokercalculator.card import Card
from pokercalculator.hand_rank import HandRank

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

def test_evaluate():

    input = "7D 2S 3C JD 5H"
    hand = Hand(Hand.from_string(input))
    assert hand._Hand__evaluate() == HandRank.HIGH_CARD

    input = "7D 2S 3C JD 2H"
    hand = Hand(Hand.from_string(input))
    assert hand._Hand__evaluate() == HandRank.ONE_PAIR

    input = "JD 2S 3C JD 2H"
    hand = Hand(Hand.from_string(input))
    assert hand._Hand__evaluate() == HandRank.TWO_PAIRS

    input = "2D 2S 3C JD 2H"
    hand = Hand(Hand.from_string(input))
    assert hand._Hand__evaluate() == HandRank.THREE_OF_A_KIND

    input = "5D 2S 3C 6D 4H"
    hand = Hand(Hand.from_string(input))
    assert hand._Hand__evaluate() == HandRank.STRAIGHT

    input = "7D 5D 3D JD 2D"
    hand = Hand(Hand.from_string(input))
    assert hand._Hand__evaluate() == HandRank.FLUSH

    # input = "3S 2S 3H 3D 2H"
    # hand = Hand(Hand.from_string(input))
    # assert hand._Hand__evaluate() == HandRank.FULL_HOUSE

    input = "7D 2S 2C 2D 2H"
    hand = Hand(Hand.from_string(input))
    assert hand._Hand__evaluate() == HandRank.FOUR_OF_A_KIND

    input = "7D 8D 6D 9D 5D"
    hand = Hand(Hand.from_string(input))
    assert hand._Hand__evaluate() == HandRank.STRAIGHT_FLUSH

    input = "KS QS TS JS AS"
    hand = Hand(Hand.from_string(input))
    assert hand._Hand__evaluate() == HandRank.ROYAL_FLUSH