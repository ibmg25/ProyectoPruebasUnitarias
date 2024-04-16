from pokercalculator.rank import Rank

def test_get_rank_by_rank_value():
    assert Rank.get_rank_by_rank_value('Q') == Rank.QUEEN