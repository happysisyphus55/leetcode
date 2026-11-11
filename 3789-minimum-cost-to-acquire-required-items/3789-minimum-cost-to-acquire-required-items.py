

class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # strategy 1 
        option1 = need1 * cost1 + need2 * cost2

        # strategy 2 
        option2 = costBoth * max(need1,need2)

        #strategy 3 mix both itme with indiv items for the remaining 
        mn = min(need1,need2)
        option3 = costBoth * mn + (need1 - mn) * cost1 + (need2 - mn) * cost2

        return min(option1,min(option2,option3))
        