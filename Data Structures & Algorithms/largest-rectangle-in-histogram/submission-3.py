class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # monotonically increasing stack
        stack, res = [], 0
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                oldIdx, oldHeight = stack.pop()
                res = max(res, (i-oldIdx)*oldHeight)
                start = oldIdx
            stack.append((start, h))
        for i, h in stack:
            res = max(res, (len(heights)-i)*h)
        return res