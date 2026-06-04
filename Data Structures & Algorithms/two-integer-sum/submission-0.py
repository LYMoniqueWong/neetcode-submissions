class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {} # val: idx
        for idx, val in enumerate(nums):
            diff = target - val
            if diff in prev_map:
                return [prev_map[diff], idx]
            prev_map[val] = idx