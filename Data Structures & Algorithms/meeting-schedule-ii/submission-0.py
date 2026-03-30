"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        mn = [(iv.start, iv.end) for iv in intervals]
        heapq.heapify(mn)
        cur = []

        res = 0
        while mn:
            a = heapq.heappop(mn)
            while cur and a[0] >= cur[0]:
                heapq.heappop(cur)
            res = max(res, 1 + len(cur))
            heapq.heappush(cur, a[1])
        return res
