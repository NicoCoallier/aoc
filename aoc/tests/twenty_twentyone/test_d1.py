from aoc.solutions.twenty_twentyone.d1 import part_one
from aoc.solutions.twenty_twentyone.d1 import part_two


test_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def test_part_one():
    assert part_one(test_data) == 7


def test_part_two():
    assert part_two(test_data) == 5
