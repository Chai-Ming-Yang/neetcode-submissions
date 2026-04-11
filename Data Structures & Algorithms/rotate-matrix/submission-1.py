class Solution:
    def rotate(self, g: List[List[int]]) -> None:
        l, r = 0, len(g)-1
        while l < r:
            for i in range(r-l):
                tmp = g[l][l+i]
                g[l][l+i] = g[r-i][l]
                g[r-i][l] = g[r][r-i]
                g[r][r-i] = g[l+i][r]
                g[l+i][r] = tmp
            r -= 1
            l += 1