class Solution:
    def hammingWeight(self, n: int) -> int:
        N = n
        res = 0
        while N > 0:
            if N % 2:
                res += 1
            N >>= 1
        return res