class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #creates an empty list to store the final answer
        res = []
        #Loops through all the intervals.
        for i in range(len(intervals)):
            #Checks if the new interval ends before the current interval starts
            if newInterval[1] < intervals[i][0]:
                #Adds the new interval to the result list.
                res.append(newInterval)
                #Returns the result along with all the remaining intervals.
                return res + intervals[i:]
                #Checks if the new interval starts after the current interval ends.
            elif newInterval[0] > intervals[i][1]:
                #Adds the current interval to the result because there is no overlap.
                res.append(intervals[i])
            #Runs when the new interval overlaps with the current interval.
            else:
                #Creates a merged interval- Chooses the smaller starting point of the two intervals & the larger ending point of the two intervals.
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        #Adds the final merged interval to the result list.
        res.append(newInterval)
        #Returns the completed list of intervals.
        return res

    #TC: O(n)
    #SC: O(n)

        