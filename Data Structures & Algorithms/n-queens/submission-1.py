class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # vis set()
        col, pDiag, nDiag = set(), set(), set()
        # pDiag = r+c   ;   nDiag = r-c
        board = [['.'] * n for _ in range(n)]
        res = []
        
        def backtrack(r):
            if r == n:
                res.append([''.join(row) for row in board])
                return
            for c in range(n):
                if (c in col or r+c in pDiag or r-c in nDiag): continue
                col.add(c); pDiag.add(r+c); nDiag.add(r-c)
                board[r][c] = 'Q'
                backtrack(r+1)
                col.remove(c); pDiag.remove(r+c); nDiag.remove(r-c)
                board[r][c] = '.'
        
        backtrack(0)
        return res