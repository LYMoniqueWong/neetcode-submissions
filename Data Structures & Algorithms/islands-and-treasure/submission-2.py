class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        # bfs from 0s
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if (nr<0 or nr>=m or nc<0 or nc>=n or grid[nr][nc] != 2147483647):
                    continue
                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))