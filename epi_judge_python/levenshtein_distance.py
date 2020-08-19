from test_framework import generic_test


def levenshtein_distance(A: str, B: str) -> int:
    edits = [ [0] * (len(B) + 1) for _ in range(len(A) + 1) ]
    for i in range(1, len(A) + 1):
        edits[i][0] = i
    for j in range(1, len(B) + 1):
        edits[0][j] = j
    
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                edits[i][j] = edits[i - 1][j - 1]
            else:
                edits[i][j] = min(edits[i - 1][j], edits[i][j - 1], edits[i - 1][j - 1]) + 1
    return edits[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
