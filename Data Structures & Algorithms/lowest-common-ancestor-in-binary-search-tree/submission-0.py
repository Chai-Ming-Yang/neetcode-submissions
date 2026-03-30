# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """ p subtree of q   or   q subtree of p
        """
        res = root
        if p == q: return p
        stack = [root]  # always going to be len() == 1
        while stack:
            n = stack.pop()
            if not n: continue
            if p.val < n.val and q.val < n.val:
                res = n 
                stack.append(n.left)
            elif p.val > n.val and q.val > n.val: 
                res = n
                stack.append(n.right)
            else:
                return n
        return res