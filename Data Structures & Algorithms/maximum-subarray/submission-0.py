class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, curr = nums[0], nums[0]
        for i in nums[1:]:
            curr = max(i, curr+i)
            res = max(res, curr)
        return res

