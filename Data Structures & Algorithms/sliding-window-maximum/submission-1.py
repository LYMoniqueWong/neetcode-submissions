class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0
        windowMax = deque()
        for r in range(len(nums)):
            while windowMax and windowMax[0][1] < l:
                windowMax.popleft()
            while windowMax and nums[r] > windowMax[-1][0]:
                windowMax.pop()
            windowMax.append((nums[r], r))
            if r > k-2:
                res.append(windowMax[0][0])
                l += 1
        return res