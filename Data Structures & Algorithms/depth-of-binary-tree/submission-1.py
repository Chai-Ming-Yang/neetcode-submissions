# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(n, depth):
            if not n: return depth
            l = dfs(n.left, depth + 1)
            r = dfs(n.right, depth + 1)
            depth = max(l, r)
            return depth
        return dfs(root, 0)