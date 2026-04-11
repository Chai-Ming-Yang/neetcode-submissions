class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        I, J = len(s), len(p)

        def dfs(i, j):
            if j == J: return i == I
            
            match = i<I and (s[i] == p[j] or p[j]==".")
            if (j + 1) < J and p[j + 1] == "*":
                return ((match and dfs(i+1, j)) or
                        dfs(i, j+2))
            if match:
                return dfs(i+1, j+1)
            return False
        return dfs(0,0)