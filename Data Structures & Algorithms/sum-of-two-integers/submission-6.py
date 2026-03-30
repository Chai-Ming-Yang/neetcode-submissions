class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        xor, carry = a, b
        while carry:
            tmp = (xor & carry) << 1
            xor = xor ^ carry
            carry = tmp
            xor &= 0xFFFFFFFF
            carry &= 0xFFFFFFFF
        return xor if xor < 0x80000000 else ~(xor ^ MASK)