class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,1,2,8]
        # [48,24,6,1]
        prefix = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        print(prefix)
        suffix = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        print(suffix)
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]
        return res
