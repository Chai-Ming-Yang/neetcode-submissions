class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        def bfs(r, c):
            q = deque([(r,c)])
            while q:
                r, c = q.popleft()
                board[r][c] = '#'
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if (nr<0 or nc<0 or nr==R or nc==C or 
                        board[nr][nc] != 'O'): continue
                    q.append((nr,nc))
        
        for r in range(R):
            if board[r][0] == 'O':  bfs(r, 0)
            if board[r][C-1] == 'O': bfs(r, C-1)
        for c in range(C):
            if board[0][c] == 'O':  bfs(0, c)
            if board[R-1][c] == 'O': bfs(R-1, c)
        
        for r in range(R):
            for c in range(C):
                if board[r][c] == 'O': board[r][c] = 'X'
                if board[r][c] == '#': board[r][c] = 'O'