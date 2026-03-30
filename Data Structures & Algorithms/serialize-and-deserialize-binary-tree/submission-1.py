# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        q = deque([root])
        while q:
            n = q.popleft()
            if not n: 
                res.append(None)
                continue
            res.append(n.val)
            q.append(n.left)
            q.append(n.right)
        return '#'.join(list(map( str, res)))
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data: return None
        data = data.split('#')
        print(data)
        return root