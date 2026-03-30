class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        vis = {}
        for s in strs:
            vis[str(sorted(s))] = vis.get(str(sorted(s)), []) + [s]
        return list(vis.values())