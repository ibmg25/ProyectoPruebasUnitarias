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
    
def __str__():
    expected_output = "Total Games: 1\nPlayer 1: 2\nPlayer 2: 0\nTie: 0" 
    assert calculator.__Calculator____str__() == expected_output
def test_break_tie():
    #han1 gana royal_flush
    hand1 = Hand([Card(Rank.TEN, Suit.HEARTS), Card(Rank.JACK, Suit.HEARTS), Card(Rank.QUEEN, Suit.HEARTS), Card(Rank.KING, Suit.HEARTS), Card(Rank.ACE, Suit.HEARTS)])
    hand2 = Hand([Card(Rank.TWO, Suit.SPADES), Card(Rank.THREE, Suit.SPADES), Card(Rank.FOUR, Suit.SPADES), Card(Rank.FIVE, Suit.SPADES), Card(Rank.SIX, Suit.SPADES)])
    result = calculator._Calculator__break_tie(hand1, hand2)
    #han2 gana con straight_flush
    assert result == 2
    hand2 = Hand([Card(Rank.TEN, Suit.HEARTS), Card(Rank.JACK, Suit.HEARTS), Card(Rank.QUEEN, Suit.HEARTS), Card(Rank.KING, Suit.HEARTS), Card(Rank.NINE, Suit.HEARTS)])
    hand1 = Hand([Card(Rank.TWO, Suit.SPADES), Card(Rank.THREE, Suit.SPADES), Card(Rank.FOUR, Suit.SPADES), Card(Rank.FIVE, Suit.SPADES), Card(Rank.SIX, Suit.SPADES)])
    result = calculator._Calculator__break_tie(hand1, hand2)
    assert result == 1 
    #han1 gana flush alta
    hand1 = Hand([Card(Rank.TWO, Suit.HEARTS), Card(Rank.THREE, Suit.HEARTS), Card(Rank.FIVE, Suit.HEARTS), Card(Rank.SEVEN, Suit.HEARTS), Card(Rank.NINE, Suit.HEARTS)])
    hand2 = Hand([Card(Rank.TWO, Suit.SPADES), Card(Rank.THREE, Suit.SPADES), Card(Rank.FOUR, Suit.SPADES), Card(Rank.FIVE, Suit.SPADES), Card(Rank.SIX, Suit.SPADES)])
    result = calculator._Calculator__break_tie(hand1, hand2)
    assert result == 0 

def test_break_tie_high_card():
    
    #empate
    rank_numbers_1 = [10, 9, 8, 7, 6]
    rank_numbers_2 = [10, 9, 8, 7, 6]
    result = calculator._Calculator__break_tie_high_card(rank_numbers_1, rank_numbers_2)
    assert result == 2
    
    #gana jugador 1
    rank_numbers_1 = [10, 9, 8, 7, 6]
    rank_numbers_2 = [9, 8, 7, 6, 5]
    result = calculator._Calculator__break_tie_high_card(rank_numbers_1, rank_numbers_2)
    assert result == 0
    
    #gana jugador 2
    rank_numbers_1 = [10, 9, 8, 7, 6]
    rank_numbers_2 = [10, 9, 8, 7, 7]
    result = calculator._Calculator__break_tie_high_card(rank_numbers_1, rank_numbers_2)
    assert result == 1 

def test_break_tie_straight():
    
    #gana jugador 1
    rank_numbers_1 = [10, 11, 12, 13, 14]  
    rank_numbers_2 = [9, 10, 11, 12, 13]  
    result = calculator._Calculator__break_tie_straight(rank_numbers_1, rank_numbers_2)
    assert result == 0 
    
    #empate
    rank_numbers_1 = [2, 3, 4, 5, 6] 
    rank_numbers_2 = [2, 3, 4, 5, 6] 
    result = calculator._Calculator__break_tie_straight(rank_numbers_1, rank_numbers_2)
    assert result == 2
    
    #gana jugador 2
    rank_numbers_1 = [2, 3, 4, 5, 6] 
    rank_numbers_2 = [3, 4, 5, 6, 7]
    result = calculator._Calculator__break_tie_straight(rank_numbers_1, rank_numbers_2)
    assert result == 1
def test_break_tie_rest():
    # empate
    rank_numbers_1 = [2, 2, 3, 4, 5]
    rank_numbers_2 = [2, 2, 3, 4, 5]
    
    result = calculator._Calculator__break_tie_rest(rank_numbers_1, rank_numbers_2,0)
    assert result == 2 
    #gana jugador 1
    rank_numbers_1 = [2, 2, 3, 4, 5]
    rank_numbers_2 = [2, 2, 3, 4, 6]
    
    result = calculator._Calculator__break_tie_rest(rank_numbers_1, rank_numbers_2,0)
    assert result == 1  
    #gana jugador 2
    rank_numbers_1 = [2, 2, 3, 4, 5]
    rank_numbers_2 = [2, 2, 3, 5, 5]
    result = calculator._Calculator__break_tie_rest(rank_numbers_1, rank_numbers_2,0)
    assert result == 2