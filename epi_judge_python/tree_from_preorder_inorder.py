from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    # Compute the data to idx value for inorder for faster search                                      
    node_to_idx = { data: i for i, data in enumerate(inorder) }

    def reconstruct(preorder_start, preorder_end, inorder_start, inorder_end):
        if preorder_end <= preorder_start or inorder_end <= inorder_start:
            return None
        
        root_inorder_idx = node_to_idx[preorder[preorder_start]]
        left_subree_size = root_inorder_idx - inorder_start

        return BinaryTreeNode(
            preorder[preorder_start],
            reconstruct(preorder_start + 1, preorder_start + 1 + left_subree_size, inorder_start, root_inorder_idx),
            reconstruct(preorder_start + 1 + left_subree_size, preorder_end, root_inorder_idx + 1, inorder_end)
        )

    return reconstruct(0, len(preorder), 0, len(inorder))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
