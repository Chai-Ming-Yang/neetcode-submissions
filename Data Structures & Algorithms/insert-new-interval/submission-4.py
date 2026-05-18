class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        mn = intervals[:] + [newInterval[:]]
        heapq.heapify(mn)
        res = [heapq.heappop(mn)]
        while mn:
            if res[-1][1] < mn[0][0]:
                res.append(heapq.heappop(mn)); continue
            res[-1][1] = max(res[-1][1], heapq.heappop(mn)[1])
        return res