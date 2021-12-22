"""This will be automated in later version
"""
import logging

from typing import List

import numpy as np

from aoc.solutions.twenty_twentyone.constants import YEAR
from aocd import get_data
from aocd import submit


DAY: int = 5


def part_one(data: List[int]) -> int:
    """Solve part one
    :param data: the input data

    :return: Part one answer
    :rtype: int
    """
    maps = np.zeros((1000, 1000))
    for i, t in enumerate(data):
        x, y = t[0].split(",")
        x, y = int(x), int(y)
        x2, y2 = t[1].split(",")
        x2, y2 = int(x2), int(y2)
        # No diag
        if x2 == x:
            lenght = (
                range(y, y2 + 1) if y < y2 else range(y, y2 - 1, -1)
            )  # Python is not inclusive
            maps[x, lenght] += 1
        elif y2 == y:
            lenght = range(x, x2 + 1) if x < x2 else range(x, x2 - 1, -1)
            maps[lenght, y] += 1
        else:
            pass

    return len(np.where(maps > 1)[0])


def part_two(data: List[int]) -> int:
    """Solve part two
    :param data: the input data

    :return: Part two answer
    :rtype: int
    """
    maps = np.zeros((1000, 1000))
    for i, t in enumerate(data):
        x, y = t[0].split(",")
        x, y = int(x), int(y)
        x2, y2 = t[1].split(",")
        x2, y2 = int(x2), int(y2)
        if x2 == x:
            lenght = (
                range(y, y2 + 1) if y < y2 else range(y, y2 - 1, -1)
            )  # Python is not inclusive
            maps[x, lenght] += 1
        elif y2 == y:
            lenght = range(x, x2 + 1) if x < x2 else range(x, x2 - 1, -1)
            maps[lenght, y] += 1
        else:
            x_lenght = range(x, x2 + 1) if x < x2 else range(x, x2 - 1, -1)
            y_lenght = range(y, y2 + 1) if y < y2 else range(y, y2 - 1, -1)
            maps[x_lenght, y_lenght] += 1
    return len(np.where(maps > 1)[0])


def main():
    """Main function"""
    logging.info("::: Loading data")
    data = get_data(day=DAY, year=YEAR)

    data = list(map(lambda x: x.split("->"), data.split("\n")))
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
