# given two lists,merge them


class Solution:
    def mergeTwoLists(self, list1, list2):
        # if the first list1 is not present ,return list2
        # similarly the other way
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            # iterate to the next
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
