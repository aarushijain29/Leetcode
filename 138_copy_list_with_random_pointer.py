"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_copy_map = {None:None} # maps old nodes to respective new nodes

        cur = head
        while cur:
            old_to_copy_map[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            # copy node corresponding to cur is stored in old_to_copy_map[cur]
            copy = old_to_copy_map[cur]
            # copy's next = copy node corresponding to cur's next node
            copy.next = old_to_copy_map[cur.next]
            # copy's random = copy node corresponding to cur's random node
            copy.random = old_to_copy_map[cur.random]
            cur = cur.next
        
        # head of copy list = copy node corresponding to old list's head node
        return old_to_copy_map[head]
