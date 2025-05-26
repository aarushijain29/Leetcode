# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # e.g. 1 -> 2 -> 3 -> 4 -> 5 -> None
        slow, fast = head, head.next
        # slow -> 1 -> 2 -> 3 -> 4 -> 5 -> None
        # fast -> 2 -> 3 -> 4 -> 5 -> None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow -> 3 -> 4 -> 5 -> None
        second = slow.next
        # second -> 4 -> 5 -> None
        slow.next = None # 3 -> None
        # first -> 1 -> 2 -> 3 -> None
        first = head

        prev = None
        cur = second
        # cur -> 4 -> 5 -> None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        second = prev
        # second -> 5 -> 4 -> None

        while second:
            first_nxt = first.next
            second_nxt = second.next
            first.next = second
            second.next = first_nxt
            first = first_nxt
            second = second_nxt
