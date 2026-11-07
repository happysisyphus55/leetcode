# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        length_of_ll = 0

        if temp is None:
            return None

        while temp is not None:
            length_of_ll += 1
            temp = temp.next

        head_remove_posn = length_of_ll - n

        if head_remove_posn == 0:
            return head.next
        else:
            temp = head

            while head_remove_posn - 1 != 0:
                temp = temp.next
                head_remove_posn -= 1

            curr_node = temp
            node_to_remove = temp.next
            next_node_to_remove = temp.next.next

            curr_node.next = next_node_to_remove
            node_to_remove.next = None

            return head
