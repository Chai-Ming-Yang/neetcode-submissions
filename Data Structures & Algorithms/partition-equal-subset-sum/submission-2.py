class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: return False
        target = total / 2
        N = len(nums)
        vis = {}
        res = 0
        for n in nums:
            res += n
            vis[n] = vis.get(n, 0) + 1
            if res < target: continue
            if res == target: return True
            cpy = sorted(list(vis.keys()))
            l, r = 0, len(cpy) - 1
            while l < r:
                m = l + (r-l) // 2
                if cpy[m] == res - target:
                    return True
                if cpy[m] > res - target:
                    r = m
                else:
                    l = m + 1
            res -= cpy[r]
            vis[cpy[r]] -= 1
            if not vis[cpy[r]]: del vis[cpy[r]]
        return False