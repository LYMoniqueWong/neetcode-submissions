class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == [] or matrix == [[]]:   return False
        row = -1
        height, width = len(matrix), len(matrix[0])
        for i in range(height): # 0 1 2
            l, r = 0, width-1
            if matrix[i][l] <= target <= matrix[i][r]:
                row = i
                break
        if row == -1:   return False
        l, r = 0, width-1
        while l <= r:
            m = (l+r)//2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                r = m-1
            else:
                l = m+1
        return False

