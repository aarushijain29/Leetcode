# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def inorder(node):
            if not node: 
                return True

            # Traverse left subtree first (inorder)
            if not inorder(node.left):
                return False
            
            # Check if current node's value is greater than the previous node's value
            # In a valid BST, inorder traversal should always yield increasing values
            if node.val <= self.prev:
                return False
            
            # Update self.prev to the current node's value before moving right
            self.prev = node.val

            # Traverse right subtree
            return inorder(node.right)
        
        self.prev = -math.inf
        return inorder(root)
