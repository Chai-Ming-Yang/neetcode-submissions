class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """ xor : even freq duplicates cancel each other """
        xor = 0
        for n in nums:
            xor ^= n
        return xor