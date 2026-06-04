class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        l, r = 0, 1
        while r < len(nums):
            if nums[l] == nums[r]:  return True
            l += 1
            r += 1
        return False
