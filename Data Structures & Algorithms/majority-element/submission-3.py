class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        return sorted(count.items(), key=lambda a: a[1])[-1][0]