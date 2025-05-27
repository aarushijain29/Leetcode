# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        max_depth = 1
        stack = []
        stack.append((root, 1))

        while stack:
            parent, depth = stack.pop(-1)
            if parent:
                max_depth = max(max_depth, depth)
                stack.append((parent.left, depth + 1))
                stack.append((parent.right, depth + 1))
        
        return max_depth
