class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in board:
            seen_row = set()
            for i in r:
                if i in seen_row and i != '.':
                    return False
                seen_row.add(i)
        for c in range(len(board[0])):
            seen_col = set()
            for r in board:
                if r[c] in seen_col and r[c] != '.':
                    return False
                seen_col.add(r[c]) 
        for square in range(9):
            seen_box = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3)*3 + i
                    col = (square%3)*3 + j
                    if board[row][col] in seen_box and board[row][col] != '.':
                        return False
                    seen_box.add(board[row][col])
            

        return True