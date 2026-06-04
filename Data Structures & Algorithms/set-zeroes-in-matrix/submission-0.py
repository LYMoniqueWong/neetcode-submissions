class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        zSet = defaultdict(list)
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zSet["r"].append(r)
                    zSet["c"].append(c)
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] != 0 and (r in zSet["r"] or c in zSet["c"]):
                    matrix[r][c] = 0


        