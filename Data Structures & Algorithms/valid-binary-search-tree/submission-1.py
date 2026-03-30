# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque([(root, -float('inf'), float('inf'))])
        while q:
            for _ in range(len(q)):
                n, minn, maxx = q.popleft()
                if not n: continue
                if n.left:
                    if minn < n.left.val and n.left.val < n.val: 
                        q.append((n.left, minn, n.val))
                    else: return False
                if n.right:
                    if n.val < n.right.val and n.right.val < maxx: 
                        q.append((n.right, n.val, maxx))
                    else: return False
        return True