class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """ binary_search:
            sorted & unsorted half
            bound-in on target range 
        """
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:    # l may be equal to mid
                if target < nums[l] or nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or nums[r] < target:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1