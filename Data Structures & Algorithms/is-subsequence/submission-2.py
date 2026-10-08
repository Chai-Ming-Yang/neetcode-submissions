class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t): return False
        i = 0
        for c in t:
            if i >= len(s):break
            if s[i] == c:
                i += 1
        return i == len(s)