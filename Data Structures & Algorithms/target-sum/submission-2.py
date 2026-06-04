class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # we only need the prev row
        dp = defaultdict(int) # dp = {} 
        dp[0] = 1 # 1 way using 0 nbs with target = 0
        
        for n in nums:
            nextDP = defaultdict(int)
            for total, count in dp.items():
                nextDP[total + n] += count
                nextDP[total - n] += count
            dp = nextDP
        return dp[target]