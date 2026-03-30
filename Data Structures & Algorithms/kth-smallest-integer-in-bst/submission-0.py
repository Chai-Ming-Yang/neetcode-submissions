# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        minn = []
        def dfs(n):
            if len(minn) == k or not n: return
            dfs(n.left)
            minn.append(n.val)
            dfs(n.right)
        dfs(root)
        return minn[k-1]