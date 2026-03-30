class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R, C = len(grid), len(grid[0])
        vis = set()
        def dfs(r, c):
            q = deque([(r, c)])
            dist = 0
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    vis.add((r, c))
                    grid[r][c] = min(grid[r][c], dist)
                    for nR, nC in {(r+1, c), (r-1, c), (r, c+1), (r, c-1)}:
                        if  (nR<0 or nC<0 or nR==R or nC==C or 
                            (nR, nC) in vis or grid[nR][nC] < 1): continue
                        q.append((nR, nC))
                dist += 1
        for r in range(R):
            for c in range(C):
                if grid[r][c] != 0: continue
                vis = set()
                dfs(r,c)