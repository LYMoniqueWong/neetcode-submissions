class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # XOR all the numbers from 0 to len(nums) with the numbers in nums
        res = 0
        for i in range(len(nums)+1):
            res ^= i
        for n in nums:
            res ^= n
        return res