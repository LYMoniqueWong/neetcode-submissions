class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        height, width = len(matrix), len(matrix[0])
        top, btn = 0, height-1
        while top <= btn:
            m = (top+btn) // 2
            if target > matrix[m][-1]:
                top = m+1
            elif target < matrix[m][0]:
                btn = m - 1
            else:
                break
        if not (top <= btn):    return False
        
        l, r = 0, width-1
        row = (top+btn) // 2
        while l <= r:
            m = (l+r)//2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                r = m-1
            else:
                l = m+1
        return False

