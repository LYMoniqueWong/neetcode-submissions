class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        a, b = len(word1), len(word2)
        dp = [[float("inf")] * (b+1) for _ in range(a+1)]
        for i in range(a+1):
            dp[i][b] = a - i
        for j in range(b+1):
            dp[a][j] = b - j
        for i in range(a-1, -1, -1):
            for j in range(b-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    insert = dp[i][j+1]
                    delete = dp[i+1][j]
                    replace = dp[i+1][j+1]
                    dp[i][j] = 1 + min(insert, delete, replace)
        return dp[0][0]
