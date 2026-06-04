class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        a, b, c = len(s1), len(s2), len(s3)
        if a + b != c:  return False
        memo = {}
        def dfs(i, j): 
        # returns whether can form s3[i+j:] from s1[i:] and s2[j:]
            if i == a and j == b:
                return True
            if (i, j) in memo:  return memo[(i, j)]
            res = False
            if i < a and s1[i] == s3[i+j]: # try s1
                res = dfs(i+1, j)
            if not res and j < b and s2[j] == s3[i+j]:
                res = dfs(i, j+1)
            memo[(i, j)] = res
            return res
        return dfs(0, 0)