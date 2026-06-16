class Solution:
    def numDecodings(self, s: str) -> int:
        dp1, dp2 = 1, 0
        for i in range(len(s)-1,-1,-1):
            dp = 0
            if s[i] != '0':
                dp = dp1
            if i+1 < len(s):
                if 10 <= int(s[i:i+2]) <= 26:
                    dp += dp2
            dp1, dp2 = dp, dp1
       
        return dp1