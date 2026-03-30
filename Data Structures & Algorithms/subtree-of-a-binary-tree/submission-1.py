# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(a, b):
            if not a and not b: return True
            if not a or not b or a.val != b.val: return False
            return same(a.left, b.left) and same(a.right, b.right)
        q = deque([root])
        while q:
            for _ in range(len(q)):
                n = q.popleft()
                if not n: continue
                if n.val == subRoot.val and same(n, subRoot): return True
                q.append(n.left)
                q.append(n.right)

        return False