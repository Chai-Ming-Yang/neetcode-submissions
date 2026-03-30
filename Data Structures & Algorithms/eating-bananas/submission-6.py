class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)

        piles.sort()
        l, r = 1, piles[-1]
        while l < r:
            m = l + (r-l)//2
            
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p)/m)
            if totalTime > h:
                l = m + 1
            else:
                r = m
        return r