class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            ss = str(sorted(s))
            if ss not in res:
                res[ss] = []
            res[ss].append(s)
        return list(res.values())