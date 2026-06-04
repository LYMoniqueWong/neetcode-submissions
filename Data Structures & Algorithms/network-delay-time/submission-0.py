class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, t in times:
            edges[u].append((v, t))

        visit, res, minHeap = set(), 0, [(0, k)]

        while minHeap:
            t1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            res = max(res, t1)
            for n2, t2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (t1+t2, n2))
        return res if len(visit) == n else -1