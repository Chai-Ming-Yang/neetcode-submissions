class Solution:
    def twoSum(self, a: List[int], target: int) -> List[int]:
        """ APPROACHES:
            1. Brute Force O(n^2)
            2. Hash Map
            3. Progressive add to Hash Map
        """
        hashmap = {}
        for i in range(len(a)):
            diff = target - a[i]
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[a[i]] = i