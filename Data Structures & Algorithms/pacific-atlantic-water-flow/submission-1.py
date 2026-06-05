class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        pacific, atlantic = set(), set()
        
        def dfs(r, c, visit):
            visit.add((r, c))
            for dr, dc in dirs:
                nr, nc = dr+r, dc+c
                if (nr >= rows or nc >= cols or nr<0 or nc<0 or 
                    (nr, nc) in visit or heights[nr][nc] < heights[r][c]):
                    continue
                dfs(nr, nc, visit)
            return

        for c in range(cols):
            dfs(0, c, pacific)
        for r in range(rows):
            dfs(r, 0, pacific)
        for c in range(cols):
            dfs(rows-1, c, atlantic)
        for r in range(rows):
            dfs(r, cols-1, atlantic)

        return [[r, c] for r, c in pacific & atlantic]