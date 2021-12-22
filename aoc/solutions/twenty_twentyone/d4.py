import logging
import re

from typing import Callable
from typing import Dict
from typing import List
from typing import Text
from typing import Tuple

import numpy as np

from aoc.solutions.twenty_twentyone.constants import YEAR
from aocd import get_data
from aocd import submit


DAY: int = 4


def bingo_loop(grids: Dict, numbers: List, exit_condition: Callable) -> Tuple:
    """Repeated part of both part (Bingo loop)
    :param grids: Grids dict and mask
    :param numbers: Bingo numbers being called
    :param exit_condition: The exit function

    :return: Unmarked values and last_number called
    :rtype: Tuple
    """
    stop = False
    gridnames = list(grids.keys())
    for n in numbers:
        for key, values in grids.items():
            if key in gridnames:
                result = np.where(values["grid"] == n)
                indexes = list(zip(result[0], result[1]))
                for index in indexes:
                    values["picked"][index[0], index[1]] = 1
                row_check = np.sum(values["picked"], axis=1)
                col_check = np.sum(values["picked"], axis=0)
                if 5.0 in row_check or 5.0 in col_check:
                    stop, unmarked, last_number, gridnames = exit_condition(
                        stop, key, values, n, gridnames
                    )
        if stop:
            break
    return unmarked, last_number


def part_one(grids: Dict, numbers: List) -> int:
    """Solve part one
    :param grids: Grids dict and mask
    :param numbers: Bingo numbers being called

    :return: Part one answer
    :rtype: int
    """

    def end_part_one(stop, key, values, n, gridnames=None):
        unmarked = values["grid"][np.where(values["picked"] == 0)]
        stop = True
        return stop, unmarked, n, gridnames

    unmarked, last_number = bingo_loop(
        grids=grids, numbers=numbers, exit_condition=end_part_one
    )
    return np.sum(unmarked) * last_number


def part_two(grids: Dict, numbers: List) -> int:
    """Solve part two
    :param grids: Grids dict and mask
    :param numbers: Bingo numbers being called

    :return: Part two answer
    :rtype: int
    """

    def end_part_two(stop, key, values, n, gridnames):
        if len(gridnames) > 1:
            gridnames.pop(gridnames.index(key))
            unmarked = None
        else:
            unmarked = values["grid"][np.where(values["picked"] == 0)]
            stop = True
        return stop, unmarked, n, gridnames

    unmarked, last_number = bingo_loop(
        grids=grids, numbers=numbers, exit_condition=end_part_two
    )
    return np.sum(unmarked) * last_number


def format_data(data: List) -> Tuple[Dict, List]:
    """ Format the data

    :param data: Input data

    :return: The bingo numbers called and the grids and mask \
    :rtype: Tuple[Dict,List]
    """
    numbers: List[int] = [int(x) for x in data[0].split(",")]
    grids: Dict[Text, np.array] = {}
    grid: List[int] = []
    for i, row in enumerate(data[1:]):
        if row == "":
            if len(grid) > 1:
                grids[str(i)] = {}
                grids[str(i)]["grid"] = np.array(grid, dtype=np.int64).reshape(5, 5)
                grids[str(i)]["picked"] = np.zeros((5, 5))
            grid = []
        else:
            grid.append(re.sub(" +", " ", row).split(" ")[-5:])
    return grids, numbers


def main():
    """Main function"""
    logging.info("::: Loading data")
    data = get_data(day=DAY, year=YEAR).split("\n")
    grids, numbers = format_data(data)

    logging.info("::: Solving part one...")
    a1 = part_one(grids=grids, numbers=numbers)
    logging.info("::: Submitting part one...")
    _ = submit(a1, part="a", day=DAY, year=YEAR)
    logging.info("::: Solving part two...")
    a2 = part_two(grids=grids, numbers=numbers)
    logging.info("::: Submitting part two...")
    _ = submit(a2, part="b", day=DAY, year=YEAR)
    logging.info("::: DONE")


if __name__ == "__main__":
    logging.basicConfig()
    logging.getLogger().setLevel(logging.INFO)
    main()
