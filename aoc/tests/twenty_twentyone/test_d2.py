from aoc.solutions.twenty_twentyone.d2 import part_one
from aoc.solutions.twenty_twentyone.d2 import part_two


test_directions = ["forward", "down", "forward", "up", "down", "forward"]
test_values = [5, 5, 8, 3, 8, 2]


def test_part_one():
    ANSWER = 150
    assert part_one(test_directions, test_values) == ANSWER


def test_part_two():
    ANSWER = 900
    assert part_two(test_directions, test_values) == ANSWER
