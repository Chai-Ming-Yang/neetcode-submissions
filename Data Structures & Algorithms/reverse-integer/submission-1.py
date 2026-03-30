class Solution:
    def reverse(self, x: int) -> int:
        MAX, MIN = 2**31-1, -2**31
        isNeg = x < 0
        res = 0
        if isNeg: n = -x
        else: n = x

        while n:
            if (res > MAX//10 or -res < MIN//10 or
                res == MAX//10 and n % 10 > MAX%10 or
                -res == MIN//10 and -n % 10 < MIN%10):
                # print(res > MAX//10)
                # print(-res < MIN//10)
                # print(res == MAX//10 and n % 10 > MAX%10)
                # print(-res == MIN//10 and -n % 10 < MIN%10)
                return 0
            res = (res * 10) + (n % 10)
            n //= 10
        return -res if isNeg else res