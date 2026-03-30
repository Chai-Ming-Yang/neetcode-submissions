class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = { c:set() for w in words for c in w }

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minL = min(len(w1), len(w2))
            if w1[:minL] == w2[:minL] and len(w2) < len(w1): return ""
            for j in range(minL):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        vis = {} # False == Vis, True == Vis & cur Path
        res = []
        
        def dfs(c):
            if c in vis: 
                return vis[c]
            vis[c] = True

            for nei in adj[c]:
                if dfs(nei): return True
            res.append(c)
            vis[c] = False
        
        for c in adj:
            if c in vis: continue
            if dfs(c): return ""
        res.reverse()
        return ''.join(res)