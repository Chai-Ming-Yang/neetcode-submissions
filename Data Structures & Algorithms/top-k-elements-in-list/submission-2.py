class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vis = {}
        for n in nums:
            vis[n] = vis.get(n, 0) + 1
        return sorted(vis, key=vis.get, reverse=True)[:k]
