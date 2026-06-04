class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        a, b = len(word1), len(word2)
        if a == b and a == 0:   return 0
        memo = {}
        def dfs(i, j): # return min # of ways to make w2[j:] from w1[i:]
            if j == b:  # del remaning chars from w1
                return a - i
            if i >= a:  # insert remaining chars from w2
                return b - j
            if (i, j) in memo:
                return memo[(i, j)]
            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(i+1, j+1)
            else:
                insert = dfs(i, j+1)
                delete = dfs(i+1, j)
                replace = dfs(i+1, j+1)
                memo[(i, j)] = 1 + min(insert, delete, replace)
            return memo[(i, j)]
        return dfs(0, 0)
