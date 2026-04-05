class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mxL = 0
        L = len(s)
        vis = set()
        wordMap = set()
        for st in wordDict:
            wordMap.add(st)
            mxL = max(mxL, len(st))
        q = deque([0])
        while q:
            i = q.popleft()
            for j in range(1, mxL + 1):
                if s[i:i+j] in wordMap:
                    if i + j == L: return True 
                    if i+j not in vis: 
                        vis.add(i+j)
                        q.append(i + j)


        return False