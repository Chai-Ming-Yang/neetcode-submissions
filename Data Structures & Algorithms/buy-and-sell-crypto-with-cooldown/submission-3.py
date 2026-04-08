class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, buy):
            if i >= len(prices): return 0
            if (i, buy) in dp: return dp[(i, buy)]

            wait = dfs(i+1, buy)
            if buy:
                buying = dfs(i+1, not buy) - prices[i]
                dp[(i, buy)] = max(wait, buying)
            else:
                selling = dfs(i+2, True) + prices[i]
                dp[(i, buy)] = max(wait, selling)
            return dp[(i, buy)]
        return dfs(0, True)