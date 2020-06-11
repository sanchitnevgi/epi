from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from collections import namedtuple

def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    Subtree = namedtuple('Subtree', ['balanced', 'height'])
    
    def _height(node):
        if not node:
            return Subtree(True, -1)
        
        left = _height(node.left)

        if not left.balanced:
            return Subtree(False, 0)

        right = _height(node.right)

        return Subtree(
                all([right.balanced, abs(left.height - right.height) <= 1]), 
                max(left.height, right.height) + 1
            )
    
    root = _height(tree)
    
    return root.balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
