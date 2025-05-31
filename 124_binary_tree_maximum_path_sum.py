# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -math.inf

        def cur_max_sum(node):
            nonlocal res
            if not node:
                return 0
                
            # If left or right contributes negatively, we ignore it by taking max with 0
            left = max(cur_max_sum(node.left), 0)
            right = max(cur_max_sum(node.right), 0)

            # Case 1: Current node is the "root" of a path that includes both left and right
            # We calculate that path sum and update global max if it's higher
            res = max(res, node.val + left + right)

            # Case 2: Return to parent: pick the larger of left or right path to continue upward
            # We can only include one child path because paths can't split when moving upward
            return node.val + max(left, right)

        cur_max_sum(root)
        return res
