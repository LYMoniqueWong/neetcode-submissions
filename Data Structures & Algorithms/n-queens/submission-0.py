class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, negDiag, posDiag = set(), set(), set()
        board = [["."]*n for i in range(n)]
        res = []
        def backtrack(r):
            if r == n:
                copy = ["".join(i) for i in board]
                res.append(copy)
                return
            for c in range(n):
                if c in cols or (r-c) in negDiag or (r+c) in posDiag:
                    continue
                cols.add(c)
                negDiag.add(r-c)
                posDiag.add(r+c)
                board[r][c] = "Q"
                backtrack(r+1)
                cols.remove(c)
                negDiag.remove(r-c)
                posDiag.remove(r+c)
                board[r][c] = "."
        backtrack(0)
        return res