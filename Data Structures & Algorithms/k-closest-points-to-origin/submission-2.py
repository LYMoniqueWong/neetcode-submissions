class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap, res = [], []
        for x, y in points:
            heap.append((x**2 + y**2, [x,y]))
        heapq.heapify(heap)
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res