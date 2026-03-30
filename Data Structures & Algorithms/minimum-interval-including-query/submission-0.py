class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        q = deque(sorted([(q, i) for i, q in enumerate(queries)]))
        mn = intervals[:]; heapq.heapify(mn)
        cur = []    # met intervals
        res = [-1] * len(q)

        while q:
            a = q.popleft()
            while mn and mn[0][0] <= a[0]:
                l, r = heapq.heappop(mn)
                heapq.heappush(cur, (r-l+1, r))
            
            while cur and cur[0][1] < a[0]:
                heapq.heappop(cur)
            
            res[a[1]] = cur[0][0] if cur else -1
        return res