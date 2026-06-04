class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, subset = [], []
        def dfs(i, sum):
            if i >= len(nums) or sum > target:
                return
            if sum == target:
                res.append(subset.copy())
                return
            subset.append(nums[i])
            sum += nums[i]
            dfs(i, sum)
            subset.pop()
            sum -= nums[i]
            dfs(i+1, sum)
        dfs(0,0)
        return res