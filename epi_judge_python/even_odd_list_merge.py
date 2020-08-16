from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    if not L:
        return L

    even_head, odd_head = ListNode(), ListNode()
    even_odd = [even_head, odd_head]
    node = L

    num = 0
    while node:
        pile = num % 2

        even_odd[pile].next = node
        even_odd[pile] = even_odd[pile].next
        node, num = node.next, num + 1
    
    even_odd[1].next = None # Important step    
    even_odd[0].next = odd_head.next

    return even_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
