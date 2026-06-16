class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dfs(i): # returns # of ways
            if i == len(s):
                return 1
            if i > len(s):
                return 0
            if s[i] == '0':
                return 0
            if i in memo:
                return memo[i]
            # always try single digit if not start w/ 0
            res = dfs(i+1)
            if i + 1 < len(s):
                if 10 <= int(s[i:i+2]) <= 26:
                    res += dfs(i+2)
            memo[i] = res
            return res
        return dfs(0)