class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        can = [False] * N
        can[0] = True

        for l in range(N):
            if not can[l]: return False
            for r in range(nums[l], -1, -1):
                if l+r >= N-1: return True
                can[l+r] = True
        return False