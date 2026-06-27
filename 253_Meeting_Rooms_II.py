"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #Creates an empty list to store all meeting start and end times.
        time = []
        #Goes through each meeting one by one.
        for i in intervals:
            #Adds the meeting's start time with +1 to show a room is needed.
            time.append((i.start, 1))
            #Adds the meeting's end time with -1 to show a room is freed.
            time.append((i.end, -1))
        #Sorts all times by time first, and if times are equal, processes ending meetings before starting meetings.
        time.sort(key=lambda x: (x[0], x[1]))

        #Sets both the maximum rooms needed (res) and current rooms in use (count) to 0.
        res = count = 0
        #Goes through every start and end event in order.
        for t in time:
            #Updates the number of rooms in use by adding +1 for a start or -1 for an end.
            count += t[1]
            #Keeps track of the highest number of rooms used at the same time.
            res = max(res, count)
        #Returns the minimum number of meeting rooms required.
        return res
    
    #TC: O(nlogn)
    #SC: O(n)