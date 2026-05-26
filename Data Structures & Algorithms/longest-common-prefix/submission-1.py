class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        resL = len(strs[0])
        for s in strs[1:]:
            mn = min(resL, len(s))
            for i in range(mn, -1, -1):
                if s[:i] == res[:i]:
                    resL = i
                    res = res[:i]
                    break
        return res