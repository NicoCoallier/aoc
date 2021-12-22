import logging

from collections import Counter
from collections import OrderedDict
from typing import List

import numpy as np

from aoc.solutions.twenty_twentyone.constants import YEAR
from aocd import get_data
from aocd import submit
from tqdm import trange


DAY: int = 6


def format_data(data: List[int]) -> List[int]:
    return np.array(list(map(lambda x: int(x), data.split(","))))


def fish_growth_model(data, number_of_days):
    t = trange(number_of_days, desc="population_size")
    for _ in t:
        cond = np.where(data == 0)[0]
        data -= 1
        data[cond] = 6
        to_add = np.array([8] * len(cond))
        data = np.concatenate([data, to_add])
        t.set_description(f"N (population size={len(data)})")
    return data


def part_one(data: List[int]) -> int:
    """Solve part one
    :param data: the input data

    :return: Part one answer
    :rtype: int
    """

    number_of_days = 80
    data = fish_growth_model(data, number_of_days)
    return len(data)


def part_two(data: List[int]) -> int:
    """Solve part two
    :param data: the input data

    :return: Part two answer
    :rtype: int
    """
    number_of_days = 256

    # Need to optimize
    # data = fish_growth_model(data, number_of_days)
    # Let's keep only a counts of the fish
    fish_counts = dict(Counter(data))
    fish_counts = {k: fish_counts.get(k, 0) for k in range(9)}
    for _ in range(number_of_days):
        zeroes = fish_counts[0]
        fish_counts[0] = 0
        for index in range(1, len(fish_counts)):
            fish_counts[index - 1] += fish_counts[index]
            fish_counts[index] = 0
        fish_counts[6] += zeroes
        fish_counts[8] = zeroes
    return sum(fish_counts.values())


def main():
    """Main function"""
    logging.info("::: Loading data")
    data = get_data(day=DAY, year=YEAR)
    part_one_data = format_data(data)

    logging.info("::: Solving part one...")
    a1 = part_one(data=part_one_data)
    logging.info("::: Submitting part one...")
    _ = submit(a1, part="a", day=DAY, year=YEAR)
    logging.info("::: Solving part two...")
    part_two_data = format_data(data)
    a2 = part_two(data=part_two_data)
    logging.info("::: Submitting part two...")
    _ = submit(a2, part="b", day=DAY, year=YEAR)
    logging.info("::: DONE")


if __name__ == "__main__":
    logging.basicConfig()
    logging.getLogger().setLevel(logging.INFO)
    main()
