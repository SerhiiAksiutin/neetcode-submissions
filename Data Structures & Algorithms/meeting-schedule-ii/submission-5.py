"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        max_count = 0
        if len(intervals) == 1:
            return max_count + 1
        elif len(intervals) == 0:
            return max_count

        start = sorted([interval.start for interval in intervals])
        end = sorted([interval.end for interval in intervals])
        print(start + end)
        count_in_porogress = 0
        i = j = 0
        
        while i < len(start):
            if start[i] < end[j]:
                count_in_porogress += 1
                i += 1
            else:
                count_in_porogress -= 1
                j += 1
            max_count = max(max_count, count_in_porogress)

        return max_count
