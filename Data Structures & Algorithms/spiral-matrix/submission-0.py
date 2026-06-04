class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def rotateAntiClockwise(matrix):
            rows, cols = len(matrix), len(matrix[0])
            for r in matrix:
                r.reverse()
            transposed = [[matrix[r][c] for r in range(rows)] for c in range(cols)]   
            return transposed

        res = []    
        while matrix:
            for i in matrix[0]:
                res.append(i)
            matrix = matrix[1:]
            if matrix:
                matrix = rotateAntiClockwise(matrix)
        return res
