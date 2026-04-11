class Solution:
    def spiralOrder(self, g: List[List[int]]) -> List[int]:
        R, C = len(g), len(g[0])
        u, d, l, r = 0, R-1, 0, C-1

        res = []
        while l < r and u < d:
            for i in range(l, r):
                res.append(g[u][i])

            for i in range(u, d):
                res.append(g[i][r])
            
            for i in range(r, l, -1):
                res.append(g[d][i])
            
            for i in range(d, u, -1):
                res.append(g[i][l])

            l+=1; r-=1; u+=1; d-=1
        

        if l == r and u == d:
            res.append(g[u][l])
        elif u == d:
            for i in range(l, r+1):
                res.append(g[u][i])
        elif l == r:
            for i in range(u, d+1):
                res.append(g[i][r])
        return res