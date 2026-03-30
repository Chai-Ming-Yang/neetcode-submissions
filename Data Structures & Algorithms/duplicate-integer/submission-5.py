class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vis = set()
        for n in nums:
            if n in vis:
                return True
            vis.add(n)
        return False