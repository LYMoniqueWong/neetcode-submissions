class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, subset = [], []
        def dfs(i, total):
            if total == target:
                res.append(subset.copy())
                return
            
            for i in range(i, len(nums)):
                if nums[i] + total > target:
                    break
                subset.append(nums[i])
                dfs(i, total + nums[i])
                subset.pop()
        dfs(0,0)
        return res