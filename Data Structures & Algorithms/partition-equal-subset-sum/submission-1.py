class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        self.sum = 0
        for i in nums:
            self.sum += i
        if self.sum % 2 != 0:    return False
        memo = {}
        def dfs(i, curSum): # returns curSum == sum / 2
            if curSum == self.sum/2:
                return True
            if i >= len(nums):
                return False
            if (i, curSum) in memo:
                return memo[(i, curSum)]
            # include cur nb
            if dfs(i+1, curSum + nums[i]):
                memo[(i, curSum)] = True
                return True
            # exclude 
            if dfs(i+1, curSum):
                memo[(i, curSum)] = False
                return True
            return False

        return dfs(0, 0)