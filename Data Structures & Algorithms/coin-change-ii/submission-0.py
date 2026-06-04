class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        memo = {}
        def dfs(i, remainingA):
            if i >= len(coins) or remainingA < 0:
                return 0
            if i < len(coins) and remainingA == 0:
                return 1
            if (i, remainingA) in memo:
                return memo[(i, remainingA)]
            # use this coin
            a = dfs(i, remainingA - coins[i])
            # don't use this coin
            b = dfs(i+1, remainingA)
            memo[(i, remainingA)] = a + b
            return a + b
        return dfs(0, amount)