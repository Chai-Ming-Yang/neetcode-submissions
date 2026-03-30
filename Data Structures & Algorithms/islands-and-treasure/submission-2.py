class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        R, C = len(grid), len(grid[0])

        def bfs(r, c):
            vis = set([(r,c)])
            q = deque([(r,c)])
            dist = 1
            while q:
                for _ in range(len(q)):
                    r,c = q.popleft()
                    for dr, dc in dirs:
                        nr, nc = r+dr, c+dc
                        if (nr<0 or nr==R or nc<0 or nc==C or
                            (nr, nc) in vis or grid[nr][nc] < 1): continue
                        q.append((nr,nc))
                        vis.add((nr,nc))
                        grid[nr][nc] = min(grid[nr][nc], dist)
                dist += 1
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0: bfs(r, c)