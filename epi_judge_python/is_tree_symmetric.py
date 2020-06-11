from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    if not tree:
        return True

    def check(node0, node1):
        if not node0 and  not node1:
            return True
        if not node0 or not node1 or node0.data != node1.data:
            return False
        
        left_symmetric = check(node0.left, node1.right)
        right_symmetric = check(node0.right, node1.left)

        return left_symmetric and right_symmetric

    return check(tree.left, tree.right)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
