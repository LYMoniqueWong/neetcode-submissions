class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit, self.islands = set(), 0
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]

        def bfs(i, j):
            if (i, j) in visit or grid[i][j] == "0":
                return
            visit.add((i, j))
            for dr, dc in dirs:
                nr, nc = i + dr, j + dc
                if ((nr, nc) in visit or nr < 0 or nc < 0 or 
                    nr >= rows or nc >= cols or grid[nr][nc] == "0"):
                    continue
                bfs(nr, nc)
            
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    self.islands += 1

        return self.islands