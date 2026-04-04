class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 1

        for i in range(amount + 1):
            if dp[i] == float('inf'): continue
            for coin in coins:
                if i + coin > amount: continue
                dp[i + coin] = min(dp[i+coin], dp[i] + 1)
        return -1 if dp[amount] == float('inf') else (dp[amount] - 1)