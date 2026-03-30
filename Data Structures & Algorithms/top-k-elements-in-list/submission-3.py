class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        return [k for k,v in sorted(freq.items(), key=lambda a: -a[1])][:k]