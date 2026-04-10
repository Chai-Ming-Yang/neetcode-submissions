class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        R, C = len(matrix), len(matrix[0])
        dp = [[0] * C for _ in range(R)]
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r, c):
            if dp[r][c]: return dp[r][c]
            res = 1
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if (nr<0 or nr==R or nc<0 or nc==C or
                    matrix[nr][nc] <= matrix[r][c]): continue
                res = max(res, 1 + dfs(nr, nc))
            dp[r][c] = res
            return dp[r][c]
        mx = 1
        for r in range(R):
            for c in range(C):
                mx = max(mx, dfs(r, c))
        return mx