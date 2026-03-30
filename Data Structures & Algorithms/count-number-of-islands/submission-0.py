class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        vis = set()
        R, C = len(grid), len(grid[0])

        def dfs(r, c):
            if (r<0 or r==R or c<0 or c==C or
                (r,c) in vis or
                grid[r][c]=="0"): return
            vis.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        res = 0
        for r in range(R):
            for c in range(C):
                print(vis)
                print((r,c))
                if grid[r][c]=="1" and (r,c) not in vis:
                    print('---..-----------')
                    dfs(r,c)
                    res += 1
        return res