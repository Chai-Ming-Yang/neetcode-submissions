class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """ APPROACHES:
            1. count, sort, take top
            2. heap
            3. bucket sort
        """
        # hashmap = defaultdict(int)
        # for n in nums: 
        #     hashmap[n] += 1
        # sorted_nums = list(sorted(hashmap.items(), key = lambda item: item[1], reverse=True))

        # return [k for k, v in sorted_nums[:k]]


        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] += 1
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res





