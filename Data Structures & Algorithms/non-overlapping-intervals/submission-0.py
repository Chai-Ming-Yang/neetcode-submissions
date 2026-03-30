class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        mn = intervals[:]
        heapq.heapify(mn)

        while len(mn) > 1:
            a = heapq.heappop(mn)
            if a[1] <= mn[0][0]:
                continue
            res += 1
            if a[1] < mn[0][1]:
                heapq.heappop(mn)
                heapq.heappush(mn, a)
        return res