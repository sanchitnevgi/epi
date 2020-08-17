from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def remove_duplicates(L: ListNode) -> Optional[ListNode]:
    it = L

    while it:
        next_distinct = it.next
        while next_distinct and next_distinct.data == it.data:
            next_distinct = next_distinct.next
        it.next = next_distinct
        it = it.next

    return L

def remove_duplicates_mine(L: ListNode) -> Optional[ListNode]:
    def del_node(node):
        next_node_data = node.next.data
        node.next = node.next.next
        node.data = next_node_data
    
    if L is None:
        return L

    node_iter = L
    while node_iter.next:
        # If duplicate node
        if node_iter.data == node_iter.next.data:
            del_node(node_iter)
        else:
            node_iter = node_iter.next

    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'remove_duplicates_from_sorted_list.py',
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
