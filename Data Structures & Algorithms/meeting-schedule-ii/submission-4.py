"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res = 0
        intervals.sort(key=lambda iv: (iv.start, iv.end))
        pq = []
        for iv in intervals:
            while pq and pq[0] <= iv.start:
                heapq.heappop(pq)
            heapq.heappush(pq, iv.end)
            res = max(res, len(pq))
        return res