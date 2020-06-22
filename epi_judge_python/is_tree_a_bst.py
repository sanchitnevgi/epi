from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from collections import namedtuple

Bounds = namedtuple('Bounds', ['lo', 'hi'])

def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    def is_bst(node, bounds: Bounds):
        if not node:
            return True
        if not (bounds.lo <= node.data <= bounds.hi):
            return False
        return (is_bst(node.left, Bounds(bounds.lo, node.data)) 
                and is_bst(node.right, Bounds(node.data, bounds.hi)))
    
    return is_bst(tree, Bounds(float('-inf'), float('inf')))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
