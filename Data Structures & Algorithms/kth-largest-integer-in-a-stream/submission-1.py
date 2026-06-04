class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        self.size = k
        for n in nums:
            self.minHeap.append(n)
        heapq.heapify(self.minHeap)

        
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        while len(self.minHeap) > self.size:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]