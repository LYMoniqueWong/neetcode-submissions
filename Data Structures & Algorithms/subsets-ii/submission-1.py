class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(curr, i):
            if i >= len(nums):
                res.append(curr.copy())
                return
            # inc
            curr.append(nums[i])
            dfs(curr, i+1)
            # exclude
            curr.pop()
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
            dfs(curr, i+1)
        dfs([], 0)
        return res