class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMax, currMin = 1, 1
        for i in nums:
            tmp = i*currMax
            currMax = max(i, i*currMax, i*currMin)
            currMin = min(i, tmp, i*currMin)
            res = max(res, currMax)
        return res