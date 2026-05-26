class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(Counter(nums).items(), key=lambda x:x[1])[-1][0]