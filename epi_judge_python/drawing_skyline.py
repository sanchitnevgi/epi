import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Rect = collections.namedtuple('Rect', ('left', 'right', 'height'))


def compute_skyline(buildings: List[Rect]) -> List[Rect]:
    min_left = min(building.left for building in buildings)
    max_right = max(building.right for building in buildings)

    heights = [0] * (max_right - min_left + 1)

    # Create skyline
    for building in buildings:
        for b_idx in range(building.left, building.right + 1):
            heights[b_idx - min_left] = max(heights[b_idx - min_left], building.height)
        
    # Merge skyline
    left = 0
    results = []
    for i in range(1, len(heights)):
        # Skyline changes, append the previous one
        if heights[i] != heights[i - 1]:
            results.append(Rect(min_left + left, i - 1 + min_left, heights[i - 1]))
            left = i

    return results + [Rect(left + min_left, max_right, heights[-1])]


@enable_executor_hook
def compute_skyline_wrapper(executor, buildings):
    buildings = [Rect(*x) for x in buildings]

    result = executor.run(functools.partial(compute_skyline, buildings))

    return [(x.left, x.right, x.height) for x in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('drawing_skyline.py',
                                       'drawing_skyline.tsv',
                                       compute_skyline_wrapper))
