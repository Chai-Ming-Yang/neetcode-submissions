class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(start, subset):
            if start == len(s):
                res.append(subset[:])
                return
            
            for i in range(start, len(s)):
                l, r = start, i
                isPal = True
                while l <= r:
                    if s[l] != s[r]: isPal = False; break
                    l += 1; r -= 1
                if start != i and not isPal:
                    continue
                subset.append(s[start:i+1])
                dfs(i+1, subset)
                subset.pop()
            

        dfs(0, [])
        return res