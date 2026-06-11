class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums2 = [-i for i in nums]
        heapq.heapify(nums2)
        res = 0
        for _ in range(k):
            res = heapq.heappop(nums2)
        return -res