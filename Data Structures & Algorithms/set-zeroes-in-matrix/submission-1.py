class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        zRow, zCol = set(), set()
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zRow.add(r)
                    zCol.add(c)
        for r in range(rows):
            for c in range(cols):
                if r in zRow or c in zCol:
                    matrix[r][c] = 0


        