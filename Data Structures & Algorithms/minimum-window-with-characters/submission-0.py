class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = {}
        include, visit = set(), set()
        for c in t:
            include.add(c)
            window[c] = 1 + window.get(c, 0)
        
        l = 0
        res = ''
        for r in range(len(s)):
            if not s[r] in include:
                continue
            window[s[r]] -= 1
            if window[s[r]] == 0:
                visit.add(s[r])

            while include == visit:
                res = s[l:r+1] if (res == '' or len(res) > (r - l + 1)) else res
                
                if s[l] in visit:
                    window[s[l]] += 1
                    if window[s[l]] > 0:
                        visit.remove(s[l])
                l += 1
            
        return res
