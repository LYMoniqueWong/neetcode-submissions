class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for a in range(len(nums)-2):
            if nums[a] > 0: break
            if a > 0 and nums[a] == nums[a-1]:  continue
            b, c = a + 1, len(nums)-1
            while b < c:
                total = nums[a] + nums[b] + nums[c]
                if total == 0:
                    res.append([nums[a], nums[b], nums[c]])
                    b += 1
                    while b < c and nums[b] == nums[b-1]:
                        b += 1
                elif total > 0:
                    c -= 1
                else:
                    b += 1
        return res