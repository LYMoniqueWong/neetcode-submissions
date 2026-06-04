class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) # 48 24 12 8
        prefix = 1 # 1 1 2 8 48
        for i in range(len(nums)):
            res[i] = res[i] * prefix
            prefix *= nums[i]
        suffix = 1 # 1 6 24 48 48
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * suffix
            suffix *= nums[i]
        return res
