class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap) # -6 -4 -3 -2 -2
        while len(maxHeap) > 1:
            y = -heapq.heappop(maxHeap) # 6
            x = -heapq.heappop(maxHeap) # 4
            if x != y:
                heapq.heappush(maxHeap, -(y-x))
        return -heapq.heappop(maxHeap) if maxHeap else 0
