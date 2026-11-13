from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0 
        cost = 0 

        # deque stores indices of running maximums in non-increasing order 
        # dq[0] is the index of he largest element in window 
        dq = deque()
        j = len(nums) - 1

        for i in range(len(nums) -1 ,-1,-1):
            num = nums[i]

            #merge smaller peaks into the new left element `num`
            while dq and nums[dq[-1]] < num:
                l = dq.pop()
                r = dq[-1] if dq else j + 1

                cost += (r-l) *( num - nums[l])

            dq.append(i)

            # shrink window from the right if operations exceed k 
            while cost > k :
                cost -= nums[dq[0]] - nums[j]
                if dq[0] == j:
                    dq.popleft()
                j -= 1

            # all subarays starting at i and ending at [i,j] are valid 
            ans += j - i + 1

        return ans         