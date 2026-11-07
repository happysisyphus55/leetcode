# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from leetcode.neetcode_250.linked_list import ListNode


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:  # type: ignore
        temp = head
        cnt = 0
        while temp is not None:
            cnt += 1
            temp = temp.next

        middle_node = (cnt // 2) + 1
        temp = head
        while temp is not None:
            middle_node -= 1
            if middle_node == 0:
                break
            temp = temp.next
        return temp

    def middleNodeOptimal(self, head):
        # using fast and slow pointers
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow
