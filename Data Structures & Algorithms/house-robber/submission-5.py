class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        dp = nums[:]
        dp[1] = max(dp[1], dp[0])
        N = len(nums)
        for i in range(2, N):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[-1]