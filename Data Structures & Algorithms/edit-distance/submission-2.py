class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        a, b = len(word1), len(word2)
        # we want b to be the smaller length, optimized space
        if a < b:
            a, b = b, a
            word1, word2 = word2, word1

        dp = [float("inf")] * (b+1)
        for j in range(b+1): # last row
            dp[j] = b - j 
        

        for i in range(a-1, -1, -1):
            newDP = [float("inf")] * (b+1)
            newDP[b] = a - i
            for j in range(b-1, -1, -1):
                if word1[i] == word2[j]:
                    newDP[j] = dp[j+1]
                else:
                    insert = newDP[j+1]
                    delete = dp[j]
                    replace = dp[j+1]
                    newDP[j] = 1 + min(insert, delete, replace)
            dp = newDP
        return dp[0]
