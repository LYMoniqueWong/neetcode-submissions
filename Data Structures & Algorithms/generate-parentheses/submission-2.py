class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(curr, open, close):
            if open == n and close == n:
                res.append(curr)
                return
            if open < n:
                backtrack(curr + "(", open+1, close)
            if open > close:
                backtrack(curr + ")", open, close+1)
        backtrack("", 0, 0)
        return res