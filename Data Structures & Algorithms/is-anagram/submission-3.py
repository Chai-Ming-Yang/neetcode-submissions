class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = dict()
        if len(s) != len(t):
            return False
        for a, b in zip(s, t):
            count[a] = count.get(a, 0) + 1
            count[b] = count.get(b, 0) - 1
        
        for val in count.values():
            if val:
                return False
        return True