class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        N = len(s)
        vis = dict()
        for i in range(N):
            vis[s[i]] = +1 + vis.get(s[i], 0)
            vis[t[i]] = -1 + vis.get(t[i], 0)
        for v in vis.values():
            if v:
                return False
        return True