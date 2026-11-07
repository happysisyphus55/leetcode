import heapq


class Solution:
    def lastStoneWeight(self, stones):
        # given an array of integers stones , where we have to mash stones
        # if x == y , both stones are destroyed
        # if x != y , the stone of weight x is destroyed and the stone
        # of weight y has nwe weight y - x
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])
