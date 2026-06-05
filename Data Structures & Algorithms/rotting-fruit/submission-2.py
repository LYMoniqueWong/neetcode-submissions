class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        freshFruit, q = 0, deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    freshFruit += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        
        mins = 0
        dirs = [[1, 0], [-1,0], [0,1], [0,-1]]
        while q and freshFruit > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = dr+r, dc+c
                    if (nr < 0 or nc < 0 or nr >= rows or nc >= cols
                        or grid[nr][nc] != 1):
                        continue
                    grid[nr][nc] = 2
                    freshFruit -= 1
                    q.append((nr, nc))
            mins += 1
        return -1 if freshFruit !=  0 else mins