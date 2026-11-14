class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.G = []
        for a in matrix:
            for i in range(1, len(a)):
                a[i] += a[i-1]
            self.G.append(a)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for r in range(row1, row2 + 1):
            if col1 == 0:
                res += self.G[r][col2]
            else:
                res += self.G[r][col2] - self.G[r][col1-1]
        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)