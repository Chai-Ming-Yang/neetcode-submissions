"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals: return True
        q = deque(sorted(intervals[:], key=lambda iv: (iv.start, iv.end)))
        a = q.popleft()
        while q:
            if a.end > q[0].start: return False
            a = q.popleft()
        return True