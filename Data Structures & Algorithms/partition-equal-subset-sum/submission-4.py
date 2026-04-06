class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: return False

        target = total // 2
        dp = [True] + [False] * (target)

        for n in nums:
            for i in range(target, -1, -1):
                if not dp[i] or i + n > target: continue
                if i + n == target: return True
                dp[i + n] = True
        return False