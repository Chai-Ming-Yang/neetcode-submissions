class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            ss = str(sorted(s))
            hashmap[ss].append(s)
        return [x for x in hashmap.values()]