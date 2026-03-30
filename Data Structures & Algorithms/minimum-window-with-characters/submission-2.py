class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ''

        count = {}
        for c in t:
            count[c] = count.get(c, 0) + 1
        l = 0
        res = ''
        for r in range(len(s)):
            if s[r] not in count:    continue
            count[s[r]] -= 1
            
            valid = True
            for v in count.values():
                if v > 0: valid = False; break
            if not valid: continue

            while s[l] not in count or count[s[l]] < 0:
                if s[l] in count: count[s[l]] += 1
                l += 1
            if res == '' or r-l+1 < len(res): res = s[l:r+1]

        return res