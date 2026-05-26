class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = len(nums)
        for i, n in enumerate(nums):
            if n == val:
                res -= 1
                nums[i] = 51
        nums.sort()
        return res