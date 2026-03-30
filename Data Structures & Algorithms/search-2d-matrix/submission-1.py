class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        M = len(matrix[0])
        while l <= r:
            m = (r-l)//2 + l
            a, b = 0, M-1
            while a <= b:
                c = (b-a)//2 + a
                if matrix[m][c] < target:
                    a = c + 1
                elif matrix[m][c] > target:
                    b = c - 1
                else:
                    return True
            if a > c:
                l = m + 1
            else:
                r = m - 1
        return False