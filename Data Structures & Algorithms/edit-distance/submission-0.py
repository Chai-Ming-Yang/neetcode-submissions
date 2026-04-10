# import sys
# sys.setrecursionlimit(2000)

class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        I, J = len(w1), len(w2)
        memo = {(I, J): 0}

        def dp(i, j):
            if (i, j) in memo: return memo[(i,j)]
            if i == I: return J - j
            if j == J: return I - i
            res = dp(i+1, j+1)
            if w1[i] != w2[j]:
                res += 1
            res = min(res, dp(i+1, j) + 1)
            res = min(res, dp(i, j+1) + 1)
            memo[(i, j)] = res
            return res
        return dp(0, 0)