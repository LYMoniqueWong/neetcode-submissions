class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        rows, cols = len(grid), len(grid[0])
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        steps = 0            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))

        while q:
            layers = len(q)
            for _ in range(layers):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if (nr<0 or nc<0 or nr>=rows or nc>=cols or
                        grid[nr][nc] != 2147483647):
                            continue
                    q.append((nr,nc))
                    grid[nr][nc] = steps + 1
            steps += 1
        return