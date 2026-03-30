class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R, C = len(grid), len(grid[0])

        def bfs(row, col):
            q = deque([(row, col)])
            vis = set()
            dist = 0
            while q: 
                print(q)
                for _ in range(len(q)):
                    r, c = q.popleft()
                    vis.add((r, c))
                    grid[r][c] = min(grid[r][c], dist)
                    for newR, newC in {(r+1, c), (r-1, c), (r, c+1), (r, c-1)}:
                        if (newR<0 or newR==R or newC<0 or newC==C or
                            (newR,newC) in vis or
                            grid[newR][newC] < 1): 
                            continue
                        q.append((newR, newC))
                dist += 1

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    print(r,c, 'in!')
                    bfs(r,c)
        