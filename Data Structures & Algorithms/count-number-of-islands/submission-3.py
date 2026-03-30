class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        vis = set()
        R, C = len(grid), len(grid[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(r, c):
            vis.add((r,c))
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if (nr<0 or nc<0 or nr==R or nc==C or 
                    (nr,nc) in vis or grid[nr][nc]=='0'): continue
                dfs(nr, nc)
        res = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c]=='1' and (r,c) not in vis: 
                    res += 1
                    dfs(r, c)
        return res