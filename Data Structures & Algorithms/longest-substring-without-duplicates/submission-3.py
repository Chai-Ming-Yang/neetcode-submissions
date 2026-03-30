class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        vis = set()
        l = 0
        for r in range(len(s)):
            if s[r] not in vis:
                vis.add(s[r])
                continue
            res = max(res, r-l)
            while l < r and s[r] in vis:
                vis.remove(s[l])
                l += 1
            vis.add(s[r])
        return max(res, len(s)-l)