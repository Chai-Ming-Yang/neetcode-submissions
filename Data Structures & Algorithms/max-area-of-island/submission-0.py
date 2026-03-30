class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        vis = set()
        R, C = len(grid), len(grid[0])

        def dfs(r, c):
            if (r<0 or r==R or c<0 or c==C or
                (r,c) in vis or grid[r][c]==0): return 0
            vis.add((r,c))
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r, c+1) +  dfs(r, c-1)

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1 and (r,c) not in vis:
                    res = max(res, dfs(r, c))
        return res