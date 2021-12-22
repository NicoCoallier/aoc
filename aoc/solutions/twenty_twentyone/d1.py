import logging

from typing import List

import numpy as np

from aoc.arithmetic.sums import sliding_sum
from aoc.solutions.twenty_twentyone.constants import YEAR
from aocd import get_data
from aocd import submit


DAY: int = 1


def count_increase(data):
    """Get the total times element increase (in order)

    :param data: The list on which to check

    :return: The total times it increases
    :rtype: int
    """
    return np.sum([1 if data[i] > data[i - 1] else 0 for i in range(1, len(data))])


def part_one(data: List[int]) -> int:
    """Solve part one (i.e. how many times it increases)
    :param data: the input data

    :return: Part one answer
    :rtype: int
    """
    slided_data = sliding_sum(data, window_length=1)
    return count_increase(slided_data)


def part_two(data: List[int]) -> int:
    """Solve part two (i.e. number of times sliding window incrase)
    :param data: the input data

    :return: The total times it increases
    :rtype: int
    """
    slided_data = sliding_sum(data, window_length=3)
    return count_increase(slided_data)


def main():
    """Main function"""
    logging.info("::: Loading data")
    data = [int(x) for x in get_data(day=DAY, year=YEAR).split("\n")]

    logging.info("::: Solving part one...")
    a1 = part_one(data=data)
    logging.info("::: Submitting part one...")
    _ = submit(a1, part="a", day=DAY, year=YEAR)
    logging.info("::: Solving part two...")
    a2 = part_two(data=data)
    logging.info("::: Submitting part two...")
    _ = submit(a2, part="b", day=DAY, year=YEAR)
    logging.info("::: DONE")


if __name__ == "__main__":
    logging.basicConfig()
    logging.getLogger().setLevel(logging.INFO)
    main()
