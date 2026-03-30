class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = { i:[] for i in range(numCourses) }
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        vis = set()
        def dfs(crs):
            if crs in vis: return []
            if not preMap[crs]: return [crs]
            vis.add(crs)
            sequence = []
            for pre in preMap[crs]:
                seq = dfs(pre)
                if not seq: return []
                sequence += seq
            vis.remove(crs)
            preMap[crs] = []
            return sequence + [crs]
        
        res = []
        resVis = set()
        for crs in range(numCourses):
            order = dfs(crs)
            if not order: return []
            for c in order:
                if c in resVis: continue
                resVis.add(c)
                res += [c]
        return res