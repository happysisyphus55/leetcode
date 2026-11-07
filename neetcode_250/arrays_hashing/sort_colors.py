from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # this is like dutch national flag problem
        # 0 -> red , 1 -> white , 2 -> blue
        count_0, count_1, count_2 = 0, 0, 0

        for i in nums:
            if i == 0:
                count_0 += 1
            elif i == 1:
                count_1 += 1
            elif i == 2:
                count_2 += 1

        counter = 0
        while count_0 > 0:
            nums[counter] = 0
            counter += 1
            count_0 -= 1

        while count_1 > 0:
            nums[counter] = 1
            counter += 1
            count_1 -= 1

        while count_2 > 0:
            nums[counter] = 2
            counter += 1
            count_2 -= 1
