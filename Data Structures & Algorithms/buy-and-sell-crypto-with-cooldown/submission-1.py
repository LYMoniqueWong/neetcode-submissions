class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n+2)] 
        # cols: canBuy=False=0, canBuy=True=1
        
        for i in range(n-1, -1, -1):
            # if canBuy=True=1
            buy = dp[i+1][0] - prices[i]
            cooldown = dp[i+1][1]
            dp[i][1] = max(cooldown, buy)

            # if canBuy=False=0
            cooldown = dp[i+1][0]
            sell = prices[i] + dp[i+2][1]
            dp[i][0] = max(cooldown, sell)
        
        return dp[0][1]    