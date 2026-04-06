class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1] * N
        res = 1
        for i in range(1, N):
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
            res = max(res, dp[i])
        return res