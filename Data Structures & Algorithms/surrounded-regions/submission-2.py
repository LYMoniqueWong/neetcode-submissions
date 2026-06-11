class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visit, rows, cols = set(), len(board), len(board[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def dfs(r, c):  # mark all non surrounded regions
        # change all Os not in visit to Xs later
            visit.add((r, c))
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if (nr < 0 or nc < 0 or nr >= rows or nc >= cols or
                    (nr, nc) in visit or board[nr][nc] == 'X'):
                    continue
                dfs(nr, nc)
        
        for c in range(cols):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[rows-1][c] == 'O':
                dfs(rows-1, c)

        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][cols-1] == 'O':
                dfs(r, cols-1)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in visit:
                    board[r][c] = 'X'
