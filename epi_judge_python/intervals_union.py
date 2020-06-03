import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

Interval = collections.namedtuple('Interval', ('left', 'right'))


def union_of_intervals(intervals: List[Interval]) -> List[Interval]:
    if not intervals:
        return []

    # Sort by the left endpoint and prefer closed intervals
    intervals.sort(key=lambda i: (i.left.val, not i.left.is_closed))
    merged = [intervals[0]]

    for left, right in intervals[1:]:
        # When empty list or the next interval starts strictly after the previous ends
        if (left.val < merged[-1].right.val
            or (left.val == merged[-1].right.val and (left.is_closed or merged[-1].right.is_closed))):
            if right.val > merged[-1].right.val or (right.val == merged[-1].right.val and right.is_closed):
                merged[-1] = Interval(merged[-1].left, right)
        else:
            merged.append(Interval(left, right))

    return merged

@enable_executor_hook
def union_of_intervals_wrapper(executor, intervals):
    intervals = [
        Interval(Endpoint(x[1], x[0]), Endpoint(x[3], x[2])) for x in intervals
    ]

    result = executor.run(functools.partial(union_of_intervals, intervals))

    return [(i.left.val, i.left.is_closed, i.right.val, i.right.is_closed)
            for i in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intervals_union.py',
                                       'intervals_union.tsv',
                                       union_of_intervals_wrapper))
