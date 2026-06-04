class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        a, b = len(s), len(t)
        if a < b:   return 0
        
        dp = [0] * (b+1) 
        dp[b] = 1
        
        for i in range(a-1, -1, -1):
            newDP = [0] * (b+1) 
            newDP[b] = 1
            for j in range(b-1, -1, -1):
                newDP[j] = dp[j]
                if s[i] == t[j]:
                    newDP[j] += dp[j+1]
            dp = newDP
        return dp[0]