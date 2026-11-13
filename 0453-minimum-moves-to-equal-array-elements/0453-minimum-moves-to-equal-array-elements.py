class Solution:
    def minMoves(self, nums: list[int]) -> int:
        nums.sort()
        count = 0 

        for num in nums:
            count += num - nums[0]
        
        return count

        