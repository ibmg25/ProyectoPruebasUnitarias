from pokercalculator.calculator import Calculator

calculator = Calculator("./txts/winner1.txt")


def test_check_winners_helper():
    assert calculator._Calculator__check_winners_helper(2, 1) == 0
    assert calculator._Calculator__check_winners_helper(1, 2) == 1
    assert calculator._Calculator__check_winners_helper(1, 1) == 2