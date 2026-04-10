class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        I, J = len(s1), len(s2)
        L = len(s3)
        if I + J != L: return False

        memo = {(I,J): True}
        def dfs(i, j):
            if (i, j) in memo: return memo[(i,j)]
            if i != I and s1[i] == s3[i+j]:
                if dfs(i+1, j): return True
            if j != J and s2[j] == s3[i+j]:
                if dfs(i, j+1): return True
            memo[(i, j)] = False
            return False
        return dfs(0, 0)