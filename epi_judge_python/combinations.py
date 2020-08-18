from typing import List

from test_framework import generic_test, test_utils


def combinations(n: int, k: int) -> List[List[int]]:
    def choose(start_idx, left_to_choose):
        # Nothing left to choose
        if left_to_choose == 0:
            result.append(partial.copy())
            return
        # Reached end of list but still left to choose, do nothing
        if start_idx == n:
            return

        # 2 cases, choose start_idx or dont
        partial.append(start_idx + 1)
        choose(start_idx + 1, left_to_choose - 1)

        partial.pop()
        choose(start_idx + 1, left_to_choose)
    
    result, partial = [], []
    choose(0, k)

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'combinations.py',
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))
