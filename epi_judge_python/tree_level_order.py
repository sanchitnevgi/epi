from typing import List
from collections import deque, namedtuple
from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    result = []

    if not tree:
        return result
    
    curr_level_nodes = [tree]

    while curr_level_nodes:
        result.append([node.data for node in curr_level_nodes])
        curr_level_nodes = [
            child for node in curr_level_nodes for child in (node.left, node.right)  if child
        ]

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
