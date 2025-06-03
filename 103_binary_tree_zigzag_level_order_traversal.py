# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        res = []

        q = deque()
        q.append((root, 0))
        level = 0

        while q:
            res.append(deque())
            while q and q[0][1] == level:
                node, lvl = q.popleft()
                if level % 2 == 0:
                    res[level].append(node.val)
                else:
                    res[level].appendleft(node.val)
                if node.left: q.append((node.left, level + 1))
                if node.right: q.append((node.right, level + 1))
            res[level] = list(res[level])
            level += 1

        return res
