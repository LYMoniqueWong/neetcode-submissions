class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res, visit = 0, set()
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]

        def bfs(r, c): # return the count of 1
            count = 1
            q = deque()
            q.append((r, c))
            visit.add((r,c))
            while q:
                row, col = q.popleft()
                for dr, dc in dirs:
                    nr, nc = dr+row, dc+col
                    if (nr in range(rows) and nc in range(cols) and 
                        (nr, nc) not in visit and grid[nr][nc] == 1):
                        count += 1
                        q.append((nr, nc))
                        visit.add((nr, nc))
            
            return count

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visit and grid[r][c] == 1:
                    res = max(res, bfs(r, c))
        return res