class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        a, b = len(s), len(p)
        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i >= a and j >= b:
                return True
            if j >= b:
                return False
            # i could be out of bounds here
            match = (i < a) and (s[i] == p[j] or p[j] == ".")
            if j+1 < b and p[j+1] == "*":
                memo[(i, j)] = (match and dfs(i+1, j)) or dfs(i, j+2)
                return memo[(i, j)]
            if match:
                memo[(i, j)] = dfs(i+1, j+1)
                return memo[(i, j)]
            else:
                memo[(i, j)] = False
                return False
        return dfs(0, 0)