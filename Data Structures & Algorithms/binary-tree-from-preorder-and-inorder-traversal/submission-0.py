# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def buildTree(Pre, In):
            if not In: return None
            n = TreeNode(Pre[0])
            Pre.popleft()
            i = 0
            while In[i] != n.val:
                i += 1
            n.left = buildTree(Pre, In[:i])
            n.right = buildTree(Pre, In[i+1:])
            return n

        return buildTree(deque(preorder[:]), inorder)