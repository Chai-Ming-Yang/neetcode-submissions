class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        par = {}
        def uFind(a):
            while a != par[a]:
                par[a] = par[par[a]]
                a = par[a]
            return a
        
        mn = []
        for i in range(len(points)):
            key = tuple(points[i])
            par[key] = key
            x1, y1 = points[i]
            for x2, y2 in points[i+1:]:
                dist = abs(x1 - x2) + abs(y1 - y2)
                heapq.heappush(mn, (dist, (x1, y1), (x2, y2)))

        res = 0
        while mn:
            w, p1, p2 = heapq.heappop(mn)
            par1, par2 = uFind(p1), uFind(p2)
            if par1 == par2: continue
            par[par1] = par2
            res += w
        return res