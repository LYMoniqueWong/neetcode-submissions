class MedianFinder:

    def __init__(self):
        # small heap: max heap; large heap: min heap
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # add to small
        # check if all #s in small <= #s in large if len sim
        # check lengths
        heapq.heappush(self.small, -1 * num)
        if self.small and self.large and (-1 * self.small[0] > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)


    def findMedian(self) -> float:
        # if len of small bigger, return max of small
        # if len of large bigger, return min of large
        # else return avg of max of small & min of large
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            return (-1 * self.small[0] + self.large[0]) / 2
        