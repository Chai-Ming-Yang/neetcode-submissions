class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = C = 0
        MASK = 0xFFFFFFFF
        cur = 1
        for _ in range(32):
            A, B = a & cur, b & cur
            res |= A ^ B ^ C
            C = (A & B | B & C | A & C) << 1
            cur <<= 1
        return res if res < 0x80000000 else ~(res ^ MASK)