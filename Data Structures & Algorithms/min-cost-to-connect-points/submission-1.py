class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:    return 0
        # create an adjacency list; (x, y): (weight, neibor [x1, y1])
        adj = defaultdict(list)
        def calCost(a, b):
            return abs(a[0]-b[0]) + abs(a[1]-b[1])
        for x, y in points:
            for j in points:
                if [x, y] != j:
                    adj[(x, y)].append((calCost([x, y], j), j))
        heap, visit, res = [(0, points[0])], set(), 0 # heap: (w, [x, y])
        while heap:
            if len(visit) == len(points):
                return res
            weight, [a, b] = heapq.heappop(heap)
            if (a, b) in visit:
                continue
            visit.add((a, b))
            res += weight
            for w, nei in adj[(a, b)]:
                heapq.heappush(heap, (w, nei))
                