class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()
        def dfs(i, subset, total):
            if total == target: 
                res.add(tuple(subset[:]))
                return
            if i == len(candidates) or total > target: return

            subset.append(candidates[i])
            dfs(i+1, subset, total+candidates[i])
            subset.pop()

            dfs(i+1, subset, total)
        dfs(0, [], 0)
        return list(map(list, res))