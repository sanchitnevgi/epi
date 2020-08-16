from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    # 2 pointers
    head = k_ahead = L
    for _ in range(k):
        k_ahead = k_ahead.next

    prev = None
    while k_ahead:
        prev, head, k_ahead = head, head.next, k_ahead.next
    
    if not prev:
        return L.next
        
    # Delete head node
    prev.next = head.next
    
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
