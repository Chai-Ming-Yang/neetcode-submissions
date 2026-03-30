class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [0] * 9
        col = [0] * 9
        box = [0] * 9
        
        for r in range(9):
            for c in range(9):
                n = board[r][c]
                if n == '.': continue
                n = int(n) -1
                if ((1<<n) & row[r] or 
                    (1<<n) & col[c] or
                    (1<<n) & box[(r//3)*3 + (c//3)]):
                    return False
                row[r] |= (1<<n)
                col[c] |= (1<<n)
                box[(r//3)*3 + (c//3)] |= (1<<n)
        return True