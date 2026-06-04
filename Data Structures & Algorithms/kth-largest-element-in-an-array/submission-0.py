class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-i for i in nums]
        heapq.heapify(heap)
        if k < 2:
            return -heap[0]
        for i in range(k-1):
            heapq.heappop(heap)
        return -heap[0]    
        # -5 -4 -3 -2 -1