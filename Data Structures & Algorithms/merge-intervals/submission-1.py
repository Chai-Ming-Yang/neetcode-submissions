class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        mn = intervals[:]
        heapq.heapify(mn)
        res = []
        while len(mn) > 1:
            a = heapq.heappop(mn)
            if a[1] < mn[0][0]:
                res.append(a); continue
            a[1] = max(a[1], heapq.heappop(mn)[1])
            heapq.heappush(mn, a)
        return res + mn