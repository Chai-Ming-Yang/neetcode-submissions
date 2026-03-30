class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = l = 0
        mp = dict()
        for r in range(len(s)):
            if s[r] in mp and mp[s[r]] >= l:
                res = max(res, r-l)
                l = mp[s[r]] + 1
            mp[s[r]] = r
        return max(res, len(s)-l)