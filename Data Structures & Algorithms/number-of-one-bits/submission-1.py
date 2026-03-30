class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        num = n
        while num:
            if num & 1:
                res += 1
            num >>= 1
        return res