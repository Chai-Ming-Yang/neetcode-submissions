class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = { u: [] for u, _ in tickets }
        for u, v in tickets:
            adj[u].append(v)
        
        N = len(tickets) + 1
        res = ["JFK"]
        def dfs(u):
            if len(res) == N: return True
            if u not in adj: return False
            tmp = adj[u][:]
            for i, v in enumerate(tmp):
                adj[u].pop(i)
                res.append(v)
                if dfs(v): return True
                adj[u].insert(i, v)
                res.pop()
            return False
        dfs("JFK")
        return res