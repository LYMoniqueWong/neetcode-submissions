class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        firstRow = False
        # first row tells us which col to set 0
        # first col except [0][0] tells us which row to set 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    if r == 0:
                        firstRow = True
                    else:
                        matrix[r][0] = 0
                    matrix[0][c] = 0
                                   
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0: # first col all 0s
            for r in range(rows):
                matrix[r][0] = 0
        if firstRow: # first row all 0s
            for c in range(cols):
                matrix[0][c] = 0
        