class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit, dirs = set(), [(0, 1), (0,-1), (1, 0), (-1, 0)]
        heap = [(grid[0][0], 0, 0)] # (max # along the path, row, col)
        while heap:
            w, r, c = heapq.heappop(heap)
            if r == rows-1 and c == cols-1:
                return w
            if (r, c) in visit:
                continue
            visit.add((r, c))
            for dr, dc in dirs:
                nr, nc = dr+r, dc+c
                if ((nr, nc) in visit or nr < 0 or nc < 0 or
                    nr >= rows or nc >= cols):
                    continue
                heapq.heappush(heap, (max(w, grid[nr][nc]), nr, nc))