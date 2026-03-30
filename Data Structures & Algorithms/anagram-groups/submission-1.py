class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """ APPROACHES:
            1. SORT EVERYTHING
            2. HASH into list
        """
        
        hashmap = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            count = tuple(count)
            hashmap[count].append(s)

        return list(hashmap.values())