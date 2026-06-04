class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d1 = {}
        for i, n in enumerate(nums):
            if target - n in d1:
                return [d1[target-n], i]
            d1[n] = i