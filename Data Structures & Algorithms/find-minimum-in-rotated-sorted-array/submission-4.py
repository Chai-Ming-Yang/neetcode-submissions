class Solution:
    def findMin(self, nums: List[int]) -> int:
        """ APPROACH:
            # 2-phase binary search #
            * 1) sorted & unsorted sides
            * 2) normal binary search
        """
        res = nums[0]
        l, r = 0, len(nums)-1

        while l <= r:
            if nums[l] < nums[r]:   # ascending
                res = min(res, nums[l])
                break

            m = l + (r-l)//2
            res = min(res, nums[m])
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        return res