class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        i, j = 0, 1
        length = len(nums)
        while j < length:
            if nums[j] == nums[i]:
                return True
            i, j = i+1, j+1
        return False

