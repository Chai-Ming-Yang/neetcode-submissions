class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        R, C = len(heights), len(heights[0])
        def bfs(starts):
            vis = set(starts)
            q = deque(starts)
            while q:
                 r, c = q.popleft()
                 for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if (nr<0 or nc<0 or nr==R or nc==C or
                        (nr,nc) in vis or heights[nr][nc] < heights[r][c]):
                        continue
                    q.append((nr,nc))
                    vis.add((nr,nc))
            return vis
        starts_pacific = [(r, 0) for r in range(R)] + [(0, c) for c in range(C)]
        starts_atlantic = [(r, C-1) for r in range(R)] + [(R-1, c) for c in range(C)]
        
        reachable_pacific = bfs(starts_pacific) # vis set
        reachable_atlantic = bfs(starts_atlantic)
        return list(reachable_pacific & reachable_atlantic)