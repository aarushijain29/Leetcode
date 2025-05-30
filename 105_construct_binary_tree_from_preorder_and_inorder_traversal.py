# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # preorder = root -> left -> right i.e. [root] + [left subtree] + [right subtree]
        # inorder = left -> root -> right i.e. [left subtree] + [root] + [right subtree]

        # We'll build the tree recursively using preorder to select the root
        # and inorder to determine the boundaries of left and right subtrees
        self.inorder_map = {}
        for idx, num in enumerate(inorder):
            self.inorder_map[num] = idx

        # This index tracks the current root node in preorder list
        self.preorder_idx = 0

        # build tree in preorder
        # using inorder to get left and right subtrees
        def dfs(left, right):
            if left > right: return None

            root = TreeNode(preorder[self.preorder_idx])
            self.preorder_idx += 1

            # mid = the idx of root in inorder
            mid = self.inorder_map[root.val]
            # all values before root are in the left subtree
            root.left = dfs(left, mid - 1)
            # all values after root are in the right subtree
            root.right = dfs(mid + 1, right)

            return root        

        return dfs(0, len(inorder) - 1)
