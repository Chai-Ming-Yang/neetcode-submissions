class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        res = []
        for i in range(N):
            target = nums[i]
            l, r = i+1, N-1
            while l < r:
                if nums[l] + nums[r] < -target: l += 1
                elif nums[l] + nums[r] > -target: r -= 1
                else: 
                    triplet = [target, nums[l], nums[r]]
                    if triplet not in res:
                        res.append(triplet)
                    l += 1
                    r -= 1
        return res