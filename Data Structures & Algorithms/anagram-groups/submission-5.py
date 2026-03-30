class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict()
        for s in strs:
            ss = str(sorted(s))
            hashmap[ss] = hashmap.get(ss, []) + [s]
        return [x for x in hashmap.values()]