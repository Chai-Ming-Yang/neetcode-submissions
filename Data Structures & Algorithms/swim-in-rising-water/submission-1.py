class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        R, C = len(grid), len(grid[0])
        vis = set((0,0))
        mn = [(grid[0][0], 0, 0)]
        time = 0
        while mn:
            t, r, c = heapq.heappop(mn)
            time = max(time, t)
            if r==R-1 and c==C-1: return time
            for dr, dc in dirs:
                nr, nc = dr+r, dc+c
                if (nr<0 or nc<0 or nr==R or nc==C or 
                    (nr,nc) in vis): continue
                vis.add((nr, nc))
                heapq.heappush(mn, (max(time, grid[nr][nc]), nr, nc))