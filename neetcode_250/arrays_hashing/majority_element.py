from collections import Counter


class Solution:
    def majorityElement(self, nums):
        counts = Counter(nums)
        # n = len(nums)

        candidate, count = counts.most_common(1)[0]
        return candidate
