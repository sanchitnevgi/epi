from typing import List

from test_framework import generic_test, test_utils


def permutations(A: List[int]) -> List[List[int]]:
    # Generates all permutations starting from position i
    def helper(i):
        # Only 1 choice
        if i == len(A) - 1:
            result.append(A.copy())
        
        for j in range(i, len(A)):
            # Swap the ith and jth position, since we are fixing j and finding all permutations starting with A[j]
            A[i], A[j] = A[j], A[i]
            
            helper(i + 1)

            # Move the ith and jth position back to continue the recursion
            A[i], A[j] = A[j], A[i]
    
    result = []
    
    helper(0)

    return result

permutations([1, 2, 3])

if __name__ == '__main__':
    pass
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
