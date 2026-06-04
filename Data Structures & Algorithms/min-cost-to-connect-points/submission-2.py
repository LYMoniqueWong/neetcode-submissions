class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n, visit, res, heap = len(points), set(), 0, [(0, 0)] # heap: (weight, idx)
        while len(visit) < n:
            w, idx = heapq.heappop(heap)
            if idx in visit:
                continue
            visit.add(idx)
            res += w
            for i in range(n):
                if i not in visit:
                    dist = abs(points[idx][0] - points[i][0]) + abs(points[idx][1] - points[i][1])
                    heapq.heappush(heap, (dist, i))
        return res