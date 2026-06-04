# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = "", ""
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        #num1, num2 = int(num1[::-1]), int(num2[::-1])
        num3 = int(num1[::-1]) + int(num2[::-1])
        num3 = (str(num3))[::-1]
        #print(num3) # str 579

        dummy = ListNode()
        tail = dummy
        for i in range(len(num3)):
            node = ListNode(int(num3[i]))
            tail.next = node
            tail = node
        return dummy.next