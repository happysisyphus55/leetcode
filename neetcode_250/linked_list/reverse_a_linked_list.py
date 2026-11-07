class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # if not reversed, then return the reversed list
        if not head:
            return None

        new_head = head
        if new_head.next:
            new_head = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return new_head

    def reverse_list_optimal(self, head):
        temp = head
        prev = None
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front

        return prev
