class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # first row tells us to change which col to 0
        # first col[1:] tells us to change which row to 0
        rows, cols = len(matrix), len(matrix[0])
        firstRow = False
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    if r == 0:
                        firstRow = True
                    else:
                        matrix[r][0] = 0 # row
                    matrix[0][c] = 0 # col
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
        if firstRow:
            for c in range(cols):
                matrix[0][c] = 0