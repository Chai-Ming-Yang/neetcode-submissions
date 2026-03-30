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
                
            if nums[l] <= nums[mid]:   # left == sorted half
                if nums[l] <= target and target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:                   # right == sorted half
                if nums[mid] <= target and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1