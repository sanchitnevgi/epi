from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
    if L is None:
        return L
    dummy = node_iter = ListNode(0, L)
    # Find the k+1 th last node
    for _ in range(k):
        node_iter = node_iter.next
    
    head = node_iter.next
    node_iter.next = None

    end_node = head
    while end_node.next:
        end_node = end_node.next

    end_node.next = L
    
    return head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('list_cyclic_right_shift.py',
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
