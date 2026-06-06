class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:  return nums[0]
        def robLinear(nums):
            memo = {}
            def dfs(i):
                if i >= len(nums):
                    return 0
                if i in memo:
                    return memo[i]
                rob = nums[i] + dfs(i+2)
                skip = dfs(i+1)
                memo[i] = max(rob, skip)
                return memo[i]
            return dfs(0)
        return max(robLinear(nums[:-1]), robLinear(nums[1:]))