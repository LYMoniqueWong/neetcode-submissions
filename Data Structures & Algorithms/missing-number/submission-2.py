class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # XOR all the numbers from 0 to len(nums) with the numbers in nums
        res = len(nums)
        for i, n in enumerate(nums):
            res ^= i ^ n
        return res