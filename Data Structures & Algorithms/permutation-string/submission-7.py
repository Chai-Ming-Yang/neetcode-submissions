class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        l = 0
        freq, vis = {}, set()
        for c1,c2 in zip(s1, s2[:len(s1)]):
            freq[c1] = freq.get(c1, 0) - 1
            freq[c2] = freq.get(c2, 0) + 1
            vis.add(c1)
        same = True
        for k in vis:
            if freq[k] != 0:
               same = False
               break
        if same: return True

        for c in s2[len(s1): len(s2)]:
            freq[c] = freq.get(c, 0) + 1
            freq[s2[l]] -= 1; l += 1
            same = True
            for k in vis:
                # print(k, freq, freq.get(k,0))
                if freq[k] != 0:
                    same = False
                    break
            if same: return True
        return False