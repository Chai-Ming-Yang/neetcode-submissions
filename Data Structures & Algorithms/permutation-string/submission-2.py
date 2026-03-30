class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count1, count = {}, {}
        for c, c2 in zip(s1, s2):
            count1[c] = 1 + count1.get(c, 0)
            count[c2] = 1 + count.get(c2, 0)
        k = len(s1)
        for i in range(len(s2)-k):
            if count1 == count:
                return True
            count[s2[i]] -= 1
            if count[s2[i]] == 0:
                del count[s2[i]]
            count[s2[i+k]] = 1 + count.get(s2[i+k], 0)
        return count1 == count