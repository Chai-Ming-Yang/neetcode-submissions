class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """ STEP:
            1. Identify Start of SEQUENCE
                (elem with no left neighbor)
            2. Find + Track right neighbors
        """
        numSet = set(nums)
        res = 0

        for num in numSet:
            if num - 1 not in numSet:
                length = 1
                while num + length in numSet:
                    length += 1
                res = max(res, length)
        return res
        