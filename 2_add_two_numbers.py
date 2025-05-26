# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        tail = dummy
        carry = 0

        def getVal(l):
            return l.val if l else 0
        
        while l1 or l2:
            cur_sum = getVal(l1) + getVal(l2) + carry
            tail.next = ListNode(cur_sum % 10, None)
            carry = cur_sum // 10
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            tail = tail.next

        if carry > 0:
            tail.next = ListNode(carry, None)
            
        return dummy.next
