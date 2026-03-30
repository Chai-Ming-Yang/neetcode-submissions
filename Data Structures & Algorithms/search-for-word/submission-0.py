class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        vis = set()
        def dfs(r, c, i):
            if i == len(word): return True
            vis.add((r,c))
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if (nr<0 or nc<0 or nr==R or nc==C or
                    (nr,nc) in vis or word[i] != board[nr][nc]): continue
                vis.add((nr,nc))
                if dfs(nr,nc, i+1): return True
            vis.remove((r,c))
            return False

        for r in range(R):
            for c in range(C):
                if board[r][c] == word[0]:
                    if dfs(r,c,1): return True
        return False
        