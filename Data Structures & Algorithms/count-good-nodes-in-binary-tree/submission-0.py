# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(n, curMax):
            if not n: return 0
            cur = 0
            if curMax <= n.val:
                curMax = n.val
                cur = 1
            cur += dfs(n.left, curMax)
            cur += dfs(n.right, curMax)
            return cur
        return dfs(root, root.val)