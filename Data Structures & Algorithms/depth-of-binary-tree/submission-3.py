# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 1)]
        res = 0
        while stack:
            n, d= stack.pop()
            if n:
                stack.append((n.left, d+1))
                stack.append((n.right, d+1))
                res = max(res, d)
        return res