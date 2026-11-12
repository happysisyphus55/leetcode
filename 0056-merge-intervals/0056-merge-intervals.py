class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # think of them in the number line and then think how will we merge each interval
        #sort and then we can start merging  start and iterate through one and check if the current last overlap with the next , then merge otherwise we dont do anything

        # TC: O(nlogn) -> n -> number of intervals given 

        intervals.sort(key= lambda i : i[0]) # sort by the start value 
        output = [intervals[0]]

        for start,end in intervals[1:]:
            # overlapping with the most recent interval check
            lastEnd = output[-1][1]

            if start <= lastEnd:
                # they are overlapping , so we merge them 
                output[-1][1] = max(lastEnd,end)
            # [1,5], [7,8] = [1,5], [7,8]
            else:
                output.append([start,end])

        return output



        