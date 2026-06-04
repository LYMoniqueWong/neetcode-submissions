class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenCols = defaultdict(set)
        seenRows = defaultdict(set)
        seenGrids = defaultdict(set)
        for r in range(9):  
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                if val in seenRows[r]:
                    return False
                seenRows[r].add(val)
                if val in seenCols[c]:
                    return False
                seenCols[c].add(val)
                gird = (r//3, c//3)
                if val in seenGrids[gird]:
                    return False
                seenGrids[gird].add(val)
        return True