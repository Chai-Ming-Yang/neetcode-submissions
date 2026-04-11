class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1.0
        for _ in range(n):
            res *= x
        for _ in range(n, 0):
            res /= x
        return res