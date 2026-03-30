class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        vCol = set()
        vPosDiag, vNegDiag = set(), set()
        # Pos = R+C ; Neg = R-C

        board = [['.'] * n for _ in range(n)]

        res = []
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if (c in vCol or (r+c) in vPosDiag or (r-c) in vNegDiag): continue
                vCol.add(c);    vPosDiag.add(r+c);  vNegDiag.add(r-c);
                board[r][c] = 'Q'
                backtrack(r+1)
                vCol.remove(c);    vPosDiag.remove(r+c);  vNegDiag.remove(r-c);
                board[r][c] = '.'
        
        backtrack(0)
        return res