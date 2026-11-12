class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        #we have to take care of the fact that intervals thjat are growing would be added, and things which are lesser than even two of them would have to be removed

        # sort the arrays, use adjacent pairs and use the algo
        # o(n) + o(nlogn) -> o(nlogn)

        intervals.sort()

        res = 0 
        prevEnd =  intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                # = is the edge case, else use our previous end and set it to the new end value
                prevEnd = end 
            else:
                res += 1
                prevEnd = min(end,prevEnd)

        return res 