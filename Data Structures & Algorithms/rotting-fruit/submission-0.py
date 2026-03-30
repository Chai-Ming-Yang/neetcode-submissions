class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        fresh = set()
        vis = set()
        q = deque([])

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1: fresh.add((r,c))
                if grid[r][c] == 2: vis.add((r,c)); q.append((r,c))
        
        res = 0
        while q and not fresh.issubset(vis):
            res += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for nr,nc in {(r+1,c), (r-1,c), (r,c+1), (r,c-1)}:
                    if (nr<0 or nc<0 or nr==R or nc==C or (nr,nc) in vis or
                        grid[nr][nc]==0):continue
                    q.append((nr,nc))
                    vis.add((nr,nc))
        return res if fresh.issubset(vis) else -1