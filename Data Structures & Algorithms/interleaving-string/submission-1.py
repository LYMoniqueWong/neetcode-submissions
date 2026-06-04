class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        a, b, c = len(s1), len(s2), len(s3)
        if a + b != c:  return False
        
        dp = [[False] * (b+1) for _ in range(a+1)]
        dp[a][b] = True
        
        for i in range(a, -1, -1):
            for j in range(b, -1, -1):
                if i == a and j == b:
                    continue
                if i < a and s1[i] == s3[i+j]:
                    dp[i][j] = dp[i+1][j]
                if not dp[i][j] and j < b and s2[j] == s3[i+j]:
                    dp[i][j] = dp[i][j+1]      
        return dp[0][0]