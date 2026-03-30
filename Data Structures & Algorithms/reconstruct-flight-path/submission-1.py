class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}
        for u, v in tickets:
            if not u in adj:
                adj[u] = []
            heapq.heappush(adj[u], v)
        res = []
        def dfs(u):
            while adj.get(u):
                dfs(heapq.heappop(adj[u]))
            res.append(u)
        dfs("JFK")
        return res[::-1]