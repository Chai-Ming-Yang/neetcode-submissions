class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        # res = 
        for n in nums: 
            hashmap[n] += 1
        sorted_nums = list(sorted(hashmap.items(), key = lambda item: item[1], reverse=True))

        return [k for k, v in sorted_nums[:k]]