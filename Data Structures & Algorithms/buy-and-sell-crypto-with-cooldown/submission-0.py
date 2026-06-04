class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i, canBuy): 
            if i >= len(prices):
                return 0
            if (i, canBuy) in memo:
                return memo[(i, canBuy)]
            cooldown = dfs(i+1, canBuy)
            if canBuy:
                buy = -prices[i] + dfs(i+1, not canBuy)
                memo[(i, canBuy)] = max(cooldown, buy)
            else:
                sell = prices[i] + dfs(i+2, not canBuy)
                memo[(i, canBuy)] = max(cooldown, sell)
            return memo[(i, canBuy)]
        
        return dfs(0, True)

            