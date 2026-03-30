"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        vis = {}

        def dfs(n):
            if not n: return
            if n in vis: return vis[n]
            vis[n] = Node(n.val)
            for nei in n.neighbors:
                tmp = dfs(nei)
                if tmp: vis[n].neighbors.append(tmp)
            return vis[n]
        return dfs(node)