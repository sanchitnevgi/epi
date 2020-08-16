from list_node import ListNode
from test_framework import generic_test


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    def reverse_list(head: ListNode) -> ListNode:
        dummy = ListNode(0)
        while head:
            dummy.next, head.next, head = head, dummy.next, head.next
        return dummy.next

    # Find the half point
    slow = fast = L
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    first_half_iter, second_half_iter = L, reverse_list(slow)

    while first_half_iter and second_half_iter:
        if first_half_iter.data != second_half_iter.data:
            return False
        
        first_half_iter, second_half_iter = first_half_iter.next, second_half_iter.next
    
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
