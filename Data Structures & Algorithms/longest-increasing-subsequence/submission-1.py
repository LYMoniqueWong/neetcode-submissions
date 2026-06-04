class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i, prevVal): # return the len of the LIS of nums[i:]
            if i == len(nums):  return 0
            if (i, prevVal) in memo:
                return memo[(i, prevVal)]
            # include
            take = 0
            if nums[i] > prevVal:
                take = 1 + dfs(i+1, nums[i])
            # exclude
            notTake = dfs(i+1, prevVal)
            memo[(i, prevVal)] = max(take, notTake)
            return memo[(i, prevVal)]
        return dfs(0, float("-inf"))