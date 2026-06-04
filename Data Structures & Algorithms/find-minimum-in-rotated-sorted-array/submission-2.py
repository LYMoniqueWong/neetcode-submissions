class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 1234 4123 3412 2341
        res = nums[0]
        l, r = 0, len(nums)-1 
        while l <= r:
            if nums[l] < nums[r]:
                res = min(nums[l], res)
                break 
            else:
                m = (l+r) // 2 
                res = min(nums[m], res)
                if nums[m] >= nums[l]: # in left half of arr
                    l = m+1 # search right
                else:
                    r = m-1
        return res