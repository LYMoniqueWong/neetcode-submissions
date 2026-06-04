class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heapq.heappush(heap, i*-1) # -6, -4, -3, -2, -2
        while len(heap) > 1:
            a = -1* heapq.heappop(heap) # 6
            b = -1* heapq.heappop(heap) # 4
            if a > b:
                heapq.heappush(heap, -(a-b))
            elif a < b:
                heapq.heappush(heap, -(b-a))
        return -heap[0] if heap else 0
