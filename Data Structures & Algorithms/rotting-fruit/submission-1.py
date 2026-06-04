class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q, mins, nbfresh = deque(), 0, 0
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    nbfresh += 1
        if nbfresh == 0: return 0
        while q and nbfresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if (nr<0 or nc<0 or nr>=rows or nc>=cols or
                        grid[nr][nc] != 1):
                        continue
                    grid[nr][nc] = 2
                    nbfresh -= 1
                    q.append((nr, nc))
            mins += 1
        return mins if nbfresh == 0 else -1