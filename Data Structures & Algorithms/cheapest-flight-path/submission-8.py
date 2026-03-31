class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """initialize with neg graph"""
        vis = { i:float('inf') for i in range(n) }
        # tmp = { i:float('inf') for i in range(n) }
        vis[src] = 0
        stops = 0
        updates = {src}
        while stops <= k and updates:
            updates = set()
            tmp = vis.copy()
            for u, v, p in flights:
                if vis[u] == float('inf') or tmp[v] <= vis[u] + p: continue
                updates.add(v)
                tmp[v] = min(tmp[v], vis[u] + p)
            stops += 1
            for v in updates:
                vis[v] = tmp[v]
        return -1 if vis[dst] == float('inf') else vis[dst]