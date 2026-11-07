from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashMap = Counter(nums)
        cutoff = len(nums) // 3
        return [num for num, count in hashMap.items() if count > cutoff]


# basically we need to sort by inverted hasmap clears cutoff or not
