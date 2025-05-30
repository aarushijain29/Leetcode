# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        res = 0
        max_path = []
        def maxDepth(node, path):
            nonlocal res, max_path
            if not node:
                return (0, path)

            left_depth, left_path = maxDepth(node.left, [])
            right_depth, right_path = maxDepth(node.right, [])
            res = max(res, left_depth + right_depth)
            max_path = max(max_path, left_path + [node] + right_path, key=len)

            return (1 + max(left_depth, right_depth),
                    [node] + max(left_path, right_path, key=len))
            
        
        maxDepth(root, [])
        return res
