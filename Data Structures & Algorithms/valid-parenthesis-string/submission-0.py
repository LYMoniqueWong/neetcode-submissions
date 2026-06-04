class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}
        def dfs(i, open): # can we form a valid string from s[i:] with open # of (
            if i == len(s):
                return open == 0
            if open < 0:
                return False
            if (i, open) in memo:
                return memo[(i, open)]
            if s[i] == "(":
                res = dfs(i+1, open+1)
            elif s[i] == ")":
                res = dfs(i+1, open-1)
            else:
                res = dfs(i+1, open+1) or dfs(i+1, open-1) or dfs(i+1, open)
            memo[(i, open)] = res
            return res
        return dfs(0, 0)