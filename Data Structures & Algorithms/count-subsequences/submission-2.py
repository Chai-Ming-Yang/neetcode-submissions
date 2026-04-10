import sys
sys.setrecursionlimit(2000)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        I, J = len(s), len(t)
        if I < J: return 0

        memo = {} # (i, j)

        def dp(i, j):
            if (i, j) in memo: return memo[(i,j)]
            if j == J: memo[(i,j)] = 1; return 1
            if i == I: return 0
            res = 0
            if s[i] == t[j]:
                res += dp(i+1, j+1)
            res += dp(i+1, j)
            
            memo[(i, j)] = res
            return res
        return dp(0, 0)