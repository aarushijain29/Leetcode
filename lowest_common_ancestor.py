# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root:
            if root.val == p.val:
                if (root.left and root.left.val == q.val) or (root.right and root.right.val == q.val):
                    return p
            elif root.val == q.val:
                if (root.left and root.left.val == p.val) or (root.right and root.right.val == p.val):
                    return q
            elif root.val < p.val and root.val < q.val:
                if root.right:
                    return self.lowestCommonAncestor(root.right, p, q)
            elif root.val > p.val and root.val > q.val:
                if root.left:
                    return self.lowestCommonAncestor(root.left, p, q)
            
            return root

                
