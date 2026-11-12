class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        inc = 1
        dec = 1
        longest = 1

        for i in range(1,len(nums)):
            # strictly increasing case 
            if nums[i] > nums[i-1]:
                inc += 1
                dec = 1
            
            elif nums[i] < nums[i-1]:
                dec += 1
                inc = 1
            
            else:
                inc = 1
                dec = 1
        
            # update the longest 
            longest = max(longest,inc,dec)
        
        return longest

        