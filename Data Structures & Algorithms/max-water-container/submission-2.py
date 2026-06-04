class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        res = 0
        while l < r and r < len(heights):
            res = max(res, ((r-l)*min(heights[r],heights[l])))
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return res