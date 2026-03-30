class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(l, r, pattern):
            if l == r and l == n:
                res.append(pattern[:])
            
            if l < n:
                pattern += '('
                dfs(l+1, r, pattern)
                pattern = pattern[:-1]
            if r < l:
                pattern += ')'
                dfs(l, r+1, pattern)
                pattern = pattern[:-1]
        dfs(0, 0, '')
        return res