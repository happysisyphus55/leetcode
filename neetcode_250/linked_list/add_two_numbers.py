# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        temp1 = l1
        temp2 = l2

        while temp1 or temp2 or carry:
            if temp1:
                val1 = temp1.val
            else:
                val1 = 0

            if temp2:
                val2 = temp2.val
            else:
                val2 = 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            # create the new node and link it
            current.next = ListNode(digit)
            current = current.next

            if temp1:
                temp1 = temp1.next
            if temp2:
                temp2 = temp2.next

        return dummy.next
