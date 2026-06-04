# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle, reverse 2nd half of the list, merge
        s, f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        second = s.next

        prev = s.next = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        
        # 2nd half of list <= 1st half
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
    
