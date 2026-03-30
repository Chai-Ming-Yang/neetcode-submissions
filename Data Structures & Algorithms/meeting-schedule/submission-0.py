"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        mn = [(iv.start, iv.end) for iv in intervals]
        heapq.heapify(mn)

        while len(mn) > 1:
            a = heapq.heappop(mn)
            if a[1] > mn[0][0]:
                return False
        return True