import collections
import functools
import heapq
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events(A: List[Event]) -> int:
    # Sort by starting times
    A.sort()

    ending_times = []
    
    for start_time, end_time in A:
        if len(ending_times) == 0 or start_time <= ending_times[0]: # Add a new meeting room
            heapq.heappush(ending_times, end_time)
        else: # Can reuse meeting room
            heapq.heapreplace(ending_times, end_time)

    return len(ending_times)


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
