class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = l = 0
        vis = set()
        for r in range(len(s)):
            if s[r] in vis:
                res = max(res, r-l)
                while s[r] in vis:
                    vis.remove(s[l])
                    l += 1
            vis.add(s[r])
        return max(res, len(s)-l)