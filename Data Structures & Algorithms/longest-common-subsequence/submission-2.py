class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 == text2:  return len(text1)
        a, b = len(text1), len(text2)
        dp = {}
        def dfs(i, j): # returns lcs from text1[i:], text2[j:]
            if i >= a or j >= b:
                return 0
            if (i, j) in dp:  return dp[(i, j)]
            if text1[i] == text2[j]:
                dp[(i, j)] = 1 + dfs(i+1, j+1)
            else:
                dp[(i, j)] = max(dfs(i, j+1), dfs(i+1, j))
            return dp[(i, j)]
        return dfs(0, 0)
