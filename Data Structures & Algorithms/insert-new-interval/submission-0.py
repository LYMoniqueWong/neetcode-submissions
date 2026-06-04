class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        res = []
        # add all intervals before new to res
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        # merge overlapping intervals into newInterval
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        # add newInterval
        res.append(newInterval)
        # add all intervals after new to res
        while i < n and intervals[i][0] > newInterval[1]:
            res.append(intervals[i])
            i += 1
        return res
