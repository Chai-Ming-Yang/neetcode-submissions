class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0': return 0
        N = len(s)
        p2, p = 1, 1
        for i in range(1, N):
            cur = 0
            if s[i] != '0':
                cur = p
            if 9 < int(s[i-1: i+1]) <= 26:
                cur += p2
            p2, p = p, cur
        return p