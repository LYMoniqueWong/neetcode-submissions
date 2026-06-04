class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res, top = [], []
        for x, y in points:
            dist = x**2 + y**2
            res.append([dist, x, y])
        heapq.heapify(res)
        for i in range(k):
            d, x, y = heapq.heappop(res)
            top.append([x,y])
        return top
