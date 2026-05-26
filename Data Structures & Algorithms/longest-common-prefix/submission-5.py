class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        a, b = strs[0], strs[-1]
        for i in range(min(len(a), len(b))):
            if a[i] != b[i]: return a[:i]
        return a