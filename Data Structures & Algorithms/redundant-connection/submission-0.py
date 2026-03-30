class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = {}
        def uFind(a):
            if a not in par: 
                par[a] = a
            while par[a] != a:
                par[a] = par[par[a]]
                a = par[a]
            return a
        
        for u, v in edges:
            pU, pV = uFind(u), uFind(v)
            if pU == pV: return [u, v]
            par[pU] = par[pV]