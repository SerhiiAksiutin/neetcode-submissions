"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    # [(0,30),(5,10),(15,20)]

    # from 0 to 30
    # from 5 to 10
    # from 15 to 20
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                if intervals[i].start < intervals[j].end and intervals[i].end > intervals[j].start:
                    return False
        return True


