class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nSet = set(nums)
        return len(nSet) != len(nums)