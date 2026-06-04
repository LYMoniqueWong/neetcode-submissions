class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        ans = nums[0]
        while l <= r:
            if nums[r] > nums[l]:
                ans = min(ans, nums[l])
                break
            m = (l+r)//2
            ans = min(ans, nums[m])
            if nums[m] >= nums[l]: # left sorted portion    
                l = m + 1# search right
            else: # right sorted portion
                r = m - 1
        return ans