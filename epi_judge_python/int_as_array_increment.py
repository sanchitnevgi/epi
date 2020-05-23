from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            return A
        
        A[i] = 0
        A[i - 1] += 1
    
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A

# Variant
def bin_add(s, t):
    # s is the smaller array
    if len(s) > len(t):
        s, t = t, s

    carry = 0
    for i in range(1, len(s) + 1):
        t[-i] = s[-i] + t[-i] + carry
        if t[-i] > 1:
            t[-i], carry = t[-i] % 2, 1
    
    for i in range(len(t) - len(s), -1, -1):
        t[i] = t[i] + carry
        if t[i] > 1:
            t[i], carry = 0, 1
        else:
            return t
    
    if carry:
        t.insert(0, 1)
    return t

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
