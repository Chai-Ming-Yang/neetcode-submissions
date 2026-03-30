class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for u, v, t in times:
            try: adj[u].append((t,v))
            except KeyError: adj[u] = [(t, v)]
        vis = set()
        res = 0
        mn = [(0, k)]
        while mn:
            curT, u = heapq.heappop(mn)
            if u in vis: continue
            vis.add(u)
            res = max(res, curT)
            while adj.get(u):
                t, v = heapq.heappop(adj[u])
                heapq.heappush(mn, (t+curT, v))
        return res if len(vis) == n else -1