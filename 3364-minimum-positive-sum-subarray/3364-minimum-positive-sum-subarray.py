class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        # sliding window problem 
        ans = math.inf
        
        # Check all possible window sizes from l to r
        for window_size in range(l, r + 1):
            window_sum = sum(nums[:window_size])
            if window_sum > 0:
                ans = min(ans, window_sum)
                
            # Slide the window across the array
            for i in range(window_size, len(nums)):
                window_sum -= nums[i - window_size]
                window_sum += nums[i]
                if window_sum > 0:
                    ans = min(ans, window_sum)
                    
        return -1 if ans == math.inf else ans
        