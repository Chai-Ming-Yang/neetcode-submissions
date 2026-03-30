class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, t in times:
            adj[u].append((t,v))
        mn = [(0, k)]
        vis = set()
        res = 0
        while mn:
            print(mn)
            time, u = heapq.heappop(mn)
            if u in vis: continue
            vis.add(u)
            res = max(res, time)
            while adj[u]:
                t, v = heapq.heappop(adj[u])
                heapq.heappush(mn, (time + t, v))
        
        return -1 if len(vis) < n else res