class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for n in nums:
            next_dp = defaultdict(int)
            for k in dp:
                next_dp[k+n] += dp[k]
                next_dp[k-n] += dp[k]
            dp = next_dp
        return dp[target]