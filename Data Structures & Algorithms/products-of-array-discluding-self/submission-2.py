class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [0] * N
        pre = [1] * N
        prod = 1
        for i, n in enumerate(nums):
            prod *= n
            pre[i] = prod
        prod = 1
        for i in range(len(nums)-1, 0, -1):
            res[i] = pre[i-1] * prod
            prod *= nums[i]
        res[0] = prod
        return res