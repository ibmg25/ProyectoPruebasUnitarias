from os import getcwd
from pokercalculator.calculator import Calculator


FILE_PATH_SOURCE = getcwd() + "\\" + "pokerdata.txt"
CALCULATOR = Calculator(FILE_PATH_SOURCE)


def test_calculator():
    Calculator(FILE_PATH_SOURCE)