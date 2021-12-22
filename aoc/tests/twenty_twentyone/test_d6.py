from aoc.solutions.twenty_twentyone.d6 import format_data
from aoc.solutions.twenty_twentyone.d6 import part_one
from aoc.solutions.twenty_twentyone.d6 import part_two


def test_part_one():
    ANSWER = 5934
    test_data = "3,4,3,1,2"
    test_data = format_data(test_data)
    assert part_one(test_data) == ANSWER


def test_part_two():
    ANSWER = 26984457539
    test_data = "3,4,3,1,2"
    test_data = format_data(test_data)
    assert part_two(test_data) == ANSWER
