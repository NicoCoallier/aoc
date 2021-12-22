"""This will be automated in later version
"""
import logging

from typing import List

import numpy as np

from aoc.solutions.twenty_twentyone.constants import YEAR
from aocd import get_data
from aocd import submit


DAY: int = 3


def get_most_binary_common(data: List[int]) -> List[int]:
    """Generate a binary number from the most common element
    in a list of binary numbers.

    """
    average_values = np.where(
        np.average(data, axis=0) == 0.5, 1, np.average(data, axis=0)
    )
    most_common = [str(int(x)) for x in np.round(average_values)]
    return most_common


def get_least_binary_common(data: List[int]) -> List[int]:
    """Generate a binary number from the least common element
    in a list of binary numbers.

    """
    most_common = [str(int(x)) for x in np.round(1 - np.average(data, axis=0))]
    return most_common


def part_one(data: List[int]) -> int:
    """Solve part one
    :param data: the input data

    :return: Part one answer
    :rtype: int
    """
    # Simple mean and round we will get most common
    most_common = get_most_binary_common(data)
    less_common = ["0" if x == "1" else "1" for x in most_common]
    epsilon_rate = int("".join(most_common), 2)
    gamma_rate = int("".join(less_common), 2)
    power_consumption = gamma_rate * epsilon_rate
    return power_consumption


def part_two(data: List[int]) -> int:
    """Solve part two
    :param data: the input data

    :return: Part two answer
    :rtype: int
    """
    oxygen_generation = c02 = data.tolist()

    for i in range(len(oxygen_generation[0]) - 1):
        most_common = get_most_binary_common(oxygen_generation)
        less_common = get_least_binary_common(c02)

        if len(c02) > 1:
            c02 = list(filter(lambda x: str(x[i]) == str(less_common[i]), c02))
        if len(oxygen_generation) > 1:
            oxygen_generation = list(
                filter(lambda x: str(x[i]) == str(most_common[i]), oxygen_generation)
            )

    oxygen_generation = list(filter(lambda x: str(x[-1]) == "1", oxygen_generation))
    c02 = list(filter(lambda x: str(x[-1]) == "0", c02))

    oxygen_generation = int("".join([str(x) for x in oxygen_generation[0]]), 2)
    c02 = int("".join([str(x) for x in c02[0]]), 2)

    return c02 * oxygen_generation


def main():
    """Main function"""
    logging.info("::: Loading data")
    data = get_data(day=DAY, year=YEAR).split("\n")
    data = [list(x) for x in data]
    data = np.array([list(map(lambda x: int(x), l)) for l in data])

    logging.info("::: Solving part one...")
    a1 = part_one(data=data)
    logging.info("::: Submitting part one...")
    _ = submit(a1, part="a", day=DAY, year=YEAR)
    logging.info("::: Solving part two...")
    a2 = part_two(data=data)
    print(a2)
    logging.info("::: Submitting part two...")
    # _ = submit(a2, part="b", day=DAY, year=YEAR)
    logging.info("::: DONE")


if __name__ == "__main__":
    logging.basicConfig()
    logging.getLogger().setLevel(logging.INFO)
    main()
