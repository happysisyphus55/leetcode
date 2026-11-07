from functools import reduce
from operator import xor

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # solution: if two numbers are same , then the bitwise xor of them would be 0
        # so the last remaining number would the unique number
        if len(nums) == 1:
            return nums[0]
        else:
            result = reduce(xor, nums)
            return result
