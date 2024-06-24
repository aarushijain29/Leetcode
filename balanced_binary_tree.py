# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def heightCalculator(self, root) -> [bool, int]:

        if root:
            leftHeight = self.heightCalculator(root.left)
            rightHeight = self.heightCalculator(root.right)
            balanced = leftHeight[0] and rightHeight[0] and abs(leftHeight[1] - rightHeight[1]) <= 1
            return balanced, 1 + max(leftHeight[1], rightHeight[1])
        else:
            return True, 0


    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root:
            return self.heightCalculator(root)[0]
        else:
            return True

       
            
            
