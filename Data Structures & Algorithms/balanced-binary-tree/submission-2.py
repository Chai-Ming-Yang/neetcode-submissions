# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def bfs(n):
            nonlocal res
            if not n or not res: return 0
            l, r = bfs(n.left), bfs(n.right)
            if l!=r and r+1!=l and r!=l+1:
                res = False
            print(n.val, l, r, l==r or r+1==l or r==l+1, res)
            return 1 + max(l, r)

        bfs(root)
        return res