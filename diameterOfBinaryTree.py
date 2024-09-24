# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def maxDepth(root):
            if root:
                left_depth = maxDepth(root.right)
                right_depth = maxDepth(root.left)
                self.res = max(self.res, left_depth + right_depth)
                return 1 + max(left_depth, right_depth)
            return 0

        maxDepth(root)
        return self.res
