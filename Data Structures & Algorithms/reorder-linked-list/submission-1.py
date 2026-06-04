# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # divide the list into halves
        s, f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        mid = s.next
        # reverse the second half
        prev = s.next = None
        while mid:
            nxt = mid.next
            mid.next = prev
            prev = mid
            mid = nxt
        # merge the two halves node by node
        # len(2nd half) <= len(1st half)
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2