"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        vis = set()
        oriToCpy = {}
        def dfs(ori):
            if not ori or ori in vis: return
            vis.add(ori)
            oriToCpy[ori] = Node(ori.val)
            for neighbor in ori.neighbors:
                dfs(neighbor)
                oriToCpy[ori].neighbors.append(oriToCpy[neighbor])

        dfs(node)
        return oriToCpy[node] if oriToCpy else None