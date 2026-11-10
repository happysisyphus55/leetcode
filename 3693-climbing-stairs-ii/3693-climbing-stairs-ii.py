class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # shifts from a counting problem to an optimization problem 

        # dp[j] stores the min cost to reach step j 
        # init with infinity, except the start step
        dp = [float('inf')] * (n+1)
        dp[0] = 0

        for j in range(1,n+1):
            landing_cost = costs[j-1]
            
            # because from a point we can only move to i+1, i+2 and i+3 points 
            for i in range(max(0, j - 3), j):
                jump_effort = (j - i) ** 2
            
                # The transition equation
                dp[j] = min(dp[j], dp[i] + landing_cost + jump_effort)

        return dp[n]