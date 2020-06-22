from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test


def rebuild_bst_from_preorder(preorder_sequence):
    def reconstruct(lower_bound, upper_bound):
        if root_idx[0] == len(preorder_sequence):
            return None

        root = preorder_sequence[root_idx[0]]

        if not (lower_bound < root < upper_bound):
            return None
        
        root_idx[0] += 1

        left_subtree = reconstruct(lower_bound, root)
        right_subtree = reconstruct(root, upper_bound)

        return BstNode(root, left_subtree, right_subtree)
    
    root_idx = [0]
    return reconstruct(float('-inf'), float('inf'))

def rebuild_bst_from_preorder_slow(preorder_sequence: List[int]
                              ) -> Optional[BstNode]:
    def reconstruct(preorder_start, preorder_end):
        if preorder_start > preorder_end:
            return None
        
        root = preorder_sequence[preorder_start]

        # Find idx where val > root
        partition_idx = preorder_start
        for i in range(preorder_start + 1, preorder_end + 1):
            if preorder_sequence[i] < root:
                partition_idx = i
            else:
                break
        
        return BstNode(
            root,
            reconstruct(preorder_start + 1, partition_idx),
            reconstruct(partition_idx + 1, preorder_end)
        )

    return reconstruct(0, len(preorder_sequence) - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('bst_from_preorder.py',
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
