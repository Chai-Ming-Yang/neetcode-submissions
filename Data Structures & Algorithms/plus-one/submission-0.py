class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = 0
        for n in digits:
            res *= 10
            res += n
        res += 1
        digits = []
        while res:
            digits.append(res % 10)
            res //= 10
        digits.reverse()
        return digits