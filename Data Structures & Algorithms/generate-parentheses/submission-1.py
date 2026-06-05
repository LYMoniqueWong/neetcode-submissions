class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open, close = "(", ")"
        res = []
        def backtrack(curr, open, close):
            if open == n and close == n:
                res.append(curr)
                return
            # add ( 
            if open < n:
                curr += "("
                backtrack(curr, open+1, close)
                curr = curr[:len(curr)-1]
            if open > close:
                curr += ")"
                backtrack(curr, open, close+1)
        backtrack("", 0, 0)
        return res