class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = [-1] * len(queries)
        queries = sorted([(v, i) for i, v in enumerate(queries)])
        iv = deque(sorted(intervals[:]))
        pq = []

        for t, i in queries:
            while iv and iv[0][1] < t: 
                iv.popleft()
            
            while iv and iv[0][0] <= t <= iv[0][1]:
                l, r = iv.popleft()
                heapq.heappush(pq, (r-l+1, r))
            
            while pq and pq[0][1] < t: 
                heapq.heappop(pq)
            
            if pq: res[i] = pq[0][0]
        return res