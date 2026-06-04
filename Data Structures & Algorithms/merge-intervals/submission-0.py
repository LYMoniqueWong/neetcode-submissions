class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n, i = len(intervals), 0
        res = []
        while i+1 < n:
            if intervals[i][1] < intervals[i+1][0]:
                res.append(intervals[i])
                i += 1
            elif intervals[i][1] >= intervals[i+1][0] and intervals[i+1][1] >= intervals[i][0]:
                newIn = [min(intervals[i+1][0], intervals[i][0]), max(intervals[i+1][1], intervals[i][1])]
                intervals[i+1] = newIn
                i += 1
        res.append(intervals[i])
        return res