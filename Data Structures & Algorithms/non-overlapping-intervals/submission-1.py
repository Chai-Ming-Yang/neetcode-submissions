class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        pq = intervals[:]; heapq.heapify(pq)
        while len(pq) > 1:
            a = heapq.heappop(pq)
            if pq[0][0] >= a[1]: continue
            res += 1
            if pq[0][1] > a[1]: pq[0] = a
        return res