class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [[set() for _ in range(3)] for _ in range(3)]
        
        for r in range(9):
            for c in range(9):
                n = board[r][c]
                if n == ".": 
                    continue
                print([r,c], n, row)
                if (n in row[r] or n in col[c] or n in box[r//3][c//3]):
                    return False
                row[r].add(n)
                col[c].add(n)
                box[r//3][c//3].add(n)
        return True