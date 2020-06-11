import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    
    def get_height(node):
        height = -1
        while node:
            node = node.parent
            height += 1
        return height
    # Get the height of node0
    node0_ht = get_height(node0)
    # Get the height of node1
    node1_ht = get_height(node1)

    # Set node0 as the larger height
    if node0_ht < node1_ht:
        node0, node1 = node1, node0
        node0_ht, node1_ht = node1_ht, node0_ht

    # Traverse node0 up till same height
    while node0_ht != node1_ht:
        node0 = node0.parent
        node0_ht -= 1

    # Move node0 and node1 together
    while node0 != node1:
        node0 = node0.parent
        node1 = node1.parent

    return node0


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor_with_parent.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
