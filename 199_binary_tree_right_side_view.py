# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q = deque()
        q.append((root, 1))
        res = []

        while q:
            node, level = q.popleft()
            if len(res) < level:
                res.append(node.val)
            if node.right:
                q.append((node.right, level + 1))
            if node.left:
                q.append((node.left, level + 1))
    
        return res
 
