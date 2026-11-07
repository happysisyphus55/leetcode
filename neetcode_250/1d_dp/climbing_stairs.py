class Solution:
    def countWaysRec(self, n, dp):
        # base case
        if n == 0:
            return 1
        if n == 1:
            return 1

        # if the result for this subproblem is already computed then return it
        if dp[n] != -1:
            return dp[n]

        dp[n] = self.countWaysRec(n - 1, dp) + self.countWaysRec(n - 2, dp)
        return dp[n]

    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)
        return self.countWaysRec(n, dp)
