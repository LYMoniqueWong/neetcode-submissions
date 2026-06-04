class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] >= nums[l]: # left sorted portion
                if target < nums[l] or target > nums[m]:
                    l = m+1 # search right
                else:
                    r = m-1
            else: # right sorted portion
                if target < nums[m] or target > nums[r]:
                    r = m-1 # search left
                else:
                    l = m+1
        if not l <= r:
            return -1