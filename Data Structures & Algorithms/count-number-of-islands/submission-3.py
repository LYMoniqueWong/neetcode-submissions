class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit, islands = set(), 0
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]

        def bfs(r, c):
            q = deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                for dr, dc in dirs:
                    nr, nc = dr+row, dc+col
                    if ((nr, nc) in visit or nr < 0 or nc < 0 or 
                        nr >= rows or nc >= cols or grid[nr][nc] == "0"):
                        continue
                    q.append((nr, nc))
                    visit.add((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1

        return islands