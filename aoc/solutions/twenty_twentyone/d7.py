import logging

from typing import List

import numpy as np

from aoc.solutions.twenty_twentyone.constants import YEAR
from aocd import get_data
from aocd import submit


DAY: int = 7


def part_one(data: List[int]) -> int:
    """Solve part one
    :param data: the input data

    :return: Part one answer
    :rtype: int
    """

    results: Dict[int, int] = {}
    for position in range(len(data)):
        results[position] = np.sum([np.abs(value - position) for value in data])
    return min(results.values())


def part_two(data: List[int]) -> int:
    """Solve part two
    :param data: the input data

    :return: Part two answer
    :rtype: int
    """
    results: Dict[int, int] = {}
    for position in range(len(data)):
        ae = [np.abs(value - position) for value in data]
        results[position] = np.sum([np.sum(list(range(1, error + 1))) for error in ae])
    return min(results.values())


def main():
    """Main function"""
    logging.info("::: Loading data")
    data = get_data(day=DAY, year=YEAR)
    data = [int(x) for x in data.split(",")]

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
