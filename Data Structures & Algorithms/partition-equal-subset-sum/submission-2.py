class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:    return False
        target = total // 2
        memo = {}
        def dfs(i, curSum): # returns curSum == sum / 2
            if curSum == target:
                return True
            if curSum > target:
                return False
            if i >= len(nums):
                return False
            if (i, curSum) in memo:
                return memo[(i, curSum)]

            memo[(i, curSum)] = dfs(i+1, curSum + nums[i]) or dfs(i+1, curSum)
            return memo[(i, curSum)]

        return dfs(0, 0)