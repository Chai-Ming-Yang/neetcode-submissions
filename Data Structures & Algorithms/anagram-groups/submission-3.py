class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        vis = dict()
        for s in strs:
            visKey = str(sorted(s))
            vis[visKey] = vis.get(visKey, []) + [s]

        return [v for v in vis.values()]