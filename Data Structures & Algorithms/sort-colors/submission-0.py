class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        j = 0
        for i in range(3):
            for _ in range(count[i]):
                nums[j] = i
                j += 1
        