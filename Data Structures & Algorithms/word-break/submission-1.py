class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dfs(i): # returns True if s[i:] can be separated into words in dict
            # i is the start idx where we start to check against dict
            if i == len(s):
                return True
            if i in memo:
                return memo[i]
            for word in wordDict:
                if s[i:i+len(word)] == word:
                    if dfs(i+len(word)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        return dfs(0)
            
            