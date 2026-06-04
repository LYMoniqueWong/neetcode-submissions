class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n+1)] 
        # dp[0] = {} ... dp[n] = {}
        dp[0][0] = 1 # 1 way using 0 nbs with target = 0
        for i in range(n):
            for total, count in dp[i].items():
                dp[i+1][total + nums[i]] += count
                dp[i+1][total - nums[i]] += count
        return dp[n][target]