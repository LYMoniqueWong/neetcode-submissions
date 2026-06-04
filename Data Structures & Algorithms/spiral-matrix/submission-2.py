class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # put 1st row, flip anticlockwise, add 1st row
        def rotateAntiClockwise(matrix):
            for row in matrix:
                row.reverse()
            return [list(row) for row in zip(*matrix)]
             
        res = []
        while matrix:
            res.extend(matrix[0])
            matrix = matrix[1:]
            if matrix:
                matrix = rotateAntiClockwise(matrix)
        return res