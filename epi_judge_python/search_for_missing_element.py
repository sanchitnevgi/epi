import collections
from typing import List
import functools

from test_framework import generic_test
from test_framework.test_failure import PropertyName

DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
                                             ('duplicate', 'missing'))


def find_duplicate_missing(A: List[int]) -> DuplicateAndMissing:
    miss_xor_dup = functools.reduce(lambda v, i: v ^ i[0] ^ i[1], enumerate(A), 0)

    differ_bit, miss_or_dup = miss_xor_dup & (~(miss_xor_dup - 1)), 0

    for i, a in enumerate(A):
        if i & differ_bit:
            miss_or_dup ^= i
        if a & differ_bit:
            miss_or_dup ^= a

    miss_or_dup_xor = miss_xor_dup ^ miss_or_dup

    return DuplicateAndMissing(miss_or_dup, miss_or_dup_xor) if miss_or_dup in A else DuplicateAndMissing(miss_or_dup_xor, miss_or_dup)


def res_printer(prop, value):
    def fmt(x):
        return 'duplicate: {}, missing: {}'.format(x[0], x[1]) if x else None

    return fmt(value) if prop in (PropertyName.EXPECTED,
                                  PropertyName.RESULT) else value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_for_missing_element.py',
                                       'find_missing_and_duplicate.tsv',
                                       find_duplicate_missing,
                                       res_printer=res_printer))
