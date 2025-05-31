# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def preorder(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)

        return ','.join(res)
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        encoded = data.split(',')
        i = 0

        def dfs():
            nonlocal i
            if encoded[i] == 'N':
                i += 1
                return None
            node = TreeNode(encoded[i])
            i += 1
            node.left = dfs()
            node.right = dfs()

            return node
        

        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
