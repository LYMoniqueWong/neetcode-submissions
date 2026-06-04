# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:    return None
        dummy = ListNode(0, head)
        first, second = head, dummy
        for _ in range(n):
            first = first.next # 3
        while first:
            first = first.next # none
            second = second.next # 2
        second.next = second.next.next
        return dummy.next