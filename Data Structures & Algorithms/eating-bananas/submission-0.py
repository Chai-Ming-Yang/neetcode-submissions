class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = l + (r-l)//2

            hoursTaken = 0
            for p in piles:
                hoursTaken += math.ceil(float(p)/k)
            
            if hoursTaken > h:
                l = k + 1
            else:
                res = k
                r = k - 1
        return res