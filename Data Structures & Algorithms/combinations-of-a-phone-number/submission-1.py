class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        cMap = {
            '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], 
            '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']
        }

        res = []
        def dfs(i, subset):
            if i == len(digits): 
                res.append(subset[:])
                return 
            for c in cMap[digits[i]]:
                subset += c
                dfs(i+1, subset)
                subset = subset[:-1]
            
        dfs(0, '')
        return res