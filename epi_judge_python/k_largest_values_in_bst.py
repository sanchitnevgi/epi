from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    result = []
    
    def traverse(node):
        if not node or len(result) == k:
            return
        traverse(node.right)
        if len(result) < k:
            result.append(node.data)
            traverse(node.left)

    traverse(tree)

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
