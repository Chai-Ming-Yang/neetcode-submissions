class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        qPacific = deque([])
        qAtlantic = deque([])
        visPacific = set()
        visAtlantic = set()
        R, C = len(heights), len(heights[0])
        for r in range(R):
            qPacific.append((r, 0))
            visPacific.add((r,0))
            qAtlantic.append((r, C-1))
            visAtlantic.add((r, C-1))
        for c in range(C):
            qPacific.append((0, c))
            visPacific.add((0, c))
            qAtlantic.append((R-1, c))
            visAtlantic.add((R-1, c))
        
        res = {}

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while qPacific:
            for _ in range(len(qPacific)):
                r, c = qPacific.popleft()
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if (nr<0 or nc<0 or nr==R or nc==C or
                        (nr, nc) in visPacific or heights[nr][nc] < heights[r][c]): continue
                    qPacific.append((nr,nc))
                    visPacific.add((nr,nc))
        while qAtlantic:
            for _ in range(len(qAtlantic)):
                r, c = qAtlantic.popleft()
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if (nr<0 or nc<0 or nr==R or nc==C or
                        (nr,nc) in visAtlantic or heights[nr][nc] < heights[r][c]): continue
                    qAtlantic.append((nr, nc))
                    visAtlantic.add((nr,nc))
        print(visPacific)
        print(visAtlantic)
        return list(visPacific & visAtlantic)