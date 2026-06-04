class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 == text2:  return len(text1)
        a, b = len(text1), len(text2)
        dp = [[0] * (b+1) for _ in range(a+1)]
        for i in range(a-1, -1, -1):
            for j in range(b-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        return dp[0][0]

