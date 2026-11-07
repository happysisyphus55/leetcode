class ListNode:
    def __init__(self, val, next) -> None:
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head):

        def rec(root, curr):
            if not curr:
                return root

            root = rec(root, curr.next)
            if not root:
                return None

            tmp = None
            if root == curr or root.next == curr:
                curr.next = None
            else:
                tmp = root.next
                root.next = curr
                curr.next = tmp
            return tmp

        head = rec(head, head.next)
