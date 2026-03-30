class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]

        def uFind(u):
            while u != par[u]:
                par[u] = par[par[u]]
                u = par[u]
            return u

        res = n
        for u, v in edges:
            pU,pV = uFind(u), uFind(v)
            if pU != pV:
                par[pU] = pV
                res -= 1
        return res