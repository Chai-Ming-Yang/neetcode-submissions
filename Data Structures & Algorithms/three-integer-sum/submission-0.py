class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        res = []
        for i in range(N-2):
            j, k = i+1, N-1
            target = nums[i]
            # two sum 
            while j < k:
                if nums[j] + nums[k] > -target:
                    k -= 1
                elif nums[j] + nums[k] < -target:
                    j += 1
                else:
                    triplet = [target, nums[j], nums[k]]
                    if triplet not in res:
                        res.append(triplet)
                    k -= 1
                    j += 1
        return res