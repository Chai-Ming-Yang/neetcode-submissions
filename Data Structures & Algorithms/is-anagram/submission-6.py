class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        vis = dict()
        for i in range(len(s)):
            vis[s[i]] = vis.get(s[i], 0) + 1
            vis[t[i]] = vis.get(t[i], 0) - 1
        for v in vis.values():
            if v: return False
        return True