class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        iv = {}
        for i, c in enumerate(s):
            if c not in iv:
                iv[c] = [i, i]
            else:
                iv[c][1] = i
        mn = list(iv.values())
        res = []
        while mn:
            a = heapq.heappop(mn)
            while mn and mn[0][0] < a[1]:
                a[1] = max(a[1], mn[0][1])
                heapq.heappop(mn)
                continue
            res.append(a[1] - a[0] + 1)
        return res