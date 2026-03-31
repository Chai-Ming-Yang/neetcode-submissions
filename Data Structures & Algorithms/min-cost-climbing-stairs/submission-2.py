class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        p, pp = cost[1], cost[0]
        for i in range(2, len(cost)):
            pp, p = p, cost[i] + min(pp, p)
        return min(p, pp)