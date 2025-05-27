# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def merge2SortedLists(head1, head2):
            l1, l2 = head1, head2
            dummy = ListNode()
            tail = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    tail.next = ListNode(l2.val)
                    l2 = l2.next
                tail = tail.next
            
            tail.next = l1 or l2
            return dummy.next
        
        if not lists:
            return None


        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged_lists.append(merge2SortedLists(lists[i], l2))
            lists = merged_lists        

        return lists[0]
