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
            if not n: return -float('inf')
            l = dfs(n.left)
            r = dfs(n.right)
            nonlocal res
            # res = max(res, max(l, r, n.val, l+n.val, r+n.val, l+r+n.val, l+r))
            res = max(res, max(n.val, l+n.val, r+n.val, l+r+n.val))
            print(n.val, [l, r], res)
            return max(n.val, l+n.val, r+n.val)
        dfs(root)
        return res