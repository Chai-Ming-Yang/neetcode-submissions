class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for u, v, t in times:
            adj[u] = adj.get(u, [])
            heapq.heappush(adj[u], (t, v))

        vis = { i: float('inf') for i in range(1, n+1) }
        q = [(0, k)]
        while q:
            t, u = heapq.heappop(q)
            if vis[u] != float('inf'): continue
            vis[u] = t
            nei = adj.get(u, [])
            while nei:
                t2, v = heapq.heappop(nei)
                heapq.heappush(q, (t2+t, v))
        res = 0
        for t in vis.values():
            res = max(res, t)
        return res if res != float('inf') else -1