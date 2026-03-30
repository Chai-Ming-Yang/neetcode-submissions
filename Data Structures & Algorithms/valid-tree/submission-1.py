class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """ VALID TREE: 
            - no loops
            - every node connected 
        """
        if not n: return

        vis = set()
        adj = {i:[] for i in range(n)}
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(cur, pre):
            if cur in vis: return False
            vis.add(cur)
            for neighbor in adj[cur]:
                if neighbor == pre: continue 
                if not dfs(neighbor, cur): return False
            return True
        return dfs(0, -1) and len(vis) == n