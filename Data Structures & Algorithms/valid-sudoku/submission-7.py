class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [0] * 9; col = row[:]; box = row[:]
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": continue
                n = 1 << int(board[r][c])
                if row[r] & n or col[c] & n or box[r//3*3 + c//3] & n:
                    return False
                row[r] |= n
                col[c] |= n
                box[r//3*3 + c//3] |= n
        return True