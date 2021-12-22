from typing import List

import numpy as np


def sliding_sum(data: List[int], window_length: int):
    """Calculate a sliding sum
    :param data: Input data
    :param window_length: Lenght of the window

    :return: The new data sum on the window size
    :rtype: List[int]
    """
    indexes: List[List[int]] = []
    for i in range(len(data)):
        index: List[int] = []
        for w in range(window_length):
            new_i = i + w
            if new_i < len(data):
                index.append(new_i)
        indexes.append(index)

    array_data = np.array(data)
    return [np.sum(array_data[j]) for j in indexes]
