class Solution:
    def twoSum(self, a: List[int], target: int) -> List[int]:
        """ APPROACHES:
            1. Brute Force O(n^2)
            2. Hash Map
            3. Progressive add to Hash Map
        """
        hashmap = {}
        for i, n in enumerate(a):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i