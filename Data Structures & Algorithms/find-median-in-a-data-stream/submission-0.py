class MedianFinder:

    def __init__(self):
        self.med = 0
        self.mn = []
        self.mx = []

    def addNum(self, num: int) -> None:
        # push
        if num < self.med:
            heapq.heappush(self.mn, -num)
        else:
            heapq.heappush(self.mx, num)
        
        # balance
        # update median
        if len(self.mn) > len(self.mx) + 1:
            heapq.heappush(self.mx, -heapq.heappop(self.mn))
        elif len(self.mx) > len(self.mn) + 1:
            heapq.heappush(self.mn, -heapq.heappop(self.mx))
        
        if len(self.mn) == len(self.mx):
            self.med = (self.mx[0] - self.mn[0]) / 2.0
        elif len(self.mn) < len(self.mx):
            self.med = self.mx[0]
        else:
            self.med = -self.mn[0]
        print(self.mn, self.mx)

    def findMedian(self) -> float:
        return self.med
        