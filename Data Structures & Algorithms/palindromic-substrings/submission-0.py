class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        N = len(s)
        def pal(l, r):
            while 0 <= l and r < N:
                if s[l] != s[r]: return
                nonlocal res; res += 1
                l -= 1; r+= 1
        for i in range(N):
            pal(i, i)
            pal(i, i+1)
        return res