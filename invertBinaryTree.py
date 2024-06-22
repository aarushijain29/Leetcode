# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root:
            dummy = TreeNode()
            dummy.left = root.left
            dummy.right = root.right
            root.left = self.invertTree(dummy.right)
            root.right = self.invertTree(dummy.left)

        return root            
        
