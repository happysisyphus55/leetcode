class Solution:
    def hasCycle(self, head):
        ## using the fast and slow pointer approach
        # slow moves one step at a time
        # fast moves two steps at a time
        #
        # if the list has a cycle , the fast pointer will eventually "lap" the slow pointer
        # meaning they will meet at some node isnide the cycle.
        # if the list has no cycle, the fast pointer will reach the end and the loop stops.
        #
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False

    def hasCycleEfficient(self, head):
        # using a set to maintian the order and make it fast
        seen = set()
        curr = head

        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next

        return False

    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        # using a hashmap
        map_p = {}
        temp = head

        while temp is not None:
            result = map_p.get(temp, False)
            if result == True:
                return True
            map_p[temp] = True
            temp = temp.next
        return False
