class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i, robbedFirst): # returns max amt
            if i >= len(nums):
                return 0
            if (i, robbedFirst) in memo:
                return memo[(i, robbedFirst)]
            # rob
            robbed = 0
            if (i == len(nums)-1 and not robbedFirst) or i < len(nums)-1:
                if i == 0:
                    robbed = nums[i] + dfs(i+2, True)
                else:
                    robbed = nums[i] + dfs(i+2, robbedFirst)
            # skip
            skip = dfs(i+1, robbedFirst)
            memo[(i, robbedFirst)] = max(robbed, skip)
            return memo[(i, robbedFirst)]
        return dfs(0, False)