# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def hasCycle(node):
            slow = node
            fast = node

            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
                if slow == fast:
                    return slow, True
            
            return slow, False

        def getCycleLen(node):
            res = 1
            pointer = node.next

            while pointer and node != pointer:
                res += 1
                pointer = pointer.next
            return res
        
        node, has_cycle = hasCycle(head)
        if not has_cycle:
            return None
        
        cycle_len = getCycleLen(node)
        start = head
        while cycle_len > 0:
            start = start.next
            cycle_len -= 1
        
        node = head
        while node != start:
            start = start.next
            node = node.next
        
        return start
        
