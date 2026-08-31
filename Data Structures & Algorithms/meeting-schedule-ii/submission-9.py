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

        start = sorted([interval.start for interval in intervals])
        end = sorted([interval.end for interval in intervals])

        count_in_progress = 0
        i = j = 0
        
        while i < len(start):
            if start[i] < end[j]:
                count_in_progress += 1
                i += 1
            else:
                count_in_progress -= 1
                j += 1
            max_count = max(max_count, count_in_progress)

        return max_count
