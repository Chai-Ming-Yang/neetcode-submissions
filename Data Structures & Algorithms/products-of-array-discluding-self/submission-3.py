class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [1] * N
        prod = 1
        for i, n in enumerate(nums):
            res[i] *= prod
            prod *= n
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= prod
            prod *= nums[i]
        return res