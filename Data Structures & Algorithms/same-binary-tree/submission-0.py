# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(a, b):
            if ((a and not b) or (b and not a)): return False
            if not a: return True

            if a.val != b.val: return False
            if not a.left and b.left or a.left and not b.left: return False
            if a.left and not dfs(a.left, b.left): return False
                
            if not a.right and b.right or a.right and not b.right: return False
            if a.right and not dfs(a.right, b.right): return False
            return True
        return dfs(p, q)