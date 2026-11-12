class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []

        for i in range(len(intervals)):
            # edge cases 
            
            # new interval is less than start internval 
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            #new interval goes after the current interval that we have 
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            # new interval is overlapping 
            else:
                newInterval = [
                    min(newInterval[0],intervals[i][0]),
                    max(newInterval[1],intervals[i][1]),
                ]
                # this new interval could still be overlapping so we dont append it yet 
        
        res.append(newInterval)
        return res 
