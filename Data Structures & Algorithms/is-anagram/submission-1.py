class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """ SOLUTIONS:
            1. sort
            2. count
        """
        # return Counter(s) == Counter(t)
        # return sorted(s) == sorted(t)
        if len(s) != len(t):
            return False
        hashdict = {}
        for a, b in zip(s, t):
            hashdict[a] = 1 + hashdict.get(a, 0)
            hashdict[b] = -1 + hashdict.get(b, 0)
        for val in hashdict.values():
            if val:
                return False
        return True