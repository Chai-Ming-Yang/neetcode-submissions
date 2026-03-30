class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [1] * N
        prod = 1
        for i in range(N):
            res[i] *= prod
            prod *= nums[i]
        prod = 1
        for j in range(N-1, -1, -1):
            res[j] *= prod
            prod *= nums[j]
        return res