class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # only depends on curr row and row below, use 2 1D arrays
        dp = [0] * (amount+1) # row below
        dp[0] = 1 # first col = remaining amt=0 shd be all 1s

        for i in range(len(coins)-1, -1, -1):
            nextDP = [0] * (amount+1) # curr row
            nextDP[0] = 1
            for j in range(1, amount+1):
                nextDP[j] = dp[j]
                if j - coins[i] >= 0:
                    nextDP[j] += nextDP[j - coins[i]]
            dp = nextDP
        return dp[amount]