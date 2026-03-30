class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minH = []
        for x, y in points:
            euc_dist = math.sqrt(x**2 + y**2)
            heapq.heappush(minH, (-euc_dist, [x,y]))
        while len(minH) > k:
            heapq.heappop(minH)
        return [item[1] for item in minH]