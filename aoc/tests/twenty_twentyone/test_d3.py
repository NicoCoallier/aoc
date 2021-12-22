import numpy as np

from aoc.solutions.twenty_twentyone.d3 import part_one
from aoc.solutions.twenty_twentyone.d3 import part_two


test_data = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]
test_data = [list(x) for x in test_data]
test_data = np.array([list(map(lambda x: int(x), l)) for l in test_data])


def test_part_one():
    ANSWER = 198
    assert part_one(test_data) == ANSWER


def test_part_two():
    ANSWER = 230
    assert part_two(test_data) == ANSWER
