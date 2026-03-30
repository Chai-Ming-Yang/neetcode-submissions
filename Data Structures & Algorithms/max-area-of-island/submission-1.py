class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        vis = set()
        R, C = len(grid), len(grid[0])
        dirs = [(1,0),(-1,0), (0,-1), (0,1)]
        def dfs(r, c):
            vis.add((r,c))
            area = 0
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if (nr<0 or nc<0 or nr==R or nc==C
                    or (nr, nc) in vis or grid[nr][nc]==0): continue
                area += dfs(nr,nc)
            return 1 + area

        res = 0
        for r in range(R):
            for c in range(C):
                if (r,c) not in vis and grid[r][c]==1:
                    res = max(res, dfs(r, c))
        return res