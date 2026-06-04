class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # put 1st row, flip anticlockwise, add 1st row            
        res = []
        while matrix:
            res += matrix.pop(0)
            if matrix:
                matrix = [list(row) for row in zip(*matrix)][::-1]
        return res