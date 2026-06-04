class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        # cols: amount  rows: coins
        dp = [[0] * (amount+1) for _ in range(n+1)]
        # first col = remaining amt=0 shd be all 1s
        for i in range(n+1):
            dp[i][0] = 1

        for i in range(n-1, -1, -1):
            for j in range(1, amount+1):
                dp[i][j] = dp[i+1][j]
                if j - coins[i] >= 0:
                    dp[i][j] += dp[i][j - coins[i]]
        return dp[0][amount]