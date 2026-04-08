class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        vis = [[0] * (n-1) + [1] for _ in range(m-1)] + [[1] * n]
        
        def dp(r, c):
            if vis[r][c] != 0: return vis[r][c]
            right = dp(r, c+1) if c+1 < n else 0
            down = dp(r+1, c)
            vis[r][c] = right + down
            return vis[r][c]
        return dp(0, 0)