from aoc.solutions.twenty_twentyone.d7 import part_one
from aoc.solutions.twenty_twentyone.d7 import part_two


test_data = "16,1,2,0,4,2,7,1,2,14"
aimed_position = 2

test_data = [int(x) for x in test_data.split(",")]


def test_part_one():
    ANSWER = 37
    assert part_one(test_data) == ANSWER


def test_part_two():
    ANSWER = 168
    assert part_two(test_data) == ANSWER
