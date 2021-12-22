import logging

from typing import Dict
from typing import List
from typing import Text

import numpy as np

from aoc.solutions.twenty_twentyone.constants import YEAR
from aocd import get_data
from aocd import submit


DAY: int = 2


def part_one(directions: List[Text], values: List[int]) -> int:
    """Solve part one
        forward X increases the horizontal position by X units.
        down X increases the depth by X units.
        up X decreases the depth by X units.

    :param directions: List of directions
    :param values: List of values in which to move in a direction

    :return: Part one answer
    :rtype: int
    """
    position: Dict[Text, int] = {"depth": 0, "horizontal": 0}
    for d, v in zip(directions, values):
        if d == "forward":
            position["horizontal"] += v
        elif d == "down":
            position["depth"] += v
        elif d == "up":
            position["depth"] -= v
        else:
            pass

    return int(position["depth"] * position["horizontal"])


def part_two(directions: List[Text], values: List[int]) -> int:
    """Solve part two
    :param directions: List of directions
    :param values: List of values in which to move in a direction


    :return: Part two answer
    :rtype: int
    """
    position: Dict[Text, int] = {"depth": 0, "horizontal": 0, "aim": 0}
    for d, v in zip(directions, values):
        if d == "forward":
            position["horizontal"] += v
            position["depth"] += v * position["aim"]
        elif d == "down":
            position["aim"] += v
        elif d == "up":
            position["aim"] -= v
        else:
            pass
    return int(position["depth"] * position["horizontal"])


def main():
    """Main function"""
    logging.info("::: Loading data")
    data = get_data(day=DAY, year=YEAR).split("\n")
    # Split direction and values
    data = [x.split(" ") for x in data]
    values = [int(x[1]) for x in data]
    directions = [x[0] for x in data]

    logging.info("::: Solving part one...")
    a1 = part_one(directions=directions, values=values)
    logging.info("::: Submitting part one...")
    _ = submit(a1, part="a", day=DAY, year=YEAR)
    logging.info("::: Solving part two...")
    a2 = part_two(directions=directions, values=values)
    logging.info("::: Submitting part two...")
    _ = submit(a2, part="b", day=DAY, year=YEAR)
    logging.info("::: DONE")


if __name__ == "__main__":
    logging.basicConfig()
    logging.getLogger().setLevel(logging.INFO)
    main()
