class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        R, C = len(matrix), len(matrix[0])
        
        def markHash(row, col):
            for i in range(C):
                if matrix[row][i] != 0:
                    matrix[row][i] = '#'
            for i in range(R):
                if matrix[i][col] != 0:
                    matrix[i][col] = '#'

        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    markHash(r, c)

        for r in range(R):
            for c in range(C):
                if matrix[r][c] == '#':
                    matrix[r][c] = 0