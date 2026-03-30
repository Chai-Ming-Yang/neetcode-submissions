# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        def dfs(n):
            if not n: return 0
            nonlocal res
            l = dfs(n.left)
            r = dfs(n.right)
            res = max(res, 
                n.val,
                n.val + l,
                n.val + r,
                n.val + l + r
            )
            return max(n.val, n.val + l, n.val + r)
        dfs(root)
        return res