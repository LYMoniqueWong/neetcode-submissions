class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:    return 0
        area, visit = 0, set()
        rows, cols = len(grid), len(grid[0])

        def bfs(r,c): # returns the area of this island
            island_area = 1
            q = deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                dirs = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in dirs:
                    r, c = row+dr, col+dc
                    if (r in range(rows) and c in range(cols) and
                        (r,c) not in visit and grid[r][c] == 1):
                        visit.add((r,c))
                        q.append((r,c))
                        island_area += 1
            return island_area

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visit and grid[r][c] == 1:
                    area = max(area, bfs(r,c))
        return area