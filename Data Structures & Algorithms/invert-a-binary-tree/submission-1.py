# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        while q:
            n = q.popleft()
            if n:
                n.left, n.right = n.right, n.left
                q.append(n.left)
                q.append(n.right)
        return root