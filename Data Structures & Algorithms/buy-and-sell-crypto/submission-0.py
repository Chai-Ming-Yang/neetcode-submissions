class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        res = l = 0
        for r in range(len(prices)):
            if prices[l] < prices[r]:
                res = max(res, prices[r] - prices[l])
            else:
                l = r
        return res