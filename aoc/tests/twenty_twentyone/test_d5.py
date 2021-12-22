from aoc.solutions.twenty_twentyone.d5 import part_one
from aoc.solutions.twenty_twentyone.d5 import part_two


test_data = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""
test_data = list(map(lambda x: x.split("->"), test_data.split("\n")))


def test_part_one():
    ANSWER = 5
    assert part_one(test_data) == ANSWER


def test_part_two():
    ANSWER = 12
    assert part_two(test_data) == ANSWER
