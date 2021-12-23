import itertools
import logging

from typing import Dict
from typing import List
from typing import Text

import numpy as np

from aoc.solutions.twenty_twentyone.constants import YEAR
from aocd import get_data
from aocd import submit


DAY: int = 8

mapper = {
    "0": "abcefg",  # 6
    "1": "cf",  # 2
    "2": "acdeg",  # 5
    "3": "acdfg",  # 5
    "4": "bcdf",  # 4
    "5": "abdfg",  # 5
    "6": "abdefg",  # 6
    "7": "acf",  # 3
    "8": "abcdefg",  # 7
    "9": "abcdfg",  # 6
}


def format_data(data: List[int]) -> List[int]:
    input = [t.split(" | ")[0].lstrip() for t in data.split("\n")]
    input = [t.split() for t in input]
    output = [t.split(" | ")[1].lstrip() for t in data.split("\n")]
    output = [t.split() for t in output]
    return input, output


def part_one(data: List[int]) -> int:
    """Solve part one
    :param data: the input data

    :return: Part one answer
    :rtype: int
    """
    unique_mapper: Dict[Text, Text] = {
        "1": "cf",
        "4": "bcdf",
        "7": "acf",
        "8": "abcdefg",
    }
    results: int = 0
    for t in data:
        for k, v in unique_mapper.items():
            for seg in t:
                if len(seg) == len(v):
                    results += 1
    return results


def part_two(input: List[int], output: List[int]) -> int:
    """Solve part two
    :param input: the input data
    :param output: output segment

    :return: Part two answer
    :rtype: int
    """
    results: int = 0
    reverse_mapper = {v: k for k, v in mapper.items()}

    for inp, out in zip(input, output):
        for permutation in itertools.permutations("abcdefg"):
            to = str.maketrans("abcdefg", "".join(permutation))
            inp_prime = ["".join(sorted(value.translate(to))) for value in inp]
            out_prime = ["".join(sorted(value.translate(to))) for value in out]
            if all(value in reverse_mapper for value in inp_prime):
                results += int("".join(reverse_mapper[value] for value in out_prime))
                break

    return results


def main():
    """Main function"""
    logging.info("::: Loading data")
    data = get_data(day=DAY, year=YEAR)
    input, output = format_data(data)

    logging.info("::: Solving part one...")
    a1 = part_one(data=output)
    logging.info("::: Submitting part one...")
    _ = submit(a1, part="a", day=DAY, year=YEAR)
    logging.info("::: Solving part two...")
    a2 = part_two(input=input, output=output)
    logging.info("::: Submitting part two...")
    _ = submit(a2, part="b", day=DAY, year=YEAR)
    logging.info("::: DONE")


if __name__ == "__main__":
    logging.basicConfig()
    logging.getLogger().setLevel(logging.INFO)
    main()
