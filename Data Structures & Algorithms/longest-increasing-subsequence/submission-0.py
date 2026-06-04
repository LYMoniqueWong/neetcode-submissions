class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def dfs(i, prevValue): # returns the LIS from idx i
            if i == len(nums):
                return 0
            # include n
            take = 0
            if nums[i] > prevValue:
                take = 1 + dfs(i+1, nums[i])
            # exclude n
            notTake = dfs(i+1, prevValue)
            return max(take, notTake)
        return dfs(0, float("-inf"))