class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        def dfs(dist):
            nonlocal res
            if dist == 0: return True
            for i in range(dist):
                if i + nums[i] >= dist:
                    print(dist, i)
                    res += 1
                    if dfs(i): return True
                    res -= 1
            return False
        dfs(len(nums)-1)
        return res