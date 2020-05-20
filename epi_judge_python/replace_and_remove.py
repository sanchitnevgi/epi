import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    copy_to, num_a = 0, 0
    # Remove all the b
    for i in range(size):
        if s[i] != 'b':
            s[copy_to] = s[i]
            copy_to += 1

        if s[i] == 'a':
            num_a += 1


    current_idx = copy_to - 1
    copy_to += num_a - 1
    final_size = copy_to + 1
    
    while current_idx >= 0:
        if s[current_idx] != 'a':
            s[copy_to] = s[current_idx]
            copy_to -= 1
        else:
            s[copy_to - 1:copy_to + 1] = 'dd'
            copy_to -= 2
        current_idx -= 1

    return final_size


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
