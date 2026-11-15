class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero = 0; prod = 1
        N = len(nums)
        for n in nums:
            if n == 0:
                zero += 1
            else:
                prod *= n
        if zero > 1:
            return [0] * N
        
        for i in range(N):
            if nums[i] == 0:
                return [0] * (i) + [prod] + [0] * (N-i-1)
            nums[i] = int(prod / nums[i])
        return nums