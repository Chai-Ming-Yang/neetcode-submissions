class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(start, subset, total):
            if total == target: 
                res.append(subset[:]); return
            
            for i in range(start, len(candidates)):
                """ same number at same level"""
                """ all possibility of the level 
                    starting with that number has already been considered """
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if total + candidates[i] > target:
                    break
                subset.append(candidates[i])
                dfs(i+1, subset, total + candidates[i])
                subset.pop()
        dfs(0, [], 0)
        return res