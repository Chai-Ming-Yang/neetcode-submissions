class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        pre, post = [0] * N, [0] * N
        p = q = 1
        i, j = 0, N-1
        for _ in nums:
            p *= nums[i] ; pre[i] = p ; i += 1
            q *= nums[j] ; post[j] = q ; j -= 1
        res = [post[1]] + [0] * (N-2) + [pre[-2]]
        for i in range(1, N-1):
            res[i] = pre[i-1] * post[i+1]
        print(pre)
        print(post)
        return res