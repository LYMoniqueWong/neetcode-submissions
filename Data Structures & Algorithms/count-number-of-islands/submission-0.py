class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited, islands = set(), 0
        def bfs(r, c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                dirs = [(1,0), (-1,0), (0,1), (0,-1)]
                for dr, dc in dirs:
                    nr, nc = row+dr, col+dc
                    if (nr in range(rows) and 
                        nc in range(cols) and
                        (nr, nc) not in visited and 
                        grid[nr][nc] == '1'):
                        q.append((nr, nc))
                        visited.add((nr, nc))
                
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == '1':
                    bfs(r, c)
                    islands += 1
        return islands