class Solution:
    def isHappy(self, n: int) -> bool:
        res = n
        vis = set([1])
        while res not in vis:
            vis.add(res)
            res = 0
            while n:
                res += (n % 10) ** 2
                n //= 10
            n = res
        return res == 1