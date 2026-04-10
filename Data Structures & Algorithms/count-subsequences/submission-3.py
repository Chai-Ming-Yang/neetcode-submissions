class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        I, J = len(s), len(t)
        dp = [[0]*J + [1] for _ in range(I+1)]

        for i in range(I-1, -1, -1):
            for j in range(J-1, -1, -1):
                dp[i][j] = dp[i+1][j]
                if s[i] == t[j]:
                    dp[i][j] += dp[i+1][j+1]
        return dp[0][0]