class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            print(1 & n)
            res = (res << 1) + (1 & n)
            n >>= 1
        return res