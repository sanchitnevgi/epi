from typing import Optional

from bst_node import BstNode
from test_framework import generic_test


def find_first_greater_than_k(tree: BstNode, k: int) -> Optional[BstNode]:
    tree, best_candiate = tree, None

    while tree:
        # Found a candidate, Left tree could have better candidate
        if k < tree.data:
            best_candiate, tree = tree, tree.left
        # No candidate found, search right tree
        else: # k >= tree.data
            tree = tree.right

    return best_candiate


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'search_first_greater_value_in_bst.py',
            'search_first_greater_value_in_bst.tsv',
            find_first_greater_than_k_wrapper))
