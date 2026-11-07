class Solution:
    def containsDuplicate(self, nums):
        item_set = set(nums)
        if len(item_set) == len(nums):
            return False
        return True
