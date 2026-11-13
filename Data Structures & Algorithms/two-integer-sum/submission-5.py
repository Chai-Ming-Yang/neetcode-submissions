class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vis = {}
        for i, x in enumerate(nums):
            if target - x in vis:
                return [vis[target - x], i]
            vis[x] = i