class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        subsum = 0
        subset = []
        def dfs(i):
            nonlocal subsum
            if subsum > target: return 
            if subsum == target: res.append(subset[:]); return 
            if i == len(nums): return
            
            subsum += nums[i];  subset.append(nums[i])
            dfs(i)
            subsum -= nums[i];  subset.pop()

            dfs(i+1)
        dfs(0)
        
        return res