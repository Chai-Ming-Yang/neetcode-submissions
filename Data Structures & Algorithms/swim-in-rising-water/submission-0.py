class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """ bidirectional search """
        R, C = len(grid), len(grid[0])
        dirs = [(1,0),(-1,0), (0,1), (0,-1)]
        t = 0
        v1, v2 = set(), set()
        q1, q2 = deque([(0, 0)]), deque([(R-1, C-1)])
        while q1 or q2:
            print(q1)
            print(q2)
            change = False
            for _ in range(len(q1)):
                r, c = q1.popleft()
                if grid[r][c] > t: q1.append((r,c)); continue
                change = True
                if (r,c) in v2: return t
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if (nr<0 or nc<0 or nr==R or nc == R or 
                        (nr, nc) in v1): continue
                    v1.add((nr,nc))
                    q1.append((nr,nc))
            for _ in range(len(q2)):
                r, c = q2.popleft()
                if grid[r][c] > t: q2.append((r,c)); continue
                change = True
                if (r,c) in v1: return t
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if (nr<0 or nc<0 or nr==R or nc==C or
                        (nr,nc) in v2): continue
                    v2.add((nr,nc))
                    q2.append((nr,nc))
            if not change: t += 1
        return 0