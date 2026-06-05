class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        dirs = [(1, 0), (-1,0), (0,1), (0,-1)]
        visit = set()

        def backtrack(i, r , c):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                    (r, c) in visit or word[i] != board[r][c]):
                return False
            visit.add((r, c))
            for dr, dc in dirs:
                if backtrack(i + 1, dr+r, dc+c):
                    return True
            visit.remove((r, c))
            return False
            

        for r in range(rows):
            for c in range(cols):
                if backtrack(0, r, c): 
                    return True
        return False