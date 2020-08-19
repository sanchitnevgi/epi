import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    values = [[0] * (capacity + 1) for _ in range(len(items) + 1)]

    for item in range(1, len(items) + 1):
        for cap in range(1, capacity + 1):
            capacity_minus_item = cap - items[item - 1].weight

            values[item][cap] = max(
                # Not considering the current item
                values[item - 1][cap],
                # Considering the current item, adding its value
                (values[item - 1][capacity_minus_item] + items[item - 1].value) if capacity_minus_item >= 0 else 0
            )

    return values[-1][-1]


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))
