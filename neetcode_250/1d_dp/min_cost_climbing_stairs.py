from functools import cache
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        @cache
        def dfs(current_step):
            # calc min cost starting from current_step to reach the top.
            if current_step >= len(cost):
                return 0

            one_step = dfs(current_step + 1)
            two_steps = dfs(current_step + 2)

            return cost[current_step] + min(one_step, two_steps)

        # can start from either step 0 or step 1 , return the min
        start_from_zero = dfs(0)
        start_from_one = dfs(1)

        return min(start_from_zero, start_from_one)
