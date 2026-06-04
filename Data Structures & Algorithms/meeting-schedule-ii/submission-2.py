"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:   return 0
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        p1, p2 = 0, 0
        res, count = 0, 0
        # max # of overlapping intervals at a point of time
        while p1 < len(start):
            if start[p1] < end[p2]:
                count += 1
                p1 += 1
                res = max(res, count)
            else:
                count -= 1
                p2 += 1
        return res

        