class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 1, len(nums)
        nums = [0] + nums
        while l < r:
            total = nums[l] + nums[r]
            if total < target:
                l += 1
            elif total > target:
                r -= 1
            else:
                return [l, r]