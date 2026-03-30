class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = res = nums[0]
        l = 0
        for r in range(1, len(nums)):
            cur += nums[r]
            if cur < nums[r]:
                l = r
                cur = nums[r]
            res = max(res, cur)
        return res