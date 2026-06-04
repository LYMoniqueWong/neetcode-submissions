class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        def dfs(i): 
            if i >= len(nums)-1:    return True
            if i in memo:   return memo[i]
            for j in range(1, nums[i]+1):
                if dfs(i+j):
                    memo[i] = True
                    return True
            memo[i] = False
            return False
        return dfs(0)