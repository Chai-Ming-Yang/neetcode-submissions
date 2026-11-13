class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for s in strs:
            res = res[:min(len(res), len(s))]
            for i in range(len(res)):
                if res[i] != s[i]:
                    res = res[:i]
                    break
        return res