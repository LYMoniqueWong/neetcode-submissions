# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2: return None
        if not list1:   return list2
        if not list2:   return list1
        head1, head2, dummy = list1, list2, ListNode()
        if head1.val < head2.val:
            dummy.next = head1
            head1 = head1.next
        else:
            dummy.next = head2
            head2 = head2.next
        nxt = dummy.next
        while head1 and head2:
            if head1.val < head2.val:
                nxt.next = head1
                nxt = head1
                head1 = head1.next
            else:
                nxt.next = head2
                nxt = head2
                head2 = head2.next
        if head1:
            nxt.next = head1
        elif head2:
            nxt.next = head2
        return dummy.next