from typing import Iterator, List
from collections import namedtuple

from test_framework import generic_test


def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    buildings = []
    Building = namedtuple('Building', ['idx', 'height'])

    for idx, height in enumerate(sequence):
        while buildings and buildings[-1].height <= height:
            buildings.pop()
        buildings.append(Building(idx, height))
    return [building.idx for building in reversed(buildings)]


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sunset_view.py', 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
