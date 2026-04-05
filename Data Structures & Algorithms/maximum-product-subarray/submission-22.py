class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        mn = mx = res = nums[0]
        for n in nums[1:]:
            if n < 0:
                mx, mn = mn, mx
            mx = max(n, n * mx)
            mn = min(n, n * mn)
            res = max(res, mx)
        return res