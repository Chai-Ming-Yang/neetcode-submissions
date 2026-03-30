class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = tuple(set(str(n) for n in range(1, 10)) for _ in range(9))
        col = tuple(set(str(n) for n in range(1, 10)) for _ in range(9))
        box = tuple(set(str(n) for n in range(1, 10)) for _ in range(9))
        box = tuple( tuple(set(str(n) for n in range(1, 10)) for _ in range(3)) for _ in range(3))

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                tile = board[r][c]
                # row
                if tile not in row[r]:
                    return False
                row[r].remove(tile)
                if tile not in col[c]:
                    return False
                col[c].remove(tile)
                if tile not in box[r//3][c//3]:
                    return False
                box[r//3][c//3].remove(tile)
        return True