class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)  # key = (r//3, c//3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                tile = board[r][c]

                if tile in row[r]:
                    return False
                row[r].add(tile)
                if tile in col[c]:
                    return False
                col[c].add(tile)
                if tile in box[str(r//3)+str(c//3)]:
                    return False
                box[str(r//3)+str(c//3)].add(tile)
        return True