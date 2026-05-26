class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for c in range(len(strs[0])):
            for s in strs:
                if len(s) == c or s[c] != strs[0][c]:
                    return s[:c]
        return strs[0]