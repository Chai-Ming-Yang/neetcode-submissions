class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        vis = set()
        res = []

        def dfs(subset):
            if len(subset) == len(nums):
                res.append(subset[:])
            
            for i in range(len(nums)):
                if i in vis: continue
                vis.add(i)
                subset.append(nums[i])
                dfs(subset)
                vis.remove(i)
                subset.pop()
        dfs([])
        return res