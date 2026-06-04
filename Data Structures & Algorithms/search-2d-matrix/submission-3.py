class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        height, length = len(matrix), len(matrix[0])
        top, btn = 0, height-1
        while top <= btn:
            m = (top+btn)//2
            if target < matrix[m][0]:
                btn = m-1
            elif target > matrix[m][-1]:
                top = m+1
            else:
                break
        if not top <= btn:  return False
        
        l, r = 0, length-1
        row = (top+btn)//2
        while l <= r:
            m = (l+r)//2
            if target == matrix[row][m]:
                return True
            elif target < matrix[row][m]:
                r = m-1
            else:
                l = m+1
        return False
            