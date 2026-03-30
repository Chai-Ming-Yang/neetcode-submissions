class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        res = l = 0
        visited = set()
        for c in s:
            if c not in visited:
                visited.add(c)
                continue
            
            res = max(res, len(visited))
            while c in visited:
                visited.remove(s[l])
                l += 1
            visited.add(c)
        return max(res, len(visited))