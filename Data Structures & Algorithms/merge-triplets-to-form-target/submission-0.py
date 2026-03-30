class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """brute-force"""
        mn = []
        A, B, C = target
        i = j = k = False
        for a, b, c in triplets:
            if a > A or b > B or c > C: continue
            if not i and A == a: i = True
            if not j and B == b: j = True
            if not k and C == c: k = True
            if i and j and k: return True
        #     heapq.heappush(mn, (-a, -b, -c))
        # x = y = z = 0
        # while mn:
        #     a, b, c = heapq.heappop(mn)
        #     if max(a,x)==A and max(b,y)==B and max(c,z) == C: return True

        return False