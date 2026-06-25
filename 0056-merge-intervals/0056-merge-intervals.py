class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #Sort the intervals based on their starting number
        intervals.sort(key=lambda pair: pair[0])
        #Put the first interval into the result list.
        output = [intervals[0]]

        #Go through each interval one by one.
        for start, end in intervals:
            #Get the ending value of the last interval in the result list.
            lastEnd = output[-1][1]

            #Check if the current interval overlaps with the last interval.
            if start <= lastEnd:
                #Extend the last interval to the larger ending value.
                output[-1][1] = max(lastEnd, end)
            #If there is no overlap
            else:#Add the current interval as a new interval in the result list
                output.append([start, end])
        #Return the final list of merged intervals.
        return output
    #TC: O(nlogn)
    #SC: O(n)