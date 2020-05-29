from typing import List
from collections import defaultdict
from test_framework import generic_test, test_utils


def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    groups = defaultdict(list)

    for word in dictionary:
        groups[''.join(sorted(word))].append(word)

    result = [group for group in groups.values() if len(group) >= 2]

    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'anagrams.py',
            'anagrams.tsv',
            find_anagrams,
            comparator=test_utils.unordered_compare))
