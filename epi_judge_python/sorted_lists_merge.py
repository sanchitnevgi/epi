from typing import Optional
import collections
import heapq

from list_node import ListNode
from test_framework import generic_test

def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    Item = collections.namedtuple('Item', ['val', 'list_idx'])
    head, curr = None, None
    lists = [L1, L2]
    
    if not lists:
        return None

    # Initialize heap, assume at least 1 item in a list
    candidate_heap = [ Item(node.data, list_idx) for list_idx, node in enumerate(lists) if node ]
    heapq.heapify(candidate_heap)

    while candidate_heap:
        # Get the minium value from heap and add to result
        min_item = heapq.heappop(candidate_heap)
        
        if not head:
            curr = ListNode(min_item.val)
            head = curr
        else:
            curr.next = ListNode(min_item.val)
            curr = curr.next

        lists[min_item.list_idx] = lists[min_item.list_idx].next
        next_item = lists[min_item.list_idx]
        
        # Check if list is exhausted
        if next_item is None:
            continue

        # Else add the next value from list to result
        item = Item(next_item.data, min_item.list_idx)
        heapq.heappush(candidate_heap, item)

    return head

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
